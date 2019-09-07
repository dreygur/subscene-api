# This is development brach of Subtitle-Finder

We are working on developing an api for Subscene(dot)com. And making the code more managable.
Don't use this branch for production use. It will always break.

Usage:
```python3
from subscene.SubScene import SubScene

sub = SubScene() # Initialize the api Class
detail = {
    'name': 'Hello',
    'year': '2008'
    }
link = sub.getDetail(detail) # Available Subtitles
print(link)
links = sub.getSubLink(link) # Link to Specific Subtitle
print(links)
down = sub.getDownLink(links[0]) # DownLoad link for Specific Language
print(down)
```

Making with :heart: by [Rakibul Yeasin](https://github.com/dreygur) and [Abdullah Zayed](https://github.com/xaadu)