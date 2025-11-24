ids = {
    "user1": [213, 213, 213, 15, 213],
    "user2": [54, 54, 119, 119, 119],
    "user3": [213, 98, 98, 35],
}
un_ids = []
for i, j in ids.items():
    for items in j:
        un_ids.append(items)


un_ids = set(un_ids)
print(un_ids)
