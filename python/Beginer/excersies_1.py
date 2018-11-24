""" This Script has some warmup excersises """

def is_off(weekday, vacation):
    """This Function will return True if it is Weekend or Vacation.

    :weekday    : Boolean value, True if it is weekday
    :vacation   : Boolean value, True if it is vacation
    :returns: Boolean : If it is work off

    Expected Results
    ------------------------------------
    | sleep_in(False, False) | True	   
    | sleep_in(True, False)  | False   
    | sleep_in(False, True)  | True	   
    | sleep_in(True, True)   | True    
    ------------------------------------
    """
    if vacation:
        return True
   else:
        return not weekday

    # One line solution
    # return vacation or not weekday
    
def monkey_trouble(a_smile, b_smile):
    """This Function will return True/False based on below condition.
    We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. 
    We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

    :a_smile   : Boolean value, True if Monkey A is smilling.
    :b_smile   : Boolean value, True if Monkey B is smilling.
    :returns: Boolean : If it is work off

    Expected Results
    ----------------------------------------
    | monkey_trouble(True, True)   | True  
    | monkey_trouble(False, False) | True  
    | monkey_trouble(True, False)  | False 
    ----------------------------------------
    """
    return (a_smile == b_smile )

def near_hundred(n):
    """This Function will return True/False based on below condition.
    Given an int n, return True if it is within 10 of 100 or 200

    :n   : int value, any number.
    :returns: Boolean : True if condition is met else False

    Expected Results
    ----------------------------------------
    | near_hundred(205)     | True  
    | near_hundred(95)      | True  
    | near_hundred(195)     | True  
    | near_hundred(115)     | False 
    | near_hundred(185)     | False 
    ----------------------------------------
    """
    return abs(100-n) <= 10 or abs(200-n)<=10
    
def front_back(str):
    """This Function will return True/False based on below condition.
    Given a string, return a new string where the first and last chars have been exchanged.

    :str   : string value.
    :returns: String : return the string based on asked condition.

    Expected Results
    ----------------------------------------
    | front_back('code')      | 'eodc'
    | front_back('a')         | 'a'  
    | front_back('ab')        | 'ba'   
    | front_back('')          | ''                          
    | front_back('Chocolate') | 'ehocolatC'                          
    ----------------------------------------
    """
    if len(str) > 1:
        return str[-1]+str[1:-1]+str[0]
    else:
        return str
    
def string_times(str,n):
    """This Function will return True/False based on below condition.
    Given a string and a non-negative int n, return a larger string that is n copies of the original string.

    :str   : string value.
    :n     : int value, number of times the str to be printed.
    :returns: String : return the string based on asked condition.

    Expected Results
    ----------------------------------------
    | string_times('Hi', 2)     | 'HiHi'
    | string_times('Hi', 3)     | 'HiHiHi'  
    | string_times('Hello', 2)  | 'HelloHello'  
    ----------------------------------------
    """
    return str*n
    
def string_bits(str):
    """This Function will return True/False based on below condition.
    Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

    :str   : string value.
    :returns: String : return the string based on asked condition.

    Expected Results
    ----------------------------------------
    | string_bits('Hello')      | 'Hlo'
    | string_bits('Hi')         | 'H'  
    | string_bits('Heeololeo')  | 'Hello'  
    ----------------------------------------
    """
    a_str = ''
    for i in [ i for i in range(len(str)) if i%2 == 0]:
        a_str += str[i]
    return a_str
    
def string_splosion(str):
    """This Function will return True/False based on below condition.
    Given a non-empty string like "Code" return a string like "CCoCodCode".

    :str   : string value.
    :returns: String : return the string based on asked condition.

    Expected Results
    ----------------------------------------
    | string_splosion('Code')  | 'CCoCodCode'
    | string_splosion('abc')   | 'aababc'  
    | string_splosion('ab')    | 'aab'  
    ----------------------------------------
    """
    new_str =''
    for i in range(len(str)):
        new_str += str[0:i+1]
        
    return new_str
   

# Test the function
is_off(False, False)
monkey_trouble(True, False) 
near_hundred(False, True) 