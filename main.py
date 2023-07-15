from lamadava import Client
cl = Client(token="BQXIvR1r3gmnU0TPmc845nEfTLeICRNX")
from flask import request, abort, current_app ,Flask
import pandas as pd
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
        print(username)
        # Process username data
        user_info_=cl.user_by_username_v1(username)
        return user_info_
    else:
           
        return "this is fin"

@app.route('/user_medias', methods=['GET','POST'])
def user_medisa():
    if request.method=='POST':
        user_id = request.form.get('user_id')
        print(user_id)
        amount = request.form.get('amount')
        test = request.form.get('test')
        # Process user_id data
        print(test)
        user_medias_=cl.user_medias_v1(user_id,amount=amount)
        # print(user_medias_)
        return user_medias_
    else:
        return "this is fin"

@app.route('/user_stories', methods=['GET','POST'])
def user_storied():
    if request.method=='POST':
        username = request.form.get('username')
        # Process user_id data
        print(username)
        user_stories=cl.user_stories_by_username_v1(username)
        
        return user_stories
    else:
        return "this is fin"


@app.route('/user_data', methods=['GET','POST'])
def user_data():
    if request.method=='POST':
        username = request.form.get('username')
        user_info_=cl.user_by_username_v1(username)
        # Process user_id data
        
        user_id=user_info_['pk']
        user_medias_=cl.user_medias_v1(user_id,amount=20)
        user_stories=cl.user_stories_by_username_v1(username)
        
        return {"user_info":user_info_,"Medias":user_medias_,"Stories":user_stories} 
    else:
        return "this is fin"

@app.route('/vca_data', methods=['GET','POST'])
def vca_data():
    if request.method=='POST':
        username = request.form.get('username')
        user_info_=cl.user_by_username_v1(username)
        user_id=user_info_['pk']
        user_medias_=cl.user_medias_v1(user_id,amount=100)
        data=user_info_
        print(data)
        pfp=data['profile_pic_url_hd']
        
        Media_urls=[]
        Media_captions=[]
        Media_likes_counts=[]
        Media_comments_counts=[]
        Media_created_ats=[]
        Author_Users=[]
        Author_dps=[]
        Author_Bios=[]
        Author_followers_couns=[]
        Authos_followings_counts=[]
        Video_Urls=[]

        for media in user_medias_ :
            med=media
            try:
                Media_url=med['thumbnail_url']
            except:
                Media_url="N/A"
            Media_caption=med['caption_text'].replace(",","").replace("\n"," ")
            Media_likes_count=med['like_count']
            Media_comments_count=med['comment_count']
            Media_created_at=med['taken_at']
            Author_User=data['username']
            Author_dp=pfp
            Author_Bio=data['biography'].replace(",","").replace("\n"," ")
            Author_followers_count=data['follower_count']
            Authos_followings_count=data['following_count']
            
            Video_Url=''
            print(med)
            if med['media_type']==2:
                Video_Url=med['video_url'] 
            
            Media_urls.append(Media_url)
            Media_captions.append(Media_caption)
            Media_likes_counts.append(Media_likes_count)
            Media_comments_counts.append(Media_comments_count)
            Media_created_ats.append(Media_created_at)
            Author_Users.append(Author_User)
            Author_dps.append(Author_dp)
            Author_Bios.append(Author_Bio)
            Author_followers_couns.append(Author_followers_count)
            Authos_followings_counts.append(Authos_followings_count)
            Video_Urls.append(Video_Url)
        

        # Create a dictionary with the variables
        data = {
            'Media_urls': Media_urls,
            'Media_captions': Media_captions,
            'Media_likes_counts': Media_likes_counts,
            'Media_comments_counts': Media_comments_counts,
            'Media_created_ats': Media_created_ats,
            'Author_Users': Author_Users,
            'Author_dps': Author_dps,
            'Author_Bios': Author_Bios,
            'Author_followers_couns': Author_followers_couns,
            'Authos_followings_counts': Authos_followings_counts,
            'Video_Urls': Video_Urls
}
   
        df = pd.DataFrame(data)
        
        return str(df)   
         
    else:
        return "this is fin"





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1000)
