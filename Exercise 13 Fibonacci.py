# Write a program that asks the user how many Fibonacci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions. Make sure to ask the user to enter
# the number of numbers in the sequence to generate.
#
# (Hint: The Fibonacci sequence is a sequence of numbers where the next number in the sequence is the
# sum of the previous two numbers in the sequence.
#
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

#  Secuencia de Fibonacci: Xn = X(n - 2) + X(n - 1)
#  Partiendo de que los dos primeros números de la serie de Fibonacci son X0 = 0 y X1 = 1...


def fibonacci():
    fibonacci_sequence = [0, 1]
    n = int(input("For 'Fibonacci sequence = X0, X1, X2, X3, ... , Xn' define n = "))

    if n == 0:
        fibonacci_sequence = [0]
    elif n == 1:
        fibonacci_sequence
    else:
        for i in range(1, n + 1):
            fibonacci_sequence.append(fibonacci_sequence[len(fibonacci_sequence) - 2] +
                                      fibonacci_sequence[len(fibonacci_sequence) - 1])
    print("Fibonacci = ", fibonacci_sequence)

fibonacci()