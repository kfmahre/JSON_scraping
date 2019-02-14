#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 21:51:46 2019

@author: Kyle Mahre
"""

import requests

search_url = "http://buckets.peterbeshai.com/api/?player=201939&season=2015"

""" Request data """
header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
response = requests.get(search_url, headers=header)
root = response.json()
username = 'kfmahre'

# This for loop iterates through the data to add up all the action type and
# adds to the variable jShot if the 'ACTION_TYPE' is 'Jump Shot':
jShot = 0
for i in range(len(root)):
    if root[i]['ACTION_TYPE'] == 'Jump Shot':
        jShot += 1

mShot = 0
# This for loop operates like the one for variable jShot, but it adds another 
# condition for 'EVENT_TYPE' being valued to 'Made Shot':
for i in range(len(root)):
    if root[i]['ACTION_TYPE'] == 'Jump Shot' and root[i]['EVENT_TYPE'] == 'Made Shot':
        mShot += 1

# Simple arithmetic to get successful attempt percentage:
SA = (mShot/jShot)*100

# Print calls:
print(username)
print(jShot)
print(mShot)
print(round(SA, 2))