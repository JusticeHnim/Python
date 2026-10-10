#Dua data vao, la 1 file json
import json
import csv
import logging

#Cau hinh logging
logging.basicConfig( 
    filename="app.log", 
    filemode="a", 
    format="%(asctime)s - %(levelname)s - %(message)s", 
    level=logging.INFO, 
    encoding="utf-8" 
)

#Ham danh gia level cua cost
def findLevel(level):
    if(level>0  and level <=10000):
        return "LOW"
    elif(10000< level <=30000):
        return "MEDIUM"
    else:
        return "HIGH"

#Ghi vet trong chuong trinh bang try...except
try:
    with open("data.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    logging.info("Đọc file data.json thành công.")
except FileNotFoundError:
    logging.error("Không tìm thấy file data.json trên hệ thống !")
    data=[]
except json.JSONDecodeError:
    logging.error("File data.json bị lỗi định dạng JSON!")
    data=[]

#Ghi ra file CSV
if data:
    with open("cleaned_expenses.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)

        writer.writerow(["Type", "Name", "Cost", "Level"])

        for item in data:
            item_type = item.get("type")
            item_cost = item.get("cost", 0)

            #Loai bo neu thieu key type hoac cost<=0
            if not item_type or item_cost<=0:
                continue

            item_name = item.get("name", "")
            item_level = findLevel(item_cost)

            writer.writerow([item_type, item_name, item_cost, item_level])

    logging.info("Đã xuất dữ liệu sạch ra file cleaned_expenses.csv thành công.")