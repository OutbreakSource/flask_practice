from flask import Flask

api = Flask(__name__)

@api.route('/profile')
def my_profile():
    response_body = {
        "name": "Daniel",
        "about" :"God help me learn Flash"
    }

    return response_body