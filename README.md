# 📇 Agenda de Contatos com Tkinter + SQLite

Aplicação desktop desenvolvida em Python com interface gráfica usando Tkinter e banco de dados SQLite. O projeto permite gerenciar contatos com nome, e-mail e telefone, além de contar com recursos adicionais como exportação/importação de CSV, busca por nome e tema escuro.

---

## ✅ Funcionalidades

- Adicionar, editar e excluir contatos
- Listar todos os contatos em uma tabela
- Busca por nome em tempo real
- Exportar contatos para arquivo CSV
- Importar contatos a partir de arquivo CSV
- Confirmação antes de excluir
- Tema escuro com alternância (claro/escuro)

---

## 🛠 Tecnologias utilizadas

- Python 3
- Tkinter (GUI)
- SQLite (banco de dados)
- CSV (para exportação/importação)

---

## ▶️ Como executar

### 1. Clone o repositório
git clone https://github.com/seu-usuario/agenda-contatos.git
cd agenda-contatos

2. Execute o projeto
python app.py

🧠 Estrutura do projeto
agenda-contatos/
├── app.py          # Interface gráfica e funcionalidades
├── banco.py        # Conexão e comandos SQL
├── contatos.db     # (criado automaticamente)
└── README.md

📷 Funcionalidades em destaque
🔍 Busca por nome com barra de pesquisa
🔄 Botões de exportar e importar contatos em CSV
🔁 Alternância entre tema claro e escuro
✅ Confirmação de exclusão com messagebox.askyesno

📂 Formato CSV suportado
Para importar:
ID,Nome,Email,Telefone
1,Fulano,fulano@email.com,(11) 99999-0000
2,Beltrano,beltrano@email.com,(22) 88888-1111
O campo ID será ignorado na importação.

👨‍💻 Autor
Desenvolvido por Lucas Cordeiro
📧 Contato: lucascordeirooliveira50@gmail.com

