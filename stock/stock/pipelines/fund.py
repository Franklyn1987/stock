# -*- coding: utf-8 -*-
from pymongo import MongoClient


class FundPipeline(object):

    collection_name = 'fund'

    def open_spider(self,spider):
        self.client = MongoClient(self.MONGODB_SERVER,self.MONGODB_PORT)
        self.db = self.client[self.MONGODB_DB]

    def close_spider(self,spider):
        self.client.close()

    @classmethod
    def from_crawler(cls, crawler):
        print 'hee'
        cls.MONGODB_SERVER = crawler.settings.get('MONGODB_SERVER')
        cls.MONGODB_PORT = crawler.settings.getint('MONGODB_PORT')
        cls.MONGODB_DB = crawler.settings.get('MONGODB_DB')
        pipe = cls()
        return pipe

    def process_item(self,item,spider):
        print 'hee'
        self.db[self.collection_name].insert(dict({'test':1}))
        return item