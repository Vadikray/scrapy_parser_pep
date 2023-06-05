import re

import scrapy
from pep_parse.items import PepParseItem

from constants import MAIN_PEP_URL, DOMAINS_PEP


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [DOMAINS_PEP]
    start_urls = [MAIN_PEP_URL]

    def parse(self, response):
        pep_links = response.css(
            'section[id=numerical-index] tbody a::attr(href)'
        )
        for link in pep_links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        name = response.css('h1.page-title::text').get()
        number = re.search(r'\d+', name)
        data = {
            'number': number[0],
            'name': name,
            'status': response.css(
                'dt:contains("Status") + dd abbr::text').get(),
        }
        yield PepParseItem(data)
