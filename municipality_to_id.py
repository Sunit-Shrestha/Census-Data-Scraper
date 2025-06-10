from bs4 import BeautifulSoup
import requests
import time
import json

list = {}
name_url = "https://censusnepal.cbs.gov.np/results/population?province=2&district=18&municipality=1"
lit_url = "https://censusapi.cbs.gov.np/api/v1/population/highlight/ward?province=4&district=38&municipality=30"
province = 1
for district in range(1, 78):
	time.sleep(3)
	testres = requests.get(f"https://censusapi.cbs.gov.np/api/v1/population/highlight/ward?province={province}&district={district}&municipality=1")
	if testres.status_code == 404:
		province += 1
		testres = requests.get(f"https://censusapi.cbs.gov.np/api/v1/population/highlight/ward?province={province}&district={district}&municipality=1")
	mun = 1
	while True:
		muntestres = requests.get(f"https://censusapi.cbs.gov.np/api/v1/population/highlight/ward?province={province}&district={district}&municipality={mun}")
		if muntestres.status_code == 404:
			break
		res = requests.get(f"https://censusnepal.cbs.gov.np/results/population?province={province}&district={district}&municipality={mun}")
		soup = BeautifulSoup(res.text, "lxml")
		divs = soup.find_all("div", class_="select__single-value")
		names = [div.text for div in divs]
		if mun == 1:
			list[names[1]] = {"id": district, "municipalities":{}}
		list[names[1]]["municipalities"][names[2]] = mun
		print(names[2], " ", mun, " ", names[1], " ", district)
		mun += 1

with open("census_id.json", "w") as f:
	json.dump(list, f, indent='\t')