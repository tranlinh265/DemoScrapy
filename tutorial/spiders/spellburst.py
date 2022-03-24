import scrapy


class QuotesSpider(scrapy.Spider):
    name = "spellburst"

    def start_requests(self):
        urls = [
            'https://leagueoflegends.fandom.com/wiki/Spell_(Legends_of_Runeterra)/Burst',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        href_urls = response.css('tr td span').xpath('@data-param').getall()

        result = ""

        for href in href_urls:

            result += " " + href + " ,"
            if href == "05SH020":
                result += "¥n¥n¥n¥n"

            if href == "01IO031":
                result += "¥n¥n¥n¥n"

            if href == "05BW006":
                result += "¥n¥n¥n¥n"

        print(result)

