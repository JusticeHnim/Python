import csv

header = ["Name", "Cost", "Level"]
space = [" "]
type1 = ["For Fun"]
data1 = [
    ["Card Pokemon", 15000, "MEDIUM"],
    ["Truyen Conan", 15000, "MEDIUM"]
]

type2 = ["Food"]
data2 = [
    ["Banh cuon", 20000, "MEDIUM"],
    ["Pho bo", 25000, "MEDIUM"]
]


type3 = ["Study"]
data3 = [
    ["But viet", 9000, "LOW"],
    ["Tai lieu", 31000, "HIGH"]
]

with open("test_file_out.csv", "w", encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(type1)
    writer.writerow(header)
    writer.writerows(data1)
    writer.writerow(space)

    writer.writerow(type2)
    writer.writerow(header)
    writer.writerows(data2)
    writer.writerow(space)

    writer.writerow(type3)
    writer.writerow(header)
    writer.writerows(data3)
    writer.writerow(space)

