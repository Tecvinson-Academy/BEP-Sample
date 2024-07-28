import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url

    def fetch_page(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the page: {e}")
            return None

    def parse_page(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.find_all('h2')
        return [title.get_text() for title in titles]

    def display_titles(self, titles):
        print("Titles found on the page:")
        for title in titles:
            print(f"- {title}")

if __name__ == "__main__":
    url = "https://example.com"
    scraper = WebScraper(url)
    page_content = scraper.fetch_page()
    if page_content:
        titles = scraper.parse_page(page_content)
        scraper.display_titles(titles)
