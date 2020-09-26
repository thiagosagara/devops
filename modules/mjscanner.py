''' Automacao para scan de redes com o objetivo de encontrar o maximo de equipamentos gerenciados possiveis.
      Funcionamento:
        - recebe uma rede, utiliza uma funcao para testar o ICMP em toda a rede, e gera uma lista com os UPs;
        - Com a lista de UP, utiliza outra função para testar o snmp (com base em uma lista de communitys),
            e gera uma base (dict) com as informações coletadas
        - Ainda com a lista de UP, utiliza a função de nmap para procurar os IPs com portas 22 e 23 abertas, e
            gera uma lista com os ICs com as portas abertas;
        - Com a lista dos ICs com as portas abertas, a função de conexão e executada, testando todos os
            acessos possiveis
'''

#imports

import json
import socket
import napalm
import nmap
from snmp_cmds import Session, snmpwalk


#Classe self
class Begin:
    def __init__(self):
        pass

class TryIcmp():
    '''
    recebe        -> rede
    processa      -> pinga    a    rede    toda
    devolve       -> lista    up | lista    down
    '''
    def __init__(self):
        pass



class TrySnmp():
    '''
    depende_de	-> TryIcmp
	recebe		-> lista up (isup) | lista de communities
	processa	-> snmpwalk para a lista de equipamentos, testa todas as comunities da lista, e coleta: hostname, versão, vendor
	devolve		-> DbInfo01 (base de IPs com as informações coletadas)
    '''

    def __init__(self):
        pass


class TryScan():
    '''
    depende_de	-> isup
	recebe		-> lista up (isup)
	processa	-> executa o nmap nas portas 22 e 23 e valida o que esta aberto
	devolve		-> uma lista de dicionários contendo as portas abertas. ex.: [{ip: '10.0.1.1', ports:(22,23)},{ip: '10.1.1.1', ports:{22}]
	Exemplos:
		import nmap
		nm = nmap.PortScanner()
		ic = nm.scan('10.3.1.81','22-23')
		print(ic['scan']['10.3.1.81']['tcp'][22]['product'])
		print(ic['scan']['10.3.1.81']['tcp'][22]['state'])
		--faz um for e coloca um if para pegar apenas os 'open'
    '''

    def __init__(self):
        pass

class TryConnect():
    '''
    depende_de	-> netscan e access
	recebe 		-> lista up (netscan) | credenciais
	processa	-> Tenta conexão nos ICs na porta 22
    '''
    def __init__(self):
        pass

    '''
    recebe 		-> lista de possiveis usuarios e senhas (criptografados)
	processa	-> descriptografa os usuarios e senhas
	devolve		-> uma lista com todos os usuarios e senhas (em dicionário) 
	  ex.: [{user: 'thiago',pass:'123'},{user: 'admin',pass:'123'}]
    '''
    def get_access(self):
        pass

