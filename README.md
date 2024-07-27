# Flow Manager

Flow Manager é um sistema de gestão de fluxo de atividades que permite a criação, visualização e controle de versões de workflows. O sistema facilita a edição visual dos workflows, a geração de fluxogramas, e o controle de aprovação e versionamento.

## Objetivos

- Criar um gerenciador de fluxo de atividades com condições para execução de acordo com seu tipo.
- Gerar arquivos JSON com a query do fluxo no padrão SQL.
- Visualizar os fluxos de trabalho em diagramas UML usando Mermaid.js.
- Implementar um sistema de versionamento para os workflows.
- Armazenar diffs das versões dos workflows usando MongoDB.
- Gerenciar aprovações de workflows no Django Admin.

## Tecnologias Utilizadas

- **Backend:** Python 3.12, Django 5, Pydantic 2.18
- **Banco de Dados:** PostgreSQL, MongoDB
- **Orquestração e Contêineres:** Docker
- **Visualização de Diagramas:** Mermaid.js

## Instalação

### Pré-requisitos

- Python 3.12+
- Docker e Docker Compose
- MongoDB

### Passos

1. Clone o repositório:

    ```sh
    git clone https://github.com/melqui-sa-menezes/flow-manager.git
    cd flow-manager
    ```

2. Crie e ative um ambiente virtual:

    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

3. Instale as dependências:

    ```sh
    pip install -r requirements.txt
    ```

4. Configure o banco de dados PostgreSQL e MongoDB no arquivo `.env`:

    ```env
    DATABASE_URL=postgres://user:password@localhost:5432/flow_manager
    MONGODB_URI=mongodb://localhost:27017/flow_manager
    ```

5. Execute as migrações do banco de dados:

    ```sh
    python manage.py migrate
    ```

6. Inicie o servidor:

    ```sh
    python manage.py runserver
    ```

7. Acesse o Django Admin no navegador:

    ```sh
    http://localhost:8000/admin/
    ```

## Estrutura do Projeto

- **models.py:** Define os modelos Workflow, Step e Approval.
- **admin.py:** Configurações do Django Admin para criação, edição e visualização de workflows.
- **views.py:** Views personalizadas para renderizar diagramas Mermaid.js.
- **templates/admin_workflow.html:** Template personalizado para exibição de diagramas no Django Admin.

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Faça o push para a branch (`git push origin feature/nova-feature`).
5. Crie um novo Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Se tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato:

- Email: melqui.menezes.dev@gmail.com
- GitHub: [melqui-sa-menezes](https://github.com/seu-usuario](https://github.com/melqui-sa-menezes)

---

**Flow Manager** - Gerencie seus workflows de forma eficiente e visual!
