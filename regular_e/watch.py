import re
import sys


def main():
    print(parse(input("HTML: ")))


# Extract the URL from the provided HTML
def parse(s):

    if re.search(r"\bhttps?://\S+", s):
        return re.search(r"\bhttps?://\S+", s).group(0)
    else:
        return None
    

       


...


if __name__ == "__main__":
    main()