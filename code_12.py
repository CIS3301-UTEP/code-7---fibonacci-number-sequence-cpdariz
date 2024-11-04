def get_fibonacci_number(position):
    if position == 0:
        return 0
    if position == 1:
        return 1
    else:
        return get_fibonacci_number(position - 1) + get_fibonacci_number(position - 2)
    
def get_fibonacci_number_sequence(number):
    sequence = []
    for i in range(1,number+1):
        sequence.append(get_fibonacci_number(i))
    return sequence
    
if __name__ == "__main__":
    position = 5
    print(f"Fibonacci number at position {position} is: {get_fibonacci_number(position)}")

    number_of_elements = 7
    print(f"Fibonacci sequence for {number_of_elements} elements: {get_fibonacci_number_sequence(number_of_elements)}")