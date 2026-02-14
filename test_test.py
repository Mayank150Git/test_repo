from playwright.sync_api import Page


def test_tc1(page:Page):
    page.goto('http://python.org')
    print(page.url)
