import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News(1234,'Passing of BBI', 'Several counties have passed the BBI bill in Kenya','https://www.standardmedia.co.ke/politics/article/2001403835/more-counties-pass-bbi-bill')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))

if__name__='__main__':
    unittest.main()