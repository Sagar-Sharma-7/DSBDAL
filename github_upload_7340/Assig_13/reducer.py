import sys

temp_total = dew_total = wind_total = 0
temp_count = dew_count = wind_count = 0

for line in sys.stdin:
    key, value = line.strip().split("\t")
    value = int(value)
    
    if key == "temp":
        temp_total += value
        temp_count += 1
    elif key == "dew":
        dew_total += value
        dew_count += 1
    elif key == "wind":
        wind_total += value
        wind_count += 1

print("Average Temperature:", temp_total / temp_count)
print("Average Dew Point:", dew_total / dew_count)
print("Average Wind Speed:", wind_total / wind_count)