from lamadava import Client
cl = Client(token="CFtr2422gV9MyO0g9tj9KPz2jhJNZmau")
from flask import Flask, request

app = Flask(__name__)

@app.route('/user_info', methods=['POST'])
def user_info():
    username = request.form.get('username')
    # Process username data
    user_info_=cl.user_by_username_v1(username)
    return user_info_

@app.route('/user_medias', methods=['POST'])
def user_medisa():
    user_id = request.form.get('user_id')
    # Process user_id data
    user_medias_=cl.user_medias(user_id)
    print(user_medias_)
    return user_medias_

@app.route('/user_stories', methods=['POST'])
def user_storied():
    username = request.form.get('username')
    # Process user_id data
    user_stories=cl.user_stories_by_username_v1(username)
    
    return user_stories

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
