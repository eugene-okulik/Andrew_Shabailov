from playwright.sync_api import Page, Dialog, expect


def test_successful_alert(page: Page):
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    button = page.get_by_role('link', name='Click')

    def accept(alert: Dialog):
        alert.accept()

    page.on('dialog', accept)
    button.click()

    result = page.locator('#result-text')
    expect(result).to_have_text('Ok')
