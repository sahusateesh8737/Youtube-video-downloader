# YouTube Video Downloader

A simple command-line Python utility to download YouTube videos and playlists with various quality options.

## Features

- Download single YouTube videos or entire playlists
- Specify video quality (best, 1080p, 720p, 480p, 360p)
- Choose custom download directory
- Progress tracking during download
- Automatic merging of video and audio streams

## Requirements

This script requires Python 3 and the `yt-dlp` library, which is a fork of `youtube-dl` with additional features and active maintenance.

### Dependencies

- Python 3.6 or higher
- yt-dlp

## Installation

1. Ensure you have Python 3 installed on your system
2. Install the required library:

```bash
pip install yt-dlp
```

## Usage

Basic usage:

```bash
python youtube_playlist_downloader.py [YouTube_URL] [options]
```

### Options

- `URL`: URL of the YouTube video or playlist (required)
- `-d, --directory`: Directory to save the videos (default: "youtube_downloads")
- `-q, --quality`: Video quality setting (choices: "best", "1080p", "720p", "480p", "360p", default: "best")

### Examples

Download a single video with default options:
```bash
python youtube_playlist_downloader.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

Download a playlist in 720p quality to a custom directory:
```bash
python youtube_playlist_downloader.py https://www.youtube.com/playlist?list=PLXwTOG3-tRwgy4lJ9j_CPwpJmr2uCaGH1 -q 720p -d my_videos
```

## How It Works

The script uses the `yt-dlp` library to:
1. Extract metadata from the provided YouTube URL
2. Determine if it's a single video or a playlist
3. Download the video(s) with the requested quality
4. Merge the video and audio streams into MP4 format
5. Save the files to the specified directory

## Notes

- The script will create the download directory if it doesn't exist
- Files are saved in the format: `[playlist_index]-[video_title].mp4`
- Existing files will not be overwritten
- The script will skip videos that cannot be downloaded due to restrictions
