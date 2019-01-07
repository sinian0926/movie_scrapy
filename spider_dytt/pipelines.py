# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime
import re
import pymongo
from spider_dytt.settings import monhodb_host,mongodb_port,mongodb_dbname,mongodb_collection
# import pymysql
# from spider_dytt.spider_rules.pre_sql import sql
# from spider_dytt.settings import mysql_host,mysql_dbname,mysql_port,mysql_user,mysql_passwd


class Spider2Pipeline(object):
    def __init__(self):
        host = monhodb_host
        port = mongodb_port
        dbname = mongodb_dbname
        sheet = mongodb_collection
        client = pymongo.MongoClient(host=host,port=port)
        mydb = client[dbname]
        self.post = mydb[sheet]

    def process_item(self, item, spider):
        data = dict(item)
        if data['download'] != None and data['download'] != '':
            self.post.insert(data)
        return item
    # def __init__(self):
    #     # 设置数据库的初始值
    #     host = mysql_host
    #     port = mysql_port
    #     user = mysql_user
    #     passwd = mysql_passwd
    #     dbname = mysql_dbname
    #
    #     self.db = pymysql.connect(host=host,port=port,user=user,passwd=passwd,db=dbname,charset='utf8')
    #     self.cursor = self.db.cursor()
    #
    #     self.cursor.execute('SET NAMES utf8;')
    #     self.cursor.execute('SET CHARACTER SET utf8;')
    #     self.cursor.execute('SET character_set_connection=utf8;')
    #
    #
    # def process_item(self, item, spider):
    #     # 将 yield 返回的 item 变成 dict
    #     data = dict(item)
    #
    #     # 获取 影片时间 及 热度
    #     time = str(re.search('日期：(.*?) \\r\\n点击：(\d+) ',data['time']).group(1))
    #     hot = str(re.search('日期：(.*?) \\r\\n点击：(\d+) ',data['time']).group(2))
    #
    #     # 生成时间
    #     d = datetime.datetime.now().strftime('%Y-%m-%d')  # '%Y-%m-%d %H:%M:%S'
    #     t = datetime.datetime.now().strftime('%H:%M:%S')
    #
    #     # 判断 下载地址 是否为空
    #     if data['download'] != None and len(data['download']) > 0:
    #         for down in data['download']:
    #             # 准备插入数据
    #             try:
    #                 # 判断影片是否已存在
    #                 self.cursor.execute(sql['cm_exist'].format(data['title'][0]))
    #                 exist = self.cursor.fetchone()[0]
    #                 if exist == None or  exist <= 0:
    #                     # 插入影片到 movie 表中
    #                     self.cursor.execute(sql['z_movie'].format(data['host'], data['classic'], data['title'][0],
    #                                                           data['desc'].replace("'", "\'"), time, hot, d, t, d, t))
    #                     # # 查询最后插入的 影片ID
    #                     # self.cursor.execute(sql['cm_lastid'])
    #                     # last_id =self.cursor.fetchone()[0]
    #                     # # 插入下载地址到 download 表
    #                     # self.cursor.execute(sql['z_down'].format(last_id,down,d,t,d,t))
    #                     self.db.commit()
    #                     try:
    #                         # 查询最后插入的 影片ID
    #                         self.cursor.execute(sql['cm_lastid'])
    #                         last_id = self.cursor.fetchone()[0]
    #                         # 插入下载地址到 download 表
    #                         self.cursor.execute(sql['z_down'].format(last_id, down, d, t, d, t))
    #                     except Exception as e:
    #                         self.db.rollback()
    #                         try:
    #                             self.cursor.execute(
    #                                 sql['z_log'].format(data['classic'], '影片：' + data['title'][0] + '—下载地址,插入失败!',
    #                                                     datetime.datetime.now()))
    #                             self.db.commit()
    #                         except Exception as e:
    #                             print('Log日志插入错误', repr(e))
    #
    #                 else:
    #                     # 影片已存在
    #                     pass
    #
    #
    #             except Exception as e:
    #                 self.db.rollback()
    #                 try:
    #                     self.cursor.execute(sql['z_log'].format(data['classic'],'影片：'+data['title'][0]+',插入失败!',datetime.datetime.now()))
    #                     self.db.commit()
    #                 except Exception as e:
    #                     print('Log日志插入错误',repr(e))
    #     else:
    #         try:
    #             self.cursor.execute(
    #                 sql['z_log'].format(data['classic'], '影片：' + data['title'][0] + ',下载地址为空!', datetime.datetime.now()))
    #             self.db.commit()
    #         except Exception as e:
    #             print('Log日志插入错误', repr(e))
    #
    #     return item