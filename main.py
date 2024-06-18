# Import 'random' and 'time' libraries
import random, time


# Store all alphabets, lowercase and uppercase, in 'letters' (List - String)
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


# Store all numbers from 0-9 in 'numbers' (List - String)
numbers = ["0", "1" , "2", "3", "4", "5", "6", "7", "8", "9"]


# Store some symbols in 'symbols' (List - String)
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


# Display welcome message
print("\nWelcome to the PyPassword Generator!")


# Get number of letters, number of numbers and number of symbols, and store it in 'number_of_letters' (Integer), 'number_of_numbers' (Integer) and 'number_of_symbols' (Integer) respectively
while True:
    try:
        number_of_letters = int(input("\nHow many letters would you like in your password (0 - 52)?\n"))
        if number_of_letters < 0 or number_of_letters > 52:
            print("\nInvalid input. Only integers within the range are accepted.")
        else:
            number_of_numbers = int(input("\nHow many numbers would you like in your password (0 - 10)?\n"))
            if number_of_numbers < 0 or number_of_numbers > 10:
                print("\nInvalid input. Only integers within the range are accepted.")
            else:
                number_of_symbols = int(input("\nHow many symbols would you like in your password (0 - 9)?\n"))
                if number_of_symbols < 0 or number_of_symbols > 9:
                    print("\nInvalid input. Only integers within the range are accepted.")
                else:
                    break
    except ValueError:
        print("\nInvalid input. Only integers are accepted.")


# Add password contents based on requirements and shuffle it to generate password
password = []
random.shuffle(letters)
random.shuffle(numbers)
random.shuffle(symbols)
for l in letters[0:number_of_letters]:
    password.append(l)
for n in numbers[0:number_of_numbers]:
    password.append(n)
for s in symbols[0:number_of_symbols]:
    password.append(s)
random.shuffle(password)
password = "".join(password)


# Display password
print(f"\nHere is your password:\n{password}")


# Display exit message
print("\nProgram exiting...")


# Exit program after 5 second delay
for delay in range(5):
    time.sleep(1)
