import re

import scrapy
from pep_parse.items import PepParseItem

from constants import DOMAINS_PEP


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [DOMAINS_PEP]
    start_urls = [f"https://{domain}/" for domain in allowed_domains]

    def parse(self, response):
        for link in response.css(
            'section[id=numerical-index] tbody a::attr(href)'
        ):
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        name = response.css('h1.page-title::text').get()
        number = re.search(r'\d+', name).group(0)
        yield PepParseItem(
            name=name,
            number=number,
            status=response.css(
                'dt:contains("Status") + dd abbr::text').get()
        )
