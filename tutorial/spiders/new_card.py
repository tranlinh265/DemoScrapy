import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://dak.gg/lor/sets/a-curious-journey',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        href_urls = response.css('li.new-cards__item a::attr(href)').getall()
        result = ""
        result2 = ""
        for href in href_urls:
            href = href.replace(
                "//dd.b.pvp.net/latest/set5/en_us/img/cards/", "")
            href = href.replace(".png", "")
            print(href)
            result += href + ","
            result2 += "'" + href + "' "
        print(result)
        print(result2)
