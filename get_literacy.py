import requests
import pandas as pd

lit_link = "https://censusapi.cbs.gov.np/api/v1/population/highlight/ward"
df = pd.read_csv("required_ids.csv", header=None, sep=",")

def get_literacy(row):
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
	json_data = requests.get(lit_link, params=params).json()
	return json_data["data"]["literacy_total"]

litdf = df.apply(get_literacy, axis=1)
litdf.to_csv("literacy.csv", header=None, index=None)
