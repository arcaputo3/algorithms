# See https://www.businessinsider.com/heres-the-answer-to-that-impossible-quant-interview-question-2011-9 for problem statement

# We have numbers of form
# 1000*a + 100*b + 10*c + d
# We want (in digit form)
# ab + cd = bc
# i.e. 10*a + b + 10*c + d = 10*b + c
def find_special_nums():
    # Create empty list for storage
    numbers = []
    # Iterate over all possible four digit numbers
    for i in range(0,9999):
         # Formatting to include 0's at front
         i = str(i)
         if len(i) < 4:
             for z in [1,2,3]:
                 if len(i) == z:
                     i = '0'*(4-z) + i
         # Get each digit
         a,b,c,d = tuple(int(x) for x in tuple(i))
         # Append if criterion satisfied
         if 10*a + b + 10*c + d == 10*b + c:
             numbers.append(i)
    return numbers

if __name__ == "__main__":
    # Get numbers
    numbers = find_special_nums()
    # Print numbers and length
    print(numbers)
    print(len(numbers))
