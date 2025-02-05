# Gerenciador de Contas

Este projeto é um gerenciador de contas desenvolvido com Flask no back-end e uma interface simples utilizando HTML, TailwindCSS e JavaScript no front-end. O objetivo é permitir que os usuários definam um salário, adicionem contas, editem, removam e visualizem um saldo atualizado, além de exportar as contas para um arquivo Excel.

## Funcionalidades

- **Definir Salário**: O usuário pode definir seu salário, que será usado para calcular o saldo disponível.
- **Adicionar Conta**: Permite adicionar uma nova conta com descrição e valor.
- **Editar Conta**: É possível editar a descrição e o valor de uma conta existente.
- **Remover Conta**: Exclui uma conta da lista de despesas.
- **Exibir Saldo**: O saldo disponível é calculado subtraindo o total das contas do salário definido.
- **Exportar Contas para Excel**: O usuário pode exportar a lista de contas para um arquivo Excel.

## Tecnologias Usadas

- **Back-end**: Flask (Python)
- **Front-end**: HTML, TailwindCSS, JavaScript
- **Exportação de Dados**: XLSX.js para gerar arquivos Excel

## Como Executar

### Pré-requisitos

Certifique-se de ter o Python 3.x instalado na sua máquina.

### 1. Instalar as dependências

Clone este repositório para o seu computador e instale as dependências necessárias:

```bash
git clone https://github.com/seu-usuario/gerenciador-contas.git
