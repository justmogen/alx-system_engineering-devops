#!/usr/bin/python3
""" Exports all to-do task info of all employees in a json format """

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            user.get("id"): [{
                "tasks": to.get("title"),
                "completed": to.get("completed"),
                "username": user.get("username")
            } for to in requests.get(url + "todos",
                                     params={"userId": user.get("id")}).json()]
            for user in users}, jsonfile)
