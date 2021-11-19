def detect_faces_uri(uri):
    """Detects faces in the file located in Google Cloud Storage or the web."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri

    response = client.face_detection(image=image)
    faces = response.face_annotations

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')
    emotions = {}

    for face in faces:
        emotions['anger'] = likelihood_name[face.anger_likelihood]
        emotions['joy'] = likelihood_name[face.joy_likelihood]
        emotions['surprise'] = likelihood_name[face.surprise_likelihood]
        emotions['sorrow'] = likelihood_name[face.sorrow_likelihood]

    if len(emotions) > 0:
        return emotions

    elif response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
