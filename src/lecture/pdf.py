import asyncio
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page()
        await pg.goto('file:///home/claude/lecture/lecture.html'); await pg.evaluate('document.fonts.ready'); await pg.wait_for_timeout(500)
        await pg.pdf(path='/home/claude/lecture/onkobari-ssc-gm-ch3.1-lecture-sheet.pdf',format='A4',print_background=True,margin={'top':'14mm','bottom':'16mm','left':'13mm','right':'13mm'},
          display_header_footer=True,header_template='<span></span>',footer_template='<div style="font-size:8px;width:100%;text-align:center;color:#9a6b00;font-family:sans-serif">অংকবাড়ি+ · SSC সাধারণ গণিত · অনুশীলনী ৩.১ · <span class="pageNumber"></span>/<span class="totalPages"></span></div>')
        await b.close()
asyncio.run(main())
