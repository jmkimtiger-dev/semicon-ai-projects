process = {"process_name" : "Etching", "Temperature" : 250, "Pressure": 1.2}

print(process["Temperature"])

#값 수정
process["Temperature"] = 300
process["Time"] = 30 #값 추가

print("View keys")
print(process.keys())

for key, value in process.items():
    print(key, ":", value)

print()
print("Exercise")

etch_process = {"process_name": "Etching", "Temperature": 300, "Pressure": 1.2, "Time" : 30}

for key, value in etch_process.items():
    print(key, ":", value)

etch_process["Temperature"]+= 5

for key, value in etch_process.items():
    print(key, ":", value)