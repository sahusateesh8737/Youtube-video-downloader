#!/usr/bin/env python3
import os
import sys
import argparse
from yt_dlp import YoutubeDL

def download_videos(url, download_dir="youtube_downloads", quality="best"):
    """
    Download videos from a YouTube URL (single video or playlist)
    
    Args:
        url (str): URL of the YouTube video or playlist
        download_dir (str): Directory to save the videos
        quality (str): Video quality to download. Options: best, 1080p, 720p, 480p, 360p
    """
    # Create the download directory if it doesn't exist
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
        print(f"Created directory: {download_dir}")
    
    # Set format based on quality parameter
    video_format = "bestvideo+bestaudio/best"
    if quality == "1080p":
        video_format = "bestvideo[height<=1080]+bestaudio/best[height<=1080]"
    elif quality == "720p":
        video_format = "bestvideo[height<=720]+bestaudio/best[height<=720]"
    elif quality == "480p":
        video_format = "bestvideo[height<=480]+bestaudio/best[height<=480]"
    elif quality == "360p":
        video_format = "bestvideo[height<=360]+bestaudio/best[height<=360]"
    
    # Configure yt-dlp options
    ydl_opts = {
        'format': video_format,  # Use the selected quality format
        'outtmpl': os.path.join(download_dir, '%(playlist_index)s-%(title)s.%(ext)s'),
        'ignoreerrors': True,  # Skip videos that cannot be downloaded
        'nooverwrites': True,  # Don't overwrite existing files
        'quiet': False,
        'verbose': False,
        'progress': True,
        'writethumbnail': False,
        'writesubtitles': False,
        'merge_output_format': 'mp4',  # Ensure videos are merged into mp4
    }
    
    print(f"Extracting information from URL: {url}")
    
    # Download the videos
    try:
        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
            if 'entries' in info:
                # This is a playlist
                playlist_title = info.get('title', 'Unknown Playlist')
                video_count = len(info['entries'])
                print(f"Playlist: {playlist_title}")
                print(f"Total videos found: {video_count}")
                
                # Now download the videos
                print(f"Starting download of {video_count} videos in {quality} quality...")
                with YoutubeDL(ydl_opts) as ydl_download:
                    ydl_download.download([url])
                
                print(f"\nDownload complete! Videos saved to: {os.path.abspath(download_dir)}")
            else:
                # This is a single video
                video_title = info.get('title', 'Unknown Video')
                print(f"Video: {video_title}")
                print(f"Starting download in {quality} quality...")
                
                with YoutubeDL(ydl_opts) as ydl_download:
                    ydl_download.download([url])
                
                print(f"\nDownload complete! Video saved to: {os.path.abspath(download_dir)}")
    except Exception as e:
        print(f"Error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download videos from a YouTube playlist or single video")
    parser.add_argument("url", nargs="?", default="https://www.youtube.com/playlist?list=PLXwTOG3-tRwgy4lJ9j_CPwpJmr2uCaGH1",
                        help="URL of the YouTube playlist or video")
    parser.add_argument("-d", "--directory", default="youtube_downloads",
                        help="Directory to save the videos (default: youtube_downloads)")
    parser.add_argument("-q", "--quality", default="best", choices=["best", "1080p", "720p", "480p", "360p"],
                        help="Quality setting (will always merge audio and video)")

    args = parser.parse_args()
    
    print("\n==== YouTube Video Downloader ====")
    print(f"URL: {args.url}")
    print(f"Download directory: {args.directory}")
    print(f"Quality: {args.quality} (will download with audio)")
    print("=" * 35)
    
    # Download the videos with combined video and audio
    download_videos(args.url, args.directory, args.quality)
