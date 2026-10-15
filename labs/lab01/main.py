# CS 31 Lab Activity 1
# October 15, 2026
# Ricardo Alvarez Davila

# 2. Display Hello, World!
print("Hello, World!")
print()

# 3. Add Two Numbers
add_num1 = 10
add_num2 = 55
add_sum = add_num1 + add_num2
print(f"{add_num1} + {add_num2} = {add_sum}")

# 4. Multiply Three Numbers
mult_a = 5
mult_b = 10
mult_c = 2
mult_product = mult_a * mult_b * mult_c
print(f"{mult_a} x {mult_b} x {mult_c} = {mult_product}")
print()

# 5, 6, 7. Variables for name and major
firstName = "Ricardo"
lastName = "Alvarez Davila"
major = "Cloud Computing"

# 8. Display Your Name
print(f"My name is {firstName} {lastName}.")

# 9. Display Your Major
print(f"My major is {major}.")
print()

# 10. Ask for num1
num1_str = input("Enter a number from 0 - 100: ")
num1 = int(num1_str)
print(f"You entered {num1}.")
print()

# 11. Ask for num2
num2_str = input("Enter a number from 10 - 10000: ")
num2 = int(num2_str)
print(f"You entered {num2}.")
print()

# 12. Multiply num1 and num2
product = num1 * num2
print(f"{num1} x {num2} = {product}")
print()

# 13. Experiment
server_count = 8
instances_per_server = 4
total_instances = server_count * instances_per_server
print(f"Cloud Experiment: Running {server_count} servers with {instances_per_server} instances gives {total_instances} total instances.")
