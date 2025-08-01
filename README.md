# 🌐 LinkExtractor

A simple Python script to extract all hyperlinks from any web page! 🚀

## 📋 Description

This program prompts the user to enter a URL, fetches the web page, and extracts all the `<a>` links found on it. It uses [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for HTML parsing and `requests` for HTTP requests.

## 🛠️ How It Works

1. The script asks you to input a URL.
2. It sends a GET request to the provided URL with a custom User-Agent.
3. If the request is successful, it parses the HTML and collects all the hyperlinks (`<a href="...">`).
4. All extracted links are printed in the terminal.

## 📦 Requirements

- Python 3.x
- [requests](https://pypi.org/project/requests/)
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/)

Install dependencies with:

```sh
pip install requests beautifulsoup4