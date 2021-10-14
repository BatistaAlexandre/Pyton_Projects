import math
import time
print("Welcome to the velocity calculator. Please enter the following: ")
print()
time.sleep(1)
m_mass = float(input("Mass (in kg): "))
user_gravity = float(input("""Choose gravity (in m/s²) from :
[1] Earth
[2] Jupiter 
"""))
if user_gravity == 1:
    g_gravity = float(9.8)
elif user_gravity == 2:
    g_gravity = float(24)
t_time = float(input("Time (in seconds): "))
user_density = float(input("""Choose the fluid:
[1] Air
[2] Water
"""))
if user_density == 1:
    p_density = float(1.3)
elif user_density == 2:
    p_density = float(1000)
A_cross_sectional_area = float(input("""Cross sectional area (in m²):"""))
#Bowling Ball = math.pi * 0.10795 ** 2
#Loaf of bread = 0.275
#Skydiver = 0.45
user_drag_constant = float(input("""Drag constant
[1] Sphere
[2] Long Cylinder
[3] Short Cylinder
[4] Cone
[5] Cube
"""))
if user_drag_constant == 1:
    C_drag_constant = float(0.47)
elif user_drag_constant == 2:
    C_drag_constant = float(0.82)
elif user_drag_constant == 3:
    C_drag_constant = float(1.15)
elif user_drag_constant == 4:
    C_drag_constant = float(0.50)
elif user_drag_constant == 5:
    C_drag_constant = float(1.05)
print()
inner_value_c = (1 / 2) * p_density * A_cross_sectional_area * C_drag_constant
print(f"The inner value of c is: {inner_value_c:.3f}")
velocity = math.sqrt((m_mass * g_gravity) / inner_value_c) * (1 - math.exp((math.sqrt(m_mass * g_gravity * inner_value_c) / m_mass) * t_time * -1))
print(f"The velocity after {t_time} seconds is: {velocity:.3f} m/s")
print()
velocity_earth = math.sqrt((m_mass * 9.8) / inner_value_c) * (1 - math.exp((math.sqrt(m_mass * 9.8 * inner_value_c) / m_mass) * t_time * -1))
velocity_jupiter = math.sqrt((m_mass * 24) / inner_value_c) * (1 - math.exp((math.sqrt(m_mass * 24 * inner_value_c) / m_mass) * t_time * -1))
print(f"The velocity on Earth would be {velocity_earth:.3f} m/s, and on Jupiter would be {velocity_jupiter:.3f} m/s")
print()
terminal_velocity = math.sqrt((m_mass * g_gravity * 2) / inner_value_c)
print(f"The terminal velocity is {terminal_velocity:.2f} m/s")