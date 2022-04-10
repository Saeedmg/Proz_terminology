import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
from random import randint


data = []

for pg in range(1, 202 + 1):

	page = requests.get("https://www.proz.com/kudoz/?kudoz_search_form=true&from=.fs&to=eng&prefs%5Bfields%5D=any&page={}".format(pg))
	soup = BeautifulSoup(page.text, 'xml')
	farsi = soup.findAll("div", {"flex-row middle-xs-flex"})


	for i in farsi:
		row = i.findAll("div", {"ks__term"})
		if len(row) == 2:
			a = row[0].text.strip()
			b = row[1].text.strip()
			data.append((a, b))
			
df = pd.DataFrame(data)
df.to_csv("result2.tsv", index=False, encoding='utf-8', sep='\t')		
		

	

	










	