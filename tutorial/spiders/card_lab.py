import scrapy
from urllib.parse import unquote

class QuotesSpider(scrapy.Spider):
    name = "cardlab"

    def start_requests(self):
        urls = [
            'https://leagueoflegends.fandom.com/wiki/List_of_cards_from_Labs_(Legends_of_Runeterra)',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        all_guardian = ""

        for i in range(1,106):
            img_xpath = "/html/body/div[4]/div[3]/div[2]/main/div[3]/div[2]/div[1]/table/tbody/tr[" + str(i) + "]/td[1]/span/a/img"
            text_xpath = "/html/body/div[4]/div[3]/div[2]/main/div[3]/div[2]/div[1]/table/tbody/tr[" + str(i) + "]/td[2]/a"
            img_url = response.xpath(img_xpath).xpath('@data-src').getall()
            img_name = response.xpath(img_xpath).xpath('@data-image-key').getall()
            text = response.xpath(text_xpath).xpath('text()').getall()

            if len(img_url) > 0 and len(img_name) > 0 and len(text) > 0:
                img_url1 = img_url[0]
                img_url1 = img_url1.split("/revision")
                img_url1 = img_url1[0]
                img_name1 = img_name[0]
                
                img_name1 = img_name1.replace(".png", "")

                text1 = text[0]
                text1 = unquote(text1)
                all_guardian += " {" + "\"name\": \"" + text1 + "\" , \"nameRef\": \"" + img_name1 +"\" }, "
                print("curl " + img_url1 + " -o " + img_name1 + ".webp")
        print("\n\n\n")
        print(all_guardian + "")