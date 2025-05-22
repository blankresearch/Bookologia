import scrapy
from .author_spider import AuthorSpider
from .book_spider import BookSpider
from ..items import BookItem, BookLoader
import random 

class GoodreadsSpider(scrapy.Spider):
    name = "goodreads"
    
    def __init__(self, start_id=1, end_id=10, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start_id = int(start_id)
        self.end_id = int(end_id)
        self.book_spider = BookSpider()

    def start_requests(self):
        for book_id in range(self.start_id, self.end_id + 1):
            url = f"https://www.goodreads.com/book/show/{book_id}"
            yield scrapy.Request(
                url, 
                callback=self.parse,
                meta={'book_id': book_id}
            )

    def parse(self, response):
        yield from self.book_spider.parse(response)
        
