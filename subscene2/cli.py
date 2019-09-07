import sys
from tqdm import tqdm
from .SubScene import SubScene

def help():
    print("""
    Use: -n 'name' -y 'year' -l 'language' [Optional]
    Usage:
        -h or --help | Show this help message
        -n or --name | Name of the movie/media
        -y or --year | Year of release
        -l or --lang | Language of desired subtitle
    """)

def run(name, year, lang):
    sub = SubScene()  # Initialize the api Class
    detail = {
        'name': name,
        'year': year
    }
    for _ in tqdm(range(1)):
        link = sub.getDetail(detail)  # Available Subtitles
        # print(link)
        links = sub.getSubLink(link, lang)  # Link to Specific Subtitle
        # print(links)
        down = sub.getDownLink(links[0])  # DownLoad link for Specific Language
        print(down)

def main():
    if len(sys.argv) < 5 or sys.argv[1][1] == 'h':
        help()
        sys.exit()
    else:
        if sys.argv[1][1] == 'n' and sys.argv[3][1] == 'y':
            name, year = sys.argv[2], sys.argv[4]
        elif sys.argv[3][1] == 'n' and sys.argv[1][1] == 'y':
            name, year = sys.argv[4], sys.argv[2]

        if len(sys.argv) > 5 and sys.argv[5][1] == 'l':
            lang = sys.argv[6][1]
        else:
            lang = 'English'

        run(name, year, lang)


if __name__ == '__main__':
    main()
