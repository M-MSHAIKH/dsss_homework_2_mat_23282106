import random

# defining function for generating random number (integer) between the min and max of the random number
#Also, return statements ensures that generated random number will be used for further coding
def min_max(minimum, maximum):
    """
    Generate a random integer between the minimum and maximum values.

    Parameters:
     - minimum (int): The minimum value.
     - maximum (int): The maximum value.

    Returns:
     - int: A random integer.
    """
    return random.randint(minimum, maximum)

# defining function for the choice of an arithmetical operations
#return statements ensure that generated choice of operation stored and will be used in the upcoming code
def arithmatic_operations():
    """
    Choose a random arithmetic operation from '+', '-', or '*'.

    Returns:
     - str: An arithmetic operation.
    """
    return random.choice(['+', '-', '*'])

# defining a third function for performing an arithmetic operations using value of n1 n2 and o
# saves the value of p and a by returing the values of the same
def calculations(n1, n2, o):
    """
    Perform an arithmetic operation based on the given numbers and operator.

    Parameters:
     - n1 (int): The first number.
     - n2 (int): The second number.
     - o (str): The arithmetic operator.

    Returns:
     - The final answer
    """
    p = f"{n1} {o} {n2}"
    if o == '+':
        a = n1 + n2
    elif o == '-':
        a = n1 - n2
    else:
        a = n1 * n2
    return p, a

def math_quiz():
    """
    Start the math quiz game.
    """
    score = 0
    total_questions = int(3.14159265359)  #convert to integer Error comes

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    #Starting the game from 0 to total_questions
    for _ in range(total_questions):
        n1 = min_max(1, 10)
        n2 = min_max(1, int(5.5)) #convert to integer Error comes
        operator = arithmatic_operations()

        problem, answer = calculations(n1, n2, operator)
        print(f"\nQuestion: {problem}")

        # Error message if user type other than integer value
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        # Checking the value entered by the user is whether right. If not then 0 score, otherwise 1 score
        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")
        # At the end priting the game end message with total score
    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()



    
