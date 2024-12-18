# projeto-automaçao-de-analise-de-vendas

### Explicação do Projeto de Automação de Análise e Relatórios

Este projeto foi desenvolvido para automatizar o processo de análise de dados e criação de relatórios em PDF, com envio dos resultados por e-mail. Ele utiliza bibliotecas populares de Python como `pandas`, `fpdf` e `smtplib`, dividindo a funcionalidade em módulos para facilitar a manutenção e reutilização. A seguir, detalhamos cada parte:

---

#### **1. Fluxo Principal (`main`)**
A função principal organiza o fluxo do processo em cinco etapas:
1. **Carregamento dos Dados**: Os dados de vendas são carregados a partir de um arquivo Excel.
2. **Tratamento dos Dados**: Realiza limpeza e preparação dos dados para análise.
3. **Análise Estatística**: Gera métricas como contagem, média e desvio padrão.
4. **Criação do Relatório**: Formata os resultados e cria um PDF contendo as análises.
5. **Envio do Relatório por E-mail**: O relatório gerado é enviado para um destinatário por e-mail.

---

#### **2. Envio de E-mail (`email_sender.py`)**
- Utiliza `smtplib` para enviar e-mails por meio do servidor SMTP do Gmail.
- Adiciona o relatório gerado como anexo.
- Configura uma mensagem com remetente, destinatário, assunto e corpo.
- Envia o e-mail de forma segura utilizando TLS.
- ![auto1](https://github.com/user-attachments/assets/726b521d-57b8-483e-b8ee-4581b2bb73a5)


**Importante:** O uso de senhas no código não é seguro. O ideal seria configurar um sistema de variáveis de ambiente ou utilizar ferramentas como o serviço OAuth2.

---

#### **3. Manipulação de Dados (`dados.py`)**
- **Carregamento**: Lê os dados de um arquivo Excel e os converte em um DataFrame com o auxílio do `pandas`.
- **Tratamento**: Remove valores nulos e ajusta os nomes das colunas, garantindo maior consistência nos dados.
- **Análise**: Calcula métricas estatísticas (contagem, média e desvio padrão) e totais, retornando um resumo e informações complementares.

---

#### **4. Criação do Relatório (`relatorio.py`)**
- Utiliza a biblioteca `fpdf` para criar um relatório PDF elegante.
- Recursos incluídos:
  - **Cabeçalho e Rodapé**: Informações como título e paginação.
  - **Tabelas**: Exibição das métricas calculadas (ex.: `count`, `mean`, `std`).
  - **Listas**: Apresentação dos nomes das colunas.
  - **Totais**: Exibição do total de vendas formatado em milhões.
- Salva o PDF em um diretório especificado.

- ![auto3](https://github.com/user-attachments/assets/1cf7323b-7671-4376-900c-bec34e3636b4)


---

#### **Principais Vantagens**
- **Automação Completa**: Desde o carregamento dos dados até o envio por e-mail.
- **Modularidade**: Código organizado em diferentes arquivos para facilitar ajustes e melhorias.
- **Relatório Profissional**: Geração de um documento PDF legível e estruturado.
- **Escalabilidade**: Pode ser adaptado para diferentes tipos de dados ou análises.

---![auto2](https://github.com/user-attachments/assets/641a8b29-1324-4c0b-ba61-0196d35c4a9b)


#### **Melhorias Futuras**
1. **Segurança**: Substituir a senha de e-mail no código por variáveis de ambiente ou usar autenticação OAuth.
2. **Interface Gráfica**: Desenvolver uma interface para facilitar o uso por não programadores.
3. **Logging**: Adicionar um sistema de registro de logs para monitorar erros e atividades.
4. **Testes Automatizados**: Implementar testes unitários para garantir a robustez do código.

Este projeto demonstra como a automação pode economizar tempo e garantir consistência em tarefas repetitivas relacionadas a análises de dados e relatórios.
