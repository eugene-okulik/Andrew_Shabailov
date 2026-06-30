from playwright.sync_api import Page, expect
import re


def test_color_with_timeout(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    color_button  = page.locator('#colorChange')

    expect(color_button).to_have_class(re.compile(r'.*text-danger.*'), timeout=10000)
