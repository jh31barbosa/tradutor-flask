- Flask Translator

  Este é um projeto simples de um tradutor de texto utilizando Flask e a API de tradução **MyMemory Translated.net**.
  ## Tecnologias Utilizadas
  - **Python 3**
  - **Flask**
  - **HTML/CSS (para a interface web)**
  - **API MyMemory Translated.net**
  ## Como Executar o Projeto
  ### 1. Clonar o Repositório
  ```bash
  git clone https://github.com/seu-usuario/flask-translator.git
  cd flask-translator
  ```
  ### 2. Criar um Ambiente Virtual (opcional, mas recomendado)
  ```bash
  python3 -m venv venv
  source venv/bin/activate  # Linux/Mac
  venv\Scripts\activate  # Windows
  ```
  ### 3. Instalar Dependências
  ```bash
  pip install -r requirements.txt
  ```
  ### 4. Executar a Aplicação
  ```bash
  python app.py
  ```
  A aplicação estará rodando em: [**http://127.0.0.1:5001**](http://127.0.0.1:5001)
  ## Como Usar
  1. Acesse a interface web do tradutor.
  2. Insira o texto que deseja traduzir.
  3. Escolha o idioma de origem e destino.
  4. Clique no botão para traduzir.
  5. O resultado da tradução será exibido na tela.
  ## Estrutura do Projeto
  ```
  flask-translator/
  ├── templates/
  │   ├── index.html  # Interface web
  ├── app.py          # Código principal
  ├── requirements.txt # Dependências do projeto
  └── README.md        # Documentação do projeto
  ```
  - ar autenticação para uso da API.
  ## Licença
  Este projeto está sob a licença MIT. Sinta-se à vontade para contribuir!



