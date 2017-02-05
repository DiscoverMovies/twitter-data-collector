from twitter_data_collector import TwitterDataCollector


a=TwitterDataCollector()
auth=a.set_database()
a.insert_user_data(auth)