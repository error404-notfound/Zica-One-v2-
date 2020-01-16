# -*- coding: utf-8 -*-

# Librerias y modulos para Satanic Senderus Mailer:
import smtplib # Simple Mail Tranfer Protocol, se usa para enviar los emails.
from email.mime.multipart import MIMEMultipart # Para las cabeceras del envio.
from email.mime.text import MIMEText # Para enviar el mensaje como queramos en texto plano o en html.
from email.mime.base import MIMEBase # Parte 1 para poder enviar archivos adjuntos
from email.encoders import encode_base64 # Parte 2 para poder codificar el archivo adjunto 
from io import open # Modulo para abrir archivos.
import os # modulo para interactuar con el Sistema Operativo.
import getpass # Modulo para ocultar las lecturas por teclado. (Para seguridad)

# Libreria Twilio API:
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Say # Generador xml Voice

# Estilo:
import pyfiglet # Se usa para el banner.
from colorama import init, Fore, Back, Style # Para darle un toque a mi primer script perro.

# Otros:
import platform # Para detectar que puto sistema usas. ;)

# Para descargar archivos. Yo lo use para Remplazus Code, para imagenes.
import urllib.request

# Para manejar el tiempo
import time

# Para mover archivos
import shutil

# Para procesar imagenes
from PIL import Image, ImageDraw, ImageFont

sistema = platform.system()

def clean():
	if sistema == "Windows":
		time.sleep(1)
		os.system("cls")

	elif sistema == "Linux":
		time.sleep(1)
		os.system("clear")
# Clases:
class Satanic_Senderus_Mailer():
	
	def __init__(self, email, password, remitente, destino, asunto, plantilla, ruta_adjunto, cantidad):
		self.email = email
		self.password = password
		self.remitente = remitente
		self.destino = destino
		self.asunto = asunto
		self.plantilla = plantilla
		self.ruta_adjunto = ruta_adjunto
		self.cantidad = cantidad
		

	def cabeceras_parametros(self):
	# Filtro email:
		lista_emails = []
		fichero_emails = open(self.destino,"r")

		for n in range(int(self.cantidad)):
			lista_emails.append(fichero_emails.readline())

		lista = []

		for n in range(len(lista_emails)):
			lista.append(lista_emails[n].rstrip("\n"))

		for n in range(int(self.cantidad)):
		# Estableciendo cabeceras:
			header = MIMEMultipart()
			header["From"] = self.remitente
			header["Cco"] = lista[n]
			header["Subject"] = self.asunto
			plantilla = MIMEText(self.plantilla, "html")
			header.attach(plantilla)

			

			# Configuracion de archivos adjuntos:
			if os.path.isfile(self.ruta_adjunto):
				adjunto = MIMEBase("aplication", "octet-stream") 
				adjunto.set_payload(open(self.ruta_adjunto, "rb").read())
				encode_base64(adjunto)
				adjunto.add_header("Content-Disposition", "attachment; filename='%s'" % os.path.basename(self.ruta_adjunto))
				header.attach(adjunto)

		# Conexion a la cuenta y al servidor
			gmail = smtplib.SMTP("smtp.gmail.com", 587)
			gmail.starttls()
			gmail.login(self.email, self.password)
			# Envio:
			gmail.sendmail(self.remitente, lista[n], header.as_string())
			print(Fore.GREEN+"Enviado correctamente. {}/{}".format(n+1, len(lista)))

class Satanic_Senderus_VoiceCall():
	def __init__(self, sid, token, voz, ruta_numeros, remitente, cantidad, lista = None):
		self.sid = sid
		self.token = token 
		self.voz = voz
		self.ruta_numeros = ruta_numeros
		self.remitente = remitente
		self.cantidad = cantidad
		self.lista = lista

	def filtro(self):
		lista_numeros = []
		fichero_numeros = open(self.ruta_numeros,"r")

		for n in range(int(self.cantidad)):
			lista_numeros.append(fichero_numeros.readline())

		self.lista = []

		for n in range(len(lista_numeros)):
			self.lista.append(lista_numeros[n].rstrip("\n"))
			


	def llamar(self):
		# Login:
		client = Client(self.sid, self.token)

		# Configuracion para llamada:
		llamar = client.calls.create(
			url = self.voz,
			to = self.lista,
			from_ = self.remitente
)
		print(Fore.YELLOW+"""
Si usted y el destinario tiene buena cobertura 
en este momento la llamada debe llegar en 3s aproximadamente
a el numero o lista introducida.""")

class Satanic_Senderus_SMS_Attacker():
	def __init__(self,sid,token, mensaje, remitente, ruta_numeros, cantidad):
		self.sid = sid
		self.token = token 
		self.mensaje = mensaje
		self.remitente = remitente
		self.ruta_numeros = ruta_numeros
		self.cantidad = cantidad
		
		
		
	# Filtro numeros:
	def filtro(self):
		lista_numeros = []
		fichero_numeros = open(self.ruta_numeros,"r")

		for n in range(int(self.cantidad)):
			lista_numeros.append(fichero_numeros.readline())

		self.lista = []

		for n in range(len(lista_numeros)):
			self.lista.append(lista_numeros[n].rstrip("\n"))
			

		# Login:
		client = Client(self.sid, self.token)


		for cantidad in range(len(self.lista)):
			message = client.messages.create(
   	            	body= self.mensaje,
        	        from_= self.remitente,
            	    to= self.lista[cantidad]
)
		print(Fore.GREEN+"Mensajes correctamente enviados. {}/{}".format(len(self.lista), len(self.lista)))



class Satanic_Remplazus_Scamming():

	

	def __init__(self, lista1 = [''], nombre = None, imagenes = None, formato = None, ruta = None, imagenes2 = []):
		self.lista1 = lista1
		self.nombre = nombre
		self.imagenes = imagenes
		self.formato = formato
		self.ruta = ruta
		self.imagenes2 = imagenes2

	def conversion_url(self, lista, formato):

		self.ruta = os.getcwd()
		self.imagenes = []

		error403 = [0]

		if len(self.imagenes) == 0:
				
			for x in range(len(lista)):
				error403[0] = x
				self.imagenes.append(lista[x])
				req = urllib.request.Request(self.imagenes[x], headers={'User-Agent': 'Mozilla/5.0'})
				respuesta = urllib.request.urlopen(req)
				html = respuesta.read()

				with open(r"{}{}.{}".format(self.nombre,x+1,self.formato), "wb") as archivo:
					archivo.write(html)

				shutil.move(r"{}{}.{}".format(self.nombre,x+1,self.formato), self.ruta+"/"+self.nombre)

			self.imagenes2 = []
			for x in range(len(self.imagenes)): 
				self.imagenes2.append("{}\\{}\\{}{}.{}".format(self.ruta,self.nombre,self.nombre,x+1, self.formato))

			print(self.imagenes2)
			time.sleep(9)

		else:
			for x in range(len(lista)-error403):
				self.imagenes.append(lista[error403+x])
				req = urllib.request.Request(self.imagenes[x], headers={'User-Agent': 'Mozilla/5.0'})
				respuesta = urllib.request.urlopen(req)
				html = respuesta.read()


				with open(r"{}{}.{}".format(self.nombre,x+1,self.formato), "wb") as archivo:
					archivo.write(html)

				shutil.move(r"{}{}.{}".format(self.nombre,x+1,self.formato), self.ruta+"/"+self.nombre)

			self.imagenes2 = []
			for x in range(len(self.imagenes)): 
				self.imagenes2.append("{}\\{}\\{}{}.{}".format(self.ruta,self.nombre, self.nombre,x+1, self.formato))

			print(self.imagenes2)


	def limpieza(self, lista):

		clean()
		
		print(Fore.RED+"Fase 1:")
		print(Fore.YELLOW+"""
Estamos limpiando 'MetaData' para su seguridad y
para 'bypass' del filtro de seguridad 'spam', porfavor
espere a que el proceso culmine.

""")

		for x in range(len(lista)):
			os.system("exiftool -all= {}".format(lista[x]))

		print(Fore.GREEN+"\nFinalizado. {}/{}".format(x+1,len(lista)))
		time.sleep(2)

	def inyeccion(self,lista):
		clean()
		print(Fore.RED+"\nFase 2:\n")
		inyeccion_pregunta = str(input(Fore.CYAN+"""
¿Desea inyectar 'MetaData' falsa personalizada? 
(y/n): > """))

		if inyeccion_pregunta == "y":
			i = str(input(Fore.CYAN+"Copyright: > "))
			i2 = str(input(Fore.CYAN+"Comment: > "))
			i3 = str(input(Fore.CYAN+"Artist: > "))

			for x in range(len(lista)):
				os.system("exiftool -copyright={} -comment={} -artist={} {}".format(i, i2, i3, lista[x]))
			print(Fore.GREEN+"\n{}/{} finalizados.".format(x+1,len(lista)))

		else:
			pass



	def hosting(self,lista):
		clean()
		print(Fore.RED+"\nFase 3:\n")
		host = str(input(Fore.CYAN+"Introduce tu url del hosting ngrok: > "))
		puerto = int(input("Introduca el puerto que esta activo en ngrok: > "))

		doc_to_bat = """start cmd.exe\npython -m http.server {}\n""".format(puerto)

		archivo_bat = open("{}\\{}\\autorun.bat".format(self.ruta, self.nombre), "w")
		archivo_bat = archivo_bat.write(str(doc_to_bat)) 

		comodin_shell = r"""
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "{}\\{}\\autorun.bat" & Chr(34), 0
Set WshShell = Nothing""".format(self.ruta, self.nombre)

		comodin = open("comodin_shell.vbs", "w")
		comodin.write(comodin_shell)
		comodin.close()
		print(Fore.YELLOW+"""
NOTA:

Se abrira una nueva ventana, solo cierrela,
esto es a causa de que tenemos que activar el servidor localhost,
de hacerlo en la misma ventana se detiene la ejecucion proxima.""")
		
		time.sleep(8)
		os.system("start comodin_shell.vbs")

		self.lista1 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
		eliminar = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
		
		if len(lista) == 11:
			
			for x in range(len(lista)):
				self.lista1[x] = lista[x].split("\\")
				eliminar[x] = len(self.lista1[x])
				eliminar[x] -= 1

				for y in range(0,eliminar[x]):
					self.lista1[x].pop(0)
			
			for x in range(len(self.lista1)):
				self.lista1[x] = "".join(self.lista1[x])
				self.lista1[x] = host+"/"+self.nombre+"/"+self.lista1[x]

		elif len(lista) == 4:

			for x in range(len(lista)):
				self.lista1[x] = lista[x].split("\\")
				eliminar[x] = len(self.lista1[x])
				eliminar[x] -= 1

				for y in range(0,eliminar[x]):
					self.lista1[x].pop(0)
			
			for x in range(len(self.lista1)):
				self.lista1[x] = "".join(self.lista1[x])
				self.lista1[x] = host+"/"+self.nombre+"/"+self.lista1[x]
			

		elif len(lista) == 9:

			for x in range(len(lista)):
				self.lista1[x] = lista[x].split("\\")
				eliminar[x] = len(self.lista1[x])
				eliminar[x] -= 1

				for y in range(0,eliminar[x]):
					self.lista1[x].pop(0)
			
			for x in range(len(self.lista1)):
				self.lista1[x] = "".join(self.lista1[x])
				self.lista1[x] = host+"/"+self.nombre+"/"+self.lista1[x]

		if len(lista) == 13:
			
			for x in range(len(lista)):
				self.lista1[x] = lista[x].split("\\")
				eliminar[x] = len(self.lista1[x])
				eliminar[x] -= 1

				for y in range(0,eliminar[x]):
					self.lista1[x].pop(0)
			
			for x in range(len(self.lista1)):
				self.lista1[x] = "".join(self.lista1[x])
				self.lista1[x] = host+"/"+self.nombre+"/"+self.lista1[x]

# Lo se... Se podia simplificar esta parte del codigo en 1, pero lo hice asi. 
				
	def formato1(self):
		# remplazus_def() = Falla de desvio critica, estudiar con split().

		self.formato = str(input(Fore.YELLOW+"""
Introduce el formato de las 
imagenes sin '.' (punto): > """))
		imagen_F1 = str(input(Fore.CYAN+r"logoheader: > "))
		imagen2_F1 = str(input(Fore.CYAN+r"banner: > "))
		imagen3_F1 = str(input(Fore.CYAN+r"imgcontexto1: > "))
		imagen4_F1 = str(input(Fore.CYAN+r"imgcontexto2: > "))	
		imagen5_F1 = str(input(Fore.CYAN+r"imgcontexto3: > "))
		imagen6_F1 = str(input(Fore.CYAN+r"imgjuntas1: > "))
		imagen7_F1 = str(input(Fore.CYAN+r"imgjuntas2: > "))
		imagen8_F1 = str(input(Fore.CYAN+r"imgjuntas3: > "))
		imagen9_F1 = str(input(Fore.CYAN+r"imgjuntas4: > "))
		imagen10_F1 = str(input(Fore.CYAN+r"imgjuntas5: > "))
		imagen11_F1 = str(input(Fore.CYAN+r"imgjuntas6: > "))
		

		# Colores:
		texto_F1 = str(input(Fore.CYAN+"Color de fondo (titulo principal): > ")) #bgtituloprincipal
		texto2_F1 = str(input(Fore.CYAN+"Color de texto (titulo principal): > ")) #colortituloprincipal
		texto3_F1 = str(input(Fore.CYAN+"Color del fondo (Boton): > ")) #bgboton
		texto4_F1 = str(input(Fore.CYAN+"Color de texto (Boton): > ")) #colorboton
		texto5_F1 = str(input(Fore.CYAN+"Color de Sub-Titulos: > ")) #colorsubtitulo

		# Textos:
		texto6_F1 = str(input(Fore.CYAN+"Texto del titulo (principal): > ")) #titulodelprimercontenido
		texto7_F1 = str(input(Fore.CYAN+"Titulo de imagen (1): > ")) #tituloimagenx, x = [1,2,3]
		texto8_F1 = str(input(Fore.CYAN+"Titulo de imagen (2): > ")) #tituloimagen2
		texto9_F1 = str(input(Fore.CYAN+"Titulo de imagen (3): > ")) #tituloimagen3
		texto10_F1 = str(input(Fore.CYAN+"""Informacion luego del titulo (texto): > """)) #contenidoprincipal
		texto11_F1 = str(input(Fore.CYAN+"Descripcion del boton (Arriba): > ")) #descripcionantesdeboton

		texto12_F1 = str(input(Fore.CYAN+"Texto (En Boton): > ")) #textodeboton
		texto13_F1 = str(input(Fore.CYAN+r"Enlace (Boton) > ")) #enlaceboton
		texto14_F1 = str(input(Fore.CYAN+"Texto Sub-Titulo 1 (Bajo del boton): > ")) #subtitulodelboton
		texto15_F1 = str(input(Fore.CYAN+"""Descripcion del Sub-Titulo 1: > """)) #descripcionsubtituloboton
		texto16_F1 = str(input(Fore.CYAN+"Encasode: > ")) #encasode
		texto17_F1 = str(input(Fore.CYAN+"Pie de pagina o footer: > ")) #piedepagina
		
		lista_textos1 = [texto_F1, texto2_F1, texto3_F1, texto4_F1,
			texto5_F1, texto6_F1, texto7_F1, texto8_F1, texto9_F1,
			texto10_F1, texto11_F1, texto12_F1, texto13_F1, texto14_F1, texto15_F1, texto16_F1, texto17_F1]

		IDs_F1 = ["bgtituloprincipal", "colortituloprincipal", "bgboton", 
    		"colorboton", "colorsubtitulo", "titulodelprimercontenido", "tituloimagen1",
    		"tituloimagen2", "tituloimagen3", "contenidoprincipal", "descripcionantesdeboton",
    		"textodeboton", "enlaceboton", "subtitulodelboton", "descripcionsubtituloboton",
    		"encasode", "piedepagina"]

		imagenes = [imagen_F1, imagen2_F1, imagen3_F1, imagen4_F1, 
			imagen5_F1,	imagen6_F1, imagen7_F1, imagen8_F1, 
			imagen9_F1, imagen10_F1, imagen11_F1]

		self.nombre = str(input("""
Introduce el nombre para guardar las fotos > """))
		os.system("mkdir {}".format(self.nombre))

		Satanic_Remplazus_Scamming.conversion_url(imagenes, self.formato)
		Satanic_Remplazus_Scamming.limpieza(self.imagenes2)
		Satanic_Remplazus_Scamming.inyeccion(self.imagenes2)
		Satanic_Remplazus_Scamming.hosting(self.imagenes2)

		imagen_F1 = self.lista1[0]
		imagen2_F1 = self.lista1[1]
		imagen3_F1 = self.lista1[2]
		imagen4_F1 = self.lista1[3] 
		imagen5_F1 = self.lista1[4]
		imagen6_F1 = self.lista1[5] 
		imagen7_F1 = self.lista1[6] 
		imagen8_F1 = self.lista1[7] 
		imagen9_F1 = self.lista1[8]
		imagen10_F1 = self.lista1[9] 
		imagen11_F1 = self.lista1[10]


		plantilla_base = open("plantilla.html", "r")
		plantilla_generada = plantilla_base.read()
		plantilla_generada = plantilla_generada.replace("logoheader", imagen_F1)
		plantilla_generada = plantilla_generada.replace("banner", imagen2_F1)
		plantilla_generada = plantilla_generada.replace("imgcontexto1", imagen3_F1)
		plantilla_generada = plantilla_generada.replace("imgcontexto2", imagen4_F1)
		plantilla_generada = plantilla_generada.replace("imgcontexto3", imagen5_F1)
		plantilla_generada = plantilla_generada.replace("imgjuntas1", imagen6_F1)
		plantilla_generada = plantilla_generada.replace("imgjuntas2", imagen7_F1)
		plantilla_generada = plantilla_generada.replace("imgjuntas3", imagen8_F1)
		plantilla_generada = plantilla_generada.replace("imgjuntas4", imagen9_F1)
		plantilla_generada = plantilla_generada.replace("imgjuntas5", imagen10_F1)
		plantilla_generada = plantilla_generada.replace("imgjuntas6", imagen11_F1)

		for x in range(len(lista_textos1)):
			plantilla_generada = plantilla_generada.replace(IDs_F1[x], lista_textos1[x])

		self.nombre = str(input(Fore.CYAN+"""
Introduce el self.nombre de tu plantilla generada 
sin extension .html: > """))

		plantilla_generada_v2 = open("{}.html".format(self.nombre), "w")
		plantilla_generada_v2.write(plantilla_generada)

		plantilla_base.close()
		plantilla_generada_v2.close()
		clean()

		print(Fore.GREEN+"""
Todo procesado. Ahora verifica tu 
plantilla generada en la misma self.ruta donde 
esta alojado la plantilla base del formato 1.""")


	def formato2(self):
		self.formato = str(input(Fore.YELLOW+"""
Introduce el formato de las 
imagenes sin '.' (punto): > """))
		imagen_F2 = str(input(Fore.CYAN+r"logoheader: > "))
		imagen2_F2 = str(input(Fore.CYAN+"imagenproducto1: > "))
		imagen3_F2 = str(input(Fore.CYAN+"imagenproducto2: > "))
		imagen4_F2 = str(input(Fore.CYAN+"imagenproducto3: > "))

		# Colores:
		texto_F2 = str(input(Fore.CYAN+"Color de fondo (titulo principal): > ")) #bgtituloprincipal
		texto2_F2 = str(input(Fore.CYAN+"Color del fondo (Boton): > ")) #bgboton
		texto3_F2 = str(input(Fore.CYAN+"Color de texto (Boton): > ")) #colorboton
		texto4_F2 = str(input(Fore.CYAN+"Texto del titulo (principal): > ")) #titulodelprimercontenido
		texto5_F2 = str(input(Fore.CYAN+"Saludo cliente: > ")) #saludocliente
		texto6_F2 = str(input(Fore.CYAN+"""Parrafo (1): > """)) #primerparrafoprincipal
		texto7_F2 = str(input(Fore.CYAN+"""Parrafo (2): > """)) #segundoparrafoprincipal
		texto8_F2 = str(input(Fore.CYAN+"""Parrafo (3): > """)) #tercerparrafoprincipal
		texto9_F2 = str(input(Fore.CYAN+"Texto (Boton): > ")) #textodeboton
		texto10_F2 = str(input(Fore.CYAN+r"Enlace (Boton): > ")) #enlaceboton
		texto11_F2 = str(input(Fore.CYAN+"""Descripcion Producto (1) > """)) #textodelproducto1
		texto12_F2 = str(input(Fore.CYAN+"""Descripcion Producto (2): > """)) #textodelproducto2
		texto13_F2 = str(input(Fore.CYAN+"""Descripcion Producto (3): > """)) #textodelproducto3
		texto14_F2 = str(input(Fore.CYAN+"Pie de Pagina o Footer: > ")) #piedepagina

		lista_textos2 = [texto_F2, texto2_F2, texto3_F2, texto4_F2,
			texto5_F2, texto6_F2, texto7_F2, texto8_F2, texto9_F2,
			texto10_F2, texto11_F2, texto12_F2, texto13_F2, texto14_F2]

		IDs_F2 = ["bgtituloprincipal", "bgboton", "colorboton", "titulodelprimercontenido",
			"saludocliente", "primerparrafoprincipal", "segundoparrafoprincipal", "tercerparrafoprincipal",
			"textodeboton", "enlaceboton", "textodelproducto1", "textodelproducto2", "textodelproducto3",
			"piedepagina"]

		imagenes = [imagen_F2, imagen2_F2, imagen3_F2, imagen4_F2]

		self.nombre = str(input("""
Introduce el nombre para guardar las fotos > """))
		os.system("mkdir {}".format(self.nombre))

		Satanic_Remplazus_Scamming.conversion_url(imagenes, self.formato)
		Satanic_Remplazus_Scamming.limpieza(self.imagenes2)
		Satanic_Remplazus_Scamming.inyeccion(self.imagenes2)
		Satanic_Remplazus_Scamming.hosting(self.imagenes2)


		imagen_F2 = self.lista1[0] 
		imagen2_F2 = self.lista1[1] 
		imagen3_F2 = self.lista1[2]
		imagen4_F2 = self.lista1[3]

		plantilla_base = open("plantilla2.html", "r")
		plantilla_generada = plantilla_base.read()
		plantilla_generada = plantilla_generada.replace("logoheader", imagen_F2)
		plantilla_generada = plantilla_generada.replace("imagenproducto1", imagen2_F2)
		plantilla_generada = plantilla_generada.replace("imagenproducto2", imagen3_F2)
		plantilla_generada = plantilla_generada.replace("imagenproducto3", imagen4_F2)


		for x in range(len(lista_textos2)):
			plantilla_generada = plantilla_generada.replace(IDs_F2[x], lista_textos2[x])

		self.nombre = str(input(Fore.CYAN+"""
Introduce el self.nombre de tu plantilla generada 
sin extension .html: > """))

		plantilla_generada_v2 = open("{}.html".format(self.nombre), "w")
		plantilla_generada_v2.write(plantilla_generada)

		plantilla_base.close()
		plantilla_generada_v2.close()

		clean()
		print(Fore.GREEN+"""
Todo procesado. Ahora verifica tu 
plantilla generada en la misma self.ruta donde 
esta alojado la plantilla base del formato 1.""")

	def formato3(self):
		self.formato = str(input(Fore.YELLOW+"""
Introduce el formato de las 
imagenes sin '.' (punto): > """))
		imagen_F3 = str(input(Fore.CYAN+r"logoheader: > "))
		imagen2_F3 = str(input(Fore.CYAN+r"bannerprincipal: > "))
		imagen3_F3 = str(input(Fore.CYAN+r"bannersecondario: > "))
		imagen4_F3 = str(input(Fore.CYAN+r"imagenenhorizontal11: > "))	
		imagen5_F3 = str(input(Fore.CYAN+r"imagenenhorizontal12: > "))
		imagen6_F3 = str(input(Fore.CYAN+r"imagenenhorizontal13: > "))
		imagen7_F3 = str(input(Fore.CYAN+r"imagenenhorizontal21: > "))
		imagen8_F3 = str(input(Fore.CYAN+r"imagenenhorizontal22: > "))
		imagen9_F3 = str(input(Fore.CYAN+r"imagenenhorizontal23: > "))
		

		# Textos primero. Luego color
		texto_F3 = str(input(Fore.CYAN+"Titulo Principal (Texto): > ")) #tituloprincipal
		texto2_F3 = str(input(Fore.CYAN+"""Descripcion Principal (1): > """)) #descripcionprincipal
		texto3_F3 = str(input(Fore.CYAN+"Texto (Boton): > ")) #textodelboton
		texto4_F3 = str(input(Fore.CYAN+"""Descripcion Principal (2): > """)) #descripcionprincipal2
		texto5_F3 = str(input(Fore.CYAN+"Texto de imagen horizontal (1): > ")) #textoimagenhorizontal11

		# Textos:
		texto6_F3 = str(input(Fore.CYAN+"Texto de imagen horizontal (2): > ")) #textoimagenhorizontal12
		texto7_F3 = str(input(Fore.CYAN+"Texto de imagen horizontal (3): > ")) #textoimagenhorizontal13
		texto8_F3 = str(input("Titulo Secundario: > ")) #titulosecundario
		texto9_F3 = str(input(Fore.CYAN+"Titulo Imagen (2): > ")) #tituloimagen2
		texto10_F3 = str(input(Fore.CYAN+"Titulo Imagen (3): > ")) #tituloimagen3
		texto11_F3 = str(input(Fore.CYAN+"Descripcion del boton (Arriba): > ")) #descripcionantesdeboton
		texto12_F3 = str(input(Fore.CYAN+"Texto de imagen horizontal v2-1 (Arriba): > ")) #textoimagenhorizontal21t
		texto13_F3 = str(input(Fore.CYAN+"Texto de imagen horizontal v2-2 (Arriba): > ")) #textoimagenhorizontal22t
		texto14_F3 = str(input(Fore.CYAN+"Texto de imagen horizontal v2-3 (Arriba): > ")) #textoimagenhorizontal23t
		texto15_F3 = str(input(Fore.CYAN+"Texto de imagen horizontal v2-1 (Abajo): > ")) #textoimagenhorizontal21b
		texto16_F3 = str(input(Fore.CYAN+"Texto de imagen horizontal v2-2 (Abajo): > ")) #textoimagenhorizontal22b
		texto17_F3 = str(input(Fore.CYAN+"Texto de imagen horizontal v2-3 (Abajo): > ")) #textoimagenhorizontal23b
		texto18_F3 = str(input(Fore.CYAN+"""Descripcion Secundaria: > """)) #descripcionsecundaria
		texto19_F3 = str(input(Fore.CYAN+"Enlace (Boton): > ")) #enlaceboton
		texto20_F3 = str(input(Fore.CYAN+"Footer o Pie de Pagina: > ")) #piedepagina
		texto21_F3 = str(input(Fore.CYAN+"Color (Boton): > ")) #colorboton

		lista_textos3 = [texto_F3, texto2_F3, texto3_F3, texto4_F3,
			texto5_F3, texto6_F3, texto7_F3, texto8_F3, texto9_F3,
			texto10_F3, texto11_F3, texto12_F3, texto13_F3, texto14_F3,
			texto15_F3, texto16_F3, texto17_F3, texto18_F3, texto19_F3, 
			texto20_F3, texto21_F3]

		IDs_F3 = ["tituloprincipal", "descripcionprincipal", "textodelboton",
			"descripcionprincipal2", "textoimagenhorizontal11", "textoimagenhorizontal12",
			"textoimagenhorizontal13", "titulosecundario", "tituloimagen2", "tituloimagen3",
			"descripcionantesdeboton", "textoimagenhorizontal21t", "textoimagenhorizontal22t",
			"textoimagenhorizontal23t", "textoimagenhorizontal21b", "textoimagenhorizontal22b",
			"textoimagenhorizontal23b", "descripcionsecundaria", "enlaceboton", "piedepagina", 
			"colorboton"]

		imagenes = [imagen_F3, imagen2_F3, imagen3_F3, imagen4_F3, imagen5_F3,
			imagen6_F3, imagen7_F3, imagen8_F3, imagen9_F3]

		self.nombre = str(input("""
Introduce el nombre para guardar las fotos > """))
		os.system("mkdir {}".format(self.nombre))

		Satanic_Remplazus_Scamming.conversion_url(imagenes, self.formato)
		Satanic_Remplazus_Scamming.limpieza(self.imagenes2)
		Satanic_Remplazus_Scamming.inyeccion(self.imagenes2)
		Satanic_Remplazus_Scamming.hosting(self.imagenes2)

		imagen_F3 = self.lista1[0] 
		imagen2_F3 = self.lista1[1] 
		imagen3_F3 = self.lista1[2] 
		imagen4_F3 = self.lista1[3] 
		imagen5_F3 = self.lista1[4]
		imagen6_F3 =  self.lista1[5]
		imagen7_F3 = self.lista1[6] 
		imagen8_F3 = self.lista1[7] 
		imagen9_F3 = self.lista1[8]

		plantilla_base = open("plantilla3.html", "r")
		plantilla_generada = plantilla_base.read()
		plantilla_generada = plantilla_generada.replace("logoheader", imagen_F3)
		plantilla_generada = plantilla_generada.replace("bannerprincipal", imagen2_F3)
		plantilla_generada = plantilla_generada.replace("bannersecondario", imagen3_F3)
		plantilla_generada = plantilla_generada.replace("imagenenhorizontal11", imagen4_F3)
		plantilla_generada = plantilla_generada.replace("imagenenhorizontal12", imagen5_F3)
		plantilla_generada = plantilla_generada.replace("imagenenhorizontal13", imagen6_F3)
		plantilla_generada = plantilla_generada.replace("imagenenhorizontal21", imagen7_F3)
		plantilla_generada = plantilla_generada.replace("imagenenhorizontal22", imagen8_F3)
		plantilla_generada = plantilla_generada.replace("imagenenhorizontal23", imagen9_F3)

		for x in range(len(lista_textos3)):
			plantilla_generada = plantilla_generada.replace(IDs_F3[x], lista_textos3[x])

		self.nombre = str(input(Fore.CYAN+"""
Introduce el self.nombre de tu plantilla generada 
sin extension .html: > """))

		plantilla_generada_v2 = open("{}.html".format(self.nombre), "w")
		plantilla_generada_v2.write(plantilla_generada)

		plantilla_base.close()
		plantilla_generada_v2.close()

		clean()
		print(Fore.GREEN+"""
Todo procesado. Ahora verifica tu 
plantilla generada en la misma self.ruta donde 
esta alojado la plantilla base del formato 1.""")


	def formato4(self):
		self.formato = str(input(Fore.YELLOW+"""
Introduce el formato de las 
imagenes sin '.' (punto): > """))
		imagen_F4 = str(input(Fore.CYAN+r"logo: > "))
		imagen2_F4 = r"""https://ci4.googleusercontent.com/proxy/-G54ZlbaxMPqzCZE-7XYhuAyfijItAWj1Szix4Cqdsiqy3AbTUxWcUayfcrHmkLuKhZ_2Ns0XXyeUVT2ukDi0ox_g5BswnV0V04j7_hZiJRML7s9YPvyeY4IN0Af4sl6qd8=s0-d-e1-ft#http://epidm.edgesuite.net/CMS/Coding/PayPal/2018/Global/headergrad_onwhite.jpg"""
		imagen3_F4 = str(input(Fore.CYAN+r"fotocupon01: > "))
		imagen4_F4 = r"""https://i.ibb.co/dtk8CwB/unnamed-1.jpg"""	
		imagen5_F4 = str(input(Fore.CYAN+r"fotopaso01: > "))
		imagen6_F4 = str(input(Fore.CYAN+r"fotopaso02: > "))
		imagen7_F4 = str(input(Fore.CYAN+r"fotopaso03: > "))
		imagen8_F4 = str(input(Fore.CYAN+r"plataforma001: > "))
		imagen9_F4 = str(input(Fore.CYAN+r"plataforma002: > "))
		imagen10_F4 = str(input(Fore.CYAN+r"plataforma003: > "))
		imagen11_F4 = str(input(Fore.CYAN+r"plataforma004: > "))
		imagen12_F4 = str(input(Fore.CYAN+r"plataforma005: > "))
		imagen13_F4 = str(input(Fore.CYAN+r"plataforma006: > "))
		

		# Textos primero. Luego color
		texto_F4 = str(input(Fore.CYAN+"Titulo Principal (Texto): > ")) #tituloazul01
		texto2_F4 = str(input(Fore.CYAN+"""Descripcion Principal (1): > """)) #descripcion01
		texto3_F4 = str(input(Fore.CYAN+"Texto (Boton): > ")) #textodelboton
		texto4_F4 = str(input(Fore.CYAN+"""Descripcion Boton: > """)) #minidescripcion_boton
		texto5_F4 = str(input(Fore.CYAN+"Texto (Boton): > ")) #textoboton01

		# Textos:
		texto6_F4 = str(input(Fore.CYAN+"Titulo (2): > ")) #tituloazul02
		texto7_F4 = str(input("Paso 1 (Texto Corto): > ")) #paso1
		texto8_F4 = str(input(Fore.CYAN+"Paso 2 (Texto Corto): > ")) #paso2
		texto9_F4 = str(input(Fore.CYAN+"Paso 3 (Texto Corto): > ")) #paso3
		texto10_F4 = str(input(Fore.CYAN+"Titulo (3): > ")) #tituloazul03
		texto11_F4 = str(input(Fore.CYAN+"Descripcion Plataformas: > ")) #minidescripcion03
		texto12_F4 = str(input(Fore.CYAN+"Enlace (Boton): > ")) #tu_scam.com

		lista_textos4 = [texto_F4, texto2_F4, texto3_F4, texto4_F4,
			texto5_F4, texto6_F4, texto7_F4, texto8_F4, texto9_F4,
			texto10_F4, texto11_F4, texto12_F4]

		IDs_F4 = ["tituloazul01", "descripcion01", "textodelboton",
			"minidescripcion_boton", "textoboton01", "tituloazul02",
			"paso1", "paso2", "paso3", "tituloazul03",
			"minidescripcion03", "tu_scam.com"]

		imagenes = [imagen_F4, imagen2_F4, imagen3_F4, imagen4_F4, imagen5_F4,
			imagen6_F4, imagen7_F4, imagen8_F4, imagen9_F4, imagen10_F4, imagen11_F4, imagen12_F4, imagen13_F4]

		self.nombre = str(input("""
Introduce el nombre para guardar las fotos > """))
		os.system("mkdir {}".format(self.nombre))

		Satanic_Remplazus_Scamming.conversion_url(imagenes, self.formato)
		Satanic_Remplazus_Scamming.limpieza(self.imagenes2)
		Satanic_Remplazus_Scamming.inyeccion(self.imagenes2)
		Satanic_Remplazus_Scamming.hosting(self.imagenes2)

		imagen_F4 = self.lista1[0] 
		imagen2_F4 = self.lista1[1] 
		imagen3_F4 = self.lista1[2] 
		imagen4_F4 = self.lista1[3] 
		imagen5_F4 = self.lista1[4]
		imagen6_F4 =  self.lista1[5]
		imagen7_F4 = self.lista1[6] 
		imagen8_F4 = self.lista1[7] 
		imagen9_F4 = self.lista1[8]
		imagen10_F4 = self.lista1[9]
		imagen11_F4 = self.lista1[10]
		imagen12_F4 = self.lista1[11]
		imagen13_F4 = self.lista1[12]

		plantilla_base = open("plantilla4.html", "r")
		plantilla_generada = plantilla_base.read()
		plantilla_generada = plantilla_generada.replace("logo001", imagen_F4)
		plantilla_generada = plantilla_generada.replace("barra01", imagen2_F4)
		plantilla_generada = plantilla_generada.replace("fotocupon01", imagen3_F4)
		plantilla_generada = plantilla_generada.replace("espacio001", imagen4_F4)
		plantilla_generada = plantilla_generada.replace("fotopaso01", imagen5_F4)
		plantilla_generada = plantilla_generada.replace("fotopaso02", imagen6_F4)
		plantilla_generada = plantilla_generada.replace("fotopaso03", imagen7_F4)
		plantilla_generada = plantilla_generada.replace("plataforma001", imagen8_F4)
		plantilla_generada = plantilla_generada.replace("plataforma002", imagen9_F4)
		plantilla_generada = plantilla_generada.replace("plataforma003", imagen10_F4)
		plantilla_generada = plantilla_generada.replace("plataforma004", imagen11_F4)
		plantilla_generada = plantilla_generada.replace("plataforma005", imagen12_F4)
		plantilla_generada = plantilla_generada.replace("plataforma006", imagen13_F4)

		for x in range(len(lista_textos4)):
			plantilla_generada = plantilla_generada.replace(IDs_F4[x], lista_textos4[x])

		self.nombre = str(input(Fore.CYAN+"""
Introduce el self.nombre de tu plantilla generada 
sin extension .html: > """))

		plantilla_generada_v2 = open("{}.html".format(self.nombre), "w")
		plantilla_generada_v2.write(plantilla_generada)

		plantilla_base.close()
		plantilla_generada_v2.close()

		clean()
		print(Fore.GREEN+"""
Todo procesado. Ahora verifica tu 
plantilla generada en la misma self.ruta donde 
esta alojado la plantilla base del formato 1.""")


class Satanic_Converter_Images():
	def __init__(self, imagen = None, nombre = None):
		self.imagen = imagen
		self.nombre = nombre

	def clean(self):
		if sistema == "Windows":
			os.system("cls")

		elif sistema == "Linux":
			os.system("clear")

	def banner(self):
		init(autoreset=True)
		banner = pyfiglet.figlet_format("Satanic Converter Images")
		print(Fore.RED+banner)
		print(Fore.YELLOW+"""\
NOTA:
- PNG a JPG (Por ahora) si tienes problemas, puedes ir a: 
https://png2jpg.com/

""")

	def funcionamiento(self):
		converter = Satanic_Converter_Images()
		converter.clean()
		
		print(Fore.RED+"""
Fase 1: Conversion...""")
		
		imagen = Image.open(self.imagen)
		fondo = Image.new("RGB", imagen.size, (255,255,255))
		fondo.paste(imagen, (0,0), imagen)
		fondo.save(self.nombre, quality = 95)
		
		print(Fore.GREEN+"Imagen convertida.")
		time.sleep(2)
		converter.clean()
		
		print(Fore.RED+"""
Fase 2: Limpieza de metadatos.""")
		
		os.system("exiftool -all= {}".format(self.nombre))
		time.sleep(2)
		converter.clean()
		print(Fore.GREEN+"Imagen convertida y limpiada.")


class Satanic_Fotus_Editus():
	def __init__(self, imagen= None, mensaje = None, color = None, tamaño =  None,
		fuente = None, nombre = None):

		self.imagen = imagen
		self.mensaje = mensaje
		self.color = color
		self.tamaño = tamaño
		self.fuente = fuente
		self.nombre = nombre 

	def clean(self):
		if sistema == "Windows":
			os.system("cls")

		elif sistema == "Linux":
			os.system("clear")

	def banner(self):
		init(autoreset=True)
		banner = pyfiglet.figlet_format("Satanic Fotus Editus")
		print(Fore.RED+banner)
		print(Fore.GREEN+"""\
Referencias Utiles:

Vectores Gratis: (Sin registro)
- https://www.freepik.es/ 

Alojamiento de Fotos: (Sin registro, brinda url directo de imagen)
- https://es.imgbb.com/

Tipografias Gratuitas:
- https://www.dafont.com/

""")

	def funcionamiento(self):
		# Espacios:

		if self.mensaje.count("\n") >= 1:
			self.mensaje = self.mensaje.replace(r"\n", "\n" )


		else:
			pass

		imagen = Image.open(self.imagen)
		imagen = imagen.resize((600, 400))
		dibujar = ImageDraw.Draw(imagen)

		fuente = ImageFont.truetype(self.fuente, self.tamaño)
		lineas = self.mensaje.splitlines()
		w = fuente.getsize(max(lineas, key=lambda s: len(s)))[0]
		h = fuente.getsize(self.mensaje)[1] * len(lineas)
		x, y = imagen.size
		x /= 2
		x -= w / 2
		y /= 2
		y -= h / 2
    
		dibujar.multiline_text((x, y), self.mensaje , font = fuente, fill = self.color,
			align="center")
		imagen.save(self.nombre)
		print(Fore.GREEN+"Tu imagen ya esta guardada y modificada")




def fotus_config():
	fotus = Satanic_Fotus_Editus()
	fotus.clean()
	fotus.banner()
	
	init(autoreset = True)

	imagen = str(input(Fore.CYAN+r"""Ruta Imagen: > """))
	mensaje = str(input(Fore.CYAN+"""Mensaje (Foto): > """))
	fotus.clean()
	color = str(input(Fore.CYAN+"""
Menu:
[1] Escoger Colores
[2] Personalizado

>>> """))

	if color == "1":
		color = str(input(Fore.CYAN+""""
COLOR:      Codigo Hex:   RGB:

BLANCO,     #FFFFFF,      RGB (255, 255, 255)
PLATA,      #C0C0C0,      RGB (192, 192, 192)
GRIS,       #808080,      RGB (128, 128, 128)
NEGRO,      #000000,      RGB (0, 0, 0)
ROJO,       #FF0000,      RGB (255, 0, 0)
MAROON,     #800000,      RGB (128, 0, 0)
AMARILLO,   #FFFF00,      RGB (255, 255, 0)
OLIVE,      #808000,      RGB (128, 128, 0)
LIME,       #00FF00,      RGB (0, 255, 0)
VERDE,      #008000,      RGB (0, 128, 0)
AQUA,       #00FFFF,      RGB (0, 255, 255)
TEAL,       #008080,      RGB (0, 128, 128)
AZUL,       #0000FF,      RGB (0, 0, 255)
NAVY,       #000080,      RGB (0, 0, 128)
FUCHSIA,    #FF00FF,      RGB (255, 0, 255))
PÚRPURA,    #800080,      RGB (128, 0, 128))

Introduce el codigo hex incluye (#): > """))

	elif color == "2":
		color = str(input(Fore.CYAN+"Introduce tu color: > "))

	else:
		print(Fore.RED+"Opcion invalida.")

	tamaño = int(input(Fore.CYAN+"Tamaño de fuente: > "))

	fotus.clean()
	fuente = str(input(Fore.CYAN+"""
Menu:
[1] Escoger Fuentes (Tipografía)
[2] Personalizado 

>>> """))

	if fuente == "1":
		fotus.clean()
		fuente = str(input("""
Menu:
[1] Estilo Navideño
[2] Estilo San Valentin (Amor)
[3] Estilo Cumpleaños (Regalo)
[4] Estilo Año Nuevo
[5] Estilo Tecnologico

>>> """)) 
		if fuente == "1":
			fuente = "fuentes/navidad.ttf"

		elif fuente == "2":
			fuente = "fuentes/amor.ttf"

		elif fuente == "3":
			fuente = "fuentes/regalo.ttf"

		elif fuente == "4":
			fuente = "fuentes/newyear.ttf"

		elif fuente == "5":
			fuente = "fuentes/tecnologico.ttf"

		else: 
			print(Fore.RED+"Opcion invalida.")

	elif fuente == "2":
		fuente = str(input(Fore.CYAN+r"""Introduce la ruta de la fuente: > """))


	nombre = str(input(Fore.CYAN+r"Nombre y extension de la nueva imagen: > "))

	fotus = Satanic_Fotus_Editus(imagen, mensaje, color, tamaño, fuente, nombre)
	fotus.funcionamiento()

# Funciones:
def mailer_config():
	
	inicio = pyfiglet.figlet_format("Satanic Senderus Mailer")
	print(Fore.RED+inicio)
	
	email = getpass.getpass(Fore.CYAN+"Cuenta Gmail (Email): > ")
	password = getpass.getpass(Fore.CYAN+"Password: > ")
	remitente2 = str(input(Fore.CYAN+"Remitente Mensaje: > "))
	remitente = "{} {}".format(remitente2,email) 
	destino = str(input(Fore.CYAN+r"Archivo Emails: > "))
	asunto = str(input(Fore.CYAN+"Asunto: > "))

	opciones_plantilla = str(input(Fore.CYAN+"""
Plantillas:
[1] PayPal (Versiones Premium)
[2] Personalizada

>>> """))

	if opciones_plantilla == "1":
		plantilla = "paypal-movil.html"
		letter = open(plantilla,"r")
		plantilla = letter.read()

	elif opciones_plantilla == "2":
		plantilla = str(input(Fore.CYAN+r"Archivo Plantilla: > "))
		letter = open(plantilla,"r")
		plantilla = letter.read()
	
	else:
		print(Fore.RED+"Comando invalido")

	ruta_adjunto = str(input(Fore.CYAN+r"""
Archivo Adjunto: > """))
	cantidad = str(input(Fore.CYAN+"Cantidad de emails: > "))
	print()

	mailer = Satanic_Senderus_Mailer(email, password, remitente, destino, asunto, plantilla, ruta_adjunto, cantidad)
	mailer.cabeceras_parametros()

def call_config():
	inicio = pyfiglet.figlet_format("Satanic Senderus VoiceCaller")
	print(Fore.RED+inicio)
	
	sid_token = open("sid_token.txt", "r")

	sid = sid_token.readline()
	sid = sid.replace(r"\n", "")
	
	token = sid_token.readline()
	token = token.replace(r"\n", "")

	
	print(Fore.YELLOW+"""
Codigo:   Lenguaje:    Pais:""")
	codigo = str(input(Fore.CYAN+"""
da-DK	  Danish,      Denmark
de-DE	  German,      Germany
en-AU	  English,     Australia
en-CA	  English,     Canada
en-GB	  English,     UK
en-IN	  English,     India
en-US	  English,     United States
ca-ES	  Catalan,     Spain
es-ES	  Spanish,     Spain
es-MX	  Spanish,     Mexico
fi-FI	  Finnish,     Finland
fr-CA	  French,      Canada
fr-FR	  French,      France
it-IT	  Italian,     Italy
ja-JP	  Japanese,    Japan
ko-KR	  Korean,      Korea
nb-NO	  Norwegian,   Norway
nl-NL	  Dutch,       Netherlands
pl-PL	  Polish,      Poland
pt-BR	  Portuguese,  Brazil
pt-PT	  Portuguese,  Portugal
ru-RU	  Russian,     Russia
sv-SE	  Swedish,     Sweden
zh-CN	  Chinese      Mandarin
zh-HK	  Chinese      Cantonese
zh-TW	  Chinese      Taiwanese Mandarin

Escriba el codigo para el lenguaje, recuerde 
solo podra enviar llamadas y sms donde halla elegido 
previamente: >>> """))

	mensaje = str(input(Fore.CYAN+"""Introduzca el mensaje para la conversion de TTS: > """))

	xml = VoiceResponse()
	xml.say(mensaje, voice='alice', language=codigo)

	pregunta = str(input("""
Opciones Voz:
[1] Alojar URL Manual (000webhost recomendado)
[2] Alojar Automatico (Inseguro sin medidad de proteccion, no funciona siempre al 100%)

>>> """))

	if pregunta == "1":
		print(Fore.CYAN+"""
Copie el codigo e introduzcalo en un archivo.xml
luego aloje en un hosting, si ya lo hizo no es necesario.\n""")

		print(Fore.YELLOW+str(xml))

	elif pregunta == "2":

		if sistema == "Windows":
			url_ngrok = str(input("Introduce tu URL ngrok: > "))
			voz_archivo = open("voz.xml", "w")
			voz_archivo.write(str(xml))
			voz_archivo.close()
			voz = url_ngrok+"/"+"voz.xml"
			puerto = str(input("Introduca el puerto que esta activo en Ngrok: > "))

			doc_to_bat = """start cmd.exe\npython -m http.server {}""".format(puerto)

			archivo_bat = open("autorun.bat", "w")
			archivo_bat = archivo_bat.write(str(doc_to_bat)) 

			comodin_shell = r"""
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "autorun.bat" & Chr(34), 0
Set WshShell = Nothing"""

			comodin = open("comodin_shell.vbs", "w")
			comodin.write(comodin_shell)
			os.system("start comodin_shell.vbs")

			print(Fore.GREEN+"\nCopielo y establezcalo como URL de voz:", """\n
{}""".format(Fore.GREEN+voz))

		elif sistema == "Linux":
			print(Fore.YELLOW+"Lo siento, solo he hecho esta parte automatica en Windows.")
			print(Fore.CYAN+"""\n 
Pasos para teminar:

1. Abra una nueva sesion y ejecute el comando:
python -m http.server su_puerto_ngrok

(Ejecuta el comando en la misma self.ruta en la 
que ejecutaste el script. Luego regresa a la sesion anterior)

""")

			avance = str(input(Fore.CYAN+"Cuando termines ejecuta 'y': >>> "))
			url_ngrok = str(input(Fore.CYAN+"Introduce tu URL ngrok: > "))
			voz_archivo = open("voz.xml", "w")
			voz_archivo.write(str(xml))
			voz_archivo.close()
			voz = url_ngrok+"/"+"voz.xml"
			puerto = str(input(Fore.CYAN+"Introduca el puerto que esta activo en Ngrok: > "))
			
			print(Fore.GREEN+"\nCopielo y establezcalo como URL de voz:", """\n
{}""".format(Fore.GREEN+voz))

		else:
			print(Fore.RED+"Lo siento, tu sistema no ha sido configurado para VoiceCaller.")

	voz = str(input(Fore.CYAN+"\nIntroduce tu URL de voz: > "))

	numeros = str(input(Fore.CYAN+r"Ruta de Numeros: > "))
	
	remitente_ = open("remitente_twilio.txt", "r")
	remitente = remitente_.readline()
	remitente = remitente.replace(r"\n", "")

	cantidad = str(input(Fore.CYAN+"Ingrese la cantidad de numeros: > "))
	
	caller = Satanic_Senderus_VoiceCall(sid, token, voz, numeros, remitente, cantidad)
	caller.filtro()
	caller.llamar()

def sms_config():
	init(autoreset=True)
	inicio = pyfiglet.figlet_format("Satanic Senderus SMS")
	print(Fore.RED+inicio)
	
	sid_token = open("sid_token.txt", "r")
	
	sid_token = open("sid_token.txt", "r")

	sid = sid_token.readline()
	sid = sid.replace(r"\n", "")
	
	token = sid_token.readline()
	token = token.replace(r"\n", "")

	
	numeros = str(input(Fore.CYAN+r"Ruta de Numeros: > "))
	
	remitente_ = open("remitente_twilio.txt", "r")
	remitente = remitente_.readline()
	remitente = remitente.replace(r"\n", "")

	cantidad = str(input(Fore.CYAN+"Ingrese la cantidad de numeros: > "))
	mensaje = str(input(Fore.CYAN+"Ingrese un mensaje: > "))
	sms = Satanic_Senderus_SMS_Attacker(sid, token, mensaje, remitente , numeros, cantidad)
	sms.filtro()


def remplazus_def():
	init(autoreset=True)
	banner = pyfiglet.figlet_format("Satanic Remplazus Scamming")
	

	print(Fore.RED+banner)
	opcion = str(input(Fore.CYAN+"""
[1] Plantilla 1
[2] Plantilla 2
[3] Plantilla 3 
[4] Plantilla 4

>>> """))

	
	if opcion == "1":
		Satanic_Remplazus_Scamming.formato1()
	
	elif opcion == "2":
		Satanic_Remplazus_Scamming.formato2()
	
	elif opcion == "3":
		Satanic_Remplazus_Scamming.formato3()

	elif opcion == "4":
		Satanic_Remplazus_Scamming.formato4()

	else:
		print(Fore.RED+"Comando invalido.")
		clean()
		remplazus_def()

Satanic_Remplazus_Scamming = Satanic_Remplazus_Scamming()

def converter_config():
	converter = Satanic_Converter_Images()
	converter.clean()
	converter.banner()
	imagen = str(input(Fore.CYAN+r"""Ruta Imagen: > """))
	nombre = str(input(Fore.CYAN+"Nombre y extension de la nueva imagen: > "))
	converter = Satanic_Converter_Images(imagen, nombre)
	converter.funcionamiento()

def banner():
	print(Fore.RED+r"""
            ._                                            ,
             (`)..                                    ,.-')
              (',.)-..                            ,.-(..`)         
               (,.' ,.)-..                    ,.-(. `.. )                    
                (,.' ..' .)-..            ,.-( `.. `.. )                     
                 (,.' ,.'  ..')-.     ,.-( `. `.. `.. )                      
                  (,.'  ,.' ,.'  )-.-('   `. `.. `.. )                       
                   ( ,.' ,.'    _== ==_     `.. `.. )                        
                    ( ,.'   _==' ~  ~  `==_    `.. )                     
                     \  _=='   ----..----  `==_   )                     
                  ,.-:    ,----___.  .___----.    -..                        
              ,.-'   (   _--====_  \/  _====--_   )  `-..                 
          ,.-'   .__.'`.  `-_I0_-'    `-_0I_-'  .'`.__.  `-..     
      ,.-'.'   .'      (          |  |          )      `.   `.-..  
  ,.-'    :    `___--- '`.__.    / __ \    .__.' `---___'    :   `-..      
-'_________`-____________'__ \  (O)  (O)  / __`____________-'________`-     
                            \ . _  __  _ . /                               
                             \ `V-'  `-V' |                                 
                              | \ \ | /  /                                 
                               V \ ~| ~/V                                   
                                |  \  /|                                    
                                 \~ | V                                  
                                  \  |                                        
                                   VV

              "Hacking is The New World, Make Your History"
               "Da us oe inice ome caus, sorulius gerrte."

                    No soy responsable de tus pecados.                        
                        
                         Satanic Senderus Tool
                                v1.0.5

                                   Δ
""".format(sistema))
def menu():

	sistema = platform.system()

	if sistema == "Windows":
		init(autoreset=True)
		os.system("title Anonymous Unknown")

		os.system("cls")

		banner()
		menu = str(input(Fore.CYAN+"""\n\nSatanic Senderus Menu:
[1] Satanic Senderus Mailer 
[2] Satanic Senderus VoiceCaller
[3] Satanic Senderus SMS Attacker
[4] Satanic Remplazus Scamming Tool 
[5] Satanic Converter PNG to JPG (Solo PC)
[6] Satanic Fotus Editus (Solo PC)

>>> """		))

		if menu == "1":
			os.system("cls")
			mailer_config()

		elif menu == "2":
			os.system("cls")
			call_config()

		elif menu == "3":
			os.system("cls")
			sms_config()

		elif menu == "4":
			os.system("cls")
			remplazus_def()

		elif menu == "5":
			os.system("cls")
			converter_config()
		
		elif menu == "6":
			os.system("cls")
			fotus_config()

		else:
			print(Fore.RED+"Comando satanicamente desconocido...")



	elif sistema == "Linux":
		init(autoreset=True)
		os.system("clear")
		
		banner()
		
		menu = str(input(Fore.CYAN+"""\n\nSatanic Senderus Menu:
[1] Satanic Senderus Mailer 
[2] Satanic Senderus VoiceCaller
[3] Satanic Senderus SMS Attacker
[4] Satanic Remplazus Scamming Tool
[5] Satanic Converter PNG to JPG (Solo PC)
[6] Satanic Fotus Editus (Solo PC)

>>> """))

		if menu == "1":
			os.system("clear")
			mailer_config()

		elif menu == "2":
			os.system("clear")
			call_config()

		elif menu == "3":
			os.system("clear")
			sms_config()

		elif menu == "4":
			os.system("clear")
			remplazus_def()

		elif menu == "5":
			os.system("clear")
			converter_config()

		elif menu == "6":
			os.system("clear")
			fotus_config()
		
		else:
			print(Fore.RED+"Comando satanicamente desconocido...")

	else:
		print(Fore.RED+"Sistema Operativo satanicamente desconocido, o no establecido por mi, perro.")

menu()
