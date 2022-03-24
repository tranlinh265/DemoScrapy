import scrapy


class QuotesSpider(scrapy.Spider):
    name = "spellfast"

    def start_requests(self):
        urls = [
            'https://leagueoflegends.fandom.com/wiki/Spell_(Legends_of_Runeterra)/Fast',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        href_urls = response.css('tr td span').xpath('@data-param').getall()

        result = ""

        for href in href_urls:

            result += " " + href + " ,"
            if href == "05PZ017":
                result += "--------"

            if href == "05SI009T1":
                result += "--------"

            if href == "05BW006T2":
                result += "--------"

        print(result)

