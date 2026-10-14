days = int(input("Enter the number of days: "))
heights = []
for day in range(1, days + 1):
    h = int(input(f"Enter the height for day {day} in centimetres: "))
    heights.append(h)

print("\n--- Output ---")
for day, h in enumerate(heights, start=1):
    print(f"day {day} ----- {h} cm")    