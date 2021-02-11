#!/usr/bin/python3.9
import requests
import random
from app_keys import app_id, app_key
banned_words = ["cancer", "child", "childbirth", "chink",  "cock",
                "confederacy", 'mutilated', "molest", "miscarriage",
                "miscarry", "midget", "mongrel"]

base_url_m = \
    "https://od-api.oxforddictionaries.com/api/v2/search/thesaurus/en?q=m&" + \
    "prefix=true"
base_url_c = \
    "https://od-api.oxforddictionaries.com/api/v2/search/thesaurus/en?q=c&" + \
    "prefix=true"

rm = requests.get(base_url_m, headers={"app_id": app_id, "app_key": app_key})
rc = requests.get(base_url_c, headers={"app_id": app_id, "app_key": app_key})

word_m = random.choice(rm.json()['results'])['word'].to_lower
while " " in word_m or "-" in word_m or word_m in banned_words:
    word_m = random.choice(rm.json()['results'])['word']

word_c = random.choice(rc.json()['results'])['word']
while " " in word_c or "-" in word_c or word_c in banned_words:
    word_c = random.choice(rc.json()['results'])['word']

print(word_m + " " + word_c)
