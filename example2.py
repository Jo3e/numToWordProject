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
<<<<<<< HEAD
        
        name = units[int(digit[0])]+ " hundred and "+tens[int(digit[1]+"0")]+"-"+units[int(digit[-1])]
    #print(name)

    elif len(digit) == 3 and int(digit[1]) == '0':
        name = units[int(digit[0])] + "hundred and "+ units[int(digit[-1])]
        

    print(name)
=======
        if int(digit[1:]) == 0:
            print (roots[int(digit[0])]+ " hundred")
        else:
            print ((roots[int(digit[0])]+ " hundred and "+number_to_words(digit[1:])))
    print ("Try again")
>>>>>>> 46811d3bc147bade76489a2e9bb3f07f11ada4ba

# number_to_words(digit)