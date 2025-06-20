import datetime
text = input("ajke ja ja korsi \n>>")
date = datetime.datetime.now().strftime("%Y-%m-%H:%M")

with open("Diary.txt", "a") as file:
    file.write(f"{date} - {text}\n")
    print("Tomar moner kotha saved")


