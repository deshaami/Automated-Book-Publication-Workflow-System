import asyncio
import os
from playwright.async_api import async_playwright

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

async def run():
    url = input("🌐 Enter the URL to capture: ")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        try:
            await page.goto(url, timeout=60000)  # 60 sec timeout
            await page.wait_for_load_state('networkidle')  # Wait until page fully loads
            screenshot_path = os.path.join(OUTPUT_DIR, "screenshot.png")
            await page.screenshot(path=screenshot_path, full_page=True)
            print(f"✅ Screenshot saved as {screenshot_path}")
        except Exception as e:
            print(f"❌ Error: {e}")
        finally:
            await browser.close()

if __name__ == "__main__":
    asyncio.run(run())
