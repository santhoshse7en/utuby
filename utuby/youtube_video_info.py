from utuby.utils import *

class info:

    """
    Collects comments from the multi-media content in YouTube when url is given.
    :param youtubeid: Unique identification for every multimedia in YouTube.
    """
    def __init__(self, url):
        self.url = url
        soup = BeautifulSoup(get(self.url).text, 'lxml')
        sys.stdout.write('===========================================' + '\n')
        sys.stdout.write('    Extracting Youtube Basic Information   ' + '\n')
        sys.stdout.write('===========================================' + '\n')
        sys.stdout.write('1. Channel Name' + '\n')
        sys.stdout.write('2. Subscribers' + '\n')
        sys.stdout.write('3. Published Date' + '\n')
        sys.stdout.write('4. Description' + '\n')
        sys.stdout.write('5. Views' + '\n')
        sys.stdout.write('6. Likes' + '\n')
        sys.stdout.write('7. Dislikes' + '\n')
        sys.stdout.write('===========================================' + '\n')
        sys.stdout.flush()

        try:
            self.channel_name = soup.select_one('.yt-user-info').getText().strip()
        except:
            self.channel_name = None

        try:
            self.subscribers = soup.select_one('.yt-subscriber-count').getText()
        except:
            self.subscribers = None

        try:
            self.published_date = soup.select_one('.watch-time-text').getText()
        except:
            self.published_date = None

        try:
            self.description = ' '.join(soup.select_one('#watch-description-text').text.split())
        except:
            self.description = None

        try:
            self.views = round(int(''.join(i for i in soup.select_one('.watch-view-count').text if i.isdigit()))/ (10 ** 5), 2)
        except:
            self.views = None

        try:
            self.likes = int(''.join(i for i in soup.select_one('button[title="I like this"]').get_text() if i.isdigit()))
        except:
            self.likes = None

        try:
            self.dislikes = int(''.join(i for i in soup.select_one('button[title="I dislike this"]').get_text() if i.isdigit()))
        except:
            self.dislikes = None