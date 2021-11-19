import os
import requests


class YelpApiHelper:
    def __init__(self):
        self.base_yelp_url = " https://api.yelp.com/v3"
        self.demoBusiness_id = "milwaukee-ale-house-milwaukee"
        # getting a yelp api key is free
        yelpKey = os.environ['YELP_KEY']
        self.header = {'Authorization': 'bearer ' + yelpKey}

    def getReviews(self, business_id):
        yelp_api_endpoint = "/businesses/" + business_id + "/reviews"
        req_url = self.base_yelp_url + yelp_api_endpoint
        print(req_url)
        r = requests.get(req_url, headers=self.header)
        if r.status_code == 200:
            print(r.text)
            business_reviews = r.json()
            print(business_reviews.keys())
            print(business_reviews)
            return business_reviews
        else:
            print(r.status_code)
            print('ERROR - try another business ID')
