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

            # comments — skip everything after # until end of line
            if ch == '#':
                while self.current_char() is not None and self.current_char() != '\n':
                    self.advance()

            elif ch in ' \t\n':
                self.advance()

            elif ch.isdigit():
                num = ''
                while self.current_char() is not None and self.current_char().isdigit():
                    num += self.current_char()
                    self.advance()
                if self.current_char() == '.':
                    num += '.'
                    self.advance()
                    while self.current_char() is not None and self.current_char().isdigit():
                        num += self.current_char()
                        self.advance()
                    self.tokens.append(('NUMBER', float(num)))
                else:
                    self.tokens.append(('NUMBER', int(num)))

            elif ch == '"':
                self.advance()
                s = ''
                while self.current_char() is not None and self.current_char() != '"':
                    s += self.current_char()
                    self.advance()
                self.advance()
                self.tokens.append(('STRING', s))

            elif ch.isalpha() or ch == '_':
                word = ''
                while self.current_char() is not None and (self.current_char().isalnum() or self.current_char() == '_'):
                    word += self.current_char()
                    self.advance()
                keywords = {
                    'let': 'LET', 'if': 'IF', 'else': 'ELSE',
                    'while': 'WHILE', 'for': 'FOR', 'to': 'TO',
                    'print': 'PRINT', 'fun': 'FUN', 'return': 'RETURN'
                }
                tok_type = keywords.get(word, 'IDENT')
                self.tokens.append((tok_type, word))

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

            elif ch == ',':
                self.tokens.append(('COMMA', ','))
                self.advance()

            else:
                raise SyntaxError(f'Unknown character: {ch!r}')

        return self.tokens