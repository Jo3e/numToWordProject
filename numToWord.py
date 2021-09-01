digit = int(input("Enter a number to convert to words: "))

def number_to_words(problem):
    global units
    units = {
        1:"one", 2:"two", 3:"three", 4:"four", 5:"five", 6:"six", 7:"seven", 8:"eight", 9:"nine",  10:"ten", 11:"eleven", 12:"twelve", 13:"thirteen", 14:"fourteen", 15:"fifteen", 16:"sixteen", 17:"seventeen",
         18:"eighteen",19:"nineteen",
         20:"twenty", 30:"thirty", 40:"fourty", 50:"fifty", 60:"sixty", 70:"seventy", 
         80:"eighty", 90:"ninety", 100:"one hundred", 200:"two hundred"
            }
    

    for number,words in list(units.items())[1:20]:
        

         if digit == number:
             print(units[number])

         else:
             pass
    for number,words in list(units.items())[21:29]:

        if digit == number:
            print(units[number])
        else:
            pass

number_to_words(digit)
x = str(digit)
print(x)
output = []
for i in x:
    output.append(i)
print(output)

if len(output) == 2:
    for number, words in units.items():
        output[0] = int()
        if output[0] and output[1] == number:
            print(units[words])
#         print(units[words])
#         text1 = output[0]
#         text2 = output[1]
#         print(f"Your number is {text1} and {text2}")
# else:
#     pass


if len(output) == 3:
    output[0] = list(units.items())[28:29]
    tex1 = output[0]
    output[1] = list(units.items())[21:27]
    tex2 = output[2]
    output[2] = list(units.items())[0:9]
    tex3 = output[2]
    print(f"Your number is {tex1}, {tex2} and {tex3}")

else:
    pass




