from lamadava import Client
cl = Client(token="CFtr2422gV9MyO0g9tj9KPz2jhJNZmau")
from flask import request, abort, current_app ,Flask
# user_info_=cl.user_by_username_v1("dheeraj_joshi2006")
# print(user_info_)
app = Flask(__name__)

# ip_ban_list=['158.247.195.112']
# @app.before_request
# def block_method():
#     ip = request.environ.get('REMOTE_ADDR')
#     if ip in ip_ban_list:
#         abort(403)

@app.route('/user_info', methods=['GET','POST'])
def user_info():
    if request.method=='POST':
        username = request.form.get('username')
        # Process username data
        user_info_=cl.user_by_username_v1(username)
        return user_info_
    else:
           
        return "this is fin"

@app.route('/user_medias', methods=['GET','POST'])
def user_medisa():
    if request.method=='POST':
        user_id = request.form.get('user_id')
        # Process user_id data
        user_medias_=cl.user_medias_v1(user_id,amount=50)
        print(user_medias_)
        return user_medias_
    else:
        return "this is fin"

@app.route('/user_stories', methods=['GET','POST'])
def user_storied():
    if request.method=='POST':
        username = request.form.get('username')
        # Process user_id data
        user_stories=cl.user_stories_by_username_v1(username)
        
        return user_stories
    else:
        return "this is fin"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
