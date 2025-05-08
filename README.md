[![PyPI Version](https://img.shields.io/pypi/v/utuby.svg)](https://pypi.org/project/utuby)
[![License](https://img.shields.io/pypi/l/utuby.svg)](https://pypi.python.org/pypi/utuby/)
[![Documentation Status](https://readthedocs.org/projects/pip/badge/?version=latest\&style=flat)](https://santhoshse7en.github.io/utuby_doc)
[![Downloads](https://pepy.tech/badge/utuby/month)](https://pepy.tech/project/utuby)

# 🎥 utuby

YouTube’s official API is restrictive 😤 — rate limits, quotas, API keys...
**utuby** is a fast and simple Python tool that scrapes YouTube **comments** without using the API —
✅ No rate limits,
✅ No keys,
✅ No restrictions.

---

## 🔗 Project Links

|  Source        |  Link                                                     |
| ---------------- | ----------------------------------------------------------- |
| 🐍 PyPI          | [utuby on PyPI](https://pypi.org/project/utuby/)            |
| 🛠 Repository    | [GitHub Repo](https://github.com/santhoshse7en/utuby/)      |
| 📚 Documentation | [Read the Docs](https://santhoshse7en.github.io/utuby_doc/) |

---

## 📦 Dependencies

* `beautifulsoup4`
* `requests`
* `lxml`
* `cssselect`
* `vaderSentiment`
* `textblob`
* `pandas`

---

## 📥 Installation

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Quick Start

```python
from utuby.utuby import youtube

url = "https://www.youtube.com/watch?v=xjQFi-HP7po"
youtube = youtube(url)
```

---

## 🔍 Features & Examples

### 🧭 Explore Available Methods

```python
print(dir(youtube))
```

![Directory](https://user-images.githubusercontent.com/47944792/58631120-20cba880-82ff-11e9-92be-300d2714d37a.PNG)

---

### 📺 Get Channel Name

```python
>>> youtube.channel_name
'Fully'
```

---

### 🧠 Sentiment Analysis of Comments

```python
>>> youtube.final_sentiment_scores
{'neu': 0.769, 'neg': 0.051, 'pos': 0.178, 'compound': 0.0}
```

---

### 📊 View YouTube Comments as DataFrame

```python
>>> youtube.youtube_comments_df.head()
```

![DataFrame](https://user-images.githubusercontent.com/47944792/58631134-2c1ed400-82ff-11e9-8575-2b362ed28cb7.PNG)

---

## 🤝 Contributing

Contributions are welcome! 🛠️
For major changes, please open an issue first to discuss what you’d like to improve or add.
✅ Don’t forget to update or add tests accordingly.

---

## 📜 License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/) 🪪

---
