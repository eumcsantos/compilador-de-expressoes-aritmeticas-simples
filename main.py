from lexer import Lexer
from parser import Parser
from codeGenerator import CodeGenerator
from virtualMachine import VirtualMachine

def main():
    # Definição da expressão matemática
    # Teste complexo para provar precedência:
    # (10 + 2) / 4 - 3 
    # Ordem esperada: 
    # 1. (10 + 2) = 12
    # 2. 12 / 4 = 3
    # 3. 3 - 3 = 0
    text = "(10 + 6) / 4 - 3"
    
    print(f"1. ENTRADA: {text}")

    try:
        # FASE 1: Análise Léxica e Sintática (Front-end)
        lexer = Lexer(text)
        parser = Parser(lexer)
        tree = parser.parse()
        print("2. PARSER: Árvore Sintática (AST) construída com sucesso.")

        # FASE 2: Geração de Código (Back-end)
        codegen = CodeGenerator()
        codegen.visit(tree)
        assembly_code = codegen.get_code()
        
        print("\n3. CÓDIGO INTERMEDIÁRIO (ASSEMBLY):")
        print("---------------------------------")
        print(assembly_code)
        print("---------------------------------")

        # FASE 3: Execução (Virtual Machine)
        vm = VirtualMachine()
        result = vm.execute(assembly_code)

        print(f"\n4. RESULTADO FINAL: {result}")
    
    except Exception as e:
        print(f"Erro durante a compilação/execução: {e}")

if __name__ == '__main__':
    main()
