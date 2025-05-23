"""Spider to extract information from a /author/show page"""

import scrapy
from scrapy import signals

from ..items import AuthorItem, AuthorLoader

class AuthorSpider(scrapy.Spider):
    name = "author"

    def _set_crawler(self, crawler):
        super()._set_crawler(crawler)
        crawler.signals.connect(self.item_scraped_callback, signal=signals.item_scraped)

    def __init__(self, author_crawl="False", item_scraped_callback=None):
        super().__init__()
        self.item_scraped_callback = item_scraped_callback
        self.author_crawl = str(author_crawl).lower() in {"true", "yes", "y"}
        if self.author_crawl:
            self.start_urls = ["https://goodreads.com/", "https://goodreads.com/author/on_goodreads"]

    def parse(self, response):
        
        url = response.request.url

        if "/blog?page=" in url:
            return

        if url.startswith("https://www.goodreads.com/author/show/"):
            yield self.parse_author(response)

        if not self.author_crawl:
            return

        influence_author_urls = response.css('div.dataItem>span>a[href*="/author/show"]::attr(href)').extract()

        for author_url in influence_author_urls:
            yield response.follow(author_url, callback=self.parse)

        similar_authors = response.css('a[href*="/author/similar"]::attr(href)').extract_first()
        if similar_authors:
            yield response.follow(similar_authors, callback=self.parse)

        all_authors_on_this_page = response.css('a[href*="/author/show"]::attr(href)').extract()
        for author_url in all_authors_on_this_page:
            yield response.follow(author_url, callback=self.parse)

    def parse_author(self, response):
        loader = AuthorLoader(AuthorItem(), response=response)
        loader.add_value('author_id', str(response.request.url).split('/')[-1])
        loader.add_css("name", 'h1.authorName>span[itemprop="name"]::text')
        loader.add_css("birthDate", 'div.dataItem[itemprop="birthDate"]::text')
        loader.add_css("deathDate", 'div.dataItem[itemprop="deathDate"]::text')
        loader.add_css("genres", 'div.dataItem>a[href*="/genres/"]::text')
        loader.add_css("influences", 'div.dataItem>span>a[href*="/author/show"]::text')
        loader.add_css("avgRating", 'span.average[itemprop="ratingValue"]::text')
        loader.add_css("reviewsCount", 'span[itemprop="reviewCount"]::attr(content)')
        loader.add_css("ratingsCount", 'span[itemprop="ratingCount"]::attr(content)')
        loader.add_css("about", 'div.aboutAuthorInfo')
        loader.add_css('authorImage', 'img[itemprop="image"]::attr(src)')
        return loader.load_item()

