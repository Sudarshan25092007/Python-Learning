# For loop: Like Java enhanced for (iterates sequences)
gym_days = [6, 5, 4, 7, 3]  # List (like ArrayList<Integer>)
total = 0
for day in gym_days:
    print(f"Day: {day}")
    total += day  # Indentation defines block!
print(f"Avg gym days: {total / len(gym_days):.1f}")  # :.1f formats float

# Range: Like Java for(int i=0; i<5; i++)
for i in range(5):  # 0 to 4
    print(f"Loop {i}: Practice Python!")

# While: Like Java while
count = 0
while count < 3:
    print("Keep coding!")
    count += 1  # Infinite without increment!

# Break/Continue: Like Java
for i in range(10):
    if i == 5:
        break  # Exit loop
    if i % 2 == 0:
        continue  # Skip even
    print(i)  # Prints odds 1,3

total_days = 0
count = 0
for _ in range(3):  # _ ignores value
    try:
        day = int(input("Gym day: "))
        total_days += day
        count += 1
    except ValueError:
        print("Invalid—skip")
if count > 0:
    print(f"Avg: {total_days / count}")

name="Sudarshan patil h j"
myname=name.strip()
for letter in myname:
    print(letter,end="-")