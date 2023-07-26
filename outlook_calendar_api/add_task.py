import requests

# Request Access Token
auth_url = "https://login.microsoftonline.com/a2d8336e-a299-4d52-8636-b7ef8c117a1d/oauth2/v2.0/token"

my_email = "xxxxx@pi.tn"
my_pass = "xxxxxx"
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

# Create a new event
graph_api_base_url = "https://graph.microsoft.com/v1.0/"
calendar_endpoint = graph_api_base_url + "me/events"
headers = {
    "Authorization": "Bearer " + access_token,
    "Content-Type": "application/json"
}
new_event = {
    "subject": "Préparer le cours de Python",
    "start": {
        "dateTime": "2023-07-28T09:00:00",
        "timeZone": "UTC"
    },
    "end": {
        "dateTime": "2023-07-28T11:00:00",
        "timeZone": "UTC"
    }
}
response = requests.post(calendar_endpoint, headers=headers, json=new_event)

if response.status_code == 200:
    print("New event added successfully!")
else:
    print(f"Failed to add the event. Status code: {response.status_code}, Response: {response.json()}")
