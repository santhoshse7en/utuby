from utuby.youtube_video_info import info
from utuby.youtube_comments import comments
from utuby.utils import *

class youtube:

    """
    Collects info. and comments from the multi-media content in YouTube when url is given.
    :param youtubeid: Unique identification for every multimedia in YouTube.
    """

    def __init__(self, url):
        start_time = datetime.now()
        info.__init__(self, url)
        comments.__init__(self, url)
        time_delta = datetime.now() - start_time
        print('\n' + str("Calculating time taken to extract info. of input url") + ":  " + str(time_delta.seconds) +  "  seconds")
