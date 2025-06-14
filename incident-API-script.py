import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def apiTicketScript():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url, verify=False)
    posts = response.json()
    print("Incident details:")
    for post in posts[:9]:
        print(f"Incident Details: {post['id']}: {post['title']}")
try:
    apiTicketScript()
except:
    pass
