#数据清洗


import pymongo
import csv


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["data"]
mycol = mydb["sites"]


result = mycol.delete_many({'value': 32767})
print(result.deleted_count)
