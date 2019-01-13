from typing import List

from bs4 import BeautifulSoup
import click
import requests
import savepagenow


def get_month_links(screen_name: str) -> List[str]:
    """Get month link for the screen_name."""
    url = f'https://twilog.org/{screen_name}/archives'
    s = get_soup(url)
    return list(
        filter(lambda x: 'month-' in x, map(lambda x: x['href'], s.select('section.main-list-box1 .side-list li a'))))


def get_soup(url: str) -> BeautifulSoup:
    """Get BeautifulSoup object for the url."""
    r = requests.get(url)
    return BeautifulSoup(r.text, 'lxml')


def parse_month(month_link: str) -> None:
    """Archive all the pages of the month list."""
    archive_url, _ = savepagenow.capture_or_cache(month_link)
    print('archived:', archive_url)
    s = get_soup(month_link)
    next_links = s.select('.nav-next a')
    if len(next_links) != 0:
        next_link = next_links[0]['href']
        parse_month(next_link)


@click.command()
@click.argument('screen_name')
def archive_user_page(screen_name):
    """Archvie all month list pages for the specified screen_name into Wayback Machine."""
    month_links = get_month_links(screen_name)
    for month_link in month_links:
        parse_month(month_link)


def main():
    archive_user_page()


if __name__ == '__main__':
    main()
