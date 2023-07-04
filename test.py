from lamadava import Client
cl = Client(token="CFtr2422gV9MyO0g9tj9KPz2jhJNZmau")
from flask import request, abort, current_app ,Flask
user_info_=cl.user_by_username_v2("dheeraj_joshi2006")
print(user_info_)
user_medias_=cl.sto
print(user_medias_)