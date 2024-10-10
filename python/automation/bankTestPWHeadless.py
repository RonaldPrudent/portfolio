from playwright.sync_api import Page


def test_parabanksmoketest(page: Page):
    page.goto("https://parabank.parasoft.com/parabank/index.htm")  # Go to this URL/webpage
    assert page.title() == "ParaBank | Welcome | Online Banking"  # Assert that this is the title of the current page

    # Assert that this text is visible on the page
    assert page.get_by_text("Customer Login").is_visible()
    assert page.get_by_text("Username").is_visible()
    assert page.get_by_text("Password").is_visible()

    # Enter this text into the textbox
    page.locator("//*[@id='loginPanel']/form/div[1]/input").fill("john")
    page.locator("//*[@id='loginPanel']/form/div[2]/input").fill("demo")
    # Click this button
    page.locator("//*[@id='loginPanel']/form/div[3]/input").click()

    # Wait for the next screen to load
    page.locator("//*[@id='showOverview']/h1").wait_for()
    # Make sure that this is the title of the current page
    assert page.title() == "ParaBank | Accounts Overview"
    # Make sure this heading is visible
    assert page.get_by_role("heading", name="Accounts Overview").is_visible()
    # Make sure the text below is visible on screen
    assert page.get_by_text("Welcome").is_visible()
    assert page.get_by_text(" John Smith").is_visible()
    # Make note of the first account number on the Accounts Table
    topAccount = page.locator("//*[@id='accountTable']/tbody/tr[1]/td[1]/a").text_content()
    # Click the account
    page.locator("//*[@id='accountTable']/tbody/tr[1]/td[1]/a").click()

    # Make sure that this is the title of the current page
    assert page.title() == "ParaBank | Account Activity"
    # Make sure this heading is visible
    assert page.get_by_role("heading", name="Account Details")
    # Make sure the account number is correct
    accountId = page.get_by_text(topAccount).text_content()
    assert accountId == topAccount
    # Make sure this link is visible
    page.locator("#headerPanel").get_by_role("link", name="About Us").is_visible()
    # Click the link
    page.locator("#headerPanel").get_by_role("link", name="About Us").click()

    # Make sure that this is the title of the current page
    assert page.title() == "ParaBank | About Us"
    # Make sure this text is on the screen
    assert page.get_by_text("ParaSoft Demo Website").is_visible()
    assert page.locator("//*[@id='rightPanel']/p[2]").text_content()
    assert page.locator("//*[@id='rightPanel']/p[2]").text_content() == "In other words: ParaBank is not a real bank!"
    assert page.get_by_text("Log Out").is_visible()
    # Log Out
    page.get_by_text("Log Out").click()

    assert page.title() == "ParaBank | Welcome | Online Banking"  # Assert that this is the title of the current page

    # Assert that this text is visible on the page
    assert page.get_by_text("Customer Login").is_visible()
    assert page.get_by_text("Username").is_visible()
    assert page.get_by_text("Password").is_visible()
