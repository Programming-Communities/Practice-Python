# Prime check karne ka tareeqa
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Main program start
name = input("Apna naam bataiye: ")

# User ke 3 pasandeeda numbers lete hain
print(f"Hello, {name}! Apke pasandeeda numbers ke sath masti karte hain.")
favorite_numbers = []
favorite_numbers.append(int(input("Apna pehla pasandeeda number dijiye: ")))
favorite_numbers.append(int(input("Apna doosra pasandeeda number dijiye: ")))
favorite_numbers.append(int(input("Apna teesra pasandeeda number dijiye: ")))

# Even ya odd check karte hain
even_odd_info = []
for number in favorite_numbers:
    if number % 2 == 0:
        even_odd_info.append((number, "even"))
    else:
        even_odd_info.append((number, "odd"))

# Even/odd result print karte hain
for number, info in even_odd_info:
    print(f"Number {number} {info} hai.")

# Har number ka square nikalte hain
for number in favorite_numbers:
    square = number ** 2
    print(f"Number {number} ka square: ({number}, {square})")

# Sum nikalte hain
total_sum = sum(favorite_numbers)
print(f"\nAmazing! Apke numbers ka sum hai: {total_sum}")

# Sum prime hai ya nahi check karte hain
if is_prime(total_sum):
    print(f"Wow, {total_sum} ek prime number hai!")
else:
    print(f"{total_sum} ek prime number nahi hai.")
