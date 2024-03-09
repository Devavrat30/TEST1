import scrapy
from ..items import QuoteItem
class fetchQuote(scrapy.Spider):
    name='quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response):

        items = QuoteItem()
        allQuotes=response.css('div.quote')

        for i in allQuotes:
            qte=i.css('span.text::text').extract()
            auth=i.css('.author::text').extract()

            items['qte']=qte
            items['auth']=auth

            yield items