from nodes import (NumberNode, StringNode, IdentNode, BinOpNode,
                   ConditionNode, LetNode, AssignNode, PrintNode,
                   IfNode, WhileNode, ForNode, FuncDefNode, FuncCallNode, ReturnNode)

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return ('EOF', None)

    def eat(self, expected_type):
        tok = self.current()
        if tok[0] != expected_type:
            raise SyntaxError(f'Expected {expected_type} but got {tok[0]!r}')
        self.pos += 1
        return tok

    def parse(self):
        statements = []
        while self.current()[0] != 'EOF':
            statements.append(self.statement())
        return statements

    def statement(self):
        tok = self.current()

        if tok[0] == 'LET':
            return self.let_statement()
        elif tok[0] == 'PRINT':
            return self.print_statement()
        elif tok[0] == 'IF':
            return self.if_statement()
        elif tok[0] == 'WHILE':
            return self.while_statement()
        elif tok[0] == 'FOR':
            return self.for_statement()
        elif tok[0] == 'FUN':
            return self.func_def()
        elif tok[0] == 'RETURN':
            return self.return_statement()
        elif tok[0] == 'IDENT':
            # could be assignment or function call
            if self.pos + 1 < len(self.tokens) and self.tokens[self.pos + 1][0] == 'ASSIGN':
                return self.assign_statement()
            elif self.pos + 1 < len(self.tokens) and self.tokens[self.pos + 1][0] == 'LPAREN':
                return self.func_call_statement()
        raise SyntaxError(f'Unexpected token: {tok}')

    def let_statement(self):
        self.eat('LET')
        name = self.eat('IDENT')[1]
        self.eat('ASSIGN')
        value = self.expression()
        return LetNode(name, value)

    def assign_statement(self):
        name = self.eat('IDENT')[1]
        self.eat('ASSIGN')
        value = self.expression()
        return AssignNode(name, value)

    def print_statement(self):
        self.eat('PRINT')
        value = self.expression()
        return PrintNode(value)

    def if_statement(self):
        self.eat('IF')
        condition = self.condition()
        self.eat('LBRACE')
        body = []
        while self.current()[0] != 'RBRACE':
            body.append(self.statement())
        self.eat('RBRACE')

        else_body = None
        if self.current()[0] == 'ELSE':
            self.eat('ELSE')
            self.eat('LBRACE')
            else_body = []
            while self.current()[0] != 'RBRACE':
                else_body.append(self.statement())
            self.eat('RBRACE')

        return IfNode(condition, body, else_body)

    def while_statement(self):
        self.eat('WHILE')
        condition = self.condition()
        self.eat('LBRACE')
        body = []
        while self.current()[0] != 'RBRACE':
            body.append(self.statement())
        self.eat('RBRACE')
        return WhileNode(condition, body)

    def for_statement(self):
        self.eat('FOR')
        var = self.eat('IDENT')[1]
        self.eat('ASSIGN')
        start = self.expression()
        self.eat('TO')
        end = self.expression()
        self.eat('LBRACE')
        body = []
        while self.current()[0] != 'RBRACE':
            body.append(self.statement())
        self.eat('RBRACE')
        return ForNode(var, start, end, body)

    def func_def(self):
        self.eat('FUN')
        name = self.eat('IDENT')[1]
        self.eat('LPAREN')
        params = []
        while self.current()[0] != 'RPAREN':
            params.append(self.eat('IDENT')[1])
            if self.current()[0] == 'COMMA':
                self.eat('COMMA')
        self.eat('RPAREN')
        self.eat('LBRACE')
        body = []
        while self.current()[0] != 'RBRACE':
            body.append(self.statement())
        self.eat('RBRACE')
        return FuncDefNode(name, params, body)

    def func_call_statement(self):
        name = self.eat('IDENT')[1]
        self.eat('LPAREN')
        args = []
        while self.current()[0] != 'RPAREN':
            args.append(self.expression())
            if self.current()[0] == 'COMMA':
                self.eat('COMMA')
        self.eat('RPAREN')
        return FuncCallNode(name, args)

    def return_statement(self):
        self.eat('RETURN')
        value = self.expression()
        return ReturnNode(value)

    def condition(self):
        left = self.expression()
        op_tok = self.current()
        if op_tok[0] in ('GT', 'LT', 'GTE', 'LTE', 'EQ', 'NEQ'):
            self.pos += 1
            right = self.expression()
            return ConditionNode(left, op_tok[1], right)
        return left

    def expression(self):
        left = self.term()
        while self.current()[0] in ('PLUS', 'MINUS'):
            op = self.current()[1]
            self.pos += 1
            right = self.term()
            left = BinOpNode(left, op, right)
        return left

    def term(self):
        left = self.factor()
        while self.current()[0] in ('MULTIPLY', 'DIVIDE'):
            op = self.current()[1]
            self.pos += 1
            right = self.factor()
            left = BinOpNode(left, op, right)
        return left

    def factor(self):
        tok = self.current()

        if tok[0] == 'NUMBER':
            self.pos += 1
            return NumberNode(tok[1])

        elif tok[0] == 'STRING':
            self.pos += 1
            return StringNode(tok[1])

        elif tok[0] == 'IDENT':
            if self.pos + 1 < len(self.tokens) and self.tokens[self.pos + 1][0] == 'LPAREN':
                return self.func_call_statement()
            self.pos += 1
            return IdentNode(tok[1])

        elif tok[0] == 'LPAREN':
            self.eat('LPAREN')
            expr = self.expression()
            self.eat('RPAREN')
            return expr

        raise SyntaxError(f'Unexpected token in expression: {tok}')