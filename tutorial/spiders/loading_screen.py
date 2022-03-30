import scrapy
from urllib.parse import unquote

class QuotesSpider(scrapy.Spider):
    name = "loadingscreen"

    def start_requests(self):
        urls = [
            'https://leagueoflegends.fandom.com/wiki/Board_(Legends_of_Runeterra)',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        href_urls = response.xpath('//a[@class="image"]').xpath('@href').getall()

        all_guardian = "["
        all_href = ""
        print("\n\n\n")
        for href in href_urls:

            if "Loading_Screen" in href:
                x = href.split('/revision/')
                image_url = x[0]
                # image_url = image_url.replace(".png", ".gif")
                y = x[0].split("/")
                image_name = y[len(y) - 1]
                image_name = image_name.replace(".png", "")

                replaced_image_name = image_name.replace("LoR_", "")
                replaced_image_name = replaced_image_name.replace("_", " ")
                
                unquote_name = unquote(replaced_image_name)
                unquote_name = unquote_name.replace(".gif", "")

                if image_name not in all_guardian:
                    all_guardian += " {" + "\"name\": \"" + unquote_name + "\" , \"nameRef\": \"" + image_name +"\" }, "
                    all_href += " " + image_url + " , "
                    print("curl " + image_url + " -o " + image_name + ".webp")
        print("\n\n\n")
        print(all_href)
        print("\n\n\n")
        print(all_guardian + "]")