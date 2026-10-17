#with open("ward.csv") as f:
 #   lines = f.readlines()
#print("the number of line is:", len(lines))

#with open("ward.csv") as f:
    #lines = f.readlines()
#for line in lines[1:]:
    #print(line.strip())

#with open("ward.csv") as f:
    #lines = f.readlines()
#for line in lines[1:]:
    #parts = line.strip().split(",")
    #print(parts)



#with open("ward.csv") as f:
#    lines = f.readlines()
#for line in lines[1:]:
#    parts = line.strip().split(",")
#    ward = parts[0]
#    area = parts[1]
    #print(ward, "has area", area)

#with open("ward.csv") as f:
 #   lines = f.readlines()
#for line in lines[1:]:
    #parts = line.strip().split(",")
   #  area_km2 = float(parts[1])
 #   area_hectares = area_km2 * 100
#    print(ward, "is", area_hectares, "hectares")
    

with open("ward.csv") as f:
    lines = f.readlines()

for line in lines[1:]:
    parts = line.strip().split(",")
    ward = parts[0]
    area_km2 = float(parts[1])
    if area_km2 > 9:
        size = "large"
    else:
        size = "small"
    print(ward, "is", size)
    