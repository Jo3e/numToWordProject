digit = input("Enter a number to convert to words: ")
0
units = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 
         6:"six", 7:"seven", 8:"eight", 9:"nine",  10:"ten", 
         11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 
         16:"sixteen", 17:"seventeen", 18:"eighteen",19:"nineteen"}
         
tens =  {20:"twenty", 30:"thirty", 40:"fourty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eight", 90:"ninety"}

hundred = { 100:"one hundred", 200:"two hundred"}

def number_to_words(userInput):

    if len(digit) <= 2 and int(digit) in units.keys():
         name = units[int(digit)]
    
    elif len(digit) == 2:
        name = tens[int(digit[0]+'0')]+"-"+units[int(digit[-1])]
        
    elif len(digit) == 3:
        
        name = units[int(digit[0])]+ " hundred and "+tens[int(digit[1]+"0")]+"-"+units[int(digit[-1])]
    print(name)

number_to_words(digit)
