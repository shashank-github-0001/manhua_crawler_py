import argparse

import requests
from bs4 import BeautifulSoup


def get_all_links(url, filter=None):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []

    soup = BeautifulSoup(response.content, "html.parser")
    links = soup.find_all("a", href=True)
    urls = [link["href"] for link in links]
    if filter:
        urls = [url for url in urls if filter in url]

    return urls


def main():
    parser = argparse.ArgumentParser(
        description="given a url it returns all the suburls"
    )
    parser.add_argument("url", type=str, help="the url you want to find suburls for")

    args = parser.parse_args()
    file_path = "urls.txt"

    if args.url == "run":
        with open(file_path, "r") as file:
            for url in file:
                filter = url.split("/")[-2]
                urls = get_all_links(url, filter)
                for a in range(5):
                    print(urls[a])
                print("\n")
    else:
        with open(file_path, "a") as append:
            append.write(args.url + "\n")


if __name__ == "__main__":
    main()
