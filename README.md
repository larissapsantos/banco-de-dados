# Banco-de-dados

A administração de uma cidade criou um programa de educação maker para incentivar professores
a ministrarem aulas de ciências, matemática e computação mais lúdicas nas escolas da rede pública de ensino. Por meio deste programa, as escolas podem receber empréstimos semestrais de
materiais e equipamentos, como kits de robótica, ferramentas, notebooks e outros recursos,
mediante a apresentação dos planos de aula dos professores que os utilizarão em suas aulas.

O programa tem como objetivo registrar e controlar:
- As solicitações semestrais de materiais;
- O estoque disponível;
- As aprovações e devoluções dos materiais;
- A organização do uso do Laboratório Maker Central (LMC).

O programa é mantido pela própria administração. A dinâmica de empréstimo é a seguinte: cada
escola cadastrada no programa possui um ou mais coordenadores escolares, responsáveis por
consolidar os planos de aula elaborados pelos professores e enviar as solicitações semestrais à
administração. Cada plano de aula deve descrever o conteúdo das aulas/atividade, os materiais
necessários, o período de execução, etc. Somente solicitações com planos de aula anexados são
analisadas pela equipe da administração, que avalia a coerência pedagógica, a disponibilidade de materiais e o histórico de devoluções da escola.

Após a aprovação, os materiais são entregues à escola e permanecem sob sua responsabilidade
durante o semestre letivo. Ao término do período, o coordenador registra a devolução, e o servidor
da administração atualiza o status dos itens (disponível, danificado ou extraviado), mantendo o
histórico de movimentações no sistema. O não cumprimento das devoluções pode impedir a escola
de participar de novos ciclos do programa.

Principais entidades:
- Servidor da administração: Analisa e aprova os planos de aula enviados pelas escolas. Autoriza
os empréstimos semestrais;
- Coordenador Escolar: Cadastra os planos de aula dos professores da escola. Consolida os
pedidos de materiais e envia a solicitação semestral para a administração;
- Professor: Elabora e submete planos de aula que utilizam materiais maker;
- Escola: Pode possuir vários professores, mas apenas um coordenador responsável pelo envio
das solicitações.

---

## Como rodar o projeto?
- Instalar o venv com `python -m venv venv`
- Ativar o venv com `source venv/bin/activate`
- Instalar as dependências do projeto com `pip install -r requirements.txt`
- Rodar o projeto com `python src/main.py`

---

## Boas práticas no desenvolvimento
- Ao instalar uma nova lib, rodar: `pip freeze > requirements.txt` para que liste as dependências necessárias para rodar o projeto.
- O projeto segue o ***padrão de arquitetura MVC*** e a seguir tem-se as responsabilidades de cada camada:
    - **Controllers**: camada de controle;
    - **Models**: manipulação dos dados;
    - **Views**: interação do usuário.
