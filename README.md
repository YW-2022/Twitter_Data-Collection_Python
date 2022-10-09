# Twitter_Data-Collection_Python

### Twitter API Authentication
Apply for Twitter academic research access ---> https://developer.twitter.com/en/products/twitter-api/academic-research</br>
Generate authentication tokens, including bear token and access token & secret. </br>

### Retrieve Data
Use [Search Tweets](https://github.com/YW-2022/Twitter_Data-Collection_Python/blob/master/Twitter_Data%20Collection_Python/tweets_content.py) and [Tweets Counts](https://github.com/YW-2022/Twitter_Data-Collection_Python/blob/master/Twitter_Data%20Collection_Python/count.py) APIs to get tweet content and tweet count respectively.

Three packages are required:
<ul>
  <li>pytwitter</li>
  <li>csv</li>
  <li>json</li>
</ul>
python-twitter-v2 0.7.8 can be downloaded here:
https://pypi.org/project/python-twitter-v2/
</br>
</br>
On the command line: <code>pip install python-twitter-v2</code>
</br>

### Text Preprocessing

<ul>
  <li>Data anonymization.</li>
  <li>Use preprocessor to remove hyperlink, @mention, emoji.</li>
  <li>Remove punctuation, special symbol, common stop-word.</li>
</ul>
tweet-preprocessor 0.6.0 can be downloaded here:
https://pypi.org/project/tweet-preprocessor/
</br>
</br>
On the command line: <code>pip install tweet-preprocessor</code>
</br>

### Data Analysis
Statistical analysis of the acquired data using python pandas and numpy libraries.

Two packages are required:
<ul>
  <li>Matplotlib</li>
  <li>Word-cloud</li>
</ul>
Word-cloud(also known as tag-cloud or wordle or weighted list in visual design). wordcloud 1.8.2.2 can be downloaded here:
https://pypi.org/project/wordcloud/
</br>
</br>
On the command line: <code>pip install wordcloud</code>
