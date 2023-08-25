import json
from instagrapi import Client
# cl=Client()
cl=Client({'uuids': {'phone_id': '2fbd9268-2227-4eea-a932-ca79b52b7b0a', 'uuid': 'd6b507cd-3320-496f-92fb-da2f4dfafad5', 'client_session_id': '3a22d148-10df-40a6-9ee1-67fd508ad413', 'advertising_id': '40ec93aa-d93f-4c91-9986-04a2b7313617', 'android_device_id': 'android-d6b19fb213cb801c', 'request_id': '181f0d0e-90d0-45ed-96e7-072822d15c8d', 'tray_session_id': '53d0be98-6e65-4052-9522-7147c8ea4180'}, 'mid': 'ZOisJwABAAHF4RksBn1jRqZHK4-h', 'ig_u_rur': None, 'ig_www_claim': None, 'authorization_data': {'ds_user_id': '50648708396', 'sessionid': '50648708396%3A5hWZMkCGSGqH1p%3A27%3AAYdBrQvJBdEGjK3mfObIMZTxpED9s2SpDnQU47AAcg'}, 'cookies': {}, 'last_login': 1692970031.5774634, 'device_settings': {'app_version': '269.0.0.18.75', 'android_version': 26, 'android_release': '8.0.0', 'dpi': '480dpi', 'resolution': '1080x1920', 'manufacturer': 'OnePlus', 'device': 'devitron', 'model': '6T Dev', 'cpu': 'qcom', 'version_code': '314665256'}, 'user_agent': 'Instagram 269.0.0.18.75 Android (26/8.0.0; 480dpi; 1080x1920; OnePlus; 6T Dev; devitron; qcom; en_US; 314665256)', 'country': 'US', 'country_code': 1, 'locale': 'en_US', 'timezone_offset': -14400})
# cl.login_by_sessionid("50648708396%3ALp9Z12wM82Vosw%3A29%3AAYfsU06Tt_ku4UbtP0Sp6EWzvIgcLOM5_cxIpcL74Q")
# cl.login("dheeraj_joshi2006","Hmdl@2006")
print(cl.get_settings()) #340282366841710301281158063818169511599   17992930484001369
threads=cl.direct_messages(340282366841710301281158063818169511599,50)
f=open("threads.json",'w',encoding='utf-8')

all_threads=[]
for i in threads:
    i=json.loads(i.json())
    print(type(i))
    print(i)
    try:
        del i['clip']['clips_metadata']
    except:
        pass
    all_threads.append(i)
    # print(i)
    
    
f.write(str(all_threads))

