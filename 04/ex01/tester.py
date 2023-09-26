from in_out import outer
from in_out import square
from in_out import pow


x = 3
my_counter = outer(x, square)
print(my_counter())
print(my_counter())
print(my_counter())
print(x)
print("---")
another_counter = outer(1.5, pow)
print(another_counter())
print(another_counter())
print(another_counter())
