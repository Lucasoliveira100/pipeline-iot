# Roteiro do vídeo pitch (meta: 3 min 30 s – o limite é 4 min)

**[0:00 – 0:25] Abertura**
Olá, eu sou o Lucas dos Santos Oliveira, aluno da UniFECAF. Neste vídeo vou apresentar o projeto
da disciplina Disruptive Architectures: IoT, Big Data e IA. Eu montei um pipeline de dados que
pega leituras de temperatura de sensores IoT, guarda num banco PostgreSQL e mostra tudo num dashboard.

**[0:25 – 1:00] Propósito**
Sensores IoT geram muitos dados o tempo todo, e se esses dados ficam soltos num arquivo CSV
é difícil analisar. A ideia do pipeline é organizar esse caminho: o dado entra, é tratado,
fica armazenado e depois vira gráfico que qualquer pessoa consegue entender.

**[1:00 – 1:50] Tecnologias e construção** (mostrar a pasta do projeto)
Usei o Python com pandas para ler o CSV do Kaggle e tratar os dados: renomeei as colunas para
português, converti a data e removi leituras repetidas. O banco é um PostgreSQL que roda dentro
de um contêiner Docker, então qualquer pessoa sobe o mesmo ambiente com um comando. A conexão é
feita com SQLAlchemy. Depois criei três views SQL: média de temperatura por dispositivo,
leituras por hora e temperatura máxima e mínima por dia.

**[1:50 – 3:00] Demonstração** (mostrar terminal e navegador)
Aqui o Docker rodando (`docker ps`). Rodo o script de carga e ele mostra quantos registros foram
inseridos. Agora abro o dashboard com `streamlit run`. O primeiro gráfico mostra a média de
temperatura, o segundo as leituras por hora do dia, e o terceiro as temperaturas máximas e mínimas
por dia. [comentar 1 ou 2 conclusões reais que aparecerem nos gráficos]

**[3:00 – 3:30] Conclusão**
O projeto mostrou na prática como integrar Python, Docker, banco de dados e visualização.
Em uma situação real, isso poderia ser usado para monitorar ambientes e alertar quando a
temperatura passar de um limite. O código está no meu GitHub, com o README explicando como rodar.
Obrigado!

**Antes de postar:** confira a duração (menos de 4:00), coloque como "Público" ou "Não listado" no YouTube e teste o link em uma aba anônima.
