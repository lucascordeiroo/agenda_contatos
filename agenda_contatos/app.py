import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import banco
import csv
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askopenfilename
from tkinter import ttk




# Criar banco e tabela
banco.criar_tabela()

# Funções
def carregar_contatos():
    for row in tree.get_children():
        tree.delete(row)
    for contato in banco.listar():
        tree.insert("", "end", values=contato)

def adicionar_contato():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    if nome:
        banco.inserir(nome, email, telefone)
        carregar_contatos()
        limpar_campos()
    else:
        messagebox.showwarning("Aviso", "O campo Nome é obrigatório.")

def excluir_contato():
    item = tree.selection()
    if item:
        contato_id = tree.item(item)["values"][0]
        nome = tree.item(item)["values"][1]
        
        confirmar = messagebox.askyesno("Confirmar Exclusão", f"Tem certeza que deseja excluir o contato:\n{nome}?")
        
        if confirmar:
            banco.deletar(contato_id)
            carregar_contatos()
    else:
        messagebox.showwarning("Aviso", "Selecione um contato para excluir.")


def editar_contato():
    item = tree.selection()
    if item:
        contato_id = tree.item(item)["values"][0]
        nome = entry_nome.get()
        email = entry_email.get()
        telefone = entry_telefone.get()
        banco.atualizar(contato_id, nome, email, telefone)
        carregar_contatos()
        limpar_campos()
    else:
        messagebox.showwarning("Aviso", "Selecione um contato para editar.")

def selecionar_contato(event):
    item = tree.selection()
    if item:
        contato = tree.item(item)["values"]
        entry_nome.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        entry_nome.insert(0, contato[1])
        entry_email.insert(0, contato[2])
        entry_telefone.insert(0, contato[3])

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_telefone.delete(0, tk.END)

def exportar_csv():
    contatos = banco.listar()
    if not contatos:
        messagebox.showinfo("Aviso", "Nenhum contato para exportar.")
        return

    caminho = asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV Files", "*.csv")],
        title="Salvar arquivo como"
    )

    if caminho:
        with open(caminho, mode='w', newline='', encoding='utf-8') as arquivo_csv:
            writer = csv.writer(arquivo_csv)
            writer.writerow(["ID", "Nome", "Email", "Telefone"])
            for contato in contatos:
                writer.writerow(contato)
        messagebox.showinfo("Exportação", f"Contatos exportados com sucesso para:\n{caminho}")

def importar_csv():
    caminho = askopenfilename(
        filetypes=[("CSV Files", "*.csv")],
        title="Selecionar arquivo CSV"
    )

    if not caminho:
        return

    try:
        with open(caminho, newline='', encoding='utf-8') as arquivo_csv:
            reader = csv.reader(arquivo_csv)
            next(reader)  
            for linha in reader:
                if len(linha) >= 4:
                    nome = linha[1]
                    email = linha[2]
                    telefone = linha[3]
                    banco.inserir(nome, email, telefone)
        carregar_contatos()
        messagebox.showinfo("Importação", "Contatos importados com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao importar: {e}")

def aplicar_tema(escuro=True):
    estilo = ttk.Style()
    estilo.theme_use("clam")

    if escuro:
        root.configure(bg="#2c2f33")
        estilo.configure("Treeview",
            background="#23272a",
            foreground="white",
            fieldbackground="#2c2f33"
        )
        estilo.configure("Treeview.Heading",
            background="#2c2f33",
            foreground="#ffffff"
        )
    else:
        root.configure(bg="#f0f0f0")
        estilo.configure("Treeview",
            background="white",
            foreground="black",
            fieldbackground="white"
        )
        estilo.configure("Treeview.Heading",
            background="#e0e0e0",
            foreground="black"
        )

    for widget in root.winfo_children():
        try:
            widget.configure(bg=root["bg"])
        except:
            pass

def alternar_tema():
    global modo_escuro
    modo_escuro = not modo_escuro
    aplicar_tema(escuro=modo_escuro)
    botao_tema.config(text="☀️ Tema Claro" if modo_escuro else "🌙 Tema Escuro")






# Interface
root = tk.Tk()
root.title("📇 Agenda de Contatos")
root.geometry("600x400")

modo_escuro = False  
aplicar_tema(escuro=modo_escuro)



frame_busca = tk.Frame(root)
frame_busca.pack(pady=5)

tk.Label(frame_busca, text="Buscar por nome:").pack(side=tk.LEFT, padx=5)
entry_busca = tk.Entry(frame_busca)
entry_busca.pack(side=tk.LEFT)

def buscar_contatos():
    nome = entry_busca.get()
    contatos = banco.buscar_por_nome(nome)
    tree.delete(*tree.get_children())
    for contato in contatos:
        tree.insert("", "end", values=contato)

tk.Button(frame_busca, text="Buscar", command=buscar_contatos).pack(side=tk.LEFT, padx=5)
tk.Button(frame_busca, text="Limpar", command=carregar_contatos).pack(side=tk.LEFT, padx=5)

# Campos de entrada
frame_form = tk.Frame(root)
frame_form.pack(pady=10)

tk.Label(frame_form, text="Nome:").grid(row=0, column=0, padx=5)
entry_nome = tk.Entry(frame_form, width=30)
entry_nome.grid(row=0, column=1)

tk.Label(frame_form, text="Email:").grid(row=1, column=0, padx=5)
entry_email = tk.Entry(frame_form, width=30)
entry_email.grid(row=1, column=1)

tk.Label(frame_form, text="Telefone:").grid(row=2, column=0, padx=5)
entry_telefone = tk.Entry(frame_form, width=30)
entry_telefone.grid(row=2, column=1)

# Botões
frame_botoes = tk.Frame(root)
frame_botoes.pack(pady=10)

botao_tema = tk.Button(root, text="🌙 Tema Escuro", command=alternar_tema)
botao_tema.pack(pady=5)


tk.Button(frame_botoes, text="Adicionar", command=adicionar_contato, width=12).grid(row=0, column=0, padx=5)
tk.Button(frame_botoes, text="Editar", command=editar_contato, width=12).grid(row=0, column=1, padx=5)
tk.Button(frame_botoes, text="Excluir", command=excluir_contato, width=12).grid(row=0, column=2, padx=5)
tk.Button(frame_botoes, text="Exportar CSV", command=exportar_csv, width=12).grid(row=0, column=3, padx=5)
tk.Button(frame_botoes, text="Importar CSV", command=importar_csv, width=12).grid(row=1, column=0, columnspan=2, pady=5)



# Lista de contatos
tree = ttk.Treeview(root, columns=("ID", "Nome", "Email", "Telefone"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Nome", text="Nome")
tree.heading("Email", text="Email")
tree.heading("Telefone", text="Telefone")
tree.pack(fill=tk.BOTH, expand=True)
tree.bind("<Double-1>", selecionar_contato)

# Carregar dados ao iniciar
carregar_contatos()

root.mainloop()
