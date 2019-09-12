# Python wraper for SubScene(.)com

We are working on developing an api for Subscene(.)com. And making the code more managable.
Before using in production please be sure it works well.

### Usage:

CLI:
```
Use: -n 'name' -y 'year' -l 'language' [Optional]
    Usage:
        -h or --help | Show this help message
        -n or --name | Name of the movie/media
        -y or --year | Year of release
        -l or --lang | Language of desired subtitle
```

Script:
```python3
from subscene2.SubScene import SubScene

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
