import requests
from pprint import pprint

URL = "http://127.0.0.1:5000/users/"

def deactivate_user(user_id):
    response = requests.delete(URL+str(user_id))
    if response.status_code == 204:
        print("Success")
    else:
        print("Error when deactivating user")

if __name__ == "__main__":
    user_id = input("Type in the user's id")
    deactivate_user(user_id)
    