# Projeto de Inserção e Consultas em Banco de Dados MySQL
Este projeto realiza a inserção de dados em um banco de dados MySQL, seguido de consultas sobre informações relacionadas a funcionários, departamentos, cargos, projetos e recursos utilizados. As consultas são salvas em arquivos JSON.

# Descrição
Este script Python interage com um banco de dados MySQL para realizar as seguintes operações:

Inserção de dados: Dados sobre cargos, departamentos, funcionários, projetos, recursos e dependentes são inseridos nas tabelas correspondentes. <br>
<br> Consultas: O script executa diversas consultas SQL no banco de dados, tais como: <br>
  - Média salarial dos funcionários responsáveis por projetos concluídos, agrupada por departamento.<br>
  - Os três recursos materiais mais usados nos projetos.<br>
  - Custo total dos projetos por departamento.<br>
  - Detalhes dos projetos em execução. <br>
  - O projeto com o maior número de dependentes envolvidos. <br>
  
<br>Os resultados das consultas são salvos em arquivos JSON para fácil manipulação e análise.

Funcionalidades
- Conexão com o banco de dados MySQL. <br>
- Inserção de dados de exemplo (comentados para evitar duplicação). <br>
- Execução de cinco consultas SQL e exportação dos resultados em arquivos JSON: <br>
    - Média de salários por departamento (para projetos concluídos). <br>
    - Três recursos materiais mais usados.<br>
    - Custo total dos projetos por departamento (para projetos concluídos).<br>
    - Projetos em execução, com detalhes sobre cada um.<br>
    - Projeto com maior número de dependentes.<br>
