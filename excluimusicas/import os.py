import os
from mutagen.mp3 import MP3

# Defina o caminho da pasta corretamente
pasta = "C:\\Users\\cleve\\Music\\musicas transferidas"

# Percorre os arquivos na pasta
for arquivo in os.listdir(pasta):
    caminho_arquivo = os.path.join(pasta, arquivo)
    
    # Verifica se o arquivo é um MP3
    if arquivo.endswith(".mp3"):
        try:
            audio = MP3(caminho_arquivo)
            
            # Exclui se a duração for menor que 60 segundos
            if audio.info.length < 60:
                os.remove(caminho_arquivo)
                print(f"Arquivo excluído: {arquivo}")

        except Exception as e:
            print(f"Erro ao processar {arquivo}: {e}")

print("Processo concluído!")