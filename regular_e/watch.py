import re
import sys


def main():
    print(parse(input("HTML: ")))


# Extract the URL from the provided HTML
def parse(s):
    match = re.search(r'<iframe[^>]*\ssrc=["\'](https?://(?:www\.)?youtube\.com/embed/([^"\']+))', s)
    if match:
        complete_url = match.group(1)  # Extract the complete URL
        video_id = match.group(2)  # Extract the video ID
        return f'{complete_url[:-11].replace("/embed/", "/")}/{video_id}'  # Construct the shorter youtu.be URL
    else:
        return None

       


...


if __name__ == "__main__":
    main()