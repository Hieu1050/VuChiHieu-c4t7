from __future__ import unicode_literals
import youtube_dl

ydl_opts = {}
link_list = ['https://www.youtube.com/watch?v=Gvf76_OCXhE','https://www.youtube.com/watch?v=mj1RAJ4JHzM']
info_list = []
for i in link_list:
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(i)
    info_list.append(result)
print (len(info_list))
import json
with open('data.json', 'w') as outfile:
    json.dump(result, outfile)

