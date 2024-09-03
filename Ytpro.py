import yt_dlp

def download_video_or_audio(url, format_choice):
    ydl_opts = {}

    if format_choice == 'mp4':
        ydl_opts = {
            'format': 'best',  # Descarga el mejor formato disponible que ya contenga video y audio combinados.
            'outtmpl': '%(title)s.%(ext)s',
        }
    elif format_choice == 'mp3':
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
    else:
        print("Opción no válida. Elija 'mp3' o 'mp4'.")
        return

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = input("Ingrese la URL del video de YouTube: ")
    format_choice = input("¿Desea descargar en formato mp3 o mp4?: ").lower()
    download_video_or_audio(url, format_choice)