import feedparser
import re
import requests
from tqdm import tqdm
import os
import shutil


RAW_DIR_PREFIX = "./downloads/raw/"
TRANSCRIPT_DIR_PREFIX = "./downloads/transcripts"
TRANSFORMED_DIR_PREFIX = "./downloads/transformed"
try:
    shutil.rmtree(RAW_DIR_PREFIX)
    shutil.rmtree(TRANSCRIPT_DIR_PREFIX)
    shutil.rmtree(TRANSFORMED_DIR_PREFIX)
except FileNotFoundError as e:
    print(f"warning - skipping: directory does not exist : {e}")

print(
    f"""
✅ crearing directories:
1  {RAW_DIR_PREFIX}
2. {TRANSCRIPT_DIR_PREFIX}
3. {TRANSFORMED_DIR_PREFIX}
"""
)
os.makedirs(RAW_DIR_PREFIX, exist_ok=True)
os.makedirs(TRANSCRIPT_DIR_PREFIX, exist_ok=True)
os.makedirs(TRANSFORMED_DIR_PREFIX, exist_ok=True)


def download_video(url):
    response = requests.get(
        url, stream=True
    )  # Download the video content in chunks
    # Get the total file size if available in headers
    total_size = int(response.headers.get("content-length", 0))

    # Open the file in binary write mode
    video_id = re.search("\d+", url).group()
    file_name = RAW_DIR_PREFIX + video_id + ".mp4"

    # Create a progress bar
    progress_bar = tqdm(
        total=total_size,
        unit="B",
        unit_scale=True,
        unit_divisor=1024,
        desc=f"Downloading {file_name}",
    )

    with open(file_name, "wb") as file:
        for chunk in response.iter_content(
            chunk_size=8192
        ):  # Adjust chunk size as needed
            if chunk:
                file.write(chunk)
                progress_bar.update(len(chunk))

    progress_bar.close()
    print(f"\nDownload complete! File saved as {file_name}")


url = "http://www.ted.com/talks/rss"
parsed = feedparser.parse(url)
entries = parsed["entries"]
urls = [i["links"][0]["href"] for i in entries][:5]

for url in urls:
    download_video(url)
