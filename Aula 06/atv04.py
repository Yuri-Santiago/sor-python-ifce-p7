"""
4. Procure no texto apontado no link todas as ocorrências números percentuais.
https://www.uol/economia/especiais/energia-solar-e-eolica-.htm#de-vento-em-popa
"""

import re
link = """
Energia que vem do céu 
Produção de energia a partir do sol e dos ventos avança no Brasil. Como isso afeta a economia e o
que esperar?

De vento em popa 
Tem sido uma daquelas histórias "apesar da crise" que vira e mexe dão as caras no noticiário. Nos últimos anos, 
as fontes de energia solar fotovoltaica (produzida a partir do sol) e eólica (a partir do vento) nadaram contra a
correnteza e registraram avanços de encher os olhos. 
Apenas em 2017, a capacidade instalada em energia eólica cresceu 28,1%, atingindo a marca de 12,8 gigawatts (GW) 
distribuídos entre pouco mais de 500 parques de geração. É o equivalente a 8,1% de toda capacidade do Brasil. 
Os dados são da Empresa de Pesquisa Energética (EPE), órgão do governo responsável por estudos sobre o setor energético.
No caso da energia solar, o salto foi ainda mais impressionante: 4.470% em apenas um ano. No começo de 2017, eram 
somente 21 megawatts, que, na virada do ano, estavam perto do primeiro gigawatt. Esse número, porém, deve ser visto com 
moderação: a energia solar continua na lanterna do sistema nacional de geração, com apenas 0,6% da potência instalada 
no Brasil. 

Dos grandes parques... 
Mais de metade do salto da energia solar veio de apenas dois empreendimentos, inaugurados em setembro: 
- a usina de Nova Olinda (na foto), localizada no município de Ribeira do Piauí (PI); 
- e a usina de Ituverava, que fica em Tabocas do Brejo Velho (BA). 
Juntas, elas têm potência de 546 MW, o suficiente para abastecer quase 570 mil casas. Construídas e operadas pelo grupo
italiano Enel, que investiu US$ 700 milhões nos projetos, são os dois maiores complexos de seu tipo na América do Sul. 

...aos pequenos lares 
Além dos projetos de grande porte, a energia solar também vem se popularizando nas casas, como uma opção para diminuir 
a conta de luz. 
Segundo a Associação Brasileira de Energia Solar Fotovoltaica (Absolar), na virada de 2016, o Brasil contava com 7.000 
unidades instaladas. Um ano mais tarde, eram mais de 16 mil. 
Um dos motivos que ajudou foi a queda no custo dos equipamentos. Segundo o Atlas de Energia Solar, o preço caiu 90% 
(os "módulos" por watt instalado passaram de US$ 3,9 para US$ 0,39). 

Natureza favorece o Brasil 
É até uma vocação natural para o Brasil. Segundo o Atlas do Potencial Eólico Brasileiro de 2001, seria possível 
instalar até 143,5 GW em geradores de energia eólica no país.
Para ter uma ideia do que isso representa, hoje o país é capaz de produzir (incluindo as hidrelétricas) cerca de 150,3 
GW, segundo o Balanço Energético Nacional de 2017. Ou seja: seria possível praticamente dobrar esse número só com vento.

Vento rápido e constante 
Nossos ventos se diferenciam não somente por sua velocidade, mas também por sua regularidade incomum. Ventos constantes 
aumentam o rendimento dos aerogeradores. Essa é uma relação expressa pelo chamado "fator capacidade", que, grosso modo, 
diz o percentual de tempo em que os equipamentos conseguem gerar eletricidade. Enquanto a média mundial é de 25%, no 
Brasil chega a 50%. 
Os ventos brasileiros são os melhores do mundo. Carlo Zorzoli, presidente da filial brasileira da Enel 

Sol a pino 
Em termos de energia solar, o país também não faz feio. 
A edição mais recente do Atlas Brasileiro de Energia Solar informa, por exemplo, que no local menos ensolarado do Brasil
é possível gerar mais eletricidade do que no ponto mais privilegiado da Alemanha --terceiro maior produtor global, atrás
do Japão e da China.  
Essa capacidade varia de uma região para outro do Brasil. O "filé mignon" abrange o interior do Nordeste e o norte de 
Minas Gerais (no mapa, é a região de cor laranja mais intensa). 

Renda e emprego no sertão 
Pequenos agricultores do Nordeste descobriram no vento uma inesperada e bem-vinda fonte de renda complementar 

Israel Joaquim de Carvalho, 34 
Caçula de uma família de três homens, o agricultor recebeu seu pedaço de terra do pai. Há quase cinco anos, tem perto 
de casa duas torres para gerar energia eólica e ganha cerca de R$ 3.500 por mês. Com o dinheiro, diz que espera poder 
ficar mais próximos dos pais, que moram longe e já estão com idade avançada, e dar uma educação melhor para os três 
filhos. "[Primeiro] vai beneficiar quem tem aerogerador, mas, indiretamente, vai beneficiar as outras pessoas também". 
Apesar da renda extra, diz que planeja continuar plantando mandioca. 

Maria Otília de Oliveira, 71 
Agricultora e agente de saúde, ela cuida da casa e toma conta da mãe e de duas sobrinhas. Arrenda terra há quase 5 anos.
Como os equipamentos precisaram ficar no local onde estava sua casa, recebeu uma indenização e construiu uma casa nova, 
maior e mais confortável. "No começo eu passei muita raiva [por causa da mudança de casa], mas melhorou a morada. Até a 
recepção do celular melhorou [risos]". O aluguel da terra para instalar três turbinas rende R$ 5.000 por mês. Com o 
dinheiro, diz que quer incentivar as sobrinhas nos estudos.

Média de R$ 2.500 por família a cada mês 
Pelas contas da Associação Brasileira de Energia Eólica (ABEEólica), já são mais de 4.000 famílias que arrendam (alugam)
parte de suas terras para a instalação de geradores de energia eólica. 
Em troca, essas famílias ganham uma parte das receitas geradas com a venda da eletricidade. A bolada se aproxima dos 
R$ 10 milhões, o que dá uma média de R$ 2.500 por família a cada mês. 
Como a instalação dos geradores não chega a inviabilizar a produção agropecuária, os produtores rurais podem continuar 
suas atividades normalmente. 

Ir aonde o melhor vento está 
Os arrendamentos não são caridade. Eles fazem sentido econômico. Uma companhia eólica tem que ir, literalmente, onde o 
vento a leva. 
"A gente depende do melhor vento. É isso o que nos dá competitividade", diz Lucas Araripe, diretor de projetos da 
empresa Casa dos Ventos (CDV), uma das principais desenvolvedoras de projetos de geração eólica no mercado. 

As melhores jazidas de vento estão justamente nas regiões mais carentes, onde as terras valem muito pouco. 
Lucas Araripe, diretor de projetos da Casa dos Ventos 

Com projetos instalados em 10 municípios distribuídos entre Bahia, Ceará, Pernambuco, Piauí e Rio Grande do Norte, a 
Casa dos Ventos vem lidando com a realidade dos sertanejos há mais de uma década. 
Segundo Araripe, comprar as terras até seria uma possibilidade, mas nem sempre é uma alternativa prática convencer as 
pessoas que estão instaladas ali há tanto tempo. "Comprar acaba ficando muito complexo, então a gente analisa caso a 
caso e tenta ir na direção do que os proprietários querem fazer."

Renda que movimenta o comércio das cidades 
As hélices que geram energia a partir dos ventos estão transformando a paisagem do semiárido brasileiro e a realidade de
alguns dos rincões mais carentes do país. 
Segundo Lucas Araripe, diretor da empresa Casa dos Ventos, o arrendamento acaba sendo a principal renda para muitas 
famílias. E não afeta só aqueles que arrendam suas terras. 

Essa renda extra dinamiza a economia local. Ela alimenta pequenos negócios como a padaria ou a farmácias local. 
Lucas Araripe, diretor de projetos da Casa dos Ventos 

A energia eólica está trazendo desenvolvimento econômico em regiões do semiárido que tinham pouca oportunidade 
econômica. 
Elbia Gannoum, presidente da ABEEólica 

O dinheiro não é o único benefício. As propriedades precisam estar com a documentação em dia antes de poder fechar os 
contratos de arrendamento. Por isso, é feito todo um trabalho preliminar de regularização. 
Não se pode ignorar também o efeito dos empregos gerados. Na região da Chapada do Araripe, no Piauí, a empresa Casa dos 
Ventos instalou seis complexos eólicos, o que atraiu novos negócios. 
"Na operação temos 20 pessoas, mas também temos fabricantes de peças que se instalaram para fornecer equipamento e 
serviços. Isso movimenta alimentação, hotelaria, aluguel de equipamentos etc.", diz Araripe. 

Tenha sua própria 'usina' 
Mudanças na regulação introduzidas pela Aneel (Agência Nacional de Energia Elétrica) ajudaram a aproximar o consumidor 
das energias renováveis. Por exemplo, há dois anos, foi liberado o "autoconsumo remoto". 

Você gera sua energia num local, injeta no sistema e pode consumir em outro, desde que ambos estejam dentro da área de 
uma mesma distribuidora. 
Rodrigo Sauaia, da Absolar 

Isso libera os projetos solares de uma amarra importante: a limitação de espaço para instalar os painéis. Quem tem uma 
área grande disponível, por exemplo em um sítio, pode investir em um sistema maior e mandar essa energia para abastecer 
sua casa principal ou negócio. 

Condomínio solar 
É possível, por exemplo, fazer parte de "condomínios solares": sistemas de geração compartilhada que atendem vários 
consumidores de uma vez só. 
"[Os clientes] criam uma cooperativa para investir em um sistema de geração onde cada um dos coopecooperados é dono de 
uma ou mais cotas", diz Rodrigo Sauaia. "Em vez de um 'sisteminha' pequeno, tenho a vantagem de uma escala maior, o que 
reduz meu custo de investimento." 
Em dezembro, entrou em operação a primeira fazenda solar. Instalada e operada pela Órigo Energia num terreno de 15 
hectares (cerca de 21 campos de futebol) em João Pinheiro (MG), a nova planta de 5 MW trabalha com um modelo de 
assinaturas que permite aos consumidores "alugarem" partes de uma usina solar. A empresa investiu cerca de R$ 5,5 
milhões para viabilizar o projeto. 
"Para os clientes, a economia [na conta de luz] pode chegar a 10%", diz o CEO da Órigo, Surya Mendonça. O foco da 
empresa são clientescomerciais de pequeno porte, para quem faria pouco sentido investir em energia solar por conta 
própria.  

Fazenda solar pronta em três meses 
Enquanto usinas de grande porte têm um prazo de desenvolvimento de alguns anos, projetos de menor porte de energia 
distribuída podem ser completados mais rapidamente. "Consigo implantar uma fazenda solar em apenas 3 meses", diz. "Além 
disso ter a geração mais pulverizada é bom para a rede de distribuição." 
Segundo o executivo, a meta da companhia é chegar a 100 fazendas solares nos próximos três anos, somando 500 MW em 
potência instalada e atendendo até 50 mil clientes. 

Alternativa para períodos de seca
A produção de energia a partir dos ventos tem sido uma alternativa à energia produzida a partir da água. Uma boa pedida 
em tempos de seca e com os reservatórios das hidrelétricas em níveis alarmantes.  
No Nordeste, que concentra cerca de dois terços da potência eólica instalada no país, não é raro que a energia dos 
ventos atenda a maior parte do consumo. O recorde foi registrado em 14 de setembro, quando 64% da energia consumida 
pelos nordestinos veio dos ventos. 
Nacionalmente, o número é bem menor. Segundo os dados mais recentes da Câmara de Comercialização de Energia Elétrica 
(CCEE), de agosto a outubro as usinas eólicas atenderam acima de 10% do mercado. Com exceção das hidrelétricas e das 
térmicas a gás ?cuja soma representa cerca de 70,5% da oferta?, essa foi a única outra fonte com dois dígitos de 
participação ao longo desse período, um feito. 

A [energia] eólica está salvando o Brasil de um racionamento. 
Élbia Gannoum, presidente executiva da Associação Brasileira de Energia Eólica 

Venta mais quando chove menos 
Há uma relação de sinergia entre as fontes hídricas e eólicas. O período mais seco é precisamente o que tem melhores 
ventos. "A eólica gera mais no período de seca, que é quando tem o maior risco de abastecimento na matriz elétrica 
brasileira [dominada por hidrelétricas]", diz Lucas Araripe, da Casa dos Ventos (CDV). 
A relação entre a baixa umidade do ar e a qualidade dos ventos também explica porque o Nordeste concentra a maior parte 
dos projetos na área. "Isso é positivo porque a região não tem vocação para a energia hídrica ou a partir de biomassa", 
afirma. 

Anos de investimento 
Esse processo não aconteceu da noite para o dia. Foram anos de investimentos e organização de mercados, um esforço que 
está amadurecendo agora. 
O primeiro megawatt de energia eólica entrou em operação em 1994, mas foi só na última década que as coisas realmente 
engrenaram, com um crescimento acumulado entre 2007 até 2016 beirando os 4.000%. 
"Apesar de todo o apelo socioambiental da energia eólica, o que realmente importa é que ela é financeiramente 
competitiva. Faz todo sentido do mundo investir nela do ponto de vista estritamente econômico", afirma Lucas Araripe, 
da empresa Casa dos Ventos. 
Em leilões de energia feitos pelo governo desde 2009, foram 650 projetos de energia eólica arrematados. O segundo lugar 
coube às termelétricas com 187 contratações. 
Essa é uma história que parece estar se repetindo --com alguns anos de atraso, mas em marcha acelerada-- com a energia 
solar. 
O primeiro leilão que arrematou projetos de energia eólica aconteceu no final de 2009 e as contratações vêm se repetindo
de forma mais ou menos regular desde então. Isso permitiu que a cadeia se estruturasse no país. 
Segundo Élbia Gannoum, presidente executiva da Associação Brasileira de Energia Eólica (ABEEólica), o grosso do parque 
industrial que vem dando suporte à expansão da energia eólica no país se instalou entre os anos de 2013 e 2014. 
"Cerca de 80% dos equipamentos que usamos é nacional. Não ficamos à mercê do câmbio [dólar]." 

Domínio chinês nos painéis solares 
Ao contrário da eólica, no caso da energia solar a cadeia ainda não está tão bem estruturada e enfrenta forte competição
de fornecedores internacionais. Os chineses praticamente dominam o mercado de painéis. 
"A competitividade dos [fabricantes de painéis solares] chineses é praticamente imbatível", diz Carlo Zorzoli, da 
italiana Enel. Mesmo assim, os painéis representam 30% do custo de uma usina solar, o que significa que os outros 70% 
ainda estão em aberto, e o Brasil pode ser competitivo nesses elos. 

Veio para ficar ou é voo de galinha? 
Com tanta coisa favor, chega até a ser difícil ver como as perspectivas possam desandar. Acontece que o risco é bastante
real. 
Até agora, o setor passou ao largo da crise que fez a economia brasileira sangrar em 2015 e 2016. Isso porque a maior 
parte dos projetos mais substanciais são contratados com anos de antecedência. Os projetos que serão entregues este ano 
foram leiloados em 2015. 
Porém, a crise fez cair o consumo de energia, e o governo acabou cancelando os leilões que estavam previstos para 2016. 
A situação só normalizou-se em dezembro, quando houve dois leilões --um com entregas para 2021 e o outro, para 2023-- 
que arremataram 574 MW de energia solar e 1,4 GW de eólica. 
Mesmo um pouco mais aliviado em relação ao futuro, está claro que há um período de vacas magras a caminho. 
O impacto deverá ser mais duramente sentido pelo setor solar, que tem menos gordura para queimar. "Teremos um abismo 
depois de 2019, quando terminam as entregas dos projetos que já estão em desenvolvimento. Deixar a cadeia produtiva 
parada por um ano inteiro teria um impacto muito ruim e pode até inviabilizar investimentos", diz Rodrigo Sauaia, da 
Absolar. 
Para ele, esse tipo de "voo de galinha" pode desestruturar o segmento em seu nascedouro. "Hoje estamos colhendo frutos 
do que semeamos entre 2012 e 2015. Para seguir nesse desenvolvimento, temos que continuar semeando."
"""

padrao = re.compile('[0-9].*%')
porcentagem = re.findall(padrao, link)
print(porcentagem)
