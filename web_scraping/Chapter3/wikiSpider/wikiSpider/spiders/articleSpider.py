from scrapy.spiders import CrawlSpider, Rule
from wikiSpider.items import Article
from scrapy.linkextractors.sgml import SgmlLinkExtractor


# has bug in Python3:
# from sgmllib import SGMLParser
# ImportError: No module named 'sgmllib'
class ArticleSpider(CrawlSpider):
    name = "article"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = [
        "https://en.wikipedia.org/wiki/Python_%28programming_language%29"]
    rules = [Rule(SgmlLinkExtractor(allow=("(/wiki/)((?!:).)*$"),),
                  callback="parse_item", follow=True)]

    def parse(self, response):
        item = Article()
        title = response.xpath('//h1/text()')[0].extract()
        print("Title is: " + title)
        item['title'] = title
        return item

# scrapy crawl article -s LOG_FILE=wiki.log
