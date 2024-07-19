import os
import tkinter as tk
from tkinter import filedialog, messagebox

def escolher_diretorio():
    diretorio_pai = filedialog.askdirectory()
    entry_diretorio.delete(0, tk.END)
    entry_diretorio.insert(0, diretorio_pai)

def limpar_nomes():
    entry_nomes.delete("1.0", tk.END)

def criar_pastas():
    diretorio_pai = entry_diretorio.get()
    nomes_pastas = entry_nomes.get("1.0", "end-1c").split('\n')

    if not os.path.exists(diretorio_pai):
        messagebox.showerror("Erro", "O diretório pai não existe.")
        return

    for nome_pasta in nomes_pastas:
        pasta_path = os.path.join(diretorio_pai, nome_pasta)
        
        # Verificar se a pasta já existe antes de tentar criar
        if not os.path.exists(pasta_path):
            try:
                os.makedirs(pasta_path)
            except OSError as e:
                messagebox.showerror("Erro", f"Falha ao criar a pasta {nome_pasta}: {str(e)}")

    messagebox.showinfo("Concluído", "Pastas criadas com sucesso!")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Criador de Pastas")

# Campo para o diretório pai
label_diretorio = tk.Label(root, text="Diretório Pai:")
label_diretorio.pack()
entry_diretorio = tk.Entry(root, width=50)
entry_diretorio.pack()

# Botão para escolher o diretório
btn_escolher_diretorio = tk.Button(root, text="Escolher Diretório", command=escolher_diretorio)
btn_escolher_diretorio.pack()

# Campo para os nomes das pastas
label_nomes = tk.Label(root, text="Nomes das Pastas:")
label_nomes.pack()
entry_nomes = tk.Text(root, height=5, width=50)
entry_nomes.pack()

# Botão para limpar os nomes das pastas
btn_limpar_nomes = tk.Button(root, text="Limpar Nomes", command=limpar_nomes)
btn_limpar_nomes.pack()

# Botão para criar as pastas
btn_criar = tk.Button(root, text="Criar Pastas", command=criar_pastas)
btn_criar.pack()

# Iniciar a interface gráfica
root.mainloop()
