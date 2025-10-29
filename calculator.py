import math

print("Select a formula to calculate:")
print("1. F = G * m1 * m2 / r**2  (Gravitational Force)")
print("2. V**2 = U**2 + 2 * a**2  (Kinematics)")
print("3. F = m * r  (Force relation)")
print("4. I = P / (4 * π * R**2)  (Intensity)")

choice = input("Enter your choice (1, 2, 3, or 4): ")


if choice == "1":
    G = float(input("Enter gravitational constant G: "))
    m1 = float(input("Enter mass m1 (kg): "))
    m2 = float(input("Enter mass m2 (kg): "))
    r = float(input("Enter distance r (m): "))
    F = G * m1 * m2 / (r ** 2)
    print("Gravitational Force F =", F, "N")

if choice == "2":
    U = float(input("Enter initial velocity U (m/s): "))
    a = float(input("Enter acceleration a (m/s²): "))
    V2 = U**2 + 2 * (a**2)
    print("Final velocity squared V² =", V2, "(m/s)²")


if choice == "3":
    m = float(input("Enter mass m (kg): "))
    r = float(input("Enter radius/distance r (m): "))
    F = m * r
    print("Force F =", F, "N")


if choice == "4":
    P = float(input("Enter power P (W): "))
    R = float(input("Enter distance R (m): "))
    I = P / (4 * math.pi * R**2)
    print("Intensity I =", I, "W/m²")


if choice not in ["1", "2", "3", "4"]:
    print("Invalid choice. Please select 1, 2, 3, or 4.")