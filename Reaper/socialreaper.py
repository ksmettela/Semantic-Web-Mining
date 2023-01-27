# -*- coding: utf-8 -*-
"""socialreaper.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1M_RCRYCoVzIBFgmYK6d5LNmZxWwOMtqy
"""

# pip install socialreaper

from socialreaper import Reddit
from socialreaper.tools import flatten

rdt = Reddit("mcARrYvmfrJoDHru2n41Lg", "Ffaz3xZKikYWBOUWuYXiPRj00zA_xQ")
threads = rdt.search("India")
threads_data = [thread["data"]["selftext"] for thread in threads]
for i in threads_data:
  print(i)

from socialreaper import YouTube


def check_dict_keys(lst, keys):
        for item in lst:
            for key in keys:
                print(item)
ytb = YouTube("AIzaSyCsG9Y9yLIWHjUvxtln7z7E0i9vyBD1Or0")
videos = ytb.channel("UC6nSFpj9HTCZ5t-N3Rm3-HA", count=50)
videos = list(videos)
check_dict_keys(videos, ["etag", "id", "kind", "snippet"])

from socialreaper import Facebook
fbk = Facebook('EAAugTEz2oJgBAGZAzZCrDe9UkC8GhvmKpuCxSjQ9yCgNLATUsgQRAZCk2ypuGcJT7ziQkWVPdbCpZCAukx82M3DxQQsJiTZC2gqMlbOtvA3muGf5oUDtfi4vGw2ThZBYyL1bZCtgyu0KH8jXkBGgXPSo6MmNRG4AhjVVxbGsyjZBfMy2Y4D2baBpiMZAlEpozZANdQRd90FdFwRoxLGkV3Mtp1EhbsWB5QEZANuwL60FcOTHzXf9ZCiKayFw')
comments = fbk.page_posts_comments("mcdonalds", post_count=1000, 
    comment_count=100000)

for comment in comments:
    print(comment['message'])