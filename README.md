# Read Me

## Dependencies and Google config:
- install python dependencies with `pip install -r requirements.txt`
- make a google cloud service account, enable Cloud Vision, and download the credentials json
  - I have a path pointing to `yelp-api-crecend-1634677290495-03a4bad6e258.json`, which was needed to authenticate with the Google Cloud Vision API. I have since shut down that project on Google Cloud.
- create environment variable that points to this downloaded credentials json and name it `GOOGLE_APPLICATION_CREDENTIALS`

## run the demo:
- start the flask server with `pip3 main.py`
- the app runs on http://127.0.0.1:5000/ 
  - the GET request takes one parameter, for the `business_id`, so if you want to get reveiws for "Milwaukee Ale House" their yelp business ID is: "milwaukee-ale-house-milwaukee", and you would pass that as a query parameter like so:
    - http://127.0.0.1:5000/yelp?business_id=milwaukee-ale-house-milwaukee

