from playwright.sync_api import sync_playwright


def obter_html(url):

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False
        )

        page = browser.new_page()

        page.goto(
            url,
            wait_until="networkidle"
        )

        html = page.content()

        browser.close()

        return html