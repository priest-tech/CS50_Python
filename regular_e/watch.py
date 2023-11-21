import re
import sys


def main():
    print(parse(input("HTML: ")))


# Extract the URL from the provided HTML
def parse(s):

    match = re.search(r"(?:https?:\/\/)?(?:www\.)?(?:youtu\.be\/|youtube\.com\/embed\/)([\w-]+)")
    if match:
        return match.group(1)
    else:
        return None

       


...


if __name__ == "__main__":
    main()