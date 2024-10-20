import subprocess
import argparse
import signal
import sys
import time
import requests
from urllib.parse import urlparse

class GoProStreamer:
    def __init__(self):
        self.process = None
        self.running = False

    def get_gopro_ip(self):
        """
        Get the GoPro's IP address. GoPro typically uses 10.5.5.9 when in WiFi mode.
        Returns the IP if successful, None otherwise.
        """
        try:
            # Test if GoPro is accessible
            response = requests.get("http://10.5.5.9/gp/gpControl/status", timeout=5)
            if response.status_code == 200:
                return "10.5.5.9"
        except requests.RequestException:
            return None
        return None

    def start_stream_mode(self, gopro_ip):
        """
        Put the GoPro into stream mode
        """
        try:
            # Enable stream mode
            requests.get(f"http://{gopro_ip}/gp/gpControl/execute?p1=gpStream&c1=start")
            # Wait for stream mode to initialize
            time.sleep(2)
        except requests.RequestException as e:
            print(f"Error setting GoPro stream mode: {e}")
            return False
        return True

    def stream(self, rtmp_url):
        """
        Start streaming from GoPro to RTMP server
        """
        gopro_ip = self.get_gopro_ip()
        if not gopro_ip:
            print("Error: Cannot connect to GoPro. Make sure it's turned on and in WiFi mode.")
            return False

        if not self.start_stream_mode(gopro_ip):
            return False

        # FFmpeg command for streaming
        # Using UDP protocol to receive video from GoPro and stream to RTMP
        ffmpeg_cmd = [
            'ffmpeg',
            '-i', f'udp://{gopro_ip}:8554',  # GoPro stream input
            '-c:v', 'libx264',               # Video codec
            '-preset', 'veryfast',           # Encoding preset for low latency
            '-tune', 'zerolatency',          # Tune for streaming
            '-b:v', '4000k',                 # Video bitrate
            '-maxrate', '4500k',             # Maximum bitrate
            '-bufsize', '9000k',             # Buffer size
            '-pix_fmt', 'yuv420p',           # Pixel format
            '-g', '60',                      # Keyframe interval
            '-c:a', 'aac',                   # Audio codec
            '-b:a', '128k',                  # Audio bitrate
            '-ar', '44100',                  # Audio sample rate
            '-f', 'flv',                     # Output format
            rtmp_url                         # RTMP URL
        ]

        try:
            self.running = True
            self.process = subprocess.Popen(
                ffmpeg_cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            print(f"Streaming started to {urlparse(rtmp_url).netloc}")

            while self.running:
                # Check if process is still running
                if self.process.poll() is not None:
                    print("FFmpeg process terminated unexpectedly")
                    break
                time.sleep(1)

        except KeyboardInterrupt:
            self.stop_streaming()
        except Exception as e:
            print(f"Streaming error: {e}")
            self.stop_streaming()

    def stop_streaming(self):
        """
        Stop the streaming process
        """
        self.running = False
        if self.process:
            self.process.terminate()
            try:
                self.process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                self.process.kill()
            self.process = None
        print("\nStreaming stopped")

def main():
    parser = argparse.ArgumentParser(description='Stream from GoPro to RTMP server')
    parser.add_argument('rtmp_url', help='RTMP URL (e.g., rtmp://a.rtmp.youtube.com/live2/your-key)')
    args = parser.parse_args()

    streamer = GoProStreamer()

    # Handle Ctrl+C gracefully
    def signal_handler(sig, frame):
        print("\nStopping stream...")
        streamer.stop_streaming()
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    # Start streaming
    streamer.stream(args.rtmp_url)

if __name__ == "__main__":
    main()
