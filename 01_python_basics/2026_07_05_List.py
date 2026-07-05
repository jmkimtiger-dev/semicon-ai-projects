temperatures = [250, 300, 280, 320, 290]

print(temperatures[0])
print(temperatures[2])

print("length :", len(temperatures))

for temp in temperatures:
    print(temp)

print()

semi_temperatures = [100, 200, 300, 400, 500]
total = 0

for temp in semi_temperatures:
    total+=temp
    print(temp)

avg = total / len(semi_temperatures)
print("average :", avg)

for temp in semi_temperatures:
    if temp > avg:
        print(temp) 

print("위치까지 출력")

for i, temp in enumerate(semi_temperatures):  #인덱스 먼저,값 나중,0번시작
    print(i, temp)

print("평균보다 높은 값 위치까지")

for i, temp in enumerate(semi_temperatures,start=1):
    if temp > avg:
        print(i, temp)