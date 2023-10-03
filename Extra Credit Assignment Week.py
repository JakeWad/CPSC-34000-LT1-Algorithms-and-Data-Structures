def str_num_multiply(num1: str, num2: str) -> str:
    # Determine the sign of the result
    sign = ''
    if num1[0] == '-' and num2[0] != '-':
        sign = '-'
        num1 = num1[1:]
    elif num1[0] != '-' and num2[0] == '-':
        sign = '-'
        num2 = num2[1:]
    
    # Reverse the input strings for easier processing
    num1 = num1[::-1]
    num2 = num2[::-1]
    
    # Initialize a list to store intermediate results
    result = [0] * (len(num1) + len(num2))
    
    # Perform multiplication digit by digit
    for i in range(len(num1)):
        for j in range(len(num2)):
            digit1 = int(num1[i])
            digit2 = int(num2[j])
            product = digit1 * digit2
            result[i + j] += product
            if result[i + j] >= 10:
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10
    
    # Convert the result list back to a string
    result_str = ''.join(map(str, result[::-1]))
    
    # Remove leading zeros
    while len(result_str) > 1 and result_str[0] == '0':
        result_str = result_str[1:]
    
    # Add the sign back to the result
    if sign:
        result_str = sign + result_str
    
    return result_str

if __name__ == '__main__':
    print("result 9*3: ", str_num_multiply("9", "3"))
    print("result 100*200: ", str_num_multiply("100", "200"))
    print("result 16*128: ", str_num_multiply("16", "128"))
    print("result -5*10: ", str_num_multiply("-5", "10"))
    print("result -64*-64: ", str_num_multiply("-64", "-64"))
    print("result 16*-64: ", str_num_multiply("16", "-64"))
