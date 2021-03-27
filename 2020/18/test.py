#!/usr/bin/python3

class Stack:
    st = None

    def __init__(self):
        self.st = []

    def peek(self):
        return self.st[-1]

    def pop(self):
        v = self.st.pop()
        return v

    def push(self, v):
        self.st.append(v)

    def empty(self):
        return not len(self.st)

    def __repr__(self):
        return self.st

    def __str__(self):
        return str(self.st)
expr = "( ( 1 + 2 ) * 3 - 4 ) * 5"

tokens = expr.split()

postfix = Stack()
ops = Stack()

def precedence(char):
    return { "(" : 5, "+" : 1, "-": 1, "*" : 3, "/" : 4 }[char]
    
for i, t in enumerate(tokens):
    print("Step {}:".format(i), tokens)
    print("          " + i * "     " + "^")
    if t.isdigit():
        postfix.push(t)
    elif t == "(":
        ops.push(t)
    else:
        if ops.empty():
            ops.push(t)
        else:
            if t == ")":
                o = ops.pop()
                while o != "(":
                    postfix.push(o)
                    o = ops.pop()
            else:
                st_precedence = precedence(ops.peek())
                op_precedence = precedence(t)
                if op_precedence >= st_precedence:
                    ops.push(t)
                else:
                    while st_precedence > op_precedence:
                        postfix.push(ops.pop())
                        if ops.empty():
                            break
                        st_precendence = precedence(ops.peek())
                    ops.push(t)
    print(ops)
    print(postfix)
    print("--")

while not ops.empty():
    postfix.push(ops.pop())
            
            
    
print(" ".join(postfix.st))

