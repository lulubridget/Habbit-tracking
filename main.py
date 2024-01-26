import requests,os
from datetime import datetime

# habbit_TOKEN=letsyoga123
# habbit_USERNAME=codingyoga
# habbit_GRAPH_ID=coingyogagraph

habbit_TOKEN=os.environ.get("habbit_TOKEN")
habbit_USERNAME=os.environ.get("habbit_USERNAME")
habbit_GRAPH_ID=os.environ.get("habbit_GRAPH_ID")


pixela_endpoint="https://pixe.la/v1/users"
user_params = {
    "token": habbit_TOKEN,
    "username": habbit_USERNAME,
    "agreeTermsOfService":"yes", 
    "notMinor":"yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params, verify=False)


graph_endpoint = f"{pixela_endpoint}/{habbit_USERNAME}/graphs/{habbit_GRAPH_ID}"
print(graph_endpoint)
graph_params = {
    "id":habbit_GRAPH_ID,
    "name":"yoga graph",
    "unit":"minute",
    "type":"float",
    "color":"sora"
}
header = {
    "X-USER-TOKEN": habbit_TOKEN
}
# graph_res= requests.put(url=graph_endpoint, json=graph_params, headers=header, verify=False)


today = datetime(year=2024, month=1, day=23)
post_pixel_endpoint = f"{pixela_endpoint}/{habbit_USERNAME}/graphs/{habbit_GRAPH_ID}/{habbit_GRAPH_ID}.html"
post_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "110"
}
response = requests.post(url=post_pixel_endpoint, json=post_params,headers=header, verify=False)
print(response.text)

# https://pixe.la/v1/users/codingyoga/graphs/coingyogagraph.html