# mjmail.py -   Programa para criar template e enviar emails para relatórios
#
#
# -------------------------------------------------------------------------------------
# Este programa e um modulo a ser usado para criacao de templates html, assim como
#  envio de emails para uma lista pre-definida
# -------------------------------------------------------------------------------------
#
# Pre-requisitos (programas):
#       smtplib
#       pprint
#       jinja2
#       json
#
# Pre-requisitos (estrutura)
#       [ -d /srv/jenkins/static/templates ] || mkdir /srv/jenkins/static/templates #cria a pasta caso ela não exista
#
#
# Histórico:
#
#       v1.0 28/07/2020, Thiago Marques
#               - Versão inicial
#

# Libs para tshoot
from pprint import pprint
# Lis para emails
import smtplib, socket
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# libs para o processamento
import sys, os, subprocess
import argparse
import json
# Libs para o template
from jinja2 import Environment, FileSystemLoader


def ej_template(db_devices, pshow, dst_mail, mail_server, devup, devdown):
    # carrega a pasta onde estao os templates em jinja2
    folder_load = FileSystemLoader('../templates')
    env = Environment(loader=folder_load)

    # informa o arquivo do template
    template = env.get_template('report.html')

    with open(db_devices, 'r') as f:
        data = json.load(f)

    # renderiza com o jinja2
    report = template.render(db_devices=data, devup=devup, devdown=devdown)

    report_file = os.getcwd() + "../templates/report.html"

    # ej_send_mail(report_file, dst_mail, mail_server)

    if pshow == 1:
        print(report)

    return report


def ej_send_mail(report_file, dst_mail, mail_server):
    # Rementente e destinatario
    sender = "Jenkins <jenkins@gmail.com.br>"
    rcpt = [dst_mail]

    # Utiliza o MIME Alternative como tipo de conteudo
    msg = MIMEMultipart('alternative')

    subject = str("Jenkins ")
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ", ".join(rcpt)

    # Recebe o arquivo HTML e armazena na variavel
    report_html = MIMEText((open(report_file, "r").read()), 'html')

    # Anexa o html na messagem.
    msg.attach(report_html)

    # Envia menssagem
    server = smtplib.SMTP(mail_server)
    server.sendmail(sender, rcpt, msg.as_string())
    server.quit()

    return report_html


# ==============================================================================
# ---- Inicio do programa
# ==============================================================================
if __name__ == '__main__':

    # limpa a tela (unix)
    os.system('clear')

    # ArgParse
    parser = argparse.ArgumentParser(
        description='Modulo para criar templates html e enviar emails (recebe informações de um dicionario.',
        prog='Jarvis Mail do Sagara',
        epilog='Contato: thiagosagara@gmail.com\n'
    )
    parser.add_argument('-f', '--file', action='store',
                        dest='db_devices', default='devices.json',
                        required=False,
                        help='Digite o nome do arquivo com o json Ex: devices.json')

    parser.add_argument('-e', '--mail', action='store',
                        dest='dst_mail', default=0,
                        required=False,
                        help='Digite o email do destinatario. Ex: thiago.marques@tivit.com')

    parser.add_argument('-d', action='store', type=int,
                        dest='show', default=0,
                        required=False,
                        help='adicione -d 1 para mostrar o html final | adicione -d 2 para mostrar a lista dos ICs que estaram no relatorio')

    parser.add_argument('-s', '--server', action='store',
                        dest='server', default='10.0.10.25',
                        required=False,
                        help='adicione o ip|nome do servidor de email para envio dos relatorios')

    # Instancia das opcoes
    db_devices = parser.parse_args().db_devices
    pshow = parser.parse_args().show
    dst_mail = parser.parse_args().dst_mail
    mail_server = parser.parse_args().server
    devup = "-"
    devdown = "-"

    ej_template(db_devices, pshow, dst_mail, mail_server, devup, devdown)

    if pshow == 2:

        dash = "-" * 60
        print(dash)
        print('{:<15s} {:<20s} {:<20s}'.format('SERVICO', 'SERVIDOR', 'IP'))
        print(dash)

        with open(db_devices, 'r') as f:
            data = json.load(f)

        for ic_key, ic_value in data.items():
            print(
                '{:<15s} {:<20s} {:<20s}'.format(data[ic_key]['service'], data[ic_key]['name'], data[ic_key]['ipaddr']))

    print('\n')
