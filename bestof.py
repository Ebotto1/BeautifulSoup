from bs4 import BeautifulSoup
from urllib2 import urlopen
import csv
BASE_URL = "http://www.washingtoncitypaper.com"
 
def make_soup(url):
html = urlopen(url).read()
return BeautifulSoup(html, "lxml")
 
