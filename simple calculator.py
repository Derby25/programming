def calculator():
    print("Multi-Number Calculator")
    print("Choose an operator:+,-,*,/")
    operator=input("operator:")

    try:
        numbers=input("Enter any numbers seperated by space:").split()
        numbers=[float(num)for num in numbers ]
        
        if not numbers : 
            return " No numbers entered "

        result=numbers[0]
        for num in numbers [1:]:
            if operator=="+":
                result += num
            elif operator=="-":
                result -= num 
            elif operator=="*":
                result *= num
            elif operator =="/":
                if num == 0:
                    result /= num
                else:
                    return " Error Division by zero "
            else :
                  return " Invalid operator "

        return f" Result : { result }"
    except ValueError : 
        return "Invalid input : Please enter numeric values "
result = calculator()
print (result)