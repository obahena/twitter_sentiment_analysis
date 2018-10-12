
from TwitterAPI import TwitterAPI
from textblob import TextBlob



api = TwitterAPI(consumer_key='4tIauUZj5suBUnT3CvjIwTMrZ',
  consumer_secret='xV0uvRFQxPaglgQUnQ4cndLcICUfk2WkD7UUpkxhn9gUzjk2xi',
  access_token_key='233693629-Cdm0oaDJQ1Z7WeIl4IKjhPfjlgwG4ri6P1nfAmZK',
  access_token_secret='OwnNdBKwV8WJ1abXMLCVOkckBdLsiHp6CjM4VtwCRSwjw')


r = api.request('search/tweets', {'q': 'Keenum'})


#Print out items on console
for item in r:
    print(item['text'] if 'text' in item else item)