# CH. 모듈 패키지
# 기본
# import msg.email
# import msg.sns

# e = msg.email.Email();
# s = msg.sns.SMS()
# e.send("010","020","이메일")
# s.send("010","020",'메세지')
# s.ping("010")

# from
from msg import email
from msg import sns
from functools import partial
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="my-app")
location = geolocator.geocode("Seoul, Korea")
print(location.address, location.raw)

e = email.Email();