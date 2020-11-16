import scrapy


class TodaysdealSpider(scrapy.Spider):
    name = 'todaysDeal'
    allowed_domains = ['www.amazon.in']
    start_urls = ['https://www.amazon.in/gp/goldbox?ref=nav_topnav_deals/']

    def parse(self, response):
        products = response.xpath('//div[@class="a-section a-spacing-none tallCellView gridColumn4 singleCell"]').extract_first()
        for product in products:
            pass
