from BinaryTree import binary_tree
import operator as op


prefix_list = []


def parse_tree(expression):

    expression = list(expression)
    p_tree = binary_tree('')
    stack = []
    stack.append(p_tree)

    current = p_tree

    for exp in expression:

        if exp is '(':
            stack.append(current)
            current.left =  binary_tree("")
            current = current.left
                       

        elif exp in "0123456789":
            current.setRoot(exp)
            current = stack.pop()
    
            
        elif exp in "*-+/":
            current.setRoot(exp)
            current.right = binary_tree('')
            current = current.right
            stack.append(current)

        elif exp is ")":
            current = stack.pop()

        else: 
            return Exception("Invalid input")  

    return current

def traverse(btree):
    

    if btree != None:
        prefix_list.append(btree.root)

        traverse(btree.left)
        traverse(btree.right)
        


def evaluator(prefix_list):

    stack = []

    ops_dict = {"+":op.add,"-":op.sub,"*":op.mul,"/":op.truediv}
    pos = 0


    while pos < len(prefix_list):

        if prefix_list[pos] in "+-*/":

            value = prefix_list[pos]

            b_tree = binary_tree('')
            b_tree.setRoot(value)
            stack.append(b_tree)
            

        elif prefix_list[pos] in "0123456789":
            value = int(prefix_list[pos])

            if stack[-1].left is None:
                stack[-1].left = binary_tree(value)
            else:
                stack[-1].right = binary_tree(value)
             
        else: 
            return Exception("Invalid expression!!")

        pos+=1


    while stack != []:
        sub_tree = stack.pop()
        operator = sub_tree.getRoot()
        operation= ops_dict[operator]

        print(operation, ':',sub_tree.getLeft().getRoot(),sub_tree.getRight().getRoot())

        total = operation(sub_tree.getLeft().getRoot(),sub_tree.getRight().getRoot())
    

        if stack != []:
            position = len(stack)+1

            if position%2 == 1:

                #right
                pos = (len(stack)//2) - 1
                
                if stack[pos].right is None:
                    stack[pos].right = binary_tree(total)
                else:
                    stack[pos].left = binary_tree(total)

            else:

                #left
                pos = (len(stack)//2)
                if stack[pos].left is None:
                    stack[pos].left = binary_tree(total)
                else:
                    stack[pos].right = binary_tree(total)

        else:
            return total


        




def main():
    exp = '((5*2)+1)'
    btree = parse_tree(exp)
    #print(btree)
    traverse(btree)
    print(prefix_list)

    print(evaluator(prefix_list))


if __name__ == "__main__":
    main()











