class Lexer:
    def __init__(self, code):
        self.code = code
        self.pos = 0
        self.tokens = []

    def current_char(self):
        if self.pos < len(self.code):
            return self.code[self.pos]
        return None

    def advance(self):
        self.pos += 1

    def tokenize(self):
        while self.current_char() is not None:
            ch = self.current_char()

            if ch in ' \t\n':
                self.advance()

            elif ch.isdigit():
                num = ''
                while self.current_char() is not None and self.current_char().isdigit():
                    num += self.current_char()
                    self.advance()
                self.tokens.append(('NUMBER', int(num)))

            elif ch == '"':
                self.advance()
                s = ''
                while self.current_char() is not None and self.current_char() != '"':
                    s += self.current_char()
                    self.advance()
                self.advance()
                self.tokens.append(('STRING', s))

            elif ch.isalpha():
                word = ''
                while self.current_char() is not None and self.current_char().isalnum():
                    word += self.current_char()
                    self.advance()
                keywords = ['let', 'if', 'while', 'print']
                if word in keywords:
                    self.tokens.append((word.upper(), word))
                else:
                    self.tokens.append(('IDENT', word))

            elif ch == '=':
                self.advance()
                if self.current_char() == '=':
                    self.advance()
                    self.tokens.append(('EQ', '=='))
                else:
                    self.tokens.append(('ASSIGN', '='))

            elif ch == '!':
                self.advance()
                if self.current_char() == '=':
                    self.advance()
                    self.tokens.append(('NEQ', '!='))

            elif ch == '>':
                self.advance()
                if self.current_char() == '=':
                    self.advance()
                    self.tokens.append(('GTE', '>='))
                else:
                    self.tokens.append(('GT', '>'))

            elif ch == '<':
                self.advance()
                if self.current_char() == '=':
                    self.advance()
                    self.tokens.append(('LTE', '<='))
                else:
                    self.tokens.append(('LT', '<'))

            elif ch == '+':
                self.tokens.append(('PLUS', '+'))
                self.advance()

            elif ch == '-':
                self.tokens.append(('MINUS', '-'))
                self.advance()

            elif ch == '*':
                self.tokens.append(('MULTIPLY', '*'))
                self.advance()

            elif ch == '/':
                self.tokens.append(('DIVIDE', '/'))
                self.advance()

            elif ch == '{':
                self.tokens.append(('LBRACE', '{'))
                self.advance()

            elif ch == '}':
                self.tokens.append(('RBRACE', '}'))
                self.advance()

            elif ch == '(':
                self.tokens.append(('LPAREN', '('))
                self.advance()

            elif ch == ')':
                self.tokens.append(('RPAREN', ')'))
                self.advance()

            else:
                raise SyntaxError(f'Unknown character: {ch!r}')

        return self.tokens