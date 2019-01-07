# -*- coding: utf-8 -*-
import scrapy
import re
from spider_dytt.items import Spider2Item as sitem

# from spider_dytt.spider_rules.get_rules import get_rules

class DyttSpiderSpider(scrapy.Spider):
    # 爬虫的名字
    name = 'dytt_spider'
    # 允许的域名
    allowed_domains = ['ygdy8.net','dytt8.net']
    # 入口的url
    start_urls = ['http://www.ygdy8.net/html/gndy/dyzz/list_23_1.html']#,'http://www.ygdy8.net/html/gndy/china/list_4_1.html','http://www.ygdy8.net/html/gndy/oumei/list_7_1.html','http://www.dytt8.net/html/gndy/rihan/list_6_1.html','http://www.ygdy8.net/html/tv/rihantv/list_8_1.html','http://www.ygdy8.net/html/tv/hytv/list_71_1.html','http://www.ygdy8.net/html/tv/oumeitv/list_9_1.html','http://www.ygdy8.net/html/zongyi2013/list_99_1.html','http://www.ygdy8.net/html/2009zongyi/list_89_1.html','http://www.ygdy8.net/html/dongman/list_16_1.html']

    def parse(self, response):
        # print(response.text)
        # 抓取次数
        tables = response.xpath('//div[@class="co_content8"]/ul/td/table[@class="tbspan"]')

        # print('tables',tables)
        for x,table in enumerate(tables):
            si = sitem()
            si['host'] = '电影天堂(http://www.ygdy8.net/,https://www.dytt8.net/)'
            si['classic'] = '最新影片'
            # 抓取 详情页 地址
            si['list_url'] = table.xpath('.//a[@class="ulink"]/@href').extract_first()
            # 抓取 电影时间 及 热度 日期：2018-11-24 16:12:15
            time = table.xpath('.//font/text()').extract_first()
            si['time'] = re.findall('([0-9]{4}\-[0-9]{2}\-[0-9]{2} [0-9]{2}:[0-9]{2}:[0-9]{2})', time)[0]
            si['hot'] = re.findall('点击：(\d+)', time)[0]
            si['simpledesc'] = table.xpath('.//tr[4]/td/text()').extract_first()
            # 进入详情页进行抓取
            yield scrapy.Request(url='http://www.ygdy8.net' + str(si['list_url']), meta={'ul': si}, callback=self.parse2)
        # 翻页
        page = response.xpath('//div[@class="x"]/td/a[text()="末页"]/@href').extract()
        if len(page) != 0:
            # 获取最大页数
            page = int(re.search(pattern='_(\d+)\.',string=str(page[0])).group(1))
            # # 开始准备翻页
            for p in range(3, 51):
                yield scrapy.Request(url='http://www.ygdy8.net/html/gndy/dyzz/list_23_' + str(p) + '.html',callback=self.parse)



    def parse2(self, response):
        # 获得传入的 item 对象
        si = response.meta['ul']
        # 抓取 电影标题
        si['title'] = response.xpath('//div[@class="title_all"]/h1/font/text()').extract()
        # 抓取电影描述
        desc = response.xpath('//div[@id="Zoom"]/span/p/span/text()|//div[@id="Zoom"]//p/text()|//div[@id="Zoom"]/span/span/text()').extract()
        desc_s = ''.join(desc).replace(u'\u3000', '').replace(r'\xa0', '').replace(
                                        r'\r\n',
                                        '').strip()
        if desc_s != None and desc_s != '':
            si['desc'] = desc_s
        else:
            si['desc'] = '该影片暂无描述'
        # 抓取 电影下载地址
        down_list = response.xpath('//td[@bgcolor="#fdfddf"]//a/@href|//td[@bgcolor="#fdfddf"]//a/text()').extract()
        ## 做一下 去重 处理
        download = list(set(down_list))
        download.sort(key=down_list.index)
        si['download'] = download
        # print('si',si)
        yield si

