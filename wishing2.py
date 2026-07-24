time=input("enter the time:")
if time.endswith("am"):
    hour=int(time[:-2])
    if 1<= hour <=12:
        print("good morning")
    else:
        print("error")
else:
    print("good afternoon")