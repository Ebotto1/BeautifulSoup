from bs4 import BeautifulSoup
from urllib2 import urlopen
import csv
BASE_URL = "http://www.chicagoreader.com"
 
def make_soup(url):
 html = urlopen(url).read()
 return BeautifulSoup(html, "lxml")
  
def get_category_links(section_url):
 soup = make_soup(section_url)
 boccat = soup.find("dl", "boccat")
 category_links = [BASE_URL + dd.a["href"] for dd in boccat.findAll("dd")]
 return category_links
 print category_links
 
def get_category_winner(category_url):
 soup = make_soup(category_url)
 category = soup.find("h1", "headline").string
 winner = [h2.string for h2 in soup.findAll("h2", "boc1")]
 runners_up = [h2.string for h2 in soup.findAll("h2", "boc2")]
 return {"category": category,
  "category_url": category_url,
  "winner": winner,
  "runners_up": runners_up}
 print category
 
if __name__ == '__main__':
 food_n_drink = ("http://www.chicagoreader.com/chicago/best-of-chicago-2011-food-drink/BestOf?oid=4106228")
 categories = get_category_links(food_n_drink)
 category_data = []
 winner_data = []
 runnerup_data = []
 category_link_data = []
 
for category in categories:
 website_category = get_category_winner(category)["category"]
 category_data.append(website_category)
  
 runnerup = get_category_winner(category)["runners_up"]
 runnerup_data.append(runnerup)
  
 winner = get_category_winner(category)["winner"]
 winner_data.append(winner)
 
 website_link = get_category_winner(category)["category_url"]
 category_link_data.append(website_link)
 
category_data_string = str(category_data).replace(u'\xa0', ' ').encode('utf-8')
runnerup_data_string = str(runnerup_data).replace(u'\xa0', ' ').encode('utf-8')
winner_data_string = str(winner_data).replace(u'\xa0', ' ').encode('utf-8')
category_link_data_string = str(category_link_data).replace(u'\xa0', ' ').encode('utf-8')
 
 
with open("best of food.csv","w") as file:
 writer = csv.writer(file)
 for var in zip(category_data_string.split(","), winner_data_string.replace("["," ").split("]"), runnerup_data_string.replace("["," ").split("]"), category_link_data_string.split(",")):
  writer.writerow(var)
