# There are different ways to reverse a number but I coded two of them here.
# This algorithm takes every digit from the right and puts it at the right of the new number.
n = int(input())
normal = n
t = 0
if n < 0:
    n = abs(n)
    t = 1
reversed1 = 0
while n != 0:
    digit = n % 10
    reversed1 = reversed1 * 10 + digit
    n //= 10
if t == 1:
    reversed1 = -reversed1

# The other way is to easily print it backwards.
# print(str(normal)[::-1])
# But to make it work for also negative numbers we have to add some steps.
x = 0
if normal < 0:
    normal = abs(normal)
    x = 1
if x == 1:
    reversed2 = -int(str(normal)[::-1])
else:
    reversed2 = int(str(normal)[::-1])

print(f"The result with the first alg is {reversed1} and with the second alg is {reversed2}")