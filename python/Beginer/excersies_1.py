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
    

# Test the function
is_off(False, False)
monkey_trouble(True, False) 
near_hundred(False, True) 