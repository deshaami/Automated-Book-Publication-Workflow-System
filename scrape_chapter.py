from playwright.sync_api import sync_playwright
import os

URL = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
OUTPUT_DIR = "output"

os.makedirs(OUTPUT_DIR, exist_ok=True)

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # use headless=False for debugging
        page = browser.new_page()
        page.goto(URL, timeout=60000)

        # ✅ Wait explicitly for the content to load
        page.wait_for_selector("div#mw-content-text", timeout=60000)

        # ✅ Screenshot full page
        page.screenshot(path=os.path.join(OUTPUT_DIR, "chapter1_screenshot.png"), full_page=True)

        # ✅ Extract visible text
        content = page.inner_text("div#mw-content-text")

        with open(os.path.join(OUTPUT_DIR, "chapter1_text.txt"), "w", encoding="utf-8") as f:
            f.write(content)

        print("✅ Screenshot and text saved.")

        browser.close()

if __name__ == "__main__":
    run()
