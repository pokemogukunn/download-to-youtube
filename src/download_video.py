import yt_dlp

def download_video(url, format='mp4'):
    # yt-dlpのオプションを設定
    ydl_opts = {
        'format': format,  # ダウンロードするフォーマット
        'outtmpl': 'data/downloads/%(title)s.%(ext)s',  # 保存先のテンプレート
    }
    
    # yt-dlpを使って動画をダウンロード
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = 'https://www.youtube.com/watch?v=VIDEO_ID'  # ダウンロードする動画のURLを指定
    download_video(video_url)
