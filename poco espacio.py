#!/usr/bin/python
# -*- coding: utf-8 -*-

#Update 13/07/2016#

#Lair_Nul4
#Directorio default /dev/xvda1
#01 10 * * * ec2-user /directory/p.py
import smtplib
from email.MIMEText import MIMEText
from urllib2 import urlopen
import subprocess
from subprocess import call
import commands
#Configuración#

directorio_para_verificar = "/dev/xvda1"

######Datos de cuenta que enviara el correo electronido
usuario_gmail = "example.alert@gmail.com"
password_gmail = "passworforexample.alert@gmail.com"
correo_receptor = "email.receptor@loquesea.com"

#Fin de Configuración


#Envio de Correo Electronico#
def enviar_mail(emisor, receptor,login,espacio):

	ip = urlopen('http://ip.42.pl/raw').read()
	mensaje = MIMEText("El servidor con ip:"+ip+" se esta quedando sin espacio, solo tiene "+espacio+"% , por favor, hay que agrandarlo")
	mensaje['From']=emisor
	mensaje['To']=receptor
	mensaje['Subject']="¡¡¡Poco Espacio En Servidor!!!"
	 
	# Nos conectamos al servidor SMTP de Gmail
	serverSMTP = smtplib.SMTP('smtp.gmail.com',587)
	serverSMTP.ehlo()
	serverSMTP.starttls()
	serverSMTP.ehlo()
	serverSMTP.login(emisor,login)
	 
	# Enviamos el mensaje
	serverSMTP.sendmail(emisor,receptor,mensaje.as_string())
	 
	# Cerramos la conexion
	serverSMTP.close()
 
#Fin del Envio de Correo Electronico#

#Verificacion de Espacio#
espacio_libre = commands.getoutput('df -H | grep '+directorio_para_verificar+' | expand | tr -s " " | cut -d " " -f5 | cut -d "%" -f1')
if espacio_libre >= 70:

	enviar_mail(usuario_gmail,correo_receptor,password_gmail,espacio_libre)
	print("Hay poco espacio, se envio un correo al administradors")
#Fin del programa#