def greet(bot_name, birth_year):
    """
    Greets the user and introduces the bot with its name and creation year.

    Parameters:
    bot_name (str): The name of the bot.
    birth_year (str): The year the bot was created.
    """
    print(f'Hello! My name is {bot_name}.')
    print(f'I was created in {birth_year}.')

def remind_name():
    """
    Prompts the user to input their name and then compliments them on their name.
    """
    print('Please, remind me of your name.')
    name = input("Your name: ")
    print(f'What a great name you have, {name}!')

def guess_age():
    """
    Asks the user for the remainders when dividing their age by 3, 5, and 7,
    then calculates and prints their age using a mathematical trick.
    """
    print('Let me guess your age.')
    print('Enter the remainders of dividing your age by 3, 5, and 7.')

    rem3 = int(input("Remainder when divided by 3: "))
    rem5 = int(input("Remainder when divided by 5: "))
    rem7 = int(input("Remainder when divided by 7: "))

    # Calculating age using the Chinese Remainder Theorem
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print(f"Your age is {age}; that's a great time to start programming!")

def count():
    """
    Prompts the user to input a number and then counts from 0 to that number,
    demonstrating the bot's counting ability.
    """
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input("Enter a number: "))
    curr = 0
    while curr <= num:
        print(f"{curr}!")  # Counting with an exclamation mark for emphasis
        curr += 1  # Incrementing the counter

def test():
    """
    Asks the user a programming-related question and keeps asking until they
    select the correct answer.
    """
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")

    # Loop until the user provides the correct answer
    while True:
        answer = int(input("Please select the correct option (1-4): "))

        if answer == 2:
            print("That's correct! Congratulations!")
            break  # Exit the loop if the answer is correct
        else:
            print("Incorrect. Please, try again.")

def end():
    """
    Concludes the conversation with a friendly message.
    """
    print('Congratulations, have a nice day!')

# Start the bot interaction
greet('Kaia', '2024')  # Adjust bot name and birth year as needed
remind_name()  # Ask for the user's name
guess_age()  # Guess the user's age
count()  # Demonstrate counting ability
test()  # Test the user's programming knowledge
end()  # End the conversation
