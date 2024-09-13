# Projeto IoT para Detecção de Enchentes

## Introdução ao Projeto

Este projeto é um sistema integrado de **Internet das Coisas (IoT)** e **Inteligência Artificial (IA)**, desenvolvido para a **detecção precoce de enchentes**. Enchentes são desastres naturais que resultam em grandes perdas de vidas e bens em diversas regiões do mundo. A proposta deste projeto é criar um sistema que monitore em tempo real o nível de água em rios ou reservatórios e faça previsões sobre o risco de enchente, fornecendo alertas antecipados.

O objetivo do sistema é alertar rapidamente as comunidades e autoridades para que possam tomar medidas preventivas, minimizando danos.

## Requisitos Funcionais

**RF1:** O sistema deve medir a velocidade de enchimento do balde com precisão.

**RF2:** O sistema deve enviar alertas para dispositivos conectados (e.g., celular, e-mail) quando o nível da água atingir um valor crítico.

**RF3:** O sistema deve ser capaz de armazenar os dados do nível de água ao longo do tempo para análise e comparação futura.

**RF4:** O sistema deverá ser capaz de identificar casos de aumento do nível da água antes de iniciar o processamento, para evitar custos desnecessários de uso do sistema.

**RF5:** O sistema deverá usar os dados coletados anteriormente para fazer uma análise preditiva de enchente.

**RF6:** O sensor de nível de água deve ter uma precisão adequada e estar devidamente posicionado para detectar pequenas variações no nível da água.

**RF7:** O Arduino deve enviar os dados processados para um servidor ou para um sistema de IA via conexão Wi-Fi.

**RF8:** A IA deve calcular a probabilidade de ocorrência de uma enchente com base nas análises de dados históricos e em tempo real com base na velocidade do nível de água no balde.

**RF9:** O sistema deve ser modular, permitindo adicionar novos sensores ou componentes sem a necessidade de reconfiguração complexa.

**RF10:** O sistema deve suportar a redundância de sensores (utilização de mais de um sensor por ponto de medição) para garantir maior precisão e evitar falhas.

## Requisitos Não Funcionais

**RNF1**: O sistema deve operar com baixo consumo de energia.

**RNF2**: O sistema deve ser resistente à água e outros elementos para garantir sua durabilidade.

**RNF3**: O sistema deve coletar informações do banco de dados da defesa civil a respeito do nível da maré.

**RNF4**: Os sensores deverão estar sempre em funcionamento, mas o processamento será ativado apenas quando os sensores começarem a detectar água (sinalizando um aumento no nível da água).

**RNF5**: O sistema deve ser construído para possibilitar uma manutenção efetiva.

**RNF6**: O sistema deve ser testado e alimentado com dados até atingir uma margem satisfatória de acertos em sua previsão.

**RNF7**: O sistema deve operar de forma contínua e precisa, sem falhas frequentes, especialmente durante eventos críticos.

**RNF8**: O sistema deve processar os dados e fornecer alertas em tempo hábil, sem atrasos significantes.

**RNF9**: O acesso ao sistema e ao banco de dados SQLServer deve ser restrito a usuários autorizados.

**RNF10**: O sistema deve ser facilmente transportável e instalável em diferentes locais sem a necessidade de grandes modificações.

## Funcionamento Geral

O projeto é baseado na integração de dispositivos IoT e algoritmos de IA. Ele utiliza os seguintes componentes:

- **Arduino Uno**: Microcontrolador que processa os dados do sensor de água.
- **Sensor de Água**: Monitora o nível de água em tempo real.
- **Componente de Wi-Fi**: Conecta o Arduino à internet, enviando dados para um servidor ou sistema de IA.
- **Notebook com Software Arduino**: Programado para processar os dados recebidos e rodar os algoritmos de IA.

### Simulação

A simulação ocorre em um ambiente controlado, onde um balde é colocado dentro de uma bacia de água. À medida que a água é adicionada ao balde, o sensor detecta o aumento do nível, e o Arduino transmite esses dados via Wi-Fi para um sistema de IA rodando em um notebook.

A IA analisa a velocidade com que o nível de água sobe e determina se há risco de enchente. Com base nisso, ela alerta o usuário via notificações.

## Fluxo de Informações

1. **Captura de Dados**: O sensor de água monitora continuamente o nível de água e envia as leituras para o Arduino Uno.
2. **Processamento Inicial**: O Arduino realiza pré-processamento básico dos dados, como filtragem de ruídos e calibração.
3. **Transmissão de Dados**: Os dados são enviados via Wi-Fi para um servidor ou sistema de IA.
4. **Análise com IA**: A IA calcula a probabilidade de uma enchente ocorrer e envia os resultados para um banco de dados SQL Server.
5. **Notificação ao Usuário**: Caso o risco de enchente seja detectado, uma notificação é enviada ao usuário (pode ser exibida no notebook ou enviada para um dispositivo móvel).

## Benefícios e Desafios

### Benefícios

- **Aviso Antecipado**: O sistema alerta antes que a enchente ocorra, permitindo a evacuação e medidas preventivas.
- **Automatização e Precisão**: O uso de IoT e IA garante monitoramento contínuo e preciso, sem intervenção humana constante.
- **Escalabilidade**: A tecnologia pode ser aplicada a cenários maiores, como rios grandes ou áreas urbanas.

### Desafios

- **Precisão dos Sensores**: Garantir alta precisão dos sensores, especialmente em condições variáveis.
- **Desempenho da IA**: A IA precisa ser robusta e precisa, o que pode exigir grande volume de dados históricos para treinamento.
- **Conectividade**: O projeto depende de uma conexão Wi-Fi estável, o que pode ser desafiador em áreas remotas.

![Diagrama do Projeto](./images/diagrama.png)

## Contribuidores

- **Eduardo da Maia Haak**
- **Larissa Hoffmann de Souza**
- **Lukas Thiago Rodrigues**
- **Mateus Akira de Oliveira Muranaka**
- **Matheus Gabriel da Silva**
