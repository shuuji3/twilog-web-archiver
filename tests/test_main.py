from bs4 import BeautifulSoup

from twilog_web_archiver.main import get_month_links, get_soup, archive_month_pages


def test_get_month_links():
    """The user @NHK_PR should have one or more monthly archive pages on twilog.org."""
    month_links = get_month_links('NHK_PR')
    assert len(month_links) > 0


def test_get_soup():
    """`get_soup()` should be able to get `BeautifulSoup` object for example.com, and it should have just one `<h1>` tag."""
    url = 'http://example.com/'
    soup = get_soup(url)
    assert type(soup) is BeautifulSoup
    assert len(soup.select('h1')) == 1


def test_archive_month_pages():
    """`archive_month_pages()` should be called without any errors."""
    archive_month_pages('https://twilog.org/NHK_PR/month-0912')


def test_archive_month_pages_with_2pages():
    """`archive_month_pages()` can archive more than two pages."""
    archive_month_pages('https://twilog.org/nhk_space/month-1802')
