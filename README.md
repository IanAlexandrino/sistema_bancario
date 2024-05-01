# Sistema Bancário

Projeto proposto como desafio no bootcamp da DIO Python AI Backend Developer. Deve ser emulado um cenário em que houve uma contratação por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem **Python**. Para a primeira versão do sistema devemos implementar apenas 3 operações: **depósito**, **saque** e **extrato**.

![Menu](/imagens/Captura%20de%20tela%202024-05-01%20171730.png)

## Depósito

Deve ser possível depositar valores **positivos** para a conta bancária. A V1 do projeto trabalha apenas com 1 usuário, dessa forma não é preciso identifiar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de **extrato**.

## Saque

O sistema deve permitir realizar **3 saques diários** com **limite máximo de R$ 500,00 por saque**. Caso o usuário não tenha **saldo em conta**, o sistema deve exibir uma mensagem informando que **não será possível sacar o dinheiro por falta de saldo**. Todos os saques devem ser armazenados em uma variável e exibidos na operação de **extrato**.

## Extrato

Essa operação deve listar **todos os depósitos e saques** realizados na conta. No fim da listagem deve ser exibido o **saldo atual** da conta. Se o extrato estiver em **branco**, exibir a mensagem: **Não foram relizadas movimentações**. Os valores devem ser exibidos utilizando o formato **R$ xxx.xx**, exemplo: 1400.45 = R$ 1500.45.