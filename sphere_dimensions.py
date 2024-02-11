import math

radius = float(input("Enter the radius of the sphere: "))
pi_value = math.pi
area = 4 * pi_value * (radius ** 2)
volume = (4 / 3) * pi_value * (radius ** 3)
print(f"Your sphere has a volume of {volume:.2f}cm^3 and an area of {area:.2f}"
      f"cm^2")
