

 
digit = int(input("Enter a number to convert to words: "))

def number_to_words(problem):

    units = {
        1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eigth", 9:"nine",  10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen",
         18:"eighteen",19:"nineteen",
         20:"twenty", 30:"thirty", 40:"fourty", 50:"fifty", 60:"sixty", 70:"seventy", 
         80:"eigth", 90:"ninety", 100:"one hundred", 200:"two hundred"
            }
    

    for number,words in list(units.items())[1:19]:
        

         if digit == number:
             print(units[number])

         else:
             pass
    for number,words in list(units.items())[20:29]:

        if digit == number:
            #print(units[number])
            print(units[number])

number_to_words(digit)


