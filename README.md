# Video Transcribing ETL Pipeline 🚀

## Description

This repository contains scripts for an ETL Pipeline that transcribes and transforms video by ffmpeg and OpenAI Whisper.

The Pipeline does the following:

- Extracts the data from the official TED API.
- Downloads the videos.
- Transcribes using OpenAI's whisper.
- Transforms (attaches transcription) using ffmpeg.
- Loads the data into an S3 Bucket.

## Prerequisites & Dependencies

- python3
- experience with APIs
- ffmpeg
- AWS Account (free tier)

## Getting Started

#### 1. Cloning the repo:

```shell
https://github.com/vinamrgrover/etl-video-proc.git
```

#### 2. Installing ffmpeg and uv

```shell
sudo apt-get update -y && sudo apt-get install ffmpeg && sudo snap install astral-uv --classic
```

#### 3. Running the script

```shell
chmod +x exec.sh
./exec.sh
```

That's all! You'll find all the generated data inside `downloads` directory.

Here's the output for `tree` command (partial - for demonstration):

```shell
.
├── raw
│   ├── 196184.mp4
│   ├── 197416.mp4
│   ├── 197690.mp4
│   ├── 197963.mp4
│   └── 198099.mp4
├── requirements.txtcd
├── transcripts
└── transformed
```

#### 4. Last and final step - Copying to S3!

```shell
aws s3 sync ./downloads/ s3://<your-bucket-name>/downloads/
```

Make sure to replace `<your_bucket_name>` with name of your official S3 Bucket.
