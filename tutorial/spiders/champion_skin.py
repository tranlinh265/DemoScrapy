# import scrapy
# from scrapy.contrib.linkextractors import LinkExtractor


# class ChampionSkinSpider(CrawlSpider):
#     name = "championskin"

#     allowed_domains = ['https://images.contentstack.io/']

#     start_urls = [
#         'https://playruneterra.com/en-sg/news/game-updates/patch-2-19-0-notes/#champion-skins']

#     rules = (
#         # Extract and follow all links!
#         Rule(LinkExtractor(callback='parse_links', follow=True),
#     )

#     def parse_links(self, response):
#         extractor=LinkExtractor(allow=r'lattes\.cnpq\.br/\d+')
#         for link in extractor.extract_links(response):
#             item=LattesItem()
#             item['url']=link.url
