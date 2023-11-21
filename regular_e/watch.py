import re
import sys


def main():
    print(parse(input("HTML: ")))


# Extract the URL from the provided HTML
def parse(s):
    url= re.findall(r'<iframe[^>]*\ssrc=["\'](https?://(?:www\.)?youtube\.com/embed/[^"\']+)["\']', s)
    if url:
        return url
    else:
        return None
       


...


if __name__ == "__main__":
    main()