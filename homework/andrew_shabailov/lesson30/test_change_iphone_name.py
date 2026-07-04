from playwright.sync_api import Page, expect, Route
import json


def test_change_iphone_name(page: Page):

    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body["body"]["digitalMat"][0]["familyTypes"][0]["productName"] = 'яблокофон 17 про'
        route.fulfill(status=response.status, body=json.dumps(body))

    page.route('**/step0_iphone/**', handle_route)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.wait_for_load_state('networkidle')

    page.get_by_role("button", name="Take a closer look - iPhone 17 Pro & iPhone 17 Pro Max").click()

    pro_title = page.locator('[data-autom="DigitalMat-overlay-header-0-0"]')
    expect(pro_title).to_have_text('яблокофон 17 про')

    page.get_by_role("radio", name="iPhone 17 Pro Max").click()

    pro_max_title = page.locator('[data-autom="DigitalMat-overlay-header-0-1"]')
    expect(pro_max_title).to_have_text('iPhone 17 Pro Max')
