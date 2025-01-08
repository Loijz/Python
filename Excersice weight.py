weight = int(input("Weight: "))
metrics = input("(K)g or (L)bs: ")
if metrics.upper() == "K":
    converted = weight / 0.45
    print("Weight in Lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("Weight in Kgs: " + str(converted))