import os
from playwright.sync_api import sync_playwright

def verify_homepage():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load local index.html
        file_path = os.path.abspath('index.html')
        page.goto(f'file://{file_path}')

        # Verify title
        print(f"Title: {page.title()}")
        assert "朱佳烽的博客" in page.title()

        # Verify content
        header_title = page.locator('.site-header .site-title').text_content()
        print(f"Header Title: {header_title}")
        assert "朱佳烽" in header_title

        description = page.locator('.site-header .site-description').text_content()
        print(f"Description: {description}")
        assert "无敌的男人，不接受反驳" in description

        # Take screenshot
        page.screenshot(path='verification/homepage.png', full_page=True)
        browser.close()

if __name__ == "__main__":
    verify_homepage()
