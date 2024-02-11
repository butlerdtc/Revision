cycling = 200
swimming = 275
jogging = 475

swim_hours = float(input("How many hours have you spent swimming: "))
bike_hours = float(input("How many hours have you spent cycling: "))
jog_hours = float(input("How many hours have you spent jogging: "))

swim_calories = swimming * swim_hours
bike_calories = cycling * bike_hours
jog_calories = jogging * jog_hours

total_calories = (swim_calories + bike_calories + jog_calories)
calories_to_kg = 3500 / 0.454
weight_lost = total_calories / calories_to_kg

print(f"You lost {weight_lost:.3f}kgs today")
