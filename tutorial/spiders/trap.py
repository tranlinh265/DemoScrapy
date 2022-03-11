import scrapy


class QuotesSpider(scrapy.Spider):
    name = "trap"

    def start_requests(self):
        urls = [
            'https://leagueoflegends.fandom.com/wiki/Trap_(Legends_of_Runeterra)',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        href_urls = response.css('tr td span').xpath('@data-param').getall()

        # print(href_urls)

        result = ""

        for href in href_urls:

            result += " " + href + " ,"
            if href == "05PZ008":
                result += "¥n¥n¥n¥n"

            if href == "05PZ014":
                result += "¥n¥n¥n¥n"

        print(result)
