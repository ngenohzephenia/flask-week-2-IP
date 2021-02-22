from app import app
from  urllib.request,jason
from models import news

News =news.News

# Getting api key
api_key =app.config['461ad7724e7445dcb49c72ba517bfdbe']
base_url = app.config["News_API_BASE_URL"]