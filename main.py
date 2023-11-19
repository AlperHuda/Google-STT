from pydub import AudioSegment
import os
from google.cloud import speech

# ffmpeg ve ffprobe 
ffmpeg_path = r'C:\ffmpeg\ffmpeg.exe'
ffprobe_path = r'C:\ffmpeg\ffprobe.exe'

# Dosya yollarını PATH'e ekleyin
os.environ['PATH'] += os.pathsep + os.path.dirname(ffmpeg_path)
os.environ['PATH'] += os.pathsep + os.path.dirname(ffprobe_path)

def convert_aac_to_mp3(input_file, output_file):
    # AAC dosyasını yükle
    audio = AudioSegment.from_file(input_file, format="aac")

    # MP3 olarak kaydet
    audio.export(output_file, format="mp3")

def split_mp3_and_transcribe(input_file, output_text_file):
    audio = AudioSegment.from_file(input_file, format="mp3")


    chunk_size_bytes = 59999


    chunks = [audio[i:i + chunk_size_bytes] for i in range(0, len(audio), chunk_size_bytes)]

t
    results = []


    for i, chunk in enumerate(chunks):

        temp_chunk_path = f"temp_chunk_{i}.mp3"
        chunk.export(temp_chunk_path, format="mp3")


        with open(temp_chunk_path, 'rb') as f:
            mp3_data = f.read()


        audio_file = speech.RecognitionAudio(content=mp3_data)


        response = client.recognize(config=config, audio=audio_file)


        results.extend(result.alternatives[0].transcript for result in response.results)


        os.remove(temp_chunk_path)


    with open(output_text_file, 'w') as text_file:
        for result in results:
            text_file.write(f"{result}\n")

    print(f"Transcription completed. Result saved to: {output_text_file}")


aac_file_path = "dosya.aac"  # AAC dosyasının yolu
mp3_file_path = "dosya.mp3"  # MP3 dosyasının kaydedileceği yol


# Google Cloud Speech-to-Text API'ye bağlan
client = speech.SpeechClient.from_service_account_file('key.json')

# RecognitionConfig ayarları
config = speech.RecognitionConfig(
    sample_rate_hertz=48000,
    language_code='tr-TR',
    model="latest_long",
)
convert_aac_to_mp3(input_file_path, converted_file_path)

output_text_file = "Combined_Output.txt"  
split_mp3_and_transcribe(mp3_file_path, output_text_file)
