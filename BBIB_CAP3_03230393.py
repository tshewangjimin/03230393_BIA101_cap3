################################
# https://github.com/tshewangjimin/03230393_BIA101_cap3
# Tshewang Dema
# BBI "B"
# 03230393
################################
# REFERENCES
# https://youtu.be/DCaKj3eIrro?si=-QZWRSEk-mskiKv5 
# https://youtu.be/1Y-Zsdf66JU?si=TYFk9DWhLcRL4jjQ

################################
# SOLUTION
# Solution Score:  495653
################################

# Define a function to process the file and calculate the sum
def process_file(filename):
    total_sum = 0
    
    # Open the file and read line by line
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()  # Remove any leading/trailing whitespace
            
            # Extract first digit from the start
            first_digit = None
            for char in line:
                if char.isdigit():
                    first_digit = char
                    break
            
            # Extract last digit from the end
            last_digit = None
            for char in reversed(line):
                if char.isdigit():
                    last_digit = char
                    break
            
            # Form the two-digit number if both digits are found
            if first_digit and last_digit:
                two_digit_number = int(first_digit + last_digit)
                total_sum += two_digit_number
    
    return total_sum

# Path to the input file
input_file = r'C:\Users\Dell\Desktop\CAP3\393.txt'

# Call the function and print the result
result = process_file(input_file)
print("The total sum from 393.txt file is :", result)
