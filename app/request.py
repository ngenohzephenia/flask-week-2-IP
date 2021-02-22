from app import app
from  urllib.request,jason
from models import news

News =news.News

# Getting api key
api_key =app.config['461ad7724e7445dcb49c72ba517bfdbe']
base_url = app.config["News_API_BASE_URL"]

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)


    return movie_results
