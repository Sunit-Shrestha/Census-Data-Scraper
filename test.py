import requests

data = requests.get("https://censusapi.cbs.gov.np/api/v1/economic?province=4&district=38&municipality=1").json()

print(data["data"]["industry"]["countSeries"][0])