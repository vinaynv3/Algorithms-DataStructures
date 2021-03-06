"""
Infix to Postfix =>Algorithm

The following algorithm implements expression conversion from infix to postfix.
Infix expression is where an operator in between two operands Ex: A+B*C, once the expression is
converted to postfix, the notion looks as ABC*+. The conversion process follows operator 
precendence rules and when operators are equal in a given expression, the operations
associate from left to right

"""
from stack import Stack

def convertor(expression):

    expression = list(expression)
    postfix_exp = ''

    operator_precedence = {'-':1,'+':2,'*':3,'/':4}

    container = Stack()

    for symbol in expression:

        if symbol in operator_precedence:

            if not container.isEmpty() and container[-1] != '(' :
                
                if operator_precedence[container[-1]] >= operator_precedence[symbol]:
                    postfix_exp += container[-1]
                    container.remove()
                    container.add(symbol)
                else:
                    container.add(symbol)
            else: 
                container.add(symbol)

        elif symbol == '(':
            container.add(symbol)

        elif symbol == ')' and not container.isEmpty():
            while container[-1] != '(':
                postfix_exp += container[-1]
                container.remove()
            container.remove()

        else:
            postfix_exp += symbol

    while not container.isEmpty():
        postfix_exp += container[-1]
        container.remove()

    return postfix_exp

def evaluator(expression):
    
    exp = expression
    pos = 0

    operators = {"/":1,"*":2,"+":3,"-":4 }

    container = Stack()

    while pos < len(exp):

        if operators.setdefault(exp[pos],0) == 1:
            
            val = int(container[-2]) / int(container[-1])
            container.remove()
            container.remove()
            container.add(val)



        elif operators.setdefault(exp[pos],0) == 2:
            
            val = int(container[-2]) * int(container[-1])
            container.remove()
            container.remove()
            container.add(val)


        elif  operators.setdefault(exp[pos],0) == 3:
            
            val = int(container[-2]) + int(container[-1])
            container.remove()
            container.remove()
            container.add(val)


        elif  operators.setdefault(exp[pos],0) == 4:
            
            val = int(container[-2]) - int(container[-1])
            container.remove()
            container.remove()
            container.add(val)

        else:
            container.add(exp[pos])
        
        pos += 1
    
    return container[-1]

def main():

    expression = convertor(input("INFIX: "))
    print(expression)
    print(evaluator(expression))


if __name__ == "__main__":
    main()
                            
