Este programa implementa um sistema de gestão de utilizadores para cálculo do Índice de Massa Corporal (IMC), utilizando um banco de dados SQLite para armazenar informações. Ele permite:

1. **Registrar utilizadores:**
  O programa solicita nome, idade, altura e peso, e armazena esses dados no banco de dados, garantindo que o nome do utilizador seja único.

3. **Calcular o IMC:**
  O IMC é calculado com base na altura e peso, e a categoria (baixo peso, peso normal, sobrepeso, obesidade) é determinada conforme os padrões da OMS.

5. **Pesquisar utilizadores:**
  O usuário pode procurar um utilizador registrado e obter os dados completos, incluindo o IMC e a categoria.

7. **Visualizar todos os utilizadores registrados.**
  A interação é feita via menu no terminal, permitindo inserir, consultar e visualizar dados de utilizadores de forma simples e eficiente. O sistema utiliza o SQLite para persistência dos dados, oferecendo uma solução leve e rápida.
