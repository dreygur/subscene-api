import sys

# Custom Modules
from api.SubScene import SubScene

# Prohbit system from writing byte-codes
sys.dont_write_bytecode = True

# The Traditional main() function
def main():
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

if __name__ == '__main __':
    main()