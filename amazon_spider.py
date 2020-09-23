import scrapy
from ..items import AmazontutorialItem
class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    page_num = 2
    start_urls = ['https://www.amazon.com/s?bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&fst=as%3Aoff&qid=1598245788&rnid=1250225011&ref=lp_283155_nr_p_n_publication_date_0']


    def parse(self, response):
        items = AmazontutorialItem()
        product_name = response.css('.a-color-base.a-text-normal::text').extract()
        product_author = response.css('.a-color-secondary .a-size-base.a-link-normal').css('::text').extract()
        product_price = response.css('.a-spacing-top-small .a-price-fraction , .a-spacing-top-small .a-price-whole').css('::text').extract()
        product_imglink = response.css('.s-image::attr(src)').extract()
        product_rating = response.css('.aok-align-bottom').css('::text').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imglink'] = product_imglink
        items['product_rating'] = product_rating

        yield items

        next_page = 'https://www.amazon.com/s?i=stripbooks&bbn=283155&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&dc&page=' + str(AmazonSpiderSpider.page_num) + '&fst=as%3Aoff&qid=1598277629&rnid=1250225011&ref=sr_pg_2'
        if AmazonSpiderSpider.page_num <=100:
            AmazonSpiderSpider.page_num += 1
            yield response.follow(next_page, callback= self.parse)






