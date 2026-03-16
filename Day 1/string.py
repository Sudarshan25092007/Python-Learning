# String basics - like Java String but with extras
greeting = "Hello, Python!"  # Or 'single quotes'
name = "Sudarshan Patil H J"

# Access chars (0-indexed, like Java charAt())
print(greeting[0])      # 'H' indexing starts from 0 same as we do in array/java.
print(greeting[-4])     # '!' (negative index from end), start from -1 unlike 0 from starting

# Slicing: greeting[start:end] (end exclusive)
print(greeting[0:4])    # 'Hello'
print(greeting[::2])    # 'Hlo,Pyhn!' (every 2nd char)

# # Common methods (chainable, no new String like Java)
print(name.lower())     # 'sudarshan'
print(name.upper())     # 'SUDARSHAN'
print(name.replace("Su", "Super"))  # 'Superdarshan'

# Check: Like Java startsWith/contains
print(name.startswith("Su"))  # True
print(" " in greeting)  # True (membership test)

# Multi-line: Triple quotes
message = """Line 1
Line 2 - like Java text blocks
even after python"""
print(message)

# name = input("Your name: ")  # User input
# days = int(input("Gym days: ") or 0)
# print(f"{name} gyms {days} days: {'Super' if days >= 5 else 'Good'} consistent!")

print(name.split())
initials = ''.join(word.upper() for word in name.split())
print(initials)