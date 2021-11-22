#从数据库读取点

import pymongo
import csv


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["data"]
mycol = mydb["sites"]


def csv_writer():
    with open('D:/Desktop/mycsv.csv', 'w') as f:
        headers = ["lat", "lon", "value"]
        writer = csv.writer(f)
        writer.writerow(headers)
        for i in mycol.find().limit(100000):
            if 119.31647 < i["lat"] < 119.34927:
                # 高程放大十倍
                a = [i["lat"], i["lng"], i["value"]]

                writer.writerow(a)


csv_writer()


