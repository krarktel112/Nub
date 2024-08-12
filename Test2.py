import asyncio
from pyppeteer import launch

async def scraper():
   browser =await launch({"headless": True})
   page = await browser.newPage()
   await page.goto("https://www.scrapingcourse.com/ecommerce/")

   ## get HTML
   await browser.close()
 
asyncio.run(scraper())
