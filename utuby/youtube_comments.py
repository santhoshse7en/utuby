from utuby.utils import *

YOUTUBE_COMMENTS_URL = 'https://www.youtube.com/all_comments?v={youtube_id}'
YOUTUBE_COMMENTS_AJAX_URL = 'https://www.youtube.com/comment_ajax'

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'

sentiment_analyzer = SentimentIntensityAnalyzer()


def find_value(html, key, num_chars=2):
    pos_begin = html.find(key) + len(key) + num_chars
    pos_end = html.find('"', pos_begin)
    return html[pos_begin: pos_end]


def extract_comments(html):
    tree = lxml.html.fromstring(html)
    item_sel = CSSSelector('.comment-item')
    text_sel = CSSSelector('.comment-text-content')
    time_sel = CSSSelector('.time')
    author_sel = CSSSelector('.user-name')

    for item in item_sel(tree):
        yield {'cid': item.get('data-cid'),
               'text': text_sel(item)[0].text_content(),
               'time': time_sel(item)[0].text_content().strip(),
               'author': author_sel(item)[0].text_content()}


def ajax_request(session, url, params, data, retries=5, sleep=15):
    for _ in range(retries):
        response = session.post(url, params=params, data=data)
        if response.status_code == 200:
            response_dict = json.loads(response.text)
            return response_dict.get('page_token', None), response_dict['html_content']
        else:
            time.sleep(sleep)


def download_comments(youtube_id, sleep=1):
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT

    # Get Youtube page with initial comments
    response = session.get(YOUTUBE_COMMENTS_URL.format(youtube_id=youtube_id))
    html = response.text


    ret_cids = []
    for comment in extract_comments(html):
        ret_cids.append(comment['cid'])
        yield comment['text']

    page_token = find_value(html, 'data-token')
    session_token = find_value(html, 'XSRF_TOKEN', 4)

    first_iteration = True

    # Get remaining comments (the same as pressing the 'Show more' button)
    while page_token:
        data = {'video_id': youtube_id,
                'session_token': session_token}

        params = {'action_load_comments': 1,
                  'order_by_time': True,
                  'filter': youtube_id}

        if first_iteration:
            params['order_menu'] = True
        else:
            data['page_token'] = page_token

        response = ajax_request(session, YOUTUBE_COMMENTS_AJAX_URL, params, data)
        if not response:
            print("Comments Unavailable for the Video: ", youtube_id)
            break

        page_token, html = response
        for comment in extract_comments(html):
            if comment['cid'] not in ret_cids:
                ret_cids.append(comment['cid'])
                yield comment['text']

        first_iteration = False
        time.sleep(sleep)


def comment_analyzer(self, url):
    neu_sum, neg_sum, compound_sum, pos_sum, count = 0,0,0,0,0
    youtube_id = ''.join(url[-11:])
    self.comments = []
    try:
        for comment in download_comments(youtube_id):
            count += 1
            sys.stdout.write('Total %d comment(s) downloaded\r' % count)
            sys.stdout.flush()
            self.comments.append(comment)
            score = sentiment_analyzer.polarity_scores(comment)
            neu_sum += score['neu']
            neg_sum += score['neg']
            pos_sum += score['pos']

        self.total_comments_count = len(self.comments)

        if count:
            time.sleep(1)
            self.final_sentiment_scores = {"neu" : round(neu_sum / count, 3), "neg" : round(neg_sum / count, 3), "pos" : round(pos_sum / count, 3), "compound" : round(compound_sum / count, 3)}
            sentiment_score = [sentiment_analyzer.polarity_scores(comment)['compound'] for comment in self.comments]
            polarity_score = [sentiment_analyzer.polarity_scores(comment) for comment in self.comments]

            sentiment = []
            for comment in self.comments:
                analysis = TextBlob(comment)
                # set sentiment positive/negative/neutral
                if analysis.sentiment.polarity > 0:
                    sentiment.append('positive')
                elif analysis.sentiment.polarity == 0:
                    sentiment.append('neutral')
                else:
                    sentiment.append('negative')

            self.youtube_comments_df = pd.DataFrame({'Youtube Comments' : self.comments, 'sentiment' : sentiment, 'sentiment_score' : sentiment_score, 'polarity_scorce' : polarity_score})
        else:
            self.final_sentiment_scores = {"neu" : 0, "neg" : 0, "pos" : 0, "compound" : 0}
            self.youtube_comments_df = None
            print('Sorry no comments for analysis! and not possible to create youtube_comments dataframe')
    except Exception as e:
        print('Error:', str(e))
        sys.exit(1)


class comments:

    """
    Collects comments from the multi-media content in YouTube when url is given.
    :param youtubeid: Unique identification for every multimedia in YouTube.
    """

    def __init__(self, url):
        self.url = url
        sys.stdout.write('===========================================' + '\n')
        sys.stdout.write('  Extracting & Analyzing Youtube Comments  ' + '\n')
        sys.stdout.write('===========================================' + '\n')
        sys.stdout.write('1. Comments' + '\n')
        sys.stdout.write('2. Final Sentiment Score' + '\n')
        sys.stdout.write('3. Total Comments Count' + '\n')
        sys.stdout.write('4. Youtube Comments DataFrame' + '\n')
        sys.stdout.write('===========================================' + '\n')
        comment_analyzer(self, url)
