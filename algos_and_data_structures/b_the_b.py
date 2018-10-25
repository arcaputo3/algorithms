import math
# Practice for methods described in Python: Beyond the Basics - Pluralsight

# --- Classes ---

# Example of a complex number class
class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def __str__(self):
        # Note the use of a conditional expression
        # Note the distinction between a cond. expression and a cond. statement
        opp = '+' if self.imag >= 0 else ''
        return "{0}{1}{2}i".format(self.real,opp,self.imag)

    def __add__(self, rhs):
        return ComplexNumber(self.real + rhs.real, self.imag + rhs.imag)

    def __sub__(self, rhs):
        return ComplexNumber(self.real - rhs.real, self.imag - rhs.imag)

    def __mul__(self, rhs):
        return ComplexNumber(self.real * rhs.real - self.imag * rhs.imag, self.real * rhs.imag + self.imag * rhs.real)

    def __abs__(self):
        return ComplexNumber(math.sqrt(self.real**2 + self.imag**2),0)


c1 = ComplexNumber(2,-3)
c2 = ComplexNumber(3, 4)
print(c1)
print(c1 + c2)
print(c1 * c2)
print(abs(c1))

# --- Callable instances ---

# Defines what is callable and what is not
print(callable(print))
print(callable(1))

# --- *args and **kwargs ---

# HYPERVOLUME: Computes the hypervolume of a hyperbox with at least one dimension
# INPUT:    n>0 int lengths where n is the number of inputted lengths
# OUTPUT:   The volume of the hyperbox with given dimensions

def hypervolume(length, *lengths):
    v = length
    for item in lengths:
        v *= item
    return v


# We can pass as many lengths as we like, as long as there is at least occurences
print(hypervolume(1))
print(hypervolume(1,2))
print(hypervolume(1,2,3))
# Using the * operator in the call, we can unpack a list as arguments
print(hypervolume(*list(range(1,10))))


# --- Zip ---
n = 5

a = list(range(n))
b = list(range(n,2*n))
c = list(range(2*n,3*n))

list_of_lists = [a,b,c]

# Print each row as is
for i in list_of_lists:
    print(i)

# Print the transpose of the list of lists
for item in zip(*list_of_lists):
    print(list(item))
