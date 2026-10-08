#Dua data vao, la 1 file json
import json
import csv

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

#Loc cac type trong data_raw
types = {item["type"] for item in data if "type" in item}
#print(types)

def findLevel(level):
    if(level>0  and level <=10000):
        return "LOW"
    elif(level>10000 and level <=30000):
        return "MEDIUM"
    else:
        return "HIGH"
    
with open("cleaned_expenses.csv", "w", encoding="utf-8", newline='') as k:
    writer = csv.writer(k) 

    for t in types:
        #Tao header
        writer.writerow(["Type", "Name", "Cost", "Level"])
        #Loc cac item co type = t va phan loai level
        for item in data:
            if "type" in item and item["type"] == t:
                name = item.get("name", "")
                cost = item.get("cost", 0)
                if(cost<=0):
                    continue
                else:
                    level = findLevel(cost)
                writer.writerow([t, name, cost, level])





