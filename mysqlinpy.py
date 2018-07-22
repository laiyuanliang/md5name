#coding:utf-8

import hashlib
import pymysql

def md5encrypt(raw):
    m = hashlib.md5()
    m.update(raw)
    return m.hexdigest()

db = pymysql.connect('localhost','root','Root@mysql01','test')
cursor = db.cursor()

namestr = '阿埃挨哎唉哀皑癌蔼矮艾碍爱隘鞍'

for i in namestr:
    for j in namestr:
        name = i + j
        hashname = md5encrypt(name.encode())

        sql = 'INSERT INTO user(name,md5_name) VALUES("%s","%s")'%(name,hashname)
        try:
            cursor.execute(sql)
        except:
            print('error happend in INSERT')
            db.rollback()

db.commit()
db.close()
