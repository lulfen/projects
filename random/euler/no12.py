smallest=1000000 # an arbitrary large number of triangle numbers to calculate
triangle_numbers=[0]
for x in range(smallest): 
    if len(triangle_numbers) ==1:
        triangle_numbers.append(1)
    else:
        triangle_numbers.append(triangle_numbers[-1]+x+1)
    divisors=[] # a list of all possible divisors for the latest triangle number
    div = 1
    t= triangle_numbers[-1] # since I'm lazy I don't like to type too much...
    while div <= int(t/div) :
        if t % div == 0:
            divisors.append(div) # save the latest calculated divisor
            divisors.append(int(t/div)) # also save the quotient to save time and processing cost
        div+=1
        if len(divisors) > 500: # the answer we're looking for
            print('got it!')
            print(triangle_numbers[-1], sorted(divisors))
            print(len(divisors))
            quit()
    if len(triangle_numbers) % 1000 == 0: # just to make it a bit more verbatim
        print(len(triangle_numbers),triangle_numbers[-1])
        print(len(divisors), divisors)
