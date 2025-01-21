from playwright.sync_api import Browser, Page, sync_playwright
from datetime import timedelta, date
import getpass


def generate_github_pat(
    username: str,
    password: str,
    token_name: str,
    scopes: list[str],
    browser_type="chromium",
):
    if len(username) == 0:
        print("Provide a valid username")
        return
    if len(password) == 0:
        print("password cannot be of length 0")
        return
    """
    Function to automate the generate of Github Personal Access token
    with playwright

    Args:
    username: str - Github username
    pasword: str - Github pasword
    token_name: str - Name/desc for the token
    scopes: list[str] - list of scopes for the token
    """
    with sync_playwright() as p:
        if browser_type == "firefox":
            browser: Browser = p.firefox.launch(headless=False)  # True for headless
        elif browser_type == "webkit":
            browser: Browser = p.webkit.launch(headless=False)  # True for headless
        else:
            browser: Browser = p.chromium.launch(headless=False)  # True for headless
        page: Page = browser.new_page()

        # Navigate to github login page
        page.goto("https://github.com/login")
        # Enter login details and login
        if page.url.__contains__("login"):
            login_page(username, password, page)

        # 2FA
        if page.url.startswith("https://github.com/sessions/verified-device"):
            print("2FA, verfiy manually.")
            page.pause()

        # navigate to new token page
        page.goto("https://github.com/settings/tokens/new/")

        if page.url.__contains__("login"):
            login_page(username, password, page)

        if page.url.startswith("https://github.com/sessions/verified-device"):
            print("2FA, verfiy manually.")
            page.pause()

        # Fill in the token details
        page.fill("input#oauth_access_description", token_name)

        # Set token expiration to 90 days
        page.get_by_role("button", name="30 days").click()
        page.get_by_text("90 days").wait_for(state="visible")
        page.get_by_text("90 days").click()

        # check all the checkboxes for scope
        for scope in scopes:
            checkbox_selector = f'input[value="{scope}"]'
            page.check(checkbox_selector)

        #        Generate the token
        page.get_by_role("button", name="Generate token").click()

        page.locator("code#new-oauth-token").wait_for(state="visible")
        # output the token
        end_date = date.today() + timedelta(days=90)
        print(
            f"Github PAT ={page.locator('code#new-oauth-token').text_content()} ({end_date})"
        )

        browser.close()


def login_page(username: str, password: str, page: Page):
    page.fill("input#login_field", username)
    page.fill("input#password", password)
    page.click("input[type=submit]")


# username: str = str(os.environ.get("GITHUB_USERNAME"))
# password: str = str(os.environ.get("GITHUB_PASSWORD"))
username: str = input("Enter github username: ")
password: str = getpass.getpass()
token_name: str = "Test Token"
scopes: list[str] = [
    "repo",
    "admin:org",
    "admin:repo_hook",
    "user",
    "admin:enterprise",
]
generate_github_pat(
    username=username, password=password, token_name=token_name, scopes=scopes
)
