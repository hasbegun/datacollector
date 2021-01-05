# from .credential import Credential
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
import os
import yaml

NAME = 'MATH226'
UID = '***'
PASSWD='***'

class Math226(scrapy.Spider):
    name = NAME

    def start_requests(self):
        urls = ['https://piazza.com/account/login']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def __save_page(self, file_name, response):
        with open(file_name, 'wb') as f:
            f.write(response.body)
        self.log(f'Save {file_name}')


    def parse(self, response):
        # filename = f'piazza.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Save {filename}')

        self.log('Parse begins...')

        # self.credential = {}
        # credentail_file = os.path.join(os.getcwd(), 'credential.yml')
        # try:
        #     self.credential = yaml.safe_load(open(credentail_file))['default']
        # except yaml.YAMLError as e:
        #     self.log('Unable to load yaml file: %s' % e)
        # except IOError as e:
        #     self.log('File not found: %s' % credentail_file )
        # self.log(self.credential)
        #
        # return [scrapy.FormRequest.from_response(response,
        #         formdata={'email': self.credential.get('uid'),
        #                   'password': self.credential.get('pwd')},
        #                   callback=self.post_login)]
        return [scrapy.FormRequest.from_response(response,
                formdata={'email': UID, 'password': PASSWD},
                callback=self.post_login)]

    def post_login(self, response):
        self.log('Post login...')
        return Request(url='http://piazza.com/sfsu/fall2015/math226?token=ZWKcsp5SRoj',
            callback=self.parse_page)

    def parse_page(self, response):
        self.__save_page('pizaaz-math226.html', response)

        sel = Selector(response)
        yield {'class_name': sel.xpath('//*[@id="topbar_current_class_number"]').get()}
        # yield {'class_name': response.css('span#topbar_current_class_number').extract()}

        # # question groups.
        # qgrp = sel.xpath('//*[@id="question_feed_questions"]')
        # for grp in qgrp.css('.question_group'):
        #     print(grp.extract())
        #     yield {
        #         'title': grp.css('.title_text').get()
        #     }
