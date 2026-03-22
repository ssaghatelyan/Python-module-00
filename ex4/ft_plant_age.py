def ft_plant_age():
    day = int(input("Enter plant age in days: "))
    if day <= 60:
        print("Plant needs more time to grow.")
    else:
        print("Plant is ready to harvest!")
