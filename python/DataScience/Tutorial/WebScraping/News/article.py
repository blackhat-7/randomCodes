from newspaper import Article

url = "https://edition.cnn.com/2020/09/06/india/india-mental-health-dst-intl-hnk/index.html"
article = Article(url)
article.download()
article.parse()
print(article.authors)
print(article.publish_date)
print(article.top_image)
article.nlp()
print(article.keywords)
print(article.summary)
