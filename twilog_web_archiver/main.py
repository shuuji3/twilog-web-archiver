from typing import List

from bs4 import BeautifulSoup
import click
import requests
from waybackpy import WaybackMachineSaveAPI


def get_month_links(screen_name: str) -> List[str]:
    """Get month link for the screen_name."""
    url = f'https://twilog.org/{screen_name}/archives'
    s = get_soup(url)
    return list(
        filter(
            lambda x: 'month-' in x,
            map(
                lambda x: x['href'], s.select('section.main-list-box1 .side-list li a')
            ),
        )
    )


def get_soup(url: str) -> BeautifulSoup:
    """Get BeautifulSoup object for the url."""
    r = requests.get(url)
    return BeautifulSoup(r.text, 'lxml')


def archive_month_pages(month_link: str) -> None:
    """Archive all the pages of the month list."""
    try:
        save_api = WaybackMachineSaveAPI(month_link)
        archive_url = save_api.archive_url
        cached = save_api.cached_save
        print(f'archived (cached: {cached}): {archive_url}')
    except MaximumSaveRetriesExceeded as e:
        print('⚠ failed to archive the page:')
        print(e)

    s = get_soup(month_link)
    next_links = s.select('.nav-next a')
    if len(next_links) != 0:
        next_link = next_links[0]['href']
        archive_month_pages(next_link)


@click.command()
@click.argument('screen_name')
def archive_user_page(screen_name):
    """Archvie all month list pages for the specified screen_name into Wayback Machine."""
    month_links = get_month_links(screen_name)
    for month_link in month_links:
        archive_month_pages(month_link)


def main():
    archive_user_page()


if __name__ == '__main__':
    main()
