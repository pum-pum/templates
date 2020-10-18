
const puppeteer = require('puppeteer');
(async () => {
  const browser = await puppeteer.launch({headless: false})
  const page = await browser.newPage()
  
  const navigationPromise = page.waitForNavigation()
  
  await navigationPromise
  
  await page.goto('https://www.google.com')
  
  await page.setViewport({ width: 1200, height: 500 })
  
  //await browser.close()
})()
