#web scraping is basically searching , downloading and cleaning of data for usage.
#in a url if you add- /robots.txt for finding what data can be scraped?
#googlebot is used to index  the webpages i.e. create a DATABASE and is used in SEO
import requests
from bs4 import BeautifulSoup
import pprint

res= requests.get("https://news.ycombinator.com/news")
res2=requests.get("https://news.ycombinator.com/news?p=2")
#print(res.text) #gives the entire HTML file
soup = BeautifulSoup(res.text, 'html.parser')
soup2= BeautifulSoup(res2.text, 'html.parser')

links=soup.select('.storylink')  #1
subtext= soup.select('.subtext')  #2
links2=soup2.select('.storylink')  #3
subtext2= soup2.select('.subtext')  #4

mega_links= links + links2
mega_subtext= subtext + subtext2

def sort_stories_by_votes(hnlist):
	return sorted(hnlist, key=lambda k:k['votes'], reverse= True) #this arranges the articles in descending order of votes.


#our aim for the hacker project is to enlist the articles of the field of our choice.
def create_custom_hn(links,subtext):
	hn=[]
	for inx , item in enumerate(links):
		title= item.getText()
		href= item.get('href', None)
		vote=subtext[inx].select('.score')
		if len(vote):
		 points= int(vote[0].getText().replace('points', ''))
		 if points >99:
		     hn.append({'title': title, 'link':href,'votes': points})
	return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links,mega_subtext))