import sys

def inputNumber(inputMessage, verify = None, verifyFail = None):
    while True:
        answer = input(inputMessage) # input() in python 2 evaluates the input!
        
        if not answer.isnumeric():
            print('Answer must be numeric')
        else:
            if not verify: # if we don't have a verify function
                return answer
                
            if verify(int(answer)): # we have a function
                return answer       # and it passed
            else:                   # else it failed. 
                print(verifyFail or "Invalid number provided")  
                                 # That's called a short circuit; a valid string evaluates to True so the second
                                 # part of the statement is ignored. 
                

if sys.version_info < (3,):
    sys.exit('Python 3 only please')
            
            
# result = inputNumber('Please enter any number: ')
# print('You entered ' + result)

result = inputNumber('Please enter any number less than 100: ', lambda x: x < 100)
print('You entered ' + result)

result = inputNumber('Please enter any number less than 10: ', lambda x: x < 10, 'Number must be less than 10')
print('You entered ' + result)

result = inputNumber('Please enter 42: ', lambda x: x == 42, 'Number must be 42')
print('You entered ' + result)