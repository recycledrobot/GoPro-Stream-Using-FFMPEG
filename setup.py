from setuptools import setup, find_packages

setup(
    name="gopro-streamer",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.28.0",
    ],
    entry_points={
        "console_scripts": [
            "gopro-stream=gopro_streamer.gopro_streamer:main",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A tool for streaming from GoPro cameras to RTMP servers",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/gopro-streamer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
