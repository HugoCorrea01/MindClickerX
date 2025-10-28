💀 MINDCLICKERX – RED HACKER EDITION
Autor: Hugo Farranha
Versão: 3.3
-------------------------------------------

MindClickerX é um auto-clicker desktop avançado desenvolvido em Python com visual “Red Hacker”, interface moderna e som de inicialização.
Ideal para portfólio, demonstrações de UI com Tkinter e projetos que combinam automação + design.

-------------------------------------------
⚙️ FUNCIONALIDADES PRINCIPAIS
-------------------------------------------
• Interface Neon Hacker com fundo escuro e animação RGB vermelha.
• Som de inicialização (boot.mp3) no splash de carregamento.
• Modo Turbo: ativa cliques em 0.001 segundos (instantâneo).
• Alternância de botão (F7): esquerdo/direito.
• Threading otimizado (sem travar o teclado).
• Log de eventos em tempo real diretamente na interface.
• Splash Screen com barra de progresso e som sincronizado.
• Ícone customizado (aparece também na barra de tarefas do Windows).
• Hotkeys globais:
   F6 → Ligar / Desligar AutoClicker
   F7 → Alternar botão esquerdo/direito
   ESC → Encerrar com segurança

-------------------------------------------
📁 ESTRUTURA DO PROJETO
-------------------------------------------
MindClickerX/
├── autoclicker.py
├── icon.ico
├── boot.mp3
├── README.txt
├── LICENSE
├── .gitignore
├── requirements.txt
└── dist/  (gerado após build)

-------------------------------------------
🧩 DEPENDÊNCIAS
-------------------------------------------
Crie e ative um ambiente virtual:

python -m venv .venv
.venv\Scripts\activate  (Windows)

Instale as dependências:
pip install -r requirements.txt

Conteúdo do requirements.txt:
pynput
playsound==1.2.2

OBS: tkinter já vem nativo com o Python.

-------------------------------------------
▶️ EXECUTAR EM MODO DESENVOLVIMENTO
-------------------------------------------
python autoclicker.py

-------------------------------------------
📦 GERAR EXECUTÁVEL (WINDOWS)
-------------------------------------------
pyinstaller --onefile --noconsole --add-data "boot.mp3;." --add-data "icon.ico;." --icon=icon.ico autoclicker.py

O executável será gerado em:
dist/MindClickerX.exe

Se o ícone não atualizar:
ie4uinit.exe -ClearIconCache

-------------------------------------------
🚀 PUBLICAR NO GITHUB
-------------------------------------------
1️⃣ Inicialize o repositório:
git init
git add .
git commit -m "Initial commit — MindClickerX Red Hacker Edition"
git branch -M main
git remote add origin https://github.com/hugofarranha/MindClickerX.git
git push -u origin main

2️⃣ Crie uma Release com o executável:
gh release create v3.3 dist/MindClickerX.exe --title "v3.3 Red Hacker Edition" --notes "Adicionado splash, som e polimento visual."

-------------------------------------------
👨‍💻 AUTOR
-------------------------------------------
Hugo Farranha
LinkedIn: https://www.linkedin.com/in/hugofarranha/
GitHub:   https://github.com/HugoCorrea01

-------------------------------------------
🧾 LICENÇA
-------------------------------------------
Este projeto está licenciado sob a MIT License.
Veja o arquivo LICENSE para mais detalhes.
