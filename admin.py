users = [
    {"name": "Alice", "role": "admin"},
    {"name": "Bob", "role": "user"},
    {"name": "Charlie", "role": "admin"},
    {"name": "David"},
    {"name": "Eve", "role": "moderator"}
]
admins=0
for users in users:
    try:
        if users["role"] == "admin":
            admins+=1
    except KeyError:
        continue
print (admins)

