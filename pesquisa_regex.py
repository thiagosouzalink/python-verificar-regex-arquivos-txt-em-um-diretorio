import re
import os
import sys


def receber_diretorio_atual():
    """Retorna diretório atual """
    return os.getcwd()

def extrair_arquivos_txt_diretorio(diretorio):  
    """
    Extrai arquivos txt de um determinado diretório 
        param
            diretorio: str - String contendo diretório
        return
            arquivos_txt: list - Lista com todos arquivos txt encontrados
    """

    # Recebe conteúdo da pasta atual
    conteudos = os.listdir(diretorio)
    # Extrair os arquivos txt entre o(s) conteúdo(s) encontrado(s) da pasta
    arquivos_txt = []
    for conteudo in conteudos:
        if os.path.isfile(f"{diretorio}\\{conteudo}"):
            if conteudo.split(".")[1] == "txt":
                arquivos_txt.append(conteudo)
    return arquivos_txt


def receber_conteudo_txt(diretorio, arquivos_txt):
    """
    Extrai conteúdo de cada arquivo txt
        param
            diretorio: str - String contendo diretório
            arquivos_txt: lis - Lista contendo arquivos txt
        return
            lista_arquivos_txt: list - Lista com todos os conteúdos de cada arquivo junto com seu nome
    """

    # Extrair conteúdo de cada arquivo txt encontrado
    lista_arquivos_txt = []
    for arquivo_txt in arquivos_txt:
        lista_arquivo_txt = [] # Guardar conteúdo do arquivo txt atual
        nome_arquivo = arquivo_txt
        lista_arquivo_txt.append(nome_arquivo) # Adiciona nome do arquivo na primeira posição
        path_arquivo_txt = f"{diretorio}\\{arquivo_txt}"
        with open(path_arquivo_txt, "r", encoding="UTF-8") as arquivo:
            conteudo_arquivo = arquivo.readlines()
            lista_arquivo_txt += conteudo_arquivo
        lista_arquivos_txt.append(lista_arquivo_txt) # Guarda todos conteúdos
    return lista_arquivos_txt
        

def formatar_expressao_regex(texto):
    """
    Formata texto em uma forma apropriada para compilação Regex
        param
            texto: str - String contendo texto para a expressão
        return
            expresao: str - String com texto em formato apropriado
    """
    # Guarda expressão em formato apropriado antes da compilação no Regex
    caracteres_especiais = "*.^$+?\\"
    expressao = ""
    for caracter in texto.lower():
        if caracter in caracteres_especiais:
            expressao += f"\\{caracter}"
        else:
            expressao += caracter
    return expressao


# Recebe expressão do usuário
texto = input("Digite a expressão de busca: ").strip()
if not texto:
    print("Você digitou uma expressão vazia.")
    sys.exit()

# Recebe texto formatado
expressao = formatar_expressao_regex(texto)

# Compilção Regex
expressao_regex = re.compile(rf"^.*{expressao}.*$")

# Recebe diretório atual
diretorio_atual = receber_diretorio_atual()

# Recebe arquivos txt
arquivos_txt = extrair_arquivos_txt_diretorio(diretorio_atual)
if not arquivos_txt:
    print("Não há arquivos txt no diretório atual.")
    sys.exit()
    
# Recebe conteúdo dos arquivos txt
conteudos_txt = receber_conteudo_txt(diretorio_atual, arquivos_txt)

# Faz a busca em cada conteúdo dos arquivos
for linha in conteudos_txt:
    print(f"\nArquivo atual: {linha[0]}")
    resultado_encontrado = []
    for i in range(1, len(linha)):
        busca = expressao_regex.search(linha[i].lower())
        if busca:
            resultado_encontrado.append(f"Linha {i}: {busca.group()}")

    # Imprime resultado
    if resultado_encontrado:
        for resultado in resultado_encontrado:
            print(resultado)
    else:
        print("Não foi encontrado nenhuma expressão neste arquivo")
            



        