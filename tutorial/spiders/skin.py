import scrapy
from urllib.parse import unquote

class QuotesSpider(scrapy.Spider):
    name = "skin"
    result1 = []
    result2 = []
    result3 = []

    def start_requests(self):
        urls = [
            '/wiki/01DE012_(Legends_of_Runeterra)',
            '/wiki/01DE012T1_(Legends_of_Runeterra)',
            '/wiki/01DE022_(Legends_of_Runeterra)',
            '/wiki/01DE022T1_(Legends_of_Runeterra)',
            '/wiki/01DE042_(Legends_of_Runeterra)',
            '/wiki/01DE042T2_(Legends_of_Runeterra)',
            '/wiki/01DE045_(Legends_of_Runeterra)',
            '/wiki/01DE045T1_(Legends_of_Runeterra)',
            '/wiki/01FR009_(Legends_of_Runeterra)',
            '/wiki/01FR009T1_(Legends_of_Runeterra)',
            '/wiki/01FR024_(Legends_of_Runeterra)',
            '/wiki/01FR024T3_(Legends_of_Runeterra)',
            '/wiki/01FR024T4_(Legends_of_Runeterra)',
            '/wiki/01FR038_(Legends_of_Runeterra)',
            '/wiki/01FR038T2_(Legends_of_Runeterra)',
            '/wiki/01FR039_(Legends_of_Runeterra)',
            '/wiki/01FR039T2_(Legends_of_Runeterra)',
            '/wiki/01IO009_(Legends_of_Runeterra)',
            '/wiki/01IO009T2_(Legends_of_Runeterra)',
            '/wiki/01IO015_(Legends_of_Runeterra)',
            '/wiki/01IO015T1_(Legends_of_Runeterra)',
            '/wiki/01IO032_(Legends_of_Runeterra)',
            '/wiki/01IO032T1_(Legends_of_Runeterra)',
            '/wiki/01IO041_(Legends_of_Runeterra)',
            '/wiki/01IO041T1_(Legends_of_Runeterra)',
            '/wiki/01NX006_(Legends_of_Runeterra)',
            '/wiki/01NX006T1_(Legends_of_Runeterra)',
            '/wiki/01NX020_(Legends_of_Runeterra)',
            '/wiki/01NX020T3_(Legends_of_Runeterra)',
            '/wiki/01NX038_(Legends_of_Runeterra)',
            '/wiki/01NX038T2_(Legends_of_Runeterra)',
            '/wiki/01NX042_(Legends_of_Runeterra)',
            '/wiki/01NX042T2_(Legends_of_Runeterra)',
            '/wiki/01PZ008_(Legends_of_Runeterra)',
            '/wiki/01PZ008T2_(Legends_of_Runeterra)',
            '/wiki/01PZ036_(Legends_of_Runeterra)',
            '/wiki/01PZ036T1_(Legends_of_Runeterra)',
            '/wiki/01PZ040_(Legends_of_Runeterra)',
            '/wiki/01PZ040T1_(Legends_of_Runeterra)',
            '/wiki/01PZ056_(Legends_of_Runeterra)',
            '/wiki/01PZ056T10_(Legends_of_Runeterra)',
            '/wiki/01SI030_(Legends_of_Runeterra)',
            '/wiki/01SI030T2_(Legends_of_Runeterra)',
            '/wiki/01SI042_(Legends_of_Runeterra)',
            '/wiki/01SI042T1_(Legends_of_Runeterra)',
            '/wiki/01SI052_(Legends_of_Runeterra)',
            '/wiki/01SI052T1_(Legends_of_Runeterra)',
            '/wiki/01SI053_(Legends_of_Runeterra)',
            '/wiki/01SI053T2_(Legends_of_Runeterra)',
            '/wiki/02BW022_(Legends_of_Runeterra)',
            '/wiki/02BW022T2_(Legends_of_Runeterra)',
            '/wiki/02BW026_(Legends_of_Runeterra)',
            '/wiki/02BW026T3_(Legends_of_Runeterra)',
            '/wiki/02BW032_(Legends_of_Runeterra)',
            '/wiki/02BW032T3_(Legends_of_Runeterra)',
            '/wiki/02BW046_(Legends_of_Runeterra)',
            '/wiki/02BW046T3_(Legends_of_Runeterra)',
            '/wiki/02BW053_(Legends_of_Runeterra)',
            '/wiki/02BW053T1_(Legends_of_Runeterra)',
            '/wiki/02DE006_(Legends_of_Runeterra)',
            '/wiki/02DE006T1_(Legends_of_Runeterra)',
            '/wiki/02FR002_(Legends_of_Runeterra)',
            '/wiki/02FR002T3_(Legends_of_Runeterra)',
            '/wiki/02IO006_(Legends_of_Runeterra)',
            '/wiki/02IO006T1_(Legends_of_Runeterra)',
            '/wiki/02NX007_(Legends_of_Runeterra)',
            '/wiki/02NX007T2_(Legends_of_Runeterra)',
            '/wiki/02PZ008_(Legends_of_Runeterra)',
            '/wiki/02PZ008T2_(Legends_of_Runeterra)',
            '/wiki/02SI008_(Legends_of_Runeterra)',
            '/wiki/02SI008T2_(Legends_of_Runeterra)',
            '/wiki/03BW004_(Legends_of_Runeterra)',
            '/wiki/03BW004T3_(Legends_of_Runeterra)',
            '/wiki/03DE011_(Legends_of_Runeterra)',
            '/wiki/03DE011T1_(Legends_of_Runeterra)',
            '/wiki/03FR006_(Legends_of_Runeterra)',
            '/wiki/03FR006T2_(Legends_of_Runeterra)',
            '/wiki/03IO002_(Legends_of_Runeterra)',
            '/wiki/03IO002T1_(Legends_of_Runeterra)',
            '/wiki/03MT009_(Legends_of_Runeterra)',
            '/wiki/03MT009T1_(Legends_of_Runeterra)',
            '/wiki/03MT054_(Legends_of_Runeterra)',
            '/wiki/03MT054T1_(Legends_of_Runeterra)',
            '/wiki/03MT055_(Legends_of_Runeterra)',
            '/wiki/03MT055T1_(Legends_of_Runeterra)',
            '/wiki/03MT056_(Legends_of_Runeterra)',
            '/wiki/03MT056T1_(Legends_of_Runeterra)',
            '/wiki/03MT058_(Legends_of_Runeterra)',
            '/wiki/03MT058T1_(Legends_of_Runeterra)',
            '/wiki/03MT087_(Legends_of_Runeterra)',
            '/wiki/03MT087T1_(Legends_of_Runeterra)',
            '/wiki/03MT217_(Legends_of_Runeterra)',
            '/wiki/03MT217T13_(Legends_of_Runeterra)',
            '/wiki/03NX007_(Legends_of_Runeterra)',
            '/wiki/03NX007T1_(Legends_of_Runeterra)',
            '/wiki/03PZ003_(Legends_of_Runeterra)',
            '/wiki/03PZ003T1_(Legends_of_Runeterra)',
            '/wiki/03SI005_(Legends_of_Runeterra)',
            '/wiki/03SI005T1_(Legends_of_Runeterra)',
            '/wiki/04BW005_(Legends_of_Runeterra)',
            '/wiki/04BW005T2_(Legends_of_Runeterra)',
            '/wiki/04DE008_(Legends_of_Runeterra)',
            '/wiki/04DE008T1_(Legends_of_Runeterra)',
            '/wiki/04FR005_(Legends_of_Runeterra)',
            '/wiki/04FR005T1_(Legends_of_Runeterra)',
            '/wiki/04IO005_(Legends_of_Runeterra)',
            '/wiki/04IO005T2_(Legends_of_Runeterra)',
            '/wiki/04MT008_(Legends_of_Runeterra)',
            '/wiki/04MT008T1_(Legends_of_Runeterra)',
            '/wiki/04NX004_(Legends_of_Runeterra)',
            '/wiki/04NX004T2_(Legends_of_Runeterra)',
            '/wiki/04PZ001_(Legends_of_Runeterra)',
            '/wiki/04PZ001T3_(Legends_of_Runeterra)',
            '/wiki/04SH003_(Legends_of_Runeterra)',
            '/wiki/04SH003T2_(Legends_of_Runeterra)',
            '/wiki/04SH003T3_(Legends_of_Runeterra)',
            '/wiki/04SH019_(Legends_of_Runeterra)',
            '/wiki/04SH019T1_(Legends_of_Runeterra)',
            '/wiki/04SH020_(Legends_of_Runeterra)',
            '/wiki/04SH020T1_(Legends_of_Runeterra)',
            '/wiki/04SH039_(Legends_of_Runeterra)',
            '/wiki/04SH039T1_(Legends_of_Runeterra)',
            '/wiki/04SH047_(Legends_of_Runeterra)',
            '/wiki/04SH047T2_(Legends_of_Runeterra)',
            '/wiki/04SH047T3_(Legends_of_Runeterra)',
            '/wiki/04SH067_(Legends_of_Runeterra)',
            '/wiki/04SH067T1_(Legends_of_Runeterra)',
            '/wiki/04SH067T4_(Legends_of_Runeterra)',
            '/wiki/04SH073_(Legends_of_Runeterra)',
            '/wiki/04SH073T2_(Legends_of_Runeterra)',
            '/wiki/04SH130_(Legends_of_Runeterra)',
            '/wiki/04SH130T2_(Legends_of_Runeterra)',
            '/wiki/04SI005_(Legends_of_Runeterra)',
            '/wiki/04SI005T1_(Legends_of_Runeterra)',
            '/wiki/04SI055_(Legends_of_Runeterra)',
            '/wiki/04SI055T2_(Legends_of_Runeterra)',
            '/wiki/05BC029_(Legends_of_Runeterra)',
            '/wiki/05BC029T5_(Legends_of_Runeterra)',
            '/wiki/05BC041_(Legends_of_Runeterra)',
            '/wiki/05BC041T1_(Legends_of_Runeterra)',
            '/wiki/05BC058_(Legends_of_Runeterra)',
            '/wiki/05BC058T2_(Legends_of_Runeterra)',
            '/wiki/05BC088_(Legends_of_Runeterra)',
            '/wiki/05BC088T2_(Legends_of_Runeterra)',
            '/wiki/05BC093_(Legends_of_Runeterra)',
            '/wiki/05BC093T2_(Legends_of_Runeterra)',
            '/wiki/05BC133_(Legends_of_Runeterra)',
            '/wiki/05BC133T1_(Legends_of_Runeterra)',
            '/wiki/05BC161_(Legends_of_Runeterra)',
            '/wiki/05BC161T1_(Legends_of_Runeterra)',
            '/wiki/05BC163_(Legends_of_Runeterra)',
            '/wiki/05BC163T1_(Legends_of_Runeterra)',
            '/wiki/05BW005_(Legends_of_Runeterra)',
            '/wiki/05BW005T1_(Legends_of_Runeterra)',
            '/wiki/05DE009_(Legends_of_Runeterra)',
            '/wiki/05DE009T1_(Legends_of_Runeterra)',
            '/wiki/05FR013_(Legends_of_Runeterra)',
            '/wiki/05FR013T4_(Legends_of_Runeterra)',
            '/wiki/05IO004_(Legends_of_Runeterra)',
            '/wiki/05IO004T2_(Legends_of_Runeterra)',
            '/wiki/05MT003_(Legends_of_Runeterra)',
            '/wiki/05MT003T2_(Legends_of_Runeterra)',
            '/wiki/05NX001_(Legends_of_Runeterra)',
            '/wiki/05NX001T1_(Legends_of_Runeterra)',
            '/wiki/05NX001T3_(Legends_of_Runeterra)',
            '/wiki/05PZ006_(Legends_of_Runeterra)',
            '/wiki/05PZ006T2_(Legends_of_Runeterra)',
            '/wiki/05PZ022_(Legends_of_Runeterra)',
            '/wiki/05PZ022T1_(Legends_of_Runeterra)',
            '/wiki/05SH014_(Legends_of_Runeterra)',
            '/wiki/05SH014T1_(Legends_of_Runeterra)',
            '/wiki/05SH014T2_(Legends_of_Runeterra)',
            '/wiki/05SI009_(Legends_of_Runeterra)',
            '/wiki/05SI009T1_(Legends_of_Runeterra)'
        ]
        for url in urls:
            url = 'https://leagueoflegends.fandom.com' + url
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        href_urls = response.xpath('//a[@class="image"]').xpath('@href').getall()

        all_guardian = ""
        all_href = ""
        all_curl = ""
        
        # print("\n\n\n")
        for href in href_urls:

            if ("-full.png" in href) and ("_" in href):
                x = href.split('/revision/')
                image_url = x[0]
                # image_url = image_url.replace(".png", ".gif")
                y = x[0].split("/")
                image_name = y[len(y) - 1]
                image_name = image_name.replace(".png", "")
                image_name = unquote(image_name)
                
                replaced_image_name = image_name.replace("LoR_", "")
                replaced_image_name = replaced_image_name.split("_")
                replaced_image_name = replaced_image_name[1]
                replaced_image_name = replaced_image_name.replace("-full", "")
                
                unquote_name = unquote(replaced_image_name)

                if image_name not in all_guardian:
                    all_guardian += " {" + "\"name\": \"" + unquote_name + "\" , \"nameRef\": \"" + image_name +"\" }, "
                    all_href += " " + image_url + " , "
                    # print("curl " + image_url + " -o " + image_name + ".webp")
        # print("\n\n\n")
        # print(all_href)
        # print("\n\n\n")
        print(all_guardian + "")


        