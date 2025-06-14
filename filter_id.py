import pandas as pd
import json

df = pd.read_csv("municipalities.csv", header=None, sep=",")
with open("census_id.json") as f:
	ids = json.load(f)

def getprovince(district):
	if district in ids.keys():
		return ids[district]["province"]
	else:
		return -1

def getdistrict(district):
	if district in ids.keys():
		return ids[district]["id"]
	else:
		return -1

def getid(data):
	for mun in ids[data[1]]["municipalities"].keys():
		if data[0] in mun:
			return ids[data[1]]["municipalities"][mun]
	return -1

df[2] = df[1].map(getprovince)
df[3] = df[1].map(getdistrict)
df[4] = df.apply(getid, axis = 1)

print(df.head())
df.to_csv("required_ids.csv", index=None, header=None)
