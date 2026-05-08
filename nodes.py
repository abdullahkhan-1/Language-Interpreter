class NumberNode:
    def __init__(self, value):
        self.value = value

class StringNode:
    def __init__(self, value):
        self.value = value

class IdentNode:
    def __init__(self, name):
        self.name = name

class BinOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class ConditionNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class LetNode:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class AssignNode:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class PrintNode:
    def __init__(self, value):
        self.value = value

class IfNode:
    def __init__(self, condition, body, else_body=None):
        self.condition = condition
        self.body = body
        self.else_body = else_body

class WhileNode:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class ForNode:
    def __init__(self, var, start, end, body):
        self.var = var
        self.start = start
        self.end = end
        self.body = body

class FuncDefNode:
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

class FuncCallNode:
    def __init__(self, name, args):
        self.name = name
        self.args = args

class ReturnNode:
    def __init__(self, value):
        self.value = value