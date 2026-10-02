from playwright.sync_api import sync_playwright
import re

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(
        "https://www.cricbuzz.com/live-cricket-scores/155422/ausa-vs-inda-2nd-unofficial-test-australia-a-tour-of-india-2026",
        wait_until="domcontentloaded"
    )

    try:
        body_text = page.locator("body").inner_text()

        match = re.search(r"\d+\s*-\s*\d+|\d+\s*/\s*\d+", body_text)
        if match:
            score = match.group(0)
            print(f"Live Score: {score}")
        else:
            print("No score pattern found in page text.")

        page.screenshot(path="score.png", full_page=True)

    except Exception as e:
        print(f"Error: {e}")

    finally:
        browser.close()