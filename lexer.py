from enum import Enum, auto

# Definição dos Tipos de Tokens
class TokenType(Enum):
    INTEGER = auto()
    PLUS    = auto()
    MINUS   = auto()
    MUL     = auto()
    DIV     = auto()
    LPAREN  = auto()
    RPAREN  = auto()
    EOF     = auto() # Fim de arquivo

class Token:
    def __init__(self, type, value=None):
        self.type = type
        self.value = value
    
    def __repr__(self):
        return f"Token({self.type.name}, {self.value})"

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos] if self.text else None

    def advance(self):
        """Avança o ponteiro para o próximo caractere no input."""
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        """Lê múltiplos dígitos para formar um número inteiro."""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        """Analisa o caractere atual e retorna o próximo token."""
        while self.current_char is not None:
            
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            
            if self.current_char.isdigit():
                return Token(TokenType.INTEGER, self.integer())
            
            if self.current_char == '+':
                self.advance()
                return Token(TokenType.PLUS, '+')
            
            if self.current_char == '-':
                self.advance()
                return Token(TokenType.MINUS, '-')
            
            if self.current_char == '*':
                self.advance()
                return Token(TokenType.MUL, '*')
            
            if self.current_char == '/':
                self.advance()
                return Token(TokenType.DIV, '/')
            
            if self.current_char == '(':
                self.advance()
                return Token(TokenType.LPAREN, '(')
            
            if self.current_char == ')':
                self.advance()
                return Token(TokenType.RPAREN, ')')
            
            raise Exception(f"Erro Léxico: Caractere inválido '{self.current_char}'")

        return Token(TokenType.EOF)