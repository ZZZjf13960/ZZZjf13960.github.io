import os
from playwright.sync_api import sync_playwright

def verify_modules_retry():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load local index.html
        file_path = os.path.abspath('index.html')
        page.goto(f'file://{file_path}')

        # Navigate to Daily Page
        page.click('text=日常')

        # Navigate to Post
        page.click('text=2026.01.12 星期一')

        # Debug: Check for the tag
        try:
            tag_text = page.locator('.post-tag').first.inner_text()
            print(f"Tag Text Found: '{tag_text}'")
            # Normalize and check
            if "# 日常" in tag_text:
                print("Assertion Passed")
            else:
                print("Assertion Failed: Text does not match")
        except Exception as e:
            print(f"Error finding tag: {e}")
            print(page.content()) # Print content to debug

        page.screenshot(path='verification/retry_post_page.png', full_page=True)
        browser.close()

if __name__ == "__main__":
    verify_modules_retry()
