from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print(current_time)
print(type(current_time))

if (datetime.now().strftime("%H:%M:%S") >= "06:00:00") and (datetime.now().strftime("%H:%M:%S") <= "23:00:00"):
    print("hi")
else:
    print("Not Hi")