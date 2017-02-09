import pymysql


class DatabaseTwitter:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        db = pymysql.connect(host='localhost', user=self.username, password=self.password, use_unicode=True, charset='utf8mb4')
        cur = db.cursor()

        sql = 'CREATE DATABASE  IF NOT EXISTS TWEET_DATA'
        cur.execute(sql)
        sql = 'USE TWEET_DATA'
        cur.execute(sql)
        sql = 'CREATE TABLE IF NOT EXISTS USER(ID NUMERIC(25) PRIMARY KEY,' \
              'NAME CHAR(25),' \
              'SCREEN_NAME CHAR(20),' \
              'PLACE CHAR(20),' \
              'STATUS VARCHAR(140))CHARACTER SET utf8 COLLATE utf8_unicode_ci'
        cur.execute(sql)

        sql = 'CREATE TABLE IF NOT EXISTS TWEETS(ID NUMERIC(25),' \
              'TID NUMERIC(25) UNIQUE,' \
              'FOREIGN KEY(ID) REFERENCES USER(ID),' \
              'PRIMARY KEY(ID,TID))CHARACTER SET utf8 COLLATE utf8_unicode_ci'
        cur.execute(sql)
        sql = 'CREATE TABLE IF NOT EXISTS TWEET_INFO(TID NUMERIC(25),' \
              'TEXT CHAR(145), ' \
              'FOREIGN KEY(TID) REFERENCES TWEETS(TID))CHARACTER SET utf8 COLLATE utf8_unicode_ci'
        cur.execute(sql)
        sql = 'CREATE TABLE IF NOT EXISTS FOLLOWING(ID NUMERIC(25),' \
              'FID NUMERIC(25) UNIQUE,' \
              'FOREIGN KEY(ID) REFERENCES USER(ID),' \
              'PRIMARY KEY(ID,FID))CHARACTER SET utf8 COLLATE utf8_unicode_ci'
        cur.execute(sql)
        sql = 'CREATE TABLE IF NOT EXISTS INTERACTION(ID NUMERIC(25),' \
              'TID NUMERIC(25),' \
              'FOREIGN KEY(ID) REFERENCES USER(ID),' \
              'PRIMARY KEY(ID,TID))CHARACTER SET utf8 COLLATE utf8_unicode_ci'
        cur.execute(sql)

    def insert_user(self, data):
        db = pymysql.connect(host='localhost', user=self.username, password=self.password, db='tweet_data', charset='utf8mb4')
        cur = db.cursor()
        sql = 'USE TWEET_DATA'
        cur.execute(sql)
        sql = "INSERT INTO USER(ID,NAME,SCREEN_NAME,PLACE,STATUS) VALUES(" + str(
            data['id']) + ",'" + data['name'] + "','" + data['screen_name'] + "','" + data['place'] + "','" + data['status'] + "')"
        try:
            cur.execute(sql)
        except pymysql.err.IntegrityError:
            print('id already exist!!')

        db.commit()

    def insert_tweet(self,tweets,data):
        db = pymysql.connect(host='localhost', user=self.username, password=self.password, db='tweet_data', charset='utf8mb4')
        cur = db.cursor()
        sql = 'USE TWEET_DATA'
        cur.execute(sql)
        for tweet in tweets:
            sql = "INSERT INTO TWEETS(ID,TID) VALUES(" + str(data['id']) + "," + str(tweet.id) + ")"
            cur.execute(sql)
            txt = str(tweet.text).encode('utf-8')
            sql = "INSERT INTO TWEET_INFO(TID,TEXT) VALUES(" + str(tweet.id) + ",'" + txt.replace("'", "\\'") + "')"
            cur.execute(sql)
            db.commit()
