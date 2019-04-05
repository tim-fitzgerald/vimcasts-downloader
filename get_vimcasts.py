import os
import re

from bs4 import BeautifulSoup
import requests

BASE_URL = "http://media.vimcasts.org/videos/"
cwd = os.getcwd()

if not os.path.exists(os.path.dirname(f"{cwd}/videos/")):
    try:
        os.makedirs(os.path.dirname(f"{cwd}/videos/"))
    except:
        print("Huh")

for i in range(1, 76):
    try:
        url = f"{BASE_URL}{i}"
        r = requests.get(url).text
        clean_text = BeautifulSoup(r, features="html.parser").get_text()
        endpoint = re.search("(.)+.(m4v|mp4)", clean_text)
        url = f"{BASE_URL}{i}/{endpoint.group()}"
        print(url)
        r = requests.get(url, allow_redirects=True)
        open(f'{cwd}/videos/{i}_{endpoint.group()}', 'wb').write(r.content)
    except:
        print("Something broke and Im lazy")
        break

print("Done! Enjoy your vimcasts")
