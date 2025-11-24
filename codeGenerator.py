from lexer import TokenType

class CodeGenerator:
    def __init__(self):
        self.output = []

    def visit(self, node):
        """Padrão Visitor para percorrer a árvore."""
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception(f'Nenhum método visit_{type(node).__name__}')

    def visit_BinOp(self, node):
        # Gera código para o filho da esquerda (empilha primeiro operando)
        self.visit(node.left)
        # Gera código para o filho da direita (empilha segundo operando)
        self.visit(node.right)

        # Gera a instrução da operação
        if node.op.type == TokenType.PLUS:
            self.emit("ADD")
        elif node.op.type == TokenType.MINUS:
            self.emit("SUB")
        elif node.op.type == TokenType.MUL:
            self.emit("MUL")
        elif node.op.type == TokenType.DIV:
            self.emit("DIV")

    def visit_Num(self, node):
        self.emit(f"PUSH {node.value}")

    def emit(self, code):
        self.output.append(code)

    def get_code(self):
        return "\n".join(self.output)