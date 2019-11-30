from scrapy import Spider, Request

from mac.items import MacItem

import string 

class MacSpider(Spider):
	name = 'mac_spider'
	allowed_urls = ['https://apps.apple.com/us/genre/mac/id39?mt=12']
	start_urls = ['https://apps.apple.com/us/genre/mac-video/id12020?mt=12&letter=A',
	'https://apps.apple.com/us/genre/mac-video/id12020?mt=12&letter=B', 
	'https://apps.apple.com/us/genre/mac-video/id12020?mt=12&letter=C', 
	'https://apps.apple.com/us/genre/mac-video/id12020?mt=12&letter=D',
	'https://apps.apple.com/us/genre/mac-video/id12020?mt=12&letter=E',
	'https://apps.apple.com/us/genre/mac-video/id12020?mt=12&letter=F',
	'https://apps.apple.com/us/genre/mac-video/id12020?mt=12&letter=G',
	'https://apps.apple.com/us/genre/mac-video/id12020?mt=12&letter=H',
	'https://apps.apple.com/us/genre/mac-video/id12020?mt=12&letter=I',
	'https://apps.apple.com/us/genre/mac-video/id12020?mt=12&letter=J',
	'https://apps.apple.com/us/genre/mac-video/id12020?mt=12&letter=K',
	'https://apps.apple.com/us/genre/mac-video/id12020?mt=12&letter=L',
	'https://apps.apple.com/us/genre/mac-video/id12020?mt=12&letter=M',
	'https://apps.apple.com/us/genre/mac-video/id12020?mt=12&letter=N',
	'https://apps.apple.com/us/genre/mac-video/id12020?mt=12&letter=O',
	'https://apps.apple.com/us/genre/mac-video/id12020?mt=12&letter=P',
	'https://apps.apple.com/us/genre/mac-video/id12020?mt=12&letter=Q',
	'https://apps.apple.com/us/genre/mac-video/id12020?mt=12&letter=R',
	'https://apps.apple.com/us/genre/mac-video/id12020?mt=12&letter=S',
	'https://apps.apple.com/us/genre/mac-video/id12020?mt=12&letter=T',
	'https://apps.apple.com/us/genre/mac-video/id12020?mt=12&letter=U',
	'https://apps.apple.com/us/genre/mac-video/id12020?mt=12&letter=V',
	'https://apps.apple.com/us/genre/mac-video/id12020?mt=12&letter=W',
	'https://apps.apple.com/us/genre/mac-video/id12020?mt=12&letter=X',
	'https://apps.apple.com/us/genre/mac-video/id12020?mt=12&letter=Y',
	' https://apps.apple.com/us/genre/mac-video/id12020?mt=12&letter=Z',
	'https://apps.apple.com/us/genre/mac-video/id12020?mt=12&letter=M&page=2#page', 
	'https://apps.apple.com/us/genre/mac-video/id12020?mt=12&letter=S&page=2#page', 
	'https://apps.apple.com/us/genre/mac-video/id12020?mt=12&letter=*']


	#def parse(self, response):
		#l = list(string.ascii_uppercase[0:26]) 
		#result_urls = ['https://apps.apple.com/us/genre/mac-medical/id12010?mt=12&letter={}'.format(x) for x in l ]

		#f#or url in result_urls[1:]:
			#yield Request(url=url, callback=self.parse_result_page)


	def parse(self, response):
		detail_urls = response.xpath('//*[@id="selectedcontent"]/div/ul/li/a/@href').extract()

		for url in detail_urls:
			yield Request(url = url, callback = self.parse_detail_page)

	def parse_detail_page(self, response):

		item  = MacItem()



		item['name'] = response.xpath('normalize-space(//h1[@class ="product-header__title app-header__title"]/text())').extract_first()
		item['rating'] = response.xpath('normalize-space(//span[@class = "we-customer-ratings__averages__display"]/text())').extract_first()
		item['size'] =  response.xpath('normalize-space(//div[2][@class ="information-list__item l-row"])').extract_first()
		item['category']  = response.xpath('normalize-space(//div[3][@class ="information-list__item l-row"])').extract_first()
		item['languages'] = response.xpath('normalize-space(//div[5][@class ="information-list__item l-row"])').extract_first() 
		item['compatibility'] = response.xpath('normalize-space(//div[4][@class ="information-list__item l-row"])').extract_first()
		item['price'] = response.xpath('normalize-space(//div[8][@class ="information-list__item l-row"])').extract_first()[6:] 

		yield item

