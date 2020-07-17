# Precedence in Python
# Example: (2 + 5) *3 = 21
print("\nPrecedence Output:")
print(2+5*3)
print((2+5)*3)

# Casting Data Types
print("\nCasting Data Types Output:")
print(float(3))
print(int(3.14))
print("Hello" + str(3))

# Variables in Python
# Example: Kinetic Energy
print("\nVariables Output:")
mass = 40
velocity = 20
kineticEnergy = (1/2) * mass * (velocity ** 2)

print("The Kinetic Energy of an object with a mass of", mass)
print("and a velocity of", velocity, end = " ")
print("has a Kinetic Energy of ", kineticEnergy)

print("and a velocity of", velocity, end=" ")
print("has a Kinetic Energy of " + str(kineticEnergy))

# Changing a variables value
print("\nChanging a variables value Output:")
mass += 10  # Equivalent to mass = mass + 10
print("New mass:", mass)

# String variable example
print("\nString Variables Output:")
firstName = "Bill"
lastName = "Gates"
fullName = firstName + " " + lastName
print("Fullname", fullName)

# Changing the Data Type of a variable
print("\nChanging Variable Type Output:")
myInt = 343
print("My Int:", myInt)
myInt = "Jonathan"
print("My Int:", myInt)