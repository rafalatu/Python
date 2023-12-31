from datetime import datetime as dt
# Get the current time, returns a value like 2022-10-09 17:46:45.151666
today = dt.now()
print(today)
# Get Unix time, returns a value like 1665566809.057217
unix_epoch_time = dt.timestamp(today)
print(unix_epoch_time)



from datetime import datetime as dt

# Get the current date and time
now = dt.now()

# Print the current date and time
print("Current date and time: ", now)

# Print the Unix epoch time
print("Unix epoch time: ", dt.timestamp(now))

# Print the weekday, month, day, year, hours, minutes, and seconds
print("Weekday: ", now.strftime("%A"))
print("Month: ", now.strftime("%B"))
print("Day: ", now.strftime("%d"))
print("Year: ", now.strftime("%Y"))
print("Hours: ", now.strftime("%H"))
print("Minutes: ", now.strftime("%M"))
print("Seconds: ", now.strftime("%S"))



