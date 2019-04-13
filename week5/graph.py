operation = {
"+": lambda a,b : a + b,
"-": lambda a,b : a-b,
"/": lambda a,b : a/b,
"*": lambda a,b : a*b
}

class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def eval(self, data=None):
        if (data is None):
            return self.eval(self)
        if(isinstance(data.data, int) or isinstance(data.data, float)):
            return data.data

        valL = self.eval(data.left)
        valR = self.eval(data.right)
        return data.data(valL,valR)

class tf:
    def add(l,r):
        return Node(operation["+"], l,r)

    def subtract(l,r):
        return Node(operation["-"], l,r)

    def multiply(l,r):
        return Node(operation["*"], l,r)

    def divide(l,r):
        return Node(operation["/"], l,r)

all = Node(operation["+"],
 left=Node(operation["+"],left=Node(operation["*"],left=Node(3),right=Node(1)),right=Node(operation["/"],left=Node(6),right=Node(3))),
 right=Node(operation["+"], left=Node(-3), right=Node(5)))

ten = tf.add(tf.divide(Node(4), Node(2)), tf.multiply(Node(3), Node(4)))

tenal = tf.add(tf.subtract(tf.add(tf.multiply(Node(3), Node(1)), tf.divide(Node(6), Node(3))), Node(3)), Node(5))
print(all.eval())
print(ten.eval())
print(tenal.eval())
"4 / 2 + 3 * 4"
"3 * 1 + 6 / 3 - 3 + 5"
