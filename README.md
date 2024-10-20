# GoPro Streamer Installation Guide

This guide provides detailed installation instructions for all required components across different operating systems.

## Table of Contents
- [Python Installation](#python-installation)
- [FFmpeg Installation](#ffmpeg-installation)
- [Project Setup](#project-setup)
- [Verification](#verification)
- [Troubleshooting](#troubleshooting)

## Python Installation

### Windows
1. Download Python 3.8 or newer from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. **Important**: Check "Add Python to PATH" during installation
4. Verify installation:
   ```bash
   python --version
   ```

### macOS
1. Using Homebrew:
   ```bash
   brew install python
   ```
2. Or download from [python.org](https://www.python.org/downloads/)
3. Verify installation:
   ```bash
   python3 --version
   ```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### Linux (Fedora)
```bash
sudo dnf install python3 python3-pip python3-virtualenv
```

## FFmpeg Installation

### Windows
1. Method 1: Using Chocolatey (Recommended)
   ```bash
   # Install Chocolatey first if you haven't:
   Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))

   # Install FFmpeg
   choco install ffmpeg
   ```

2. Method 2: Manual Installation
   - Download from [ffmpeg.org](https://ffmpeg.org/download.html#build-windows)
   - Extract the ZIP file
   - Add FFmpeg's bin folder to System PATH:
     1. Right-click 'This PC' → Properties
     2. Advanced system settings → Environment Variables
     3. Under System Variables, find 'Path'
     4. Click Edit → New
     5. Add the path to FFmpeg's bin folder

### macOS
1. Using Homebrew (Recommended):
   ```bash
   brew install ffmpeg
   ```

2. Using MacPorts:
   ```bash
   sudo port install ffmpeg
   ```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install ffmpeg

# For additional codecs and formats
sudo apt install \
    ffmpeg \
    libavcodec-extra \
    libavformat-dev \
    libavutil-dev \
    libswscale-dev
```

### Linux (Fedora)
```bash
sudo dnf install ffmpeg ffmpeg-devel
```

### Linux (CentOS/RHEL)
```bash
# Enable RPM Fusion repositories
sudo dnf install --nogpgcheck https://dl.fedoraproject.org/pub/epel/epel-release-latest-$(rpm -E %rhel).noarch.rpm
sudo dnf install --nogpgcheck https://mirrors.rpmfusion.org/free/el/rpmfusion-free-release-$(rpm -E %rhel).noarch.rpm
sudo dnf install --nogpgcheck https://mirrors.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-$(rpm -E %rhel).noarch.rpm

# Install FFmpeg
sudo dnf install ffmpeg ffmpeg-devel
```

## Project Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/gopro-streamer.git
   cd gopro-streamer
   ```

2. Create and activate virtual environment:

   **Windows:**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   **macOS/Linux:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

4. Install the package in development mode:
   ```bash
   pip install -e .
   ```

## Verification

1. Verify Python installation:
   ```bash
   python --version  # Should show 3.8 or newer
   ```

2. Verify FFmpeg installation:
   ```bash
   ffmpeg -version  # Should show FFmpeg version and configuration
   ```

3. Verify GoPro Streamer installation:
   ```bash
   # Make sure your GoPro is connected via WiFi first
   gopro-stream --version
   ```

## Troubleshooting

### FFmpeg Issues

1. "FFmpeg command not found":
   ```bash
   # Check if FFmpeg is in PATH
   which ffmpeg  # On Unix-like systems
   where ffmpeg  # On Windows

   # Check if FFmpeg runs
   ffmpeg -version
   ```

2. Missing codecs:
   ```bash
   # Ubuntu/Debian
   sudo apt install ubuntu-restricted-extras

   # Fedora
   sudo dnf install ffmpeg-libs
   ```

### Python Environment Issues

1. "Python command not found":
   - Verify Python is in PATH
   - Try using `python3` instead of `python`

2. "pip command not found":
   ```bash
   # Install pip if missing
   python -m ensurepip --default-pip
   ```

3. Virtual environment issues:
   ```bash
   # If venv creation fails, install python3-venv
   # Ubuntu/Debian:
   sudo apt install python3-venv

   # Fedora:
   sudo dnf install python3-virtualenv
   ```

### Permission Issues

1. Linux/macOS:
   ```bash
   # If you get permission errors
   sudo chown -R $USER:$USER ~/.local
   ```

2. Windows:
   - Run terminal as Administrator for system-wide installations
   - Check folder permissions in installation directory

### Network Issues

1. GoPro Connection:
   - Verify WiFi connection to GoPro
   - Check GoPro IP accessibility:
     ```bash
     ping 10.5.5.9
     ```

2. RTMP Connection:
   - Test network speed: [speedtest.net](https://www.speedtest.net)
   - Verify firewall settings for RTMP port (typically 1935)

For additional help or issues not covered here, please:
1. Check the [GitHub Issues](https://github.com/yourusername/gopro-streamer/issues)
2. Submit a new issue with:
   - Your OS and version
   - Python version (`python --version`)
   - FFmpeg version (`ffmpeg -version`)
   - Complete error message
   - Steps to reproduce the issue
