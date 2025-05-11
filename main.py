from parser import parser
from interpreter import execute_program
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            code = f.read()
    else:
        print("Modo interativo (Ctrl+D para sair)")
        code = ""
        try:
            while True:
                line = input("> ")
                code += line + "\n"
        except EOFError:
            pass

    result = parser.parse(code)
    if result is None:
        print("Erro de sintaxe ao interpretar o ficheiro.")
    else:
        execute_program(result)
