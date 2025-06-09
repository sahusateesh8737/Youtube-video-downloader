#!/usr/bin/env python3
import os
import sys
import subprocess
from yt_dlp import YoutubeDL

def download_playlist(playlist_url, download_dir="downloads"):
    """
    Download all videos from a YouTube playlist using yt-dlp
    
    Args:
        playlist_url (str): The URL of the YouTube playlist
        download_dir (str): Directory where videos will be saved
    """
    try:
        # Create download directory if it doesn't exist
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)
            print(f"Created download directory: {download_dir}")
        
        # Set options for yt-dlp
        options = {
            'format': 'best',                   # Choose the best quality
            'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),  # Output template
            'ignoreerrors': True,              # Skip videos that cannot be downloaded
            'nooverwrites': True,              # Don't overwrite existing files
            'geo_bypass': True,                # Bypass geographical restrictions
            'nocheckcertificate': True,        # Don't check certificates
            'quiet': False,                    # Display progress
            'no_warnings': False,              # Show warnings
            'verbose': False,                  # Not too verbose
            'progress': True                   # Show progress bar
        }
        
        # Create a YoutubeDL object with the options
        with YoutubeDL(options) as ydl:
            # Get playlist info
            playlist_info = ydl.extract_info(playlist_url, download=False)
            
            if 'entries' in playlist_info:
                print(f"Playlist Title: {playlist_info.get('title', 'Unknown')}")
                print(f"Number of videos in playlist: {len(playlist_info['entries'])}")
                
                # Download each video in the playlist
                ydl.download([playlist_url])
                
                print(f"\nDownload complete! All videos saved to '{download_dir}' folder.")
            else:
                print("No videos found in the playlist.")
                return False
                
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False
    
    return True

if __name__ == "__main__":
    # The playlist URL
    playlist_url = "https://youtube.com/playlist?list=PLXwTOG3-tRwgy4lJ9j_CPwpJmr2uCaGH1&si=DKPBeB0U7FpXd8Bo"
    
    # Optional: Allow user to specify a custom download directory
    download_dir = "youtube_downloads"
    if len(sys.argv) > 1:
        download_dir = sys.argv[1]
    
    print("Starting YouTube Playlist Downloader...")
    print(f"Playlist URL: {playlist_url}")
    print(f"Videos will be saved to: {download_dir}")
    
    # Download the playlist
    download_playlist(playlist_url, download_dir)