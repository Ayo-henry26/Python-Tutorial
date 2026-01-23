user_role = {
    "Jesse" : "read",
    "Ayo" : "admin",
    "Rasheed" : "read",
    "Alameen" : "read"
}

while True:
    username = input("Enter admin name: ")
    if user_role.get(username) == "admin":
        print("Access Granted")
        break
    elif user_role.get(username) == "read":
        print("Access Denied")
    else:
        print("Enter a valid username")