import os
from playwright.sync_api import sync_playwright

def verify_modules():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load local index.html
        file_path = os.path.abspath('index.html')
        page.goto(f'file://{file_path}')

        # 1. Verify Menu Links
        menu_items = page.locator('.menu-container .menu').all_text_contents()
        print(f"Menu Items: {menu_items}")
        assert "篮球" in menu_items
        assert "日常" in menu_items

        # 2. Verify Modules Section
        modules_count = page.locator('.modules-section a').count()
        print(f"Modules Count: {modules_count}")
        assert modules_count == 5

        # 3. Verify Navigation to Daily Page
        page.click('text=日常')
        assert "daily.html" in page.url

        # 4. Verify Daily Page Content
        assert "日常板块" in page.content()
        assert "2026.01.12 星期一" in page.content()

        # Take screenshot of Daily page
        page.screenshot(path='verification/daily_page.png', full_page=True)

        # 5. Verify Navigation to Post
        page.click('text=2026.01.12 星期一')
        assert "20260112-xing-qi-yi" in page.url
        assert "# 日常" in page.content()

        # Take screenshot of Post page
        page.screenshot(path='verification/post_page.png', full_page=True)

        browser.close()

if __name__ == "__main__":
    verify_modules()
