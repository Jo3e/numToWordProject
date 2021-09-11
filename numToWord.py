digit = input("Enter a number to convert to words: ")

units = {
        1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine",  10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen",
         18:"eighteen",19:"nineteen"}
         
tens =  {

         20:"twenty", 30:"thirty", 40:"fourty", 50:"fifty", 60:"sixty", 70:"seventy", 
         80:"eight", 90:"ninety"}
         
hundred = { 100:"one hundred", 200:"two hundred"}

def number_to_words(problem):

    if len(digit) <= 2 and int(digit) in units.keys():
        
         print(units[int(digit)])

    
    elif len(digit) == 2 and int(digit) in tens.keys():
        print(tens[int(digit)])

    

    elif len(digit) == 2:
            
        split_number = []

        for letters in digit:
            split_number.append(letters)

        if len(split_number) == 2:
            
            first_letter = split_number[0] + '0'
            second_letter = split_number[1]

        for num in tens.keys():
            first_letter = int(first_letter)
            if first_letter == num:
                global split_tens
                split_tens = tens[first_letter]

        for num in units.keys():
            second_letter = int(second_letter)
            if second_letter == num:
                global split_unit
                split_unit = units[second_letter]

        print(split_tens,'-', split_unit)

    split_number = []

    for letters in digit:
        split_number.append(letters)
    
    if len(split_number) == 3 and split_number[1] == '0':

            
            first_letter = split_number[0] 
            
            second_letter = split_number[1] + '0'
            merged_letters = first_letter + second_letter
            
            third_letter = split_number[2]
            

            for num in hundred.keys():
                merged_letters = int(merged_letters)
                if merged_letters == num:
                    global split_hundred
                    split_hundred = hundred[merged_letters]

            for num in units.keys():
                third_letter = int(third_letter)
                if third_letter == num:
                    global split_units
                    split_units = units[third_letter]

            print(split_hundred, 'and',split_units)


    
    elif len(digit) == 3 and int(digit) in hundred.keys():
        print(hundred[int(digit)])


    elif len(digit) == 3:
        split_number = []

        for letters in digit:
            split_number.append(letters)

        
        if len(split_number) == 3:
            first_letter = split_number[0] + "00" 
            second_letter = split_number[1] + "0"
            third_letter = split_number[2]
            # print(first_letter, second_letter, third_letter)

            for num in split_number:
                first_letter = int(first_letter)
                second_letter = int(second_letter)
            # if split_number[1] == int(0):
            #     second_letter = "and"
                third_letter = int(third_letter)
                if first_letter == hundred.keys():
                    pass
                if second_letter == tens.keys():
                    pass
                if third_letter == units.keys():
                    pass
            print(hundred[first_letter], "and", tens[second_letter], units[third_letter])

           
'''
>>>> Ify check this one out.

roots = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 
         6:"six", 7:"seven", 8:"eight", 9:"nine",  10:"ten", 
         11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 
         16:"sixteen", 17:"seventeen", 18:"eighteen",19:"nineteen", 20:"twenty", 
         30:"thirty", 40:"fourty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety"}

def number_to_words(digit):
    # digit = input("Type a number: ")
    if int(digit) in roots.keys():
         print (roots[int(digit)])
    
    elif len(digit) == 2:
        print (roots[int(digit[0]+'0')]+"-"+number_to_words(digit[-1]))
        
    elif len(digit) == 3:
        if int(digit[1:]) == 0:
            print (roots[int(digit[0])]+ " hundred")
        else:
            print ((roots[int(digit[0])]+ " hundred and "+number_to_words(digit[1:])))
    print ("Try again")

# number_to_words(digit)

'''
    
    
    

number_to_words(digit)




 

