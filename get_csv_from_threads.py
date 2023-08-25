from threads import data
import pandas as pd 
Urls=[]
Thumbnail_urls=[]
UserNames=[]

for i in data:
    # if i['item_type']!='text' and i['item_type']!='item_type':
    if i['item_type']=='clip':
        url=f"https://www.instagram.com/p/{i['clip']['code']}"
        Urls.append(url)
        Thumbnail_url=i['clip']['thumbnail_url']
        Thumbnail_urls.append(Thumbnail_url)
        UserName=i['clip']['user']['username']
        UserNames.append(UserName)

df=pd.DataFrame({
    "Url":Urls,
    "Thumbnail_url":Thumbnail_urls,
    "UserName":UserNames
})     

df.to_csv("Super_Mumbai_Batch_1.csv",index=False)  
        