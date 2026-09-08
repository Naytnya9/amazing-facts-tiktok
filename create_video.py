import subprocess
import os

WIDTH = 1080
HEIGHT = 1920

# Create a simple vertical background
subprocess.run([
    "ffmpeg",
    "-y",
    "-f", "lavfi",
    "-i", f"color=c=black:s={WIDTH}x{HEIGHT}:d=10",
    "-frames:v", "1",
    "background.png"
], check=True)

# Create 9:16 video from background + narration
subprocess.run([
    "ffmpeg",
    "-y",
    "-loop", "1",
    "-i", "background.png",
    "-i", "narration.wav",
    "-vf", f"scale={WIDTH}:{HEIGHT}",
    "-c:v", "libx264",
    "-preset", "veryfast",
    "-pix_fmt", "yuv420p",
    "-c:a", "aac",
    "-shortest",
    "-movflags", "+faststart",
    "amazing_fact.mp4"
], check=True)

print("Video created successfully!")
print("Created: amazing_fact.mp4")