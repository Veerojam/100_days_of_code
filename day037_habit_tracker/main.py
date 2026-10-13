import requests
from datetime import datetime

USERNAME = "astroyax"
TOKEN = "askd00123958asdjngj9234109dnfgjkdsng98123aaa"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph404"
today = datetime.now()

# graph_config = {
#     "id": "graph404",
#     "name": "smthnew",
#     "unit": "commit",
#     "type": "int",
#     "color": "ajisai",
# }

post_pixel_body = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "50",
    "comment": "wellwellwell"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(url=graph_endpoint, json=post_pixel_body, headers=headers)
print(response.text)

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)