# @andreyquerino
#
# Todas as imagens da pasta para o formato .webp

from pathlib import Path
from PIL import Image

pastaDasImagens = 'PASTA COM AS IMAGENS' # pasta das images

def converter_para_webp(source):
    destino = source.with_suffix(".webp")
    imagem = Image.open(source)              # Abre a imagem
    imagem.save(destino, format="webp")      # Converte a imagem para webp
    return destino


def main():
    arquivos = Path(pastaDasImagens).glob("**/*") # Todos os arquivos do diretório
    for arquivo in arquivos:
        arquivo_webp = converter_para_webp(arquivo)
        print(arquivo_webp)
    print("\n\n Converção finalizada...\n\n")


main()