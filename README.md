[![PyPI Version](https://img.shields.io/pypi/v/utuby.svg)](https://pypi.org/project/utuby)
[![Coverage Status](https://coveralls.io/repos/github/santhoshse7en/utuby/badge.svg?branch=master)](https://coveralls.io/github/santhoshse7en/utuby?branch=master)
[![License](https://img.shields.io/pypi/l/utuby.svg)](https://pypi.python.org/pypi/utuby/)
[![Documentation Status](https://readthedocs.org/projects/pip/badge/?version=latest&style=flat)](https://santhoshse7en.github.io/utuby_doc)

# utuby

YouTube's API is annoying to work with, and has lots of limitations. utuby is a simple script for downloading Youtube comments without using the Youtube API - No API rate limits. No restrictions. Extremely fast.

| Source         | Link                                         |
| ---            |  ---                                         |
| PyPI:          | https://pypi.org/project/utuby/             |
| Repository:    | https://github.com/santhoshse7en/utuby/     |
| Documentation: | https://santhoshse7en.github.io/utuby_doc/  |


## Dependencies

* beautifulsoup4
* requests
* lxml
* cssselect
* vaderSentiment
* textblob
* pandas


## Dependencies Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install following
```bash
pip install -r requirements.txt
```

## A Glance

Download it by clicking the green download button here on Github. You only need to parse specific YouTube URL as argument.

```python
>>> from utuby.utuby import youtube

>>> url = 'https://www.youtube.com/watch?v=xjQFi-HP7po'

>>> youtube = youtube(url)
```

Directory of youtube class

```python
>>> print(dir(youtube))
```

![ytdir](https://user-images.githubusercontent.com/47944792/58631120-20cba880-82ff-11e9-92be-300d2714d37a.PNG)

**Examples for Extracting YouTube Channel Name**

```python
>>> youtube.channel_name

'Fully'
```

**Examples Calculating Sentiment Scores for extracted YouTube Comments**

```python
>>> youtube.final_sentiment_scores

{'neu': 0.769, 'neg': 0.051, 'pos': 0.178, 'compound': 0.0}
```

**Youtube Comments DataFrame**

```python
>>> youtube.youtube_comments_df.head()
```

![ytdf](https://user-images.githubusercontent.com/47944792/58631134-2c1ed400-82ff-11e9-8575-2b362ed28cb7.PNG)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
