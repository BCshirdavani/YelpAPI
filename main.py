import os
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

import CloudVisionHelper
from YelpApiHelper import YelpApiHelper

app = Flask(__name__)
CORS(app)

yelpApiHelper = YelpApiHelper()

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"yelp-api-crecend-1634677290495-03a4bad6e258.json"


@app.route('/yelp')
@cross_origin()
def yelp():
    business_id = request.args.get('business_id')
    print(business_id)
    response = yelpApiHelper.getReviews(business_id)

    if response == None:
        return "ERROR - please try another business ID"
    else:
        # TODO: keep controller simple, shoudl refactor and push method to another service
        reviews = response['reviews']
        for review in reviews:
            image_uri = review['user']['image_url']
            emotions = CloudVisionHelper.detect_faces_uri(image_uri)
            review['emotions'] = emotions
        print(reviews)
        jsonReviews = jsonify(reviews)

        return jsonReviews


if __name__ == '__main__':
    app.run(debug=True)
