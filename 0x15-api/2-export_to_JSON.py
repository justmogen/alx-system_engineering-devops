#!/usr/bin/python3
"""Export to-do list information for a specified employee ID in json format."""

import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": to.get("title"),
                "completed": to.get("completed"),
                "username": username
            } for to in todos]}, jsonfile)
