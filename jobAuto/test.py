import json
with open('user.json') as details:
    user_data=json.load(details)

for key in user_data['Role']:
    role=key
    break

print(user_data['Role'][role][0])