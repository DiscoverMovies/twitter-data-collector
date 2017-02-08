import pymysql

def initial(self):
    db=pymysql.connect(host='localhost',user=self.username,password=self.password,use_unicode=True,charset='utf8')
    cur=db.cursor()

    sql='CREATE DATABASE  IF NOT EXISTS TWEET_DATA'
    cur.execute(sql)
    sql='USE TWEET_DATA'
    cur.execute(sql)
    sql='CREATE TABLE IF NOT EXISTS USER(ID NUMERIC(25) PRIMARY KEY,' \
        'NAME CHAR(25),' \
        'SCREEN_NAME CHAR(20),' \
        'PLACE CHAR(20),' \
        'STATUS VARCHAR(140))'
    cur.execute(sql)

    sql='CREATE TABLE IF NOT EXISTS TWEETS(ID NUMERIC(25),' \
        'TID NUMERIC(25) UNIQUE,' \
        'FOREIGN KEY(ID) REFERENCES USER(ID),' \
        'PRIMARY KEY(ID,TID))'
    cur.execute(sql)
    sql='CREATE TABLE IF NOT EXISTS TWEET_INFO(TID NUMERIC(25),' \
        'TEXT CHAR(145), ' \
        'FOREIGN KEY(TID) REFERENCES TWEETS(TID))'
    cur.execute(sql)
    sql='CREATE TABLE IF NOT EXISTS FOLLOWING(ID NUMERIC(25),' \
        'FID NUMERIC(25) UNIQUE,' \
        'FOREIGN KEY(ID) REFERENCES USER(ID),' \
        'PRIMARY KEY(ID,FID))'
    cur.execute(sql)
    sql='CREATE TABLE IF NOT EXISTS INTERACTION(ID NUMERIC(25),' \
        'TID NUMERIC(25),' \
        'FOREIGN KEY(ID) REFERENCES USER(ID),' \
        'PRIMARY KEY(ID,TID))'
    cur.execute(sql)


def insert_user(id,name,screen,place,status,username,passwd):
    db = pymysql.connect(host='localhost', user=username, password=passwd,db='tweet_data',charset='utf8')
    cur = db.cursor()
    sql='USE TWEET_DATA'
    cur.execute(sql)
    sql="INSERT INTO USER(ID,NAME,SCREEN_NAME,PLACE,STATUS) VALUES("+str(id)+",'"+name+"','"+screen+"','"+place+"','"+status+"')"
    cur.execute(sql)
    db.commit()


def insert_tweet(id,tid,text,username,passwd):
    db=pymysql.connect(host='localhost', user=username, password=passwd,db='tweet_data',charset='utf8')
    cur=db.cursor()
    sql='USE TWEET_DATA'
    cur.execute(sql)
    sql = "INSERT INTO TWEETS(ID,TID) VALUES("+str(id)+","+str(tid)+")"
    cur.execute(sql)
    sql="INSERT INTO TWEET_INFO(TID,TEXT) VALUES("+str(tid)+",'"+str(text).replace("'", "\\'")+"')"
    print("SQL:",sql)
    cur.execute(sql)
    db.commit()



