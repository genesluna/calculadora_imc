![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![CESMAC EAD](https://res.cloudinary.com/dxylve8nt/image/upload/v1709508355/cesmac_ead_downloaded_logo_r7qz3z.jpg)

# Calculadora de IMC

Código fonte para explicação de testes unitários para o Projeto Integrador V-A do curso de Análise e Desenvolvimento de Sistemas EAD do CESMAC.

São abordados testes que assegurem que a Calculadora de IMC:

- Deve calcular o IMC corretamente para diferentes valores de peso e altura

- Deve categorizar corretamente o IMC em categorias específicas.

- Deve calcular corretamente o IMC e a categoria do IMC para um conjunto de peso e altura dados.

- Deve lidar adequadamente com a entrada de valores inválidos para peso e altura.

- Deve levantar uma exceção ao lidar com uma altura menor ou igual a zero.

- Deve levantar uma exceção ao lidar com um peso menor ou igual a zero.

## Vídeo com a criação e explicação dos testes

[![Vídeo com a criação e explicação dos testes](https://img.youtube.com/vi/j1jVH6RsAZc/maxresdefault.jpg)](https://www.youtube.com/watch?v=j1jVH6RsAZc)

## Utilizando o código

Para iniciar a criação dos testes, é necessário clonar o projeto do GitHub:

```shell
git clone https://github.com/genesluna/calculadora_imc.git
```

### Se ainda não tem o git instalado, segue vídeo explicando a instalação e configuração:

https://youtu.be/RLx63VZ9wSc?si=2mwPE7lQgqlTD1Jj&t=26

## Rodando o código

```shell
python main.py
```

## Rodando os testes

```shell
python -m unittest tests/test_calculadora_imc.py
```

## Links para os 4 desafios:

O aluno deve escolher um dos códigos abaixo e criar os testes necessários seguindo o que aprendeu na aula.

https://github.com/genesluna/calculadora_simples

https://github.com/genesluna/conversor_de_unidades

https://github.com/genesluna/simulador_caixa_eletronico

https://github.com/genesluna/gerador_de_senhas

