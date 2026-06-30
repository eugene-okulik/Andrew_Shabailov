from playwright.sync_api import Page


def test_fill_auth_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')

    page.get_by_placeholder('First Name').fill('Andrew')
    page.get_by_placeholder('Last Name').fill('Shabailov')
    page.get_by_placeholder('name@example.com').fill('andrew@mail.ru')
    page.locator('[value="Male"]').check()
    page.get_by_placeholder('Mobile Number').fill('375252267900')

    date_of_birth = page.locator('#dateOfBirthInput')
    date_of_birth.press('Control+a')
    date_of_birth.fill('18 Nov 1992')

    subjects = page.locator('.subjects-auto-complete__input-container')
    subjects.click()
    subjects.press_sequentially('P')
    subjects.press('Enter')

    page.locator('#hobbies-checkbox-1').check()
    page.get_by_placeholder('Current Address').fill('USA, Huston, st.Anderson')

    page.locator("#stateCity-wrapper").scroll_into_view_if_needed()

    page.locator("#state").click()
    page.get_by_role("option", name="Rajasthan").click()

    page.locator("#city").click()
    page.get_by_role("option", name="Jaiselmer").click()

    page.get_by_role("button", name="Submit").click()
