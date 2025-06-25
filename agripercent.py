import requests
import pandas as pd

emp_link = "https://censusapi.cbs.gov.np/api/v1/economic"
df = pd.read_csv("required_ids.csv", header=None, sep=",")

def get_emp(row):
	province = row[2]
	district = row[3]
	mun = row[4]
	if province == -1 or district == -1 or mun == -1:
		return -1
	params = {
		"province": province,
		"district": district,
		"municipality": mun
	}
	json_data = requests.get(emp_link, params=params).json()
	econ_data = json_data["data"]["industry"]["countSeries"][0] 
	return int(econ_data["data"][0] * 1000 / econ_data["total"]) / 10

empdf = df.apply(get_emp, axis=1)
empdf.to_csv("agripercent.csv", header=None, index=None)
