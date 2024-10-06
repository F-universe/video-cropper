import os
from moviepy.editor import VideoFileClip

# Definisci le coordinate dell'area da ritagliare
x1, y1 = 127, 275  # Angolo in alto a sinistra
x2, y2 = 414, 809  # Angolo in basso a destra

# Calcola la larghezza e l'altezza del ritaglio
width = x2 - x1
height = y2 - y1

def crop_video(input_video_path, output_video_path):
    try:
        # Carica il video
        video = VideoFileClip(input_video_path)
        
        # Ritaglia il video usando l'area definita
        cropped_video = video.crop(x1=x1, y1=y1, width=width, height=height)
        
        # Salva il video ritagliato in formato mp4
        cropped_video.write_videofile(output_video_path, codec="libx264", audio_codec="aac")  # Cambia codec e formato
        print(f"Video salvato correttamente: {output_video_path}")
    except Exception as e:
        print(f"Errore nel ritagliare il video {input_video_path}: {str(e)}")

def process_all_videos_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith((".mp4", ".avi", ".mkv")):  # Controlla i formati video comuni
            input_video_path = os.path.join(directory, filename)
            output_video_path = os.path.join(directory, f"cropped_{filename}")
            print(f"Ritaglio del video: {input_video_path}")
            crop_video(input_video_path, output_video_path)

if __name__ == "__main__":
    # Percorso della cartella dei video
    video_directory = r"C:\Users\fabio\OneDrive\Desktop\F-universe\instagram(1)\videos"
    
    # Processa tutti i video nella cartella
    process_all_videos_in_directory(video_directory)
