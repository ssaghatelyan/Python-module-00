def  ft_count_harvest_recursive():
    days_count = int(input("Days until harvest: "))
    def print_days(curr, total):
        if curr > total:
            print("Harvest time!")
        else:
            print(f"Day {curr}")
            print_days(curr + 1, total)
    print_days(1, days_count)