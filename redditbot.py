import praw
import requests
import time

reddit = praw.Reddit(
    client_id = 'id',
    client_secret = 'secret',
    username = 'username',
    password = 'password',
    user_agent = 'cricket wc weather bot by /u/himanscience'

)

#print(reddit.read_only)
subreddit = reddit.subreddit('CricketShitpost')

keyphrase = '!cricketwcweather'

api_address = 'https://samples.openweathermap.org/data/2.5/weather?appid=daf6b9f4fd27d31ca3cf23cd8b37e24b&q='
country_code = ',GB'
city = ['Birmingham', 'Bristol', 'Cardiff', 'Chester-le-Street', 'Leeds', 'London', 'Manchester', 'Nottingham', 'Southampton', 'Taunton' ]


for comment in subreddit.stream.comments(skip_existing=True):
    if keyphrase in comment.body:
        try:
            weath = ''
            for i in city:
                url = api_address + i + country_code
                json_data = requests.get(url).json()
                weath = weath + i + ": " + json_data['weather'][0]['description'] + ', \n'
            comment.reply(weath)
            print(weath)
            time.sleep(60)
        except:
            print('too frequent')