# import package - need install 
from pytwitter import Api
import csv
import json

# csvname:test.csv - can be changed to other names or addresses
csvFile = open('test.csv', 'w')
# use csv Writer
csvWriter = csv.writer(csvFile)
# csv column name - can be changed to other names
csvWriter.writerow(['create_date', 'tweet_id', 'author_id', 'content'])

# bearer_token - abc is your bearer_token - need to be replaced - bearer_token can be obtained from Twitter developer platform
api = Api(bearer_token='''abc''')

# YYYY-MM-DDTHH:mm:ssZ
# query = 'xxx' - query keywords. If multiple keywords are set at the same time, separate them with spaces.
# start_time and end_time - be careful to keep this format
ans = api.search_tweets(query='vr chemistry', query_type='all', start_time='2020-04-01T00:00:00.000Z',
                        end_time='2020-04-23T00:00:00.000Z', tweet_fields=['created_at', 'author_id'], max_results=500, return_json=True)
ans_json = json.dumps(ans)
print(ans_json)
json_dict = json.loads(ans_json)
data_list = json_dict["data"]
for i in range(0, len(data_list)):
    date_c = data_list[i]["created_at"]
    id = data_list[i]["id"]
    text = data_list[i]['text']
    author_id = data_list[i]['author_id']
    csvWriter.writerow([date_c, id, author_id, text])
