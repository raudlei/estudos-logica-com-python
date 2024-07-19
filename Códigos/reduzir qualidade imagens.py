from PIL import Image
import os

# Diretório de entrada e saída
input_directory = r'' #insira o diretório de entrada
output_directory = r'' #insira o diretório de saída

# Criar o diretório de saída se não existir
os.makedirs(output_directory, exist_ok=True)

# Resolução desejada
nova_largura = 2304  # Substitua pelo valor desejado
nova_altura = 1734  # Substitua pelo valor desejado

# Percorrer todas as imagens no diretório de entrada
for filename in os.listdir(input_directory):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Caminho completo para a imagem de entrada
        input_path = os.path.join(input_directory, filename)

        # Abrir a imagem
        imagem = Image.open(input_path)

        # Redimensionar a imagem
        nova_imagem = imagem.resize((nova_largura, nova_altura))

        # Caminho completo para a imagem de saída
        output_path = os.path.join(output_directory, filename)

        # Salvar a nova imagem
        nova_imagem.save(output_path)

print("Processo concluído. Imagens redimensionadas e salvas em:", output_directory)
