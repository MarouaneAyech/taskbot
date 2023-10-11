import requests

# Request Access Token
auth_url = "https://login.microsoftonline.com/a2d8336e-a299-4d52-8636-b7ef8c117a1d/oauth2/v2.0/token"

my_email="xxxxxx@pi.tn"
my_pass = "xxxxxxx"
client_id = "c6e7381b-14b1-45e4-956b-3d7347aeb5cc"
client_secret = "9Q38Q~1U.bTzsgy476GlKnYrGzTQx2JYQMFhoamF"
data = {
    "grant_type": "password",
    "client_id": client_id,
    "client_secret": client_secret,
    "scope": "https://graph.microsoft.com/.default",
    "username": my_email,
    "password": my_pass
}
auth_response = requests.post(auth_url, data=data)
access_token = auth_response.json()["access_token"]

# Fetch Calendar events
graph_api_base_url = "https://graph.microsoft.com/v1.0/"
calendar_endpoint = graph_api_base_url + "me/events"
headers = {
    "Authorization": "Bearer " + access_token
}
response = requests.get(calendar_endpoint, headers=headers)
events = response.json()["value"]

# Print event details
for event in events:
    print(f"Subject: {event['subject']}")
    print(f"Start: {event['start']['dateTime']}")
    print(f"End: {event['end']['dateTime']}")
    print("------------------------")