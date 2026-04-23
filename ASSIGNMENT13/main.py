file = open("sample_weather.txt", "r")

# Skip header
next(file)

temp_sum = 0
dew_sum = 0
wind_sum = 0
count = 0

for line in file:
    data = line.strip().split(",")

    temperature = float(data[1])
    dewpoint = float(data[2])
    windspeed = float(data[3])

    temp_sum += temperature
    dew_sum += dewpoint
    wind_sum += windspeed
    count += 1

file.close()

# Calculate averages
avg_temp = temp_sum / count
avg_dew = dew_sum / count
avg_wind = wind_sum / count

# Print results
print("Average Temperature:", avg_temp)
print("Average Dew Point:", avg_dew)
print("Average Wind Speed:", avg_wind)