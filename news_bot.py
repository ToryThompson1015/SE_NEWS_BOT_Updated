import feedparser
import requests
import random

# Hardcoded Slack webhook URL
SLACK_WEBHOOK_URL = 'https://hooks.slack.com/services/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'  # <-- Replace with your actual webhook

# Pool of 7 tech news RSS feeds
RSS_FEEDS = [
    'https://www.theverge.com/rss/index.xml',
    'https://techcrunch.com/feed/',
    'http://feeds.arstechnica.com/arstechnica/index',
    'https://www.wired.com/feed/rss',
    'https://www.infoq.com/feed/',
    'https://thenextweb.com/feed/',
    'https://feeds.feedburner.com/oreilly/radar/atom',
]

# Number of articles to post
total_articles = 2

def fetch_articles(feeds):
    articles = []
    for feed_url in feeds:
        feed = feedparser.parse(feed_url)
        for entry in feed.entries:
            if 'title' in entry and 'link' in entry:
                articles.append({'title': entry.title, 'link': entry.link})
    return articles

def post_to_slack(articles, webhook_url):
    if not articles:
        print('No articles found to post.')
        return
    message = '*Good Morning!!\' Here Are todays Tech News!! Enjoy!!:*\n'
    for article in articles:
        message += f"• <{article['link']}|{article['title']}>\n"
    payload = {'text': message}
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 200:
        print('Articles posted to Slack successfully!')
    else:
        print(f'Failed to post to Slack: {response.status_code} {response.text}')

def main():
    articles = fetch_articles(RSS_FEEDS)
    random.shuffle(articles)
    selected_articles = articles[:total_articles]
    post_to_slack(selected_articles, SLACK_WEBHOOK_URL)

if __name__ == '__main__':
    main()
