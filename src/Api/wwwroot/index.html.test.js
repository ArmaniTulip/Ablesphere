const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto('http://localhost:5000');

    // Check if the page title is correct
    const title = await page.title();
    if (title !== 'API Documentation') {
        console.error('Title is incorrect:', title);
        process.exit(1);
    }

    // Check if all links are functional
    const links = await page.$$eval('nav ul li a', anchors => anchors.map(a => a.href));
    for (const link of links) {
        try {
            const response = await page.goto(link);
            if (!response.ok()) {
                console.error('Link is broken:', link);
                process.exit(1);
            }
        } catch (error) {
            console.error('Error accessing link:', link, error);
            process.exit(1);
        }
    }

    console.log('All tests passed successfully.');
    await browser.close();
})();