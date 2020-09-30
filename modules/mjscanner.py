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
import time, sys, os, subprocess
from netaddr import *
from snmp_cmds import Session, snmpwalk
from pprint import pprint
from datetime import datetime


#Classe self
class Begin:
    def __init__(self, dbug):
        # Variavel para debug
        pass

#herda a classe Begin
class TryIcmp(Begin):
    '''
    recebe        -> rede
    processa      -> pinga    a    rede    toda
    devolve       -> lista    up | lista    down
    '''
    def __init__(self, dbug, net_target):
        #herda o parametro dbug
        #super().__init__(dbug)
        super().__init__(dbug)
        self._net_target = IPNetwork(net_target)
        self.dbug = dbug

    def get_range(self):

        dest = self._net_target
        ic_info = []

        if self.dbug == 1:
            print('[INFO] - Valida se o ip digitado é um /32')

        if dest.prefixlen == 32:
            ic_info.append(dest[0])

        else:
            if self.dbug == 1:
                print('[INFO] - Coleta a lista de todos os ips no range')

            for ip in dest.iter_hosts():
                ic_info.append(ip)

        return ic_info

    def shoot_icmp(self, devices):
        if self.dbug == 1:
            print('[INFO] - Iniciando disparos de icmp (ping) para a lista de devices')




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

    def load_ics(self, devices_filename='devices'):

        if self.dbug == 1:
            print('[INFO] - Carrega o arquivo com os ICs')

        devices = {}
        # Abre o arquivo que contem os equipamentos
        with open(devices_filename) as device_file:
            for device_line in device_file:
                # Cria uma lista com os equips (colocando todos em UP.
                ic_info = list(map(str.upper, device_line.strip().split(',')))

                # Cria um dicionario secundario para cada equipamento no arquivo
                # na linha abaixo, ele joga esta informacao no dicionario criado no comeco da funcao
                ic = {
                    "name": ic_info[0],
                    "ipaddr": ic_info[1],
                    "dev_type": ic_info[2],
                    "username": ic_info[3],
                    "password": ic_info[4],
                    "acc_method": ic_info[5]
                }

                if self.dbug == 1:
                    print('[INFO] - Carregado as informações de um ic da lista')
                elif self.dbug == 2:
                    print('[INFO] - Carregado as informações de um ic da lista')
                    print('[DEBUG] - Informações do IC: \n\t{0} \n\t{1} \n\t{2} \n\t{3} \n\t{4} \n\t{5} \n\t{6}'
                          .format(ic_info[0], ic_info[1], ic_info[2], ic_info[3], ic_info[4], ic_info[5], ic_info[6]))

                devices[ic['ipaddr']] = ic

        # transforma a lista (dict) em json
        jsdevices = json.dumps(devices)

        if self.dbug == 1:
            print('[INFO] - lista de equipamentos em json')
            print(jsdevices)

        return jsdevices

    '''
    recebe 		-> lista de possiveis usuarios e senhas (criptografados)
	processa	-> descriptografa os usuarios e senhas
	devolve		-> uma lista com todos os usuarios e senhas (em dicionário) 
	  ex.: [{user: 'thiago',pass:'123'},{user: 'admin',pass:'123'}]
    '''
    def get_access(self):
        pass

