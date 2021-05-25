"""
1. O echo server é capaz de atender múltiplos clientes? Por que?
Resposta: Não, o Echo Server normalmente só atende um cliente por vez, tendo q finalizar o processo por inteiro para
atender o próximo cliente. Porque sua arquitetura single thread não permite múltiplas requisições.

2. Como seria implementado um echo server Multi-Thread?
Resposta: Nós precisamos, claro, usar Threads no nosso servidor, ela irá viabilizar as nossas aplicações. Deixaremos a
aplicação dentro de uma função e para cada cliente criamos uma thread para lidar com as requisições do cliente.

3. Cite exemplos de aplicações que demandam o uso de threads.
Resposta: Quaisquer aplicações na Internet que usam servidores multi-thread, como o youtube, google, amazon, etc.

4. Criar um echo server Multi-Threaded que realize o cálculo do IMC do usuário
e o cliente equivalente.
Resposta: Scripts criados nesse diretótio.
"""