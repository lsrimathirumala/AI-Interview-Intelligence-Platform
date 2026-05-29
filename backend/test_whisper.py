import whisper
import imageio_ffmpeg
import os

ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()
print("FFmpeg:", ffmpeg_path)
print("Exists:", os.path.exists(ffmpeg_path))

model = whisper.load_model("base")

result = model.transcribe("uploads/sample-speech-1m.mp3")

print(result["text"])