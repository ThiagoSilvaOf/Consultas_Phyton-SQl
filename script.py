import mysql.connector
from mysql.connector import Error
import json

def inserir_dados():
  try:
    conn = mysql.connector.connect(
      host="localhost",  
      user="Thiago",       
      password="admin",
      database="dados_empresaDB" 
      )
      
    if conn.is_connected():
      print("Conexão bem-sucedida ao banco de dados!")

      cursor = conn.cursor()

      """
      CODIGO DE INSERÇÃO COMENTADO PARA EVITAR A DUPLICIDADE DOS DADOS, CUJO OS PROPIOS JA FORAM INSERIDOS
      """
      # cursor.execute("INSERT INTO Cargos (nome, salario_base) VALUES (%s, %s)", ('Analista de Sistemas', 4000.00))
      # cursor.execute("INSERT INTO Cargos (nome, salario_base) VALUES (%s, %s)", ('Desenvolvedor', 6000.00))
      # cursor.execute("INSERT INTO Cargos (nome, salario_base) VALUES (%s, %s)", ('Gerente de TI', 12000.00))
      # cursor.execute("INSERT INTO Cargos (nome, salario_base) VALUES (%s, %s)", ('Coordenador de Projetos', 8000.00))
      # cursor.execute("INSERT INTO Cargos (nome, salario_base) VALUES (%s, %s)", ('Analista de Suporte', 3500.00))
      # cursor.execute("INSERT INTO Cargos (nome, salario_base) VALUES (%s, %s)", ('Analista de Banco de Dados', 4500.00))
      # cursor.execute("INSERT INTO Cargos (nome, salario_base) VALUES (%s, %s)", ('Programador Front-end', 5000.00))

      # cursor.execute("INSERT INTO Departamentos (nome, localizacao) VALUES (%s, %s)", ('TI', 'São Paulo'))
      # cursor.execute("INSERT INTO Departamentos (nome, localizacao) VALUES (%s, %s)", ('RH', 'Rio de Janeiro'))
      # cursor.execute("INSERT INTO Departamentos (nome, localizacao) VALUES (%s, %s)", ('Marketing', 'Belo Horizonte'))
      # cursor.execute("INSERT INTO Departamentos (nome, localizacao) VALUES (%s, %s)", ('Financeiro', 'São Paulo'))
      # cursor.execute("INSERT INTO Departamentos (nome, localizacao) VALUES (%s, %s)", ('Vendas', 'Curitiba'))
      # cursor.execute("INSERT INTO Departamentos (nome, localizacao) VALUES (%s, %s)", ('TI', 'Rio de Janeiro'))
      # cursor.execute("INSERT INTO Departamentos (nome, localizacao) VALUES (%s, %s)", ('RH', 'São Paulo'))

      
      # cursor.execute("INSERT INTO Funcionarios (nome, idade, cidade, cargo_id, departamento_id) VALUES (%s, %s, %s, %s, %s)", 
      #                 ('Carlos Silva', 30, 'São Paulo', 1, 1))
      # cursor.execute("INSERT INTO Funcionarios (nome, idade, cidade, cargo_id, departamento_id) VALUES (%s, %s, %s, %s, %s)", 
      #                 ('Fernanda Oliveira', 28, 'Rio de Janeiro', 2, 2))
      # cursor.execute("INSERT INTO Funcionarios (nome, idade, cidade, cargo_id, departamento_id) VALUES (%s, %s, %s, %s, %s)", 
      #                 ('Pedro Santos', 35, 'Belo Horizonte', 3, 3))
      # cursor.execute("INSERT INTO Funcionarios (nome, idade, cidade, cargo_id, departamento_id) VALUES (%s, %s, %s, %s, %s)", 
      #                 ('Mariana Costa', 25, 'Curitiba', 4, 5))
      # cursor.execute("INSERT INTO Funcionarios (nome, idade, cidade, cargo_id, departamento_id) VALUES (%s, %s, %s, %s, %s)", 
      #                 ('Lucas Almeida', 32, 'São Paulo', 5, 4))
      # cursor.execute("INSERT INTO Funcionarios (nome, idade, cidade, cargo_id, departamento_id) VALUES (%s, %s, %s, %s, %s)", 
      #                 ('André Souza', 29, 'São Paulo', 1, 1))
      # cursor.execute("INSERT INTO Funcionarios (nome, idade, cidade, cargo_id, departamento_id) VALUES (%s, %s, %s, %s, %s)", 
      #                 ('Juliana Martins', 34, 'Rio de Janeiro', 2, 2))
      # cursor.execute("INSERT INTO Funcionarios (nome, idade, cidade, cargo_id, departamento_id) VALUES (%s, %s, %s, %s, %s)", 
      #                 ('Gustavo Oliveira', 40, 'Belo Horizonte', 3, 3))
      # cursor.execute("INSERT INTO Funcionarios (nome, idade, cidade, cargo_id, departamento_id) VALUES (%s, %s, %s, %s, %s)", 
      #                 ('Camila Ferreira', 31, 'Curitiba', 4, 5))
      # cursor.execute("INSERT INTO Funcionarios (nome, idade, cidade, cargo_id, departamento_id) VALUES (%s, %s, %s, %s, %s)", 
      #                 ('Ricardo Lima', 27, 'São Paulo', 5, 4))
      # cursor.execute("INSERT INTO Funcionarios (nome, idade, cidade, cargo_id, departamento_id) VALUES (%s, %s, %s, %s, %s)", 
      #           ('Julia Pires', 30, 'São Paulo', 6, 1))
      # cursor.execute("INSERT INTO Funcionarios (nome, idade, cidade, cargo_id, departamento_id) VALUES (%s, %s, %s, %s, %s)", 
      #           ('Fernando Lima', 25, 'Rio de Janeiro', 7, 2))
      # cursor.execute("INSERT INTO Funcionarios (nome, idade, cidade, cargo_id, departamento_id) VALUES (%s, %s, %s, %s, %s)", 
      #           ('Carlos Alberto', 28, 'São Paulo', 6, 1))

      
      # for funcionario_id in range(1, 14):  
      #     for mes in ['Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto']:
      #         salario = 3000.00 + (funcionario_id * 500)  
      #         cursor.execute("INSERT INTO HistoricoSalarios (funcionario_id, mes, ano, salario) VALUES (%s, %s, %s, %s)", 
      #                         (funcionario_id, mes, 2024, salario))


      # for funcionario_id in range(1, 14):  
      #     cursor.execute("INSERT INTO Dependentes (funcionario_id, nome, parentesco, idade) VALUES (%s, %s, %s, %s)", 
      #                     (funcionario_id, f"Dependente {funcionario_id}A", 'Filho', 5))
      #     cursor.execute("INSERT INTO Dependentes (funcionario_id, nome, parentesco, idade) VALUES (%s, %s, %s, %s)", 
      #                     (funcionario_id, f"Dependente {funcionario_id}B", 'Filha', 3))


      # cursor.execute("INSERT INTO Projetos (nome, descricao, data_inicio, data_conclusao, funcionario_responsavel_id, custo, status) VALUES (%s, %s, %s, %s, %s, %s, %s)",
      #                 ('Projeto A', 'Desenvolvimento de sistema para o cliente X', '2024-01-01', '2024-12-31', 1, 50000.00, 'Em Execução'))
      # cursor.execute("INSERT INTO Projetos (nome, descricao, data_inicio, data_conclusao, funcionario_responsavel_id, custo, status) VALUES (%s, %s, %s, %s, %s, %s, %s)",
      #                 ('Projeto B', 'Reestruturação de rede de dados', '2024-02-01', '2024-08-31', 2, 30000.00, 'Concluído'))
      # cursor.execute("INSERT INTO Projetos (nome, descricao, data_inicio, data_conclusao, funcionario_responsavel_id, custo, status) VALUES (%s, %s, %s, %s, %s, %s, %s)",
      #                 ('Projeto C', 'Campanha de marketing digital', '2024-03-01', '2024-07-31', 3, 20000.00, 'Em Planejamento'))
      # cursor.execute("INSERT INTO Projetos (nome, descricao, data_inicio, data_conclusao, funcionario_responsavel_id, custo, status) VALUES (%s, %s, %s, %s, %s, %s, %s)",
      #           ('Projeto D', 'Desenvolvimento de aplicativo mobile', '2024-04-01', '2024-12-31', 6, 25000.00, 'Em Execução'))
      # cursor.execute("INSERT INTO Projetos (nome, descricao, data_inicio, data_conclusao, funcionario_responsavel_id, custo, status) VALUES (%s, %s, %s, %s, %s, %s, %s)",
      #           ('Projeto E', 'Criação de um website institucional', '2024-05-01', '2024-08-31', 7, 18000.00, 'Concluído'))
      # cursor.execute("INSERT INTO Projetos (nome, descricao, data_inicio, data_conclusao, funcionario_responsavel_id, custo, status) VALUES (%s, %s, %s, %s, %s, %s, %s)",
      #           ('Projeto F', 'Implementação de sistema de CRM', '2024-06-01', '2024-11-30', 8, 22000.00, 'Concluído'))


      # cursor.execute("INSERT INTO RecursosProjeto (projeto_id, descricao, tipo_recurso, quantidade, data_utilizacao) VALUES (%s, %s, %s, %s, %s)",
      #                 (1, 'Compra de servidores', 'Material', 10, '2024-02-01'))
      # cursor.execute("INSERT INTO RecursosProjeto (projeto_id, descricao, tipo_recurso, quantidade, data_utilizacao) VALUES (%s, %s, %s, %s, %s)",
      #                 (1, 'Mão de obra especializada', 'Humano', 5, '2024-03-01'))
      # cursor.execute("INSERT INTO RecursosProjeto (projeto_id, descricao, tipo_recurso, quantidade, data_utilizacao) VALUES (%s, %s, %s, %s, %s)",
      #                 (2, 'Compra de equipamentos de rede', 'Material', 3, '2024-02-15'))
      # cursor.execute("INSERT INTO RecursosProjeto (projeto_id, descricao, tipo_recurso, quantidade, data_utilizacao) VALUES (%s, %s, %s, %s, %s)",
      #                 (2, 'Consultoria externa', 'Humano', 2, '2024-04-10'))
      # cursor.execute("INSERT INTO RecursosProjeto (projeto_id, descricao, tipo_recurso, quantidade, data_utilizacao) VALUES (%s, %s, %s, %s, %s)",
      #                 (3, 'Publicidade online', 'Financeiro', 15000.00, '2024-03-20'))
      # Recursos de projetos
      # cursor.execute("INSERT INTO RecursosProjeto (projeto_id, descricao, tipo_recurso, quantidade, data_utilizacao) VALUES (%s, %s, %s, %s, %s)",
      #           (1, 'Compra de notebooks', 'Material', 15, '2024-06-01'))
      # cursor.execute("INSERT INTO RecursosProjeto (projeto_id, descricao, tipo_recurso, quantidade, data_utilizacao) VALUES (%s, %s, %s, %s, %s)",
      #           (2, 'Serviços de hospedagem de site', 'Financeiro', 5000.00, '2024-07-01'))
      # cursor.execute("INSERT INTO RecursosProjeto (projeto_id, descricao, tipo_recurso, quantidade, data_utilizacao) VALUES (%s, %s, %s, %s, %s)",
      #           (3, 'Licenciamento de software CRM', 'Financeiro', 8000.00, '2024-08-01'))


      conn.commit()
      print("Dados inseridos com sucesso!")

      # 1. Trazer a média dos salários (atual) dos funcionários responsáveis por projetos concluídos, agrupados por departamento.
      consulta1 = """
      SELECT d.nome AS Departamento, 
              AVG(h.salario) AS Media_Salario
      FROM HistoricoSalarios h
      JOIN Funcionarios f ON h.funcionario_id = f.id
      JOIN Departamentos d ON f.departamento_id = d.id
      JOIN Projetos p ON p.funcionario_responsavel_id = f.id
      WHERE p.status = 'Concluído'
      GROUP BY d.nome;
      """
      cursor.execute(consulta1)
      resultado1 = cursor.fetchall()
      print("Consulta 1 - Média dos salários por departamento (Projetos Concluídos):")
      for row in resultado1:
          print(row)

      resultado1_json = []
      for row in resultado1:
        resultado1_json.append({
          "Departamento": row[0],
          "Media_Salario":  str(float(row[1]))   
        })

      with open("consulta_media_salarios.json", "w") as f:
        json.dump(resultado1_json, f, indent=4)

      print("\nConsulta 1 - Média dos salários por departamento (Projetos Concluídos) salva em 'consulta_media_salarios.json'.")

      # 2. Identificar os três recursos materiais mais usados nos projetos, listando a descrição do recurso e a quantidade total usada.
      consulta2 = """
      SELECT r.descricao, SUM(r.quantidade) AS Quantidade_Total
      FROM RecursosProjeto r
      WHERE r.tipo_recurso = 'Material'
      GROUP BY r.descricao
      ORDER BY Quantidade_Total DESC
      LIMIT 3;
      """
      cursor.execute(consulta2)
      resultado2 = cursor.fetchall()
      print("\nConsulta 2 - Três recursos materiais mais usados nos projetos:")
      for row in resultado2:
          print(row)

      resultado2_json = []
      for row in resultado2:
        resultado2_json.append({
          "Descricao": row[0],
          "Quantidade_Total":int(row[1])
        })

      with open("consulta_recursos_mais_usados.json", "w") as f:
        json.dump(resultado2_json, f, indent=4)

      print("\nConsulta 2 - Três recursos materiais mais usados nos projetos salva em 'consulta2_recursos_mais_usados.json'.")

      # 3. Calcular o custo total dos projetos por departamento, considerando apenas os projetos 'Concluídos'.
      consulta3 = """
      SELECT d.nome AS Departamento, 
              SUM(p.custo) AS Custo_Total
      FROM Projetos p
      JOIN Funcionarios f ON f.id = p.funcionario_responsavel_id
      JOIN Departamentos d ON f.departamento_id = d.id
      WHERE p.status = 'Concluído'
      GROUP BY d.nome;
      """
      cursor.execute(consulta3)
      resultado3 = cursor.fetchall()
      print("\nConsulta 3 - Custo total dos projetos por departamento (Projetos Concluídos):")
      for row in resultado3:
          print(row)

      resultado3_json = []
      for row in resultado3:
        resultado3_json.append({
          "Departamento": row[0],
          "Custo_Total": float(row[1])   
        })

      with open("consulta3_custo_total_por_departamento.json", "w") as f:
        json.dump(resultado3_json, f, indent=4)

      print("\nConsulta 3 - Custo total dos projetos por departamento (Projetos Concluídos) salva em 'consulta3_custo_total_por_departamento.json'.")

      # 4. Listar todos os projetos com seus respectivos nomes, custo, data de início, data de conclusão e o nome do funcionário responsável, que estejam 'Em Execução'.
      consulta4 = """
      SELECT p.nome AS Nome_Projeto, 
              p.custo, 
              p.data_inicio, 
              p.data_conclusao, 
              f.nome AS Funcionário_Responsável
      FROM Projetos p
      JOIN Funcionarios f ON f.id = p.funcionario_responsavel_id
      WHERE p.status = 'Em Execução';
      """
      cursor.execute(consulta4)
      resultado4 = cursor.fetchall()
      print("\nConsulta 4 - Projetos em Execução:")
      for row in resultado4:
          print(row)

      # 5. Identificar o projeto com o maior número de dependentes envolvidos, considerando que os dependentes são associados aos funcionários que estão gerenciando os projetos.
      consulta5 = """
      SELECT p.nome AS Nome_Projeto, 
              f.nome AS Funcionário_Responsável, 
              COUNT(d.id) AS Numero_Dependentes
      FROM Projetos p
      JOIN Funcionarios f ON f.id = p.funcionario_responsavel_id
      JOIN Dependentes d ON d.funcionario_id = f.id
      GROUP BY p.id
      ORDER BY Numero_Dependentes DESC
      LIMIT 1;
      """
      cursor.execute(consulta5)
      resultado5 = cursor.fetchall()
      print("\nConsulta 5 - Projeto com o maior número de dependentes envolvidos:")
      for row in resultado5:
          print(row)


  except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
  finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Conexão fechada.")

inserir_dados()          

