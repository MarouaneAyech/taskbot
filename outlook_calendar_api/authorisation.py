import requests

# Point de terminaison d'autorisation OAuth 2.0 (v2) :
# -----------------------------------------------------
# Ce point de terminaison est la première étape du processus d'authentification OAuth 2.0. 
# Il est utilisé pour initier l'authentification de l'utilisateur et demander son consentement. 
# Lorsqu'on redirige l'utilisateur vers ce point de terminaison, il est invité à s'authentifier et 
# à approuver les autorisations demandées par votre application.

# Point de terminaison d'autorisation OAuth 2.0 (v2)
authorize_url = "https://login.microsoftonline.com/a2d8336e-a299-4d52-8636-b7ef8c117a1d/oauth2/v2.0/authorize"

# Les informations d'identification
my_email = "xxxxxxx.tn"
my_pass = "xxxxxxxx"
client_id = "4cb54644-785a-48d7-abcd-be881aa75f80"

# Paramètres de la demande d'autorisation
params = {
    "client_id": client_id,
    "response_type": "code",  # Utilisez "code" pour le flux d'authentification code/autorisation
    "redirect_uri": "http://www.pi.tn",
    "scope": "https://graph.microsoft.com/.default",  # Les autorisations demandées
}

# On construit l'url de la page de connexion Azure AD dans laquelle s'effectue le consentement de l'utilisateur
# L'utilsiateur s'athentifie et doit accepter pour avoir le code d'accès
authorization_url = f"{authorize_url}?client_id={params['client_id']}&response_type={params['response_type']}&redirect_uri={params['redirect_uri']}&scope={params['scope']}"

# On affiche la redirection de l'utilisateur vers la page de connexion Azure AD
print(f"Redirigez l'utilisateur vers cette URL pour l'authentification et le consentement : {authorization_url}")