class VirtualMachine:
    def __init__(self):
        self.stack = []

    def execute(self, code):
        """Lê as instruções assembly linha por linha e as executa."""
        instructions = code.strip().split('\n')
        
        print("\n--- Início da Execução na VM ---")
        
        for line in instructions:
            # Divide a instrução em operação e argumento (se houver)
            parts = line.split()
            opcode = parts[0]
            
            # Operação PUSH: coloca valor na pilha
            if opcode == 'PUSH':
                value = int(parts[1])
                self.stack.append(value)
                print(f"EXEC: PUSH {value} \t| Pilha: {self.stack}")

            # Operações Aritméticas: consomem 2 valores e devolvem 1
            elif opcode in ('ADD', 'SUB', 'MUL', 'DIV'):
                # Atenção: Em uma pilha, o primeiro 'pop' é o operando da DIREITA
                right = self.stack.pop()
                left = self.stack.pop()
                
                result = 0
                if opcode == 'ADD':
                    result = left + right
                elif opcode == 'SUB':
                    result = left - right
                elif opcode == 'MUL':
                    result = left * right
                elif opcode == 'DIV':
                    # Divisão inteira para manter consistência com TokenType.INTEGER
                    result = int(left / right) 
                
                self.stack.append(result)
                print(f"EXEC: {opcode} ({left}, {right}) \t| Pilha: {self.stack}")
            
            else:
                raise Exception(f"Instrução desconhecida: {opcode}")

        # O resultado final é o único item restante na pilha
        if not self.stack:
            return None
        return self.stack[0]