'''
Rhombus of Stars

Create a program that reads a positive integer N as input and prints on the console a rhombus with size n.

----------------------------------------------------------------

n = 3
  *      # i = 0, 2 spaces (n - 1 - i spaces), 1 star
 * *     # i = 1, 1 spaces (n - 1 - i spaces), 1 star, 1 space, 1 star
* * *    # i = 2, 0 spaces, 1 star, 1 space, 1 star, 1 space, 1 star
 * *
  *


n = 4
   *
  * *
 * * *
* * * *
 * * *
  * *
   *

'''


def print_row(n, row):
    for space in range(n - row):
        print(' ', end='')
    for start in range(1, row):
        print('*', end=' ')
    print('*')


def print_up(n):
    for row in range(1, n + 1):
        print_row(n, row)


def print_bottom(n):
    for row in range(n - 1, 0, -1):
        print_row(n, row)


def print_rhombus(n):
    print_up(n)
    print_bottom(n)


n = int(input())
print_rhombus(n)