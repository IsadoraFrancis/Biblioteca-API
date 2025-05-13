# 📚 API de Livros com Flask

Uma API RESTful simples construída com [Flask](https://flask.palletsprojects.com/), que permite gerenciar um acervo de livros fictício com operações CRUD (Create, Read, Update, Delete).

Estudo de desenvolvimento de APIs em Python para entender os conceitos básicos de rotas, requisições e manipulação de dados em memória

---

## 🚀 Funcionalidades

- ✅ Listar todos os livros  
- 📖 Obter um livro específico por ID  
- ✍️ Adicionar um novo livro  
- 🛠 Atualizar dados de um livro existente  
- 🗑 Remover um livro do acervo  

---

## 🛠 Tecnologias utilizadas

- [Python 3.x](https://www.python.org/)  
- [Flask](https://flask.palletsprojects.com/) — microframework web  

---

## ▶️ Como rodar o projeto

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/nome-do-repo.git
cd nome-do-repo
```

2. Instale o Flask (caso ainda não tenha):
```bash
pip install flask
```

3. Execute o app:
```bash
python app.py
```

4. Acesse no navegador ou via ferramentas como Postman:
```
http://localhost:5000/livros
```

---

## 📬 Rotas disponíveis

| Método | Rota             | Descrição                     |
|--------|------------------|-------------------------------|
| GET    | /livros          | Retorna todos os livros       |
| GET    | /livros/<id>     | Retorna um livro específico   |
| POST   | /livros          | Adiciona um novo livro        |
| PUT    | /livros/<id>     | Atualiza um livro existente   |
| DELETE | /livros/<id>     | Remove um livro               |

---

## 💡 Exemplo de JSON para POST/PUT

```json
{
  "id": 4,
  "título": "O Vampiro Lestat",
  "autor": "Anne Rice"
}
```
