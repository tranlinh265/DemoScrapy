import scrapy


class QuotesSpider(scrapy.Spider):
    name = "spellfocus"

    def start_requests(self):
        urls = [
            'https://leagueoflegends.fandom.com/wiki/Spell_(Legends_of_Runeterra)#Focus',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        href_urls = response.xpath('//div[@class="wds-tab__content wds-is-current"]')

        result = ""

        for href in href_urls:
            test = href.css('tr td span').xpath('@data-param').getall()
            for t in test:
                result += " " + t + " ,"
                if t == "05IO002":
                    result += "¥n¥n¥n¥n"

                if t == "05PZ014":
                    result += "¥n¥n¥n¥n"

            print(result)

