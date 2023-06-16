from lamadava import Client
cl = Client(token="CFtr2422gV9MyO0g9tj9KPz2jhJNZmau")
from flask import Flask, request
user_info_=cl.user_by_username_v1("dheeraj_joshi2006")
print(user_info_)
app = Flask(__name__)

@app.route('/user_info', methods=['GET','POST'])
def user_info():
    if request.method=='Post':
        username = request.form.get('username')
        # Process username data
        user_info_=cl.user_by_username_v1(username)
        return user_info_
    else:
           
        return "this is fin"

@app.route('/user_medias', methods=['GET','POST'])
def user_medisa():
    if request.method=='Post':
        user_id = request.form.get('user_id')
        # Process user_id data
        user_medias_=cl.user_medias(user_id)
        print(user_medias_)
        return user_medias_
    else:
        return "this is fin"

@app.route('/user_stories', methods=['GET','POST'])
def user_storied():
    if request.method=='Post':
        username = request.form.get('username')
        # Process user_id data
        user_stories=cl.user_stories_by_username_v1(username)
        
        return user_stories
    else:
        return "this is fin"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
