digit = input("Enter a number to convert to words: ")

units = {
        1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eigth", 9:"nine",  10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen",
         18:"eighteen",19:"nineteen"}
         
tens =  {

         20:"twenty", 30:"thirty", 40:"fourty", 50:"fifty", 60:"sixty", 70:"seventy", 
         80:"eigth", 90:"ninety"}
         
hundred = { 100:"one hundred", 200:"two hundred"
            }

def number_to_words(problem):

    if len(digit) <= 2 and int(digit) in units.keys():
        
         print(units[int(digit)])
            
    elif len(digit) == 2:
             

    
   

        split_number = []
        for letters in digit:
            split_number.append(letters)

        if len(split_number) == 2:
            global first_letter
            first_letter = split_number[0] + '0'
            global second_letter
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


#         print(units[words])
#         text1 = output[0]
#         text2 = output[1]
#         print(f"Your number is {text1} and {text2}")
# else:
#     pass


number_to_words(digit)



