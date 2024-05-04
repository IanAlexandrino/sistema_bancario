# Sistema Bancário **v1.0**

Projeto proposto como desafio no bootcamp da DIO Python AI Backend Developer. Deve ser emulado um cenário em que houve uma contratação por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem **Python**. Para a primeira versão do sistema devemos implementar apenas 3 operações: **depósito**, **saque** e **extrato**.

![Menu](/imagens/Captura%20de%20tela%202024-05-01%20171730.png)

## Depósito

Deve ser possível depositar valores **positivos** para a conta bancária. A V1 do projeto trabalha apenas com 1 usuário, dessa forma não é preciso identifiar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de **extrato**.

## Saque

O sistema deve permitir realizar **3 saques diários** com **limite máximo de R$ 500,00 por saque**. Caso o usuário não tenha **saldo em conta**, o sistema deve exibir uma mensagem informando que **não será possível sacar o dinheiro por falta de saldo**. Todos os saques devem ser armazenados em uma variável e exibidos na operação de **extrato**.

## Extrato

Essa operação deve listar **todos os depósitos e saques** realizados na conta. No fim da listagem deve ser exibido o **saldo atual** da conta. Se o extrato estiver em **branco**, exibir a mensagem: **Não foram relizadas movimentações**. Os valores devem ser exibidos utilizando o formato **R$ xxx.xx**, exemplo: 1400.45 = R$ 1500.45.

# Sistema Bancário **v2.0**

Neste desafio, a ideia é **otimizar** o Sistema Bancário previamente desenvolvido com o uso de **funções** Python. O objetivo é **aprimorar** a estrutura e a eficiência do sistema, implementando as operações de depósito, saque e extrato em **funções** específicas. O código existente terá de ser **refatorado**, dividindo-o em funções reutilizáveis, facilitando a manutenção e o entendimento do sistema como um todo. Além de que 2 novas funções terão de ser adicionadas: **cadastrar usuário(cliente)** e **cadastrar conta bancária**.

![Menu](/imagens/Captura%20de%20tela%202024-05-04%20021938.png)

## Cadastrar Usuário (cliente)

O programa deve armazenar os usuários em uma **lista**, um usuário é composto por: **nome**, **data de nascimento**, **cpf** e **endereço**. O endereço é uma **string** com o formato: **logradouro - bairro - cidade/sigla estado**. Deve ser armazenado somente os **números** do CPF. Não podemos cadastrar 2 usuários com o **mesmo CPF**.

## Cadastrar Conta Corrente

O programa deve armazenar contas em uma **lista**, uma conta é composta por **agência**, **número da conta** e **usuário**. O número da conta é **sequencial, iniciando em 1**. O número da agência é **fixo**: **"0001"**. O usuário pode ter **mais de uma conta**, mas uma conta pertence a somente **um usuário**.