import scrapy


class QuotesSpider(scrapy.Spider):
    name = "follower"

    def start_requests(self):
        urls = [
            'https://leagueoflegends.fandom.com/wiki/Follower_(Legends_of_Runeterra)',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        href_urls = response.css('tr td span').xpath('@data-param').getall()

        print(href_urls)

        result = ""

        for href in href_urls:

            result += " " + href + " ,"
            if href == "05PZ031T1":
                result += "¥n¥n¥n¥n"

            if href == "04SH059":
                result += "¥n¥n¥n¥n"

        print(result)
