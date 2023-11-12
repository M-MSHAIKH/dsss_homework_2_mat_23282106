#Importing random numbers and performing mathematical tasks on it
import random

# defining function for generating random number (integer) between the min and max of the random number
#Also, return statements ensures that generated random number will be used for further coding
def min_max(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)

# defining function for the choice of an arithmetical operations
#return statements ensure that generated choice of operation stored and will be used in the upcoming code
def arithmatic_operations():
    return random.choice(['+', '-', '*'])

# defining a third function for performing an arithmetic operations using value of n1 n2 and o
# saves the value of p and a by returing the values of the same
def claculations(n1, n2, o):
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2   # Changing the sign for performing correct operations from - to +
    elif o == '-': a = n1 + n2  # Changing the sign for performing correct operations from - to +
    else: a = n1 * n2
    return p, a

def math_quiz():
    s = 0
    t_q = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 =  min_max(1, 10); n2 = min_max(1, 5.5); o = arithmatic_operations()

        PROBLEM, ANSWER = claculations(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()
