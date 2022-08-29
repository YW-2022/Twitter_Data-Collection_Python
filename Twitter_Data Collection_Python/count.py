# import package - need install 
from pytwitter import Api
import csv
import json

# csvname:test.csv - can be changed to other names or addresses
csvFile = open('test.csv', 'w')
# use csv Writer
csvWriter = csv.writer(csvFile)
# csv column name - can be changed to other names
csvWriter.writerow(['day', 'count_number'])

# bearer_token - abc is your bearer_token - need to be replaced - bearer_token can be obtained from Twitter developer platform
api = Api(bearer_token='''abc''')

# YYYY-MM-DDTHH:mm:ssZ
# query = 'xxx' - query keywords
# granularity can be set to day, hour, minute
# start_time and end_time - be careful to keep this format
ans = api.get_tweets_counts(query='#vr', search_type='all', granularity='day',
                            start_time='2022-06-01T00:00:00.000Z', 
                            end_time='2022-07-01T00:00:00.000Z', return_json=True)
print(ans)
ans_json = json.dumps(ans)  
json_dict = json.loads(ans_json)    
data_list = json_dict["data"]
for i in range(0, len(data_list)):
    start = data_list[i]["start"]
    tweet_count = data_list[i]["tweet_count"]
    csvWriter.writerow([start, tweet_count])
