#!/bin/bash

rm -rf .venv
uv venv
source .venv/bin/activate && uv pip install -r requirements.txt
python3 main.py

for file in $(ls ./downloads/raw); do
    file_number=$(echo $file | cut -d '.' -f1)
    video_path="./downloads/raw/$file"
    echo "✅ Generating transcript for $video_path"
    TORCH_DEVICE=mps whisper $video_path --model tiny --output_dir="./downloads/transcripts" --output_format="srt"
    srt_path="./downloads/transcripts/$file_number.srt"
    echo "✅ Adding subtitles to the video $video_path"
    ffmpeg -i "$video_path" -vf subtitles="$srt_path" "./downloads/transformed/${file_number}.mp4"
done

