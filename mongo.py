#coding=utf-8
from pymongo import *

client = MongoClient('mongodb://stu:123@localhost:27017/stu')  #获得客户端，建立连接

db = client.stu#切换数据库

stu = db.stu#获取集合

#stu.insert_one({'name':'吴帅'})  #插入

#stu.update_one({'name':'吴帅'},{'$set':{'name':'吴帅的小LL'}})  #修改

#stu.delete_one({'name':'li'}) #删除
#stu.delete_many() #删除


# cursor = stu.find({'age':{'$lt':20}}) #查找
# for i in cursor:
#     print(i['name'])

cursor = stu.find().sort('age',DESCENDING) # 排序DESCENDING  ASCENDING
for i in cursor:
    print(i)