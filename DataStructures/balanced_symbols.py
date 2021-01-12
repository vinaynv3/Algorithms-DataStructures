"""
Parentheses balanced symbols - A General case 
ex: 1.  [{()}] -> Match
    2.  [(]) -> Dont match
"""
#validates matching parentheses
def match(top,symbol):

    bracket_match_catalog = {'(':1,')':1,'{':2,'}':2,'[':3,']':3}

    if bracket_match_catalog[top] ==  bracket_match_catalog[symbol]:
        return True
    else:
        return False


from stack import Stack

def validate_parentheses(aString):

    s = Stack()
    balanced = False
    index = 0

    while index < len(aString) and not balanced:
    
        symbol = aString[index]

        if symbol in '({[':
            s.add(symbol)

        else:
            top = s[-1]
            if match(top,symbol):
                s.remove()
            else:
                balanced = True
        index +=1

    if s.isEmpty() and not balanced:
        return True

    else:
        return False


if __name__ == "__main__":
    s1 = '{{([][])}()}'
    s2 = '[{()]'
    print(s1,':',validate_parentheses(s1))
    print(s2,':',validate_parentheses(s2))
