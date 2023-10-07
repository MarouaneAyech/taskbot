import requests

# Après que l'utilisateur a donné son consentement, il a noramlement reçu un code d'autorisation sur la page de redirection.
# On peut échanger maintenant le code d'autorisation  contre un jeton d'accès via le point de terminaison "token".

# Request Access Token
auth_url = "https://login.microsoftonline.com/a2d8336e-a299-4d52-8636-b7ef8c117a1d/oauth2/v2.0/token"

my_email="xxxxxx@pi.tn"
my_pass = "xxxxxxx"
client_id = "4cb54644-785a-48d7-abcd-be881aa75f80" #"c6e7381b-14b1-45e4-956b-3d7347aeb5cc"
client_secret = "Eh88Q~wIe2Pei3P35cXuN_iO0OKWRCyZx2bchaQ4" #"MtS8Q~41HELMlcqT3TkGdDIu7pj4Cp3No0XjebSr"
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
    "subject": "Meet sur projet taskbot",
    "start": {
        "dateTime": "2023-10-07T17:00:00",
        "timeZone": "Africa/Tunis"
    },
    "end": {
        "dateTime": "2023-10-07T17:30:00",
        "timeZone": "Africa/Tunis"
    }
}
response = requests.post(calendar_endpoint, headers=headers, json=new_event)

if 200<=response.status_code<= 205:
    print("New event added successfully!")
else:
    print(f"Failed to add the event. Status code: {response.status_code}, Response: {response.json()}")
