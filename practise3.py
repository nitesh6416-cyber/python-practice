import time
hour = int(time.strftime('%H'))
if hour<12:
    print("GOOD MORNING")
elif hour<16:
    print("GOOD AFTERNOON")
elif hour<21:
    print("GOOD EVENING")
else:
    print("good night sir")