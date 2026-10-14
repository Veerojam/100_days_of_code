from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com")
response.raise_for_status()

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="a", class_="storylink")

article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_nr = max(article_upvotes)
largest_index = article_upvotes.index(largest_nr)


# for i in range(len(article_texts)):
#     print(f"{article_texts[i]}, {article_links[i]}. Upvotes: {article_upvotes[i]}")

for text, link, upvotes in zip(article_texts, article_links, article_upvotes):
    print(f"{text}, {link}. Upvotes: {upvotes}")

# print(article_texts[largest_index])
# print(article_links[largest_index])


# with open("./day045_beautifulsoup/website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)

# anchor_tags = soup.find_all(name="a")
# print(anchor_tags)

# for tag in anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText()) #get only the text
# print(section_heading.name) # print only the name of the ..
# print(section_heading.get("class"))


# company_url = soup.select_one(selector="p a") # get a hold of an element with specific tags (a within p)
# print(company_url)

# name = soup.select_one(selector="#name") 
# print(name)

# headings = soup.select(".heading")
# print(headings)