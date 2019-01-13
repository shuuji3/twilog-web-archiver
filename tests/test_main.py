from bs4 import BeautifulSoup

from twilog_web_archiver.main import get_month_links, get_soup, parse_month


def test_get_month_links():
    """@NHK_PR は 1 つ以上の月別アーカイブページを持つ。"""
    month_links = get_month_links('NHK_PR')
    assert len(month_links) > 0


def test_get_soup():
    """get_soup() は example.com の BeautifulSoup オブジェクトを取得し、ちょうど 1 つの <h1> タグを持つ。"""
    url = 'http://example.com/'
    soup = get_soup(url)
    assert type(soup) is BeautifulSoup
    assert len(soup.select('h1')) == 1


def test_parse_month():
    """エラーなしに終了する。"""
    parse_month('https://twilog.org/NHK_PR/month-0912')


def test_parse_month_with_2pages():
    parse_month('https://twilog.org/nhk_space/month-1802')
