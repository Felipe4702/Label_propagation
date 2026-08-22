# Detecção de Comunidades com Label Propagation

**Aluno:** Cassiuscray Felipe dos Santos - Matrícula: 2024007815
**Aluno:** Bryan Luiz Veloso da Silva - Matrícula: 2024007753

# Instruções para clonar e criar o ambiente:

1- Abra o terminal e rode: git clone https://github.com/Felipe4702/Label_propagation
2- Entre na pasta rodando: cd Label_propagation
3- Crie o ambiente rodando: conda env create -f environment.yml
4- Depois ative o ambiente com: conda activate label_prop
5- Para executar, use: python main.py data/rede1.csv

# Relatório dos testes nos datasets:

1- Na Rede 1, o algoritmo dividiu a rede em 2 comunidades na maioria das vezes, refletindo os dois grupos separados.
<img width="640" height="480" alt="grafo_rede1" src="https://github.com/user-attachments/assets/6c670b34-3b1d-4f0c-b797-fe650d5a9c3f" />

2- Na Rede 2, a rede inteira convergiu para 1 comunidade só, porque a rede é muito densa e a propagação unifica todo mundo.
<img width="640" height="480" alt="grafo_rede2" src="https://github.com/user-attachments/assets/7436db2a-5ee6-42cc-9367-8c75df347ed4" />

3- No Zachary, o algoritmo funcionou perfeitamente e dividiu a rede em 2 ou 3 comunidades, separando as "panelinhas" principais do clube.

<img width="640" height="480" alt="grafo_zachary" src="https://github.com/user-attachments/assets/5a9ff190-f04e-4e03-8584-0c9a79316239" />


# Principais dificuldades na implementação:

A maior barreira foi pensar em como calcular a moda e fazer o desempate aleatório usando o que eu tinha disponível, precisei ir atras de varias funções especificas.
Foi necessário quebrar a cabeça com np.unique e np.where. Além disso para plotar o grafo também foi necessário um esforço a mais para entender como funciona.
