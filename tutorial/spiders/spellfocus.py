import scrapy


class QuotesSpider(scrapy.Spider):
    name = "spellfocus"

    def start_requests(self):
        urls = [
            'https://leagueoflegends.fandom.com/wiki/Spell_(Legends_of_Runeterra)/Focus',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        href_urls = response.css('tr td span').xpath('@data-param').getall()

        result = ""

        for href in href_urls:

            result += " " + href + " ,"
            if href == "05PZ030":
                result += "--------"

            if href == "01IO031":
                result += "--------"

            if href == "05BC145":
                result += "--------"
           
        print(result)
