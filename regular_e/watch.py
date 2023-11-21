import re
import sys


def main():
    print(parse(input("HTML: ")))


# Extract the URL from the provided HTML
def parse(s):
    match = re.search(r'<iframe[^>]*\ssrc=["\'](https?://(?:www\.)?youtube\.com/embed/([^"\']+))', s)
    if match:
        protocol = match.group(1)[:5]  # Extract the protocol (http or https)
        video_id = match.group(2)  # Extract the video ID
        return f'{protocol}{video_id}'  # Return the URL with the same protocol as provided
    else:
        return None

       


...


if __name__ == "__main__":
    main()