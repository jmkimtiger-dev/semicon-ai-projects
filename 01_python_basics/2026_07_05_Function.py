def greet(name):
    print(f"Hello, {name}!") 
greet("Jaemin")

def add(a,b):
    result = a+b
    return result

tot = add(3,5)
print(tot)

def calculate_average(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    return avg

temperatures = [30, 25, 28, 32, 29]
avg_temp = calculate_average(temperatures)
print(avg_temp)

def print_process_info(process):
    for key, value in process.items():
        print(f"{key} : {value}")
        
def get_temperature(process):
    return process["temperature"]

etch_process = {
    "process_name" : "etching",
    "temperature" : 250,
    "pressure" : 1.5,
    "time" : 120
}

print_process_info(etch_process)
print(get_temperature(etch_process))

temp = get_temperature(etch_process)
print(f"Temperature is {temp} degrees")
