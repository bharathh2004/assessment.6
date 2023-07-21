import json
f = open('D:\employees.json')
data = json.load(f)
for i in data['employee']:
    print(i)

# import json

# dict = {"tamilnadu":"chennai","telangana":"hydrabad","tripura":"agartala","karnataka":"bangalore","kerala":"thiruvanandhapuram"}
# with open('D:\employees.json','w')as file:
#   json.dump(dict,file) 