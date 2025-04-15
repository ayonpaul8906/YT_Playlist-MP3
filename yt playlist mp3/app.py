import os
import yt_dlp

# Function to download YouTube playlist videos as MP3 without FFmpeg
def download_playlist_audio(url):
    download_folder = "downloads"
    
    # Create 'downloads' folder if it doesn't exist
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    # yt-dlp options for downloading audio in the best available format
    ydl_opts = {
        "format": "bestaudio/best",  # Choose best audio available
        "extractaudio": True,  # Extract audio without post-processing (no conversion)
        "outtmpl": os.path.join(download_folder, "%(title)s.%(ext)s"),  # Output file template
        "noplaylist": False,  # Allow playlist downloading
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])  # Download the playlist

# Example usage
playlist_url = "https://youtube.com/playlist?list=PLO7-VO1D0_6MnOoKQGmYNY2OoCOP3GRfm&si=Tj1Oj1UBbI4mEHHp"
download_playlist_audio(playlist_url)

