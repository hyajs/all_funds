import scrapy,csv,logging
from bs4 import BeautifulSoup

class AvailableFundsSpider(scrapy.Spider):
    name = 'available_funds'

    def start_requests(self):

        url = 'http://quotes.money.163.com/fund/jzzs_{ID}.html?start=1998-01-09&end=2020-07-30'
        with open('all_funds.csv') as f:
            f_csv = csv.reader(f)
            for row in f_csv:
                matches = row[1][26:32]
                yield scrapy.Request(url.format(ID=matches), meta={'code':matches,'name':row[0]}, callback=self.parse)
        f.close()

    def parse(self, response):
        item = {}

        try:
            bs = BeautifulSoup(response.text,'html.parser')

            tables = bs.find('tbody').find_all('tr')
            for table in tables:
                item['code'] = response.meta['code']
                item['name'] = response.meta['name']
                item['date'] = table.text.split('\n')[1]
                item['networth'] = table.text.split('\n')[2]
                item['current_value'] = table.text.split('\n')[3]
                item['change_percent'] = table.text.split('\n')[4]
                yield item
        except:
            print('wrong! +  url is ' + str(response.request))



