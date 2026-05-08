from nodes import (NumberNode, StringNode, IdentNode, BinOpNode,
                   ConditionNode, LetNode, AssignNode, PrintNode,
                   IfNode, WhileNode)

class Interpreter:
    def __init__(self):
        self.env = {}

    def run(self, statements):
        for stmt in statements:
            self.execute(stmt)

    def execute(self, node):
        if isinstance(node, LetNode):
            if node.name in self.env:
                raise NameError(f'Variable "{node.name}" already declared. Use assignment instead.')
            self.env[node.name] = self.evaluate(node.value)

        elif isinstance(node, AssignNode):
            if node.name not in self.env:
                raise NameError(f'Variable "{node.name}" not declared. Use let first.')
            self.env[node.name] = self.evaluate(node.value)

        elif isinstance(node, PrintNode):
            print(self.evaluate(node.value))

        elif isinstance(node, IfNode):
            if self.evaluate(node.condition):
                for stmt in node.body:
                    self.execute(stmt)

        elif isinstance(node, WhileNode):
            while self.evaluate(node.condition):
                for stmt in node.body:
                    self.execute(stmt)

        else:
            raise RuntimeError(f'Unknown statement node: {type(node)}')

    def evaluate(self, node):
        if isinstance(node, NumberNode):
            return node.value

        elif isinstance(node, StringNode):
            return node.value

        elif isinstance(node, IdentNode):
            if node.name not in self.env:
                raise NameError(f'Variable "{node.name}" is not defined.')
            return self.env[node.name]

        elif isinstance(node, BinOpNode):
            left  = self.evaluate(node.left)
            right = self.evaluate(node.right)
            if node.op == '+': return left + right
            if node.op == '-': return left - right
            if node.op == '*': return left * right
            if node.op == '/':
                if right == 0:
                    raise ZeroDivisionError('Cannot divide by zero.')
                return left / right

        elif isinstance(node, ConditionNode):
            left  = self.evaluate(node.left)
            right = self.evaluate(node.right)
            if node.op == '>':  return left > right
            if node.op == '<':  return left < right
            if node.op == '>=': return left >= right
            if node.op == '<=': return left <= right
            if node.op == '==': return left == right
            if node.op == '!=': return left != right

        else:
            raise RuntimeError(f'Unknown expression node: {type(node)}')