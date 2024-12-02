import re

# Lista de palavras reservadas
python_keywords = [
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
    'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
    'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
    'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield'
]

# Definição das categorias
token_list = [
    # Keywords (Palavras reservadas do Python)
    ('KEYWORD', r'\b(' + '|'.join(python_keywords) + r')\b'),  # Todas as palavras reservadas
    # Identifiers
    ('IDENTIFIER', r'[a-zA-Z_]\w*'),  # Identificadores
    # Literals
    ('LITERAL', r'\d+(\.\d*)?|\'[^\']*\'|\"[^\"]*\"'),  # Números, strings com aspas simples ou duplas
    # Delimiters
    ('DELIMITER', r'[;,\(\)\{\}\[\]]'),  # Delimitadores
    # Operators
    ('OPERATOR', r'[+\-*/%=<>!&|~^:]'),  # Operadores
    # Whitespace (ignorar)
    ('WHITESPACE', r'\s+'),  # Espaços em branco
    # Unknown
    ('UNKNOWN', r'.'),  # Qualquer outro caractere
]

# Compilação dos padrões
token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_list)

# Função para tokenizar o código
def tokenize(code):
    tokens = []
    for match in re.finditer(token_regex, code):
        tipo = match.lastgroup
        valor = match.group()
        if tipo == 'WHITESPACE':
            continue  # Ignorar espaços em branco
        elif tipo == 'UNKNOWN':
            raise ValueError(f"Caractere desconhecido: {valor}")
        tokens.append((tipo, valor))
    return tokens

# Interface
def main():
    print("Digite o código Python a ser analisado. Para finalizar, digite 'sair'.\n")
    while True:
        try:
            code = input("Código > ")
            if code.lower() == 'sair':
                print("Encerrando o analisador.")
                break
            tokens = tokenize(code)
            print("\nTokens:")
            for token in tokens:
                print(f"Tipo: {token[0]}, Valor: {token[1]}")
            print(f"\nQuantidade de tokens encontrados: {len(tokens)}\n")
        except ValueError as e:
            print(f"Erro léxico: {e}\n")

if __name__ == '__main__':
    main()
