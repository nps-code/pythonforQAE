data = {
    "users": [
        {
            "userId": 1,
            "firstName": "Krish",
            "lastName": "Lee",
            "phoneNumber": "123456",
            "emailAddress": "krish.lee@learningcontainer.com"
        },
        {
            "userId": 2,
            "firstName": "racks",
            "lastName": "jacson",
            "phoneNumber": "123456",
            "emailAddress": "racks.jacson@learningcontainer.com"
        }
]
}

print(data["users"][1]["emailAddress"])
if data["users"][1]["emailAddress"] == "racks.jacson@learningcontainer.com":
    print("Match")
else:
    print("No Match")


