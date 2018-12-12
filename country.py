#File 1

import pandas as pd

#file 1 create city data

index_country = [1,2,3,4,5,6,7,8,9,10,
                 11,12,13,14,15,16,17,18,19,20,
                 21,22,23,24,25,26,27,28,29,30,
                 31,32,33,34,35,36,37,38,39,40,
                 41,42,43,44,45,46,47,48,49,50,
                 51,52,53,54,55,56,57,58,59,60,
                 61,62,63]
name_country = ['Bangwa','Wutthakat','Talat Phlu','Pho Nimit','Wongwian Yai'
                ,'Krung Thon Buri','Saphan Taksin','Surasak','Suksa Witthaya'
                ,'Chong Nonsi','Sala Daeng','Ratchadamri','Siam Silom','National Stadium'
                ,'Bearing','Bang Na','Udom Suk','Punnawithi','Bang Chak','On Nut','Phra Khanong','Ekkamai'
                ,'Thong Lo','Phrom Phong','Asok','Nana','Phloen Chit','Chit Lom','Siam','Ratchathewi','Phaya Thai BTS'
                ,'Victory Monument','Sanam Pao','Ari','Sena Ruam','Saphan Khwai','Mo Chit'
                ,'Hua Lamphong','Sam Yan','Si Lom','Lumphini','Khlong Taei','Queen Sirikit National Convention Centre'
                ,'Sukhumwit','Phetchaburi','Pha Ram 9','Thailand Cultural Centre','Huai Khwang','Sutthisan'
                ,'Ratchadaphisek','Lat Phrao','Phahon Yothin','Chatuchak Park','Kamphaeng Phet','Bang Sue'
                ,'Phaya Thai ARL','Ratchaprarop','Makkasan','Ramkhamhaeng','Hua Mak','Ban Thap Chang','Lat Krabang'
                ,'Suvarnabhumi']
name_line = ['BTS Silom Line','BTS Sukhumvit Line','MRT','ARL']

station_open = ['Yes']*63

station_open[8] = 'No'
station_open[34] = 'No'



d = {'index':index_country,'country_name':name_country,'station_open':station_open}
data = pd.DataFrame(data=d)
data.to_csv("country.csv",index=False)




