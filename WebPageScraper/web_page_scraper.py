import os
import re
import requests
from bs4 import BeautifulSoup


class WebParser:
    def __init__(self, url: str, pages_number: int, pages_type: str):
        self.url = url
        self.pages_number = pages_number
        self.pages_type = pages_type

    @staticmethod
    def __get_page(url: str) -> str:
        """
            Getting requested page
            url: str - requested url
            return: str
        """
        retries = 3
        while retries > 0:
            try:
                page = requests.get(url, timeout=10)
                if page.status_code == 200:
                    return page.text
            except requests.exceptions.RequestException:
                pass
            retries -= 1
        raise ValueError("Failed to retrieve page")

    def __save_page(self, link: str, page_number: int) -> None:
        """
            Saving page to device
            link: str - requested url
            page_number: int - quantity of pages
            return: None
        """
        page = self.__get_page(link)
        soup = BeautifulSoup(page, "html.parser")
        parsed_text = soup.get_text()
        name = soup.find('title').text
        text = re.sub(r"\n+", "\n", parsed_text)
        directory = f'page_{page_number}'
        os.makedirs(directory, exist_ok=True)
        file_path = os.path.join(os.getcwd(), directory, f"{name}.txt")
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text)

    def parse(self) -> None:
        """
            Start point of class
            return: None
        """
        for i in range(1, self.pages_number + 1):
            page = self.__get_page(self.url)
            soup = BeautifulSoup(page, "html.parser")
            content = {}
            for elem in soup.select('.u-full-height.c-card.c-card--flush'):
                link = f"https://www.nature.com{elem.select_one('a')['href']}"
                title = elem.select_one('.c-meta__type').text
                if title.startswith(self.pages_type):
                    if title not in content:
                        content[title] = []
                    content[title].append(link)
            for title, links in content.items():
                for link in links:
                    self.__save_page(link, i)
            new_url = soup.select_one('[data-test="page-next"] a')['href']
            self.url = f"https://www.nature.com{new_url}"


def main():
    """ 
        Main method of program
        return: None
    """
    url = "https://www.nature.com/nature/articles?sort=PubD0ate&year=2022&page=1"

    pages_number = get_number_of_pages()
    if pages_number is None:
        print("Invalid number of pages")
        return

    pages_type = get_page_type()

    web_parser = WebParser(url, pages_number, pages_type)

    try:
        web_parser.parse()
    except ValueError as error:
        print(error)
    except KeyboardInterrupt:
        print("OK")

    print("Saved all articles!")


def get_number_of_pages():
    """
        Getter of number_of_pages
        return: int | None
    """
    try:
        return int(input("Enter number of pages: "))
    except ValueError:
        return None


def get_page_type():
    """
        Getter of pages_type
        return: str | None
    """
    return input("Enter type of pages: ").title()


if __name__ == "__main__":
    main()

