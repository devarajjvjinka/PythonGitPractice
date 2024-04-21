input_range = range(1 ,51)

for inputs in input_range:
    if inputs%3==0 and inputs%5==0:
        print(inputs ," = FizzBuzz")
    else:
        if inputs % 3 == 0 and inputs % 5 != 0:
             print(inputs," = Fizz")
        else:
            if inputs % 3 != 0 and inputs % 5 == 0:
                print(inputs," = Buzz")
            else:
                if inputs % 3 != 0 and inputs % 5 != 0:
                    print(inputs);
