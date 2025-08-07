import requests

import os








os.system("clear")
 #Raw string to avoid unicode issues
print("""\033[33m
  ▘    ▄▖  ▐▘         ▗ ▘    
  ▌▛▌  ▐ ▛▌▜▘▛▌▛▘▛▛▌▀▌▜▘▌▛▌▛▌
  ▌▙▌  ▟▖▌▌▐ ▙▌▌ ▌▌▌█▌▐▖▌▙▌▌▌
   ▌                         

\033[00m
\033[35m====================================
\033[31mOwner      : J1S4N
GitHub     : J1S4N
Facebook   : J1SAN
\033[35m====================================
""")

ip= input("Enter Targat IP :")
rq= requests.get("http://ip-api.com/json/"+ip)

tx= rq.json()

print("\n\033[1;34m📍 IP Address Information\033[0m")
print("\033[34m" + "="*35 + "\033[0m")
print(f"\033[1;32m🌍 Country        :\033[0m {tx['country']} ({tx['countryCode']})")
print(f"\033[1;32m🗺️ Region          :\033[0m {tx['regionName']}")
print(f"\033[1;32m🏙️ City            :\033[0m {tx['city']}")
print(f"\033[1;32m📮 Zip Code       :\033[0m {tx['zip']}")
print(f"\033[1;32m📌 Coordinates    :\033[0m {tx['lat']},{tx['lon']}")
print(f"\033[1;32m⏰ Timezone       :\033[0m {tx['timezone']}")
print(f"\033[1;32m🌐 ISP            :\033[0m {tx['isp']}")
print(f"\033[1;32m🏢 Organization   :\033[0m {tx['org']}")
print(f"\033[1;32m🔍 IP Address     :\033[0m {tx['query']}")
print("\033[34m" + "="*35 + "\033[0m")



#{'status': 'success', 'country': 'Bangladesh', 'countryCode': 'BD', 'region': 'B', 'regionName': 'Chittagong', 'city': 'Chittagong', 'zip': '4100', 'lat': 22.2231, 'lon': 91.8441, 'timezone': 'Asia/Dhaka', 'isp': 'CONNECT 3', 'org': 'Farhan Fuad', 'as': 'AS138548 CONNECT 3', 'query': '103.185.24.183'}



#নিচে রঙসহ একটি সুন্দর ডিজাইন দেওয়া হলো, যা Python টার্মিনালে কাজ করবে (ANSI escape codes ব্যবহৃত হয়েছে):

#```python
#print("\n\033[1;34m📍 IP Address Information\033[0m")
#print("\033[34m" + "="*35 + "\033[0m")
#print(f"\033[1;32m🌍 Country        :\033[0m {tx['country']} ({tx['countryCode']})")
#print(f"\033[1;32m🗺️ Region         :\033[0m {tx['regionName']}")
#print(f"\033[1;32m🏙️ City           :\033[0m {tx['city']}")
#print(f"\033[1;32m📮 Zip Code       :\033[0m {tx['zip']}")
#print(f"\033[1;32m📌 Coordinates    :\033[0m {tx['lat']}, {tx['lon']}")
#print(f"\033[1;32m⏰ Timezone       :\033[0m {tx['timezone']}")
#print(f"\033[1;32m🌐 ISP            :\033[0m {tx['isp']}")
#print(f"\033[1;32m🏢 Organization   :\033[0m {tx['org']}")
#print(f"\033[1;32m🔍 IP Address     :\033[0m {tx['query']}")
#print("\033[34m" + "="*35 + "\033[0m")
#```

#*রঙগুলোর মানে:*
#- *নীল (Blue):* শিরোনাম ও বর্ডার
#- *সবুজ (Green):* লেবেল
#- *সাদা (Default):* ভ্যালু

#তুমি চাইলে রঙ কাস্টমাইজ করতেও পারো। এটা Windows Terminal, Termux, Linux Terminal ইত্যাদিতে ভালো কাজ করবে।