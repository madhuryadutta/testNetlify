import json 
    
f = open("wordlist.txt", "r")
myString =f.read()
myList = myString.split()
res_dict = {}
for i in range(0, len(myList)):
    res_dict[myList[i]] =1
print(res_dict)
# Convert and write JSON object to file
with open("wordlist.json", "w") as outfile: 
    json.dump(res_dict, outfile)