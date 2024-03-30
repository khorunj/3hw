import requests
from bs4 import BeautifulSoup
import json 

URL = 'http://quotes.toscrape.com'

def get_urls():
  urls_list = ['http://quotes.toscrape.com']
  next_page = 'http://quotes.toscrape.com'
  while next_page:
    html_doc = requests.get(next_page)
    soup = BeautifulSoup(html_doc.text, 'html.parser')
    content = soup.select('nav ul.pager li.next a')
    

    for link in content:
        urls_list.append(URL + link['href'])
    next_page=soup.select_one('nav ul.pager li.next a')
    if next_page:
      next_page = URL + next_page['href']
  return urls_list


quotes=[]
authors_url=[]
authors=[]
for link in get_urls():
  html_doc = requests.get(link)
  soup = BeautifulSoup(html_doc.text, 'html.parser')
  content = soup.select('div[class=container] div[class=row] div[class=col-md-8] div[class=quote]')
  
  for li in content:
    quote_text = li.find('span', attrs={'class':'text'}).text.strip()
    author = li.find('small', attrs={'class':'author'}).text.strip()
    tags_element = li.find('div', class_='tags')
    tags_meta = tags_element.find('meta', attrs={'class':'keywords'})
    tags = tags_meta['content'].split(',') if tags_meta else []
    quote_data = {
        "tags" : tags,
        "author" : author,
        "quote" : quote_text
    }
    quotes.append(quote_data)
    abouts=li.select_one('a')['href']
    authors_url.append(URL+abouts)
    
json_data = json.dumps(quotes, indent=4)
with open('quotes.json', 'w') as json_file:
    json_file.write(json_data)

for page in authors_url:
  html_doc = requests.get(page)
  soup = BeautifulSoup(html_doc.text, 'html.parser')
  content = soup.select('div[class=container] div[class=author-details]')
  fullname = soup.find('h3', class_='author-title').text.strip()
  born_date = soup.find('span', class_='author-born-date').text.strip()
  born_location = soup.find('span', class_='author-born-location').text.strip()
  description = soup.find('div', class_='author-description').text.strip()
  authors_data = {
      "fullname": fullname,
      "born_date": born_date,
      "born_location": born_location,
      "description": description
  }
  authors.append(authors_data)
json_data = json.dumps(authors, indent=4)
with open('authors.json', 'w') as json_file:
    json_file.write(json_data)





 
    

 
 