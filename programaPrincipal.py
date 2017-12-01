from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk # Permite el manejo de imagenes
from urllib import request # Permite descargar archivos desde internet (imagenes)
import http.client # Permite la comunicación entre Python e Internet
import chilkat # Se utiliza para parsear el contenido del archivo 'start.xml'
import os.path # Se utiliza para verificar si el archivo 'start.xml' existe
import os, sys  # Permite controlar el shell

xml = chilkat.CkXml()
archivo = "start.xml"

class Pelicula:
    def __init__(self):
        self.nombre = ""
        self.tipo = ""
        self.duracion = ""
        
        self.genero = ""
        self.directores = ""
        self.escritores = ""
        self.actores = ""
        self.premios = ""
        self.fechaLanzamiento = ""
        self.anno = ""
        self.idiomas = ""
        self.sinopsis = "" 
        self.metascore = ""
        self.imDBRate = ""
        self.linkImagen = ""
        self.listaPeliculas = []

    def setNombre(self,nombre):
        self.nombre = nombre
    def getNombre(self):
        return self.nombre

    def setTipo(self,tipo):
        self.tipo = tipo
    def getTipo(self):
        return self.tipo

    def setDuracion(self,duracion):
        self.duracion = duracion
    def getDuracion(self):
        return self.duracion

    def setGenero(self,genero):
        self.genero = genero
    def getGenero(self):
        return self.genero

    def setDirectores(self,directores):
        self.directores = directores
    def getDirectores(self):
        return self.directores

    def setEscritores(self,escritores):
        self.escritores = escritores
    def getEscritores(self):
        return self.escritores

    def setActores(self,actores):
        self.actores = actores
    def getActores(self):
        return self.actores

    def setPremios(self,premios):
        self.premios = premios
    def getPremios(self):
        return self.premios

    def setFechaLanzamiento(self,fechaLanzamiento):
        self.fechaLanzamiento = fechaLanzamiento
    def getFechaLanzamiento(self):
        return self.fechaLanzamiento

    def setAnno(self,anno):
        self.anno = anno
    def getAnno(self):
        return self.anno

    def setIdiomas(self,idiomas):
        self.idiomas = idiomas
    def getIdiomas(self):
        return self.idiomas

    def setSinopsis(self,sinopsis):
        self.sinopsis = sinopsis
    def getSinopsis(self):
        return self.sinopsis

    def setMetascore(self,metascore):
        self.metascore = metascore
    def getMetascore(self):
        return self.metascore

    def setImDBRate(self,imDBRate):
        self.imDBRate = imDBRate
    def getImDBRate(self):
        return self.imDBRate

    def setEnlaceImagen(self,linkImagen):
        self.linkImagen = linkImagen
    def getEnlaceImagen(self):
        return self.linkImagen

    def setListaPeliculas(self,listaPeliculas):
        self.listaPeliculas = listaPeliculas
    def getListaPeliculas(self):
        return self.listaPeliculas

 
class Coordenadas:
    def __init__(self):
        self.XX = 70
        self.YY = 80
        self.contador = 0

    def setCoordenadaX(self,XX):
        self.XX = XX
    def getCoordenadaX(self):
        return self.XX
    
    def setCoordenadaY(self,YY):
        self.YY = YY
    def getCoordenadaY(self):
        return self.YY

    def setContador(self,contador):
        self.contador = contador
    def getContador(self):
        return self.contador


claseCoordenada = Coordenadas()
clasePelicula = Pelicula()


def abrirVentana(ventana):# Hace posible abrir una nueva ventana, enviandole como parametro el nombre de la ventana
    ventana.deiconify()

def cerrarVentana(ventana):
    ventana.withdraw()

def configurarFrame(canvas):
    #Restablece la región de desplazamiento para abarcar todo el frame cada vez que se inserte una pelicula(boton y label)  
    canvas.configure(scrollregion=canvas.bbox("all"))
    
def comprobarExistencia(archivo):#-->> start.xml
    if os.path.exists(archivo):
        return True
    else:
        archivoXML = open("start.xml","a")
        archivoXML.write("<Peliculas>\n")
        archivoXML.write("")
        archivoXML.close()

def enviarCorreo(correoEntry):
    try:
        correo = correoEntry.get()
        mailman = chilkat.CkMailMan()

        success = mailman.UnlockComponent("30-day trial")
        if (success != True):
            return messagebox.showinfo("Atención!","El correo ingresado no es válido")
            sys.exit()

        mailman.put_SmtpHost("smtp.gmail.com")
        mailman.put_SmtpUsername("basedatospelis@gmail.com")
        mailman.put_SmtpPassword("basepelis123")

        email = chilkat.CkEmail()

        fileOnDisk = "images/"+clasePelicula.getNombre()+".jpg"
        filePathInHtml = clasePelicula.getNombre()+".jpg"

        success = email.AddRelatedFile2(fileOnDisk,filePathInHtml)
        if (success != True):
            return messagebox.showinfo("Atención!","El correo ingresado no es válido")
            sys.exit()

        htmlBody = "<html><body> Información de la película "+clasePelicula.getNombre()+"<br> Tipo: "+ clasePelicula.getTipo()+"<br> Duración: "+ clasePelicula.getDuracion()+"<br> Género: "+ clasePelicula.getGenero()+"<br> Directores: "+ clasePelicula.getDirectores()+"<br> Escritores: "+ clasePelicula.getEscritores()+"<br> Actores: "+ clasePelicula.getActores()+"<br> Premios: "+clasePelicula.getPremios()+"<br> Fecha de Lanzamient: "+clasePelicula.getFechaLanzamiento()+"<br> Año: "+clasePelicula.getAnno()+"<br> Idiomas: "+clasePelicula.getIdiomas()+"<br> Sinopsis: "+clasePelicula.getSinopsis()+"<br> Metascore: "+clasePelicula.getMetascore()+"<br>  ImDBRate: "+clasePelicula.getImDBRate()+"<br> Poster <br><img src=\""+clasePelicula.getNombre()+".jpg\"""> </body></html>"

        email.SetHtmlBody(htmlBody)
        email.put_Subject("Recomendación de película.")
        success = email.AddTo("Admin",str(correo))
        email.put_From("<basedatospelis@gmail.com>")

        success = mailman.SendEmail(email)
        if (success != True):
            return messagebox.showinfo("Atención!","El correo ingresado no es válido")

        else:
            return messagebox.showinfo("Atención!","El correo se ha enviado satisfactoriamente!.")
    except:
        return messagebox.showinfo("Atención!","El correo ingresado no es válido")


def buscarPelicula():
    nombrePelicula = cajaTexto.get() #Obtiene lo que se escribe en 'ventanaBuscarPelicula'
    
    if nombrePelicula == "": #En caso de que no se escriba nada
        return messagebox.showinfo("Atención!","Por favor, escriba el nombre de la película que desea buscar.")
        
    else:
        nombrePelicula = nombrePelicula.split() #Validación para la dirección http, ya que si se inserta un nombre con espacios...
        nombrePelicula = "+".join(nombrePelicula) #..este no funciona y para que sea valido se deben unir con un '+'
        
        atributosPelicula = http.client.HTTPSConnection("www.omdbapi.com")#Web principal

        try:
            atributosPelicula.request("GET", "http://www.omdbapi.com/?t="+nombrePelicula+"&y=&plot=full&r=xml") #PARAMETROS: t,y,r 
            resultado = atributosPelicula.getresponse()

            informacionPelicula = resultado.read()

            atributosPelicula.close()

            if informacionPelicula == b'<root response="False"><error>Movie not found!</error></root>':
                return messagebox.showinfo("Error!","La pelicula introducida es inválida o no existe.")#Validación en caso de no poder establecer conexión
            else:
                insertarInformacion = open("Storage.xml","a")

                insertarInformacion.write(str(informacionPelicula)) #Inserta todo el contenido de la pelicula buscada
                insertarInformacion.close()
                #Storage --------------------------------------------------
                success = xml.LoadXmlFile("Storage.xml")
                busqueda = xml.FirstChild()
                
                nombrePelicula = busqueda.getAttrValue("title")
                nombrePeliculaMOD = busqueda.getAttrValue("title")
                nombrePeliculaMOD = nombrePeliculaMOD.split()
                nombrePeliculaMOD = "_".join(nombrePeliculaMOD)
                duracionPelicula = busqueda.getAttrValue("runtime")
                generoPelicula = busqueda.getAttrValue("genre")
                directorPelicula = busqueda.getAttrValue("director")
                escritorPelicula = busqueda.getAttrValue("writer")
                actoresPelicula = busqueda.getAttrValue("actors")
                premioPelicula = busqueda.getAttrValue("awards") 
                lanzamientoPelicula = busqueda.getAttrValue("released")
                annoPelicula = busqueda.getAttrValue("year") 
                idiomasPelicula = busqueda.getAttrValue("language")
                metascorePelicula = busqueda.getAttrValue("metascore")
                imDBRatePelicula = busqueda.getAttrValue("imdbRating")
                sinopsisPelicula = busqueda.getAttrValue("plot")
                tipoPelicula = busqueda.getAttrValue("type")
                posterPelicula = busqueda.getAttrValue("poster")
                #------------------------------------------------------------

                indice = 0
                
                while indice < len(clasePelicula.listaPeliculas):
                    if nombrePelicula == clasePelicula.listaPeliculas[indice]:
                        os.remove("Storage.xml")
                        return messagebox.showinfo("Error!","La pelicula introducida ya ha sido buscada anteriormente!")
                    else:
                        indice += 1

                clasePelicula.listaPeliculas += [nombrePelicula]
                
                insertarInformacion = open("start.xml","a")

                puntajeUsuario = 0
                insertarInformacion.write("<Pelicula_"+nombrePeliculaMOD+">\n")
                insertarInformacion.write(" <title>"+nombrePelicula+"</title>")
                insertarInformacion.write(" <type>"+tipoPelicula+"</tipe>")
                insertarInformacion.write(" <runtime>"+duracionPelicula+"</runtime>")
                insertarInformacion.write(" <genre>"+generoPelicula+"</genre>")
                insertarInformacion.write(" <director>"+directorPelicula+"</director>")
                insertarInformacion.write(" <writer>"+escritorPelicula+"</writer>")
                insertarInformacion.write(" <actors>"+actoresPelicula+"</actors>")
                insertarInformacion.write(" <awards>"+premioPelicula+"</awards>")
                insertarInformacion.write(" <released>"+lanzamientoPelicula+"</released>")
                insertarInformacion.write(" <year>"+annoPelicula+"</year>")
                insertarInformacion.write(" <language>"+idiomasPelicula+"</language>")
                insertarInformacion.write(" <metascore>"+metascorePelicula+"</metascore>")
                insertarInformacion.write(" <imdbRating>"+imDBRatePelicula+"</imdbRating>")
                insertarInformacion.write(" <plot>"+sinopsisPelicula+"</plot>")
                insertarInformacion.write(" <poster>"+posterPelicula+"</poster>\n")
                insertarInformacion.write(" <puntajeUsuario>"+str(puntajeUsuario)+"</puntajeUsuario>\n")
                insertarInformacion.write("</Pelicula_"+nombrePeliculaMOD+">\n")

                insertarInformacion.close()
                os.remove("Storage.xml")
                insertarBotonEtiqueta(nombrePelicula,nombrePeliculaMOD)
                
        except:
            atributosPelicula.close()
            return messagebox.showinfo("Error!","Por favor, verifique su conexión a Internet!.")


def insertarBotonEtiqueta(nombrePelicula,nombrePeliculaMOD): 
    success = xml.LoadXmlFile("start.xml")
    
    xSearchRoot = xml.FindChild("Pelicula_"+nombrePeliculaMOD)
    xBeginAfter = xSearchRoot.GetSelf()

    if (success != True):
        print(xml.lastErrorText()) #En caso de que el archivo no exista
        sys.exit()
        
    else:
        xSearch = xSearchRoot.GetSelf()
        poster = xSearch.SearchForTag2(xBeginAfter,"poster")
        imagenPelicula = xSearch.content()
        if imagenPelicula == "N/A":                       #En caso de que la pelicula no tenga poster...
            poster = Image.open("images/noDisponiblethumbnail.jpg")#...se inserta la imagen predeterminada
            photo = ImageTk.PhotoImage(poster)

        else:
            descargarImagen = open("images/"+nombrePelicula+".jpg", "wb") #Descarga el poster de la pelicula buscada...
            descargarImagen.write(request.urlopen(imagenPelicula).read()) #...en la carpeta 'images'
            descargarImagen.close()

            #---Modifica las dimensiones de la imagen
            img = Image.open("images/"+nombrePelicula+".jpg")
            imagenMod = img.resize((260,352))
            imagenMod.save("images/"+nombrePelicula+".jpg")

            img = Image.open("images/"+nombrePelicula+".jpg")
            imagenMod = img.resize((150,150))
            imagenMod.save("images/"+nombrePelicula+"thumbnail.jpg")
            #--------
            
            #Añade el label y el botón en la pantaña de inicio
            poster = Image.open("images/"+nombrePelicula+"thumbnail.jpg")
            photo = ImageTk.PhotoImage(poster)

        coordenadaX = claseCoordenada.getCoordenadaX()+30
        claseCoordenada.getCoordenadaX()
        coordenadaY = claseCoordenada.getCoordenadaY()+30
        contador = claseCoordenada.getContador()
        
        
        #Botones de la pantalla de inicio
        botonPelicula = Button(frame,image = photo,command=lambda: parsearMostrarContenido(nombrePelicula,nombrePeliculaMOD))
        botonPelicula.poster = photo
        botonPelicula.grid(row=claseCoordenada.getCoordenadaY(),column=claseCoordenada.getCoordenadaX())
  
        etiqueta = Label(frame,text = nombrePelicula) 
        etiqueta.config(font=tipoLetra)
        etiqueta.grid(row=claseCoordenada.getCoordenadaY()-30,column=claseCoordenada.getCoordenadaX())

        if contador == 2:
            claseCoordenada.setCoordenadaY(coordenadaY+40) 
            claseCoordenada.setContador(0) 
            claseCoordenada.setCoordenadaX(70)

    
        else:
            claseCoordenada.setCoordenadaX(coordenadaX+360)
            claseCoordenada.setContador(contador+1)

            
        espaciador = Label(frame,text="                        ")
        espaciador.grid(row=4,column=4)
        #---------------------------

        #print (clasePelicula.getListaPeliculas())

    return cerrarVentana(ventanaBuscarPelicula)


def parsearMostrarContenido(nombrePelicula,nombrePeliculaMOD):
    success = xml.LoadXmlFile("start.xml")
    
    xSearchRoot = xml.FindChild("Pelicula_"+nombrePeliculaMOD)
    xBeginAfter = xSearchRoot.GetSelf()

    xSearch = xSearchRoot.GetSelf()
    types = xSearch.SearchForTag2(xBeginAfter,"title")
    nombrePelicula = xSearch.content()
    clasePelicula.setNombre(nombrePelicula)

    xSearch = xSearchRoot.GetSelf()
    types = xSearch.SearchForTag2(xBeginAfter,"type")
    tipoPelicula = xSearch.content()
    clasePelicula.setTipo(tipoPelicula)

    xSearch = xSearchRoot.GetSelf()
    runtime = xSearch.SearchForTag2(xBeginAfter,"runtime")
    duracionPelicula = xSearch.content()
    clasePelicula.setDuracion(duracionPelicula)

    xSearch = xSearchRoot.GetSelf()
    genre = xSearch.SearchForTag2(xBeginAfter,"genre")
    generoPelicula = xSearch.content()
    clasePelicula.setGenero(generoPelicula)

    xSearch = xSearchRoot.GetSelf()
    director = xSearch.SearchForTag2(xBeginAfter, "director")
    directorPelicula = xSearch.content()
    clasePelicula.setDirectores(directorPelicula)
    
    xSearch = xSearchRoot.GetSelf()
    writer = xSearch.SearchForTag2(xBeginAfter,"writer")
    escritorPelicula = xSearch.content()
    clasePelicula.setEscritores(escritorPelicula)

    xSearch = xSearchRoot.GetSelf()
    actors = xSearch.SearchForTag2(xBeginAfter,"actors")
    actoresPelicula = xSearch.content()
    clasePelicula.setActores(actoresPelicula)

    xSearch = xSearchRoot.GetSelf()
    awards = xSearch.SearchForTag2(xBeginAfter,"awards")
    premioPelicula = xSearch.content()
    clasePelicula.setPremios(premioPelicula)
    
    xSearch = xSearchRoot.GetSelf()
    released = xSearch.SearchForTag2(xBeginAfter,"released")
    lanzamientoPelicula = xSearch.content()
    clasePelicula.setFechaLanzamiento(lanzamientoPelicula)

    xSearch = xSearchRoot.GetSelf()
    year = xSearch.SearchForTag2(xBeginAfter,"year")
    annoPelicula = xSearch.content()
    clasePelicula.setAnno(annoPelicula)
    
    xSearch = xSearchRoot.GetSelf()
    language = xSearch.SearchForTag2(xBeginAfter,"language")
    idiomasPelicula = xSearch.content()
    clasePelicula.setIdiomas(idiomasPelicula)
    
    xSearch = xSearchRoot.GetSelf()
    metascore = xSearch.SearchForTag2(xBeginAfter,"metascore")
    metascorePelicula = xSearch.content()
    clasePelicula.setMetascore(metascorePelicula)

    xSearch = xSearchRoot.GetSelf()
    imdbRating = xSearch.SearchForTag2(xBeginAfter,"imdbRating")
    imDBRatePelicula = xSearch.content()
    clasePelicula.setImDBRate(imDBRatePelicula)

    xSearch = xSearchRoot.GetSelf()
    plot = xSearch.SearchForTag2(xBeginAfter,"plot")
    sinopsisPelicula = xSearch.content()
    clasePelicula.setSinopsis(sinopsisPelicula)

    xSearch = xSearchRoot.GetSelf()
    plot = xSearch.SearchForTag2(xBeginAfter,"poster")
    poster = xSearch.content()
    clasePelicula.setEnlaceImagen(poster)

    xSearch = xSearchRoot.GetSelf()
    puntajeUser = xSearch.SearchForTag2(xBeginAfter,"puntajeUsuario")
    puntajeUsuario = xSearch.content()
        
    def imprimirSinopsis(): #Sub-funcion para asignar las propiedades al Label 'Sinopsis'
        sinopsis = Label(informacionPelicula,text="Sinopsis:")
        sinopsis.config(font = tipoLetra)
        sinopsis.place(x=45,y=438)

    def imprimirNombre():
        nombre = Label(informacionPelicula,text=nombrePelicula)
        nombre.config(font = tipoLetra)
        nombre.place(x=45,y=25)


    informacionPelicula = Toplevel(proyecto)
    informacionPelicula.title("Información de la película")
    informacionPelicula.geometry("800x600")
    informacionPelicula.resizable(0,0)
#------------------------------------------------Compartir
    Button(informacionPelicula,text="  Compartir  ",command=lambda: abrirVentana(ventanaCompartir)).place(x=705,y=20)
    ventanaCompartir = Toplevel(proyecto)
    ventanaCompartir.title("Compartir película")
    ventanaCompartir.geometry("450x220")
    ventanaCompartir.resizable(0,0)
    ventanaCompartir.protocol("WM_DELETE_WINDOW", "onexit")
    ventanaCompartir.withdraw()

    Label(ventanaCompartir,text="Por favor, ingrese el correo al que desea compartir la película:").place(x=60,y=40)
    correoEntry = Entry(ventanaCompartir)
    correoEntry.place(x=65,y=80,width=315,height=30)

    Button(ventanaCompartir,text="   Enviar   ",command=lambda: enviarCorreo(correoEntry)).place(x=240,y=135)
    Button(ventanaCompartir,text="   Atras   ",command=lambda: cerrarVentana(ventanaCompartir)).place(x=130,y=135)
#------------------------------------------------
    Label(informacionPelicula,text=imprimirNombre()) #Nombre
    Label(informacionPelicula,text=imprimirSinopsis()) #Sinopsis
    Label(informacionPelicula,text="Tipo: "+tipoPelicula).place(x=335,y=52)
    Label(informacionPelicula,text="Duración: "+duracionPelicula).place(x=335,y=87)
    Label(informacionPelicula,text="Género: "+generoPelicula).place(x=335,y=122)
    Label(informacionPelicula,text="Director(es): "+directorPelicula).place(x=335,y=157)
    Label(informacionPelicula,text="Escritor(es): "+escritorPelicula).place(x=335,y=192)
    Label(informacionPelicula,text="Actor(es): "+actoresPelicula).place(x=335,y=227)
    Label(informacionPelicula,text="Premios: "+premioPelicula).place(x=335,y=262)
    Label(informacionPelicula,text="Fecha de lanzamiento: "+lanzamientoPelicula).place(x=520,y=52)
    Label(informacionPelicula,text="Año: "+annoPelicula).place(x=520,y=87)
    Label(informacionPelicula,text="Idioma(as): "+idiomasPelicula).place(x=520,y=122)

    labelframe = LabelFrame(informacionPelicula, text="Rates:")
    labelframe.place(x=335,y=315,width=390,height=100)
    Label(labelframe, text="Metascore: "+metascorePelicula).place(x=1,y=25)
    Label(labelframe, text="imDBRate: "+imDBRatePelicula).place(x=120,y=25)
    Label(labelframe, text="Mi rate: ").place(x=240,y=25)

    scrollbar = Scrollbar(informacionPelicula)
    scrollbar.place(x=745,y=465,height=120)
    
    textoSinopsis = Text(informacionPelicula,yscrollcommand = scrollbar.set)
    textoSinopsis.place(x=45,y=465,width=700,height=120) #Sinopsis
    textoSinopsis.insert("1.0",sinopsisPelicula)
    textoSinopsis.config(state="disable")

    scrollbar.config(command = textoSinopsis.yview)

        #Poster pelicula (Ventana-->> informacionPelicula)
    try:
        poster = Image.open("images/"+nombrePelicula+".jpg")
        photo = ImageTk.PhotoImage(poster)
        posterPelicula = Label(informacionPelicula,image = photo)
        posterPelicula.poster = photo
        posterPelicula.place(x=45,y=50,width=270,height=360)
    except:
        #En caso de no disponer del poster
        poster = Image.open("images/noDisponible.jpg")
        photo = ImageTk.PhotoImage(poster)
        posterPelucula = Label(informacionPelicula, image = photo)
        posterPelucula.poster = photo
        posterPelucula.place(x=45,y=50,width=270,height=360)

    checkCmd = IntVar()
    checkCmd.set(0)
    
    def peliculaFavoritos(): #Sub-función
        if checkCmd.get() != 0:
            agregarPelicula = open("Películas Favoritas.txt","a")
            agregarPelicula.write(nombrePelicula+"\n")
            agregarPelicula.close()
            checkCmd.set(1)
            messagebox.showinfo("¡Atención!","¡Se ha agregado la pelicula "+str(nombrePelicula)+" a las lista de favoritos en el directorio local!")
            
    agregarFavoritos = Checkbutton(informacionPelicula, variable=checkCmd, onvalue=1, offvalue=0, text="Agregar a favoritos",command=lambda:peliculaFavoritos()).place(x=192,y=415)

    rateUsuario = Entry(informacionPelicula,width=7)
    rateUsuario.place(x=630,y=355)
    salvarRate = Button(informacionPelicula,text="Salvar Rate",command=lambda:print(rateUsuario.get()))
    salvarRate.place(x=590,y=385)


def inicioXML(): #Función que inserta las películas anteriormente buscadas
    success = xml.LoadXmlFile("start.xml")
    hijosPelicula = (xml.get_NumChildren())
    print("Cantidad de películas almacenadas: " + str(xml.get_NumChildren()))

    contador = 0
    while contador < xml.get_NumChildren():
        pelicula = xml.getChildTagByIndex(contador)
        xSearchRoot = xml.FindChild(pelicula)
        xBeginAfter = xSearchRoot.GetSelf()

        xSearch = xSearchRoot.GetSelf()
        types = xSearch.SearchForTag2(xBeginAfter,"title")
        nombrePelicula = xSearch.content()
        nombrePeliculaMOD = nombrePelicula.split()
        nombrePeliculaMOD = "_".join(nombrePeliculaMOD)
        
        clasePelicula.listaPeliculas += [nombrePelicula]

        insertarBotonEtiqueta(nombrePelicula,nombrePeliculaMOD)

        #print(xml.getChildTagByIndex(contador))
        contador+=1



proyecto = Tk()
proyecto.title("Tarea Programada 3")
proyecto.geometry("800x600+270+50")
proyecto.resizable(0,0) #Evita expandir la ventana
tipoLetra = ('times', 15, 'bold')

canvas = Canvas(proyecto, borderwidth=0)
frame = Frame(canvas)
barraDesplazamiento = Scrollbar(proyecto, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=barraDesplazamiento.set)

barraDesplazamiento.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)
canvas.create_window((4,4), window=frame, anchor="nw")
barraDesplazamiento.config(command=canvas.yview)

frame.bind("<Configure>", lambda event, canvas=canvas: configurarFrame(canvas))

#-------------------------------------------------------------VENTANA: Buscar Pelicula
ventanaBuscarPelicula = Toplevel(proyecto)
ventanaBuscarPelicula.title("Buscar película")
ventanaBuscarPelicula.geometry("450x220+440+170")
ventanaBuscarPelicula.resizable(0,0)
ventanaBuscarPelicula.protocol("WM_DELETE_WINDOW", "onexit") #Impide cierrar la ventana por medio de la 'X'. Evitar errores para abrir de nuevo la ventana
ventanaBuscarPelicula.withdraw()

Label(ventanaBuscarPelicula,text="Por favor, ingrese el nombre de la película que desea buscar:").place(x=60,y=40)
cajaTexto = Entry(ventanaBuscarPelicula)
cajaTexto.grid()
cajaTexto.place(x=65,y=80,width=315,height=30)

Button(ventanaBuscarPelicula,text="   Buscar   ",command=lambda: buscarPelicula()).place(x=240,y=135)
Button(ventanaBuscarPelicula,text="   Atras   ",command=lambda: cerrarVentana(ventanaBuscarPelicula)).place(x=130,y=135)
#-------------------------------------------------------------VENTANA: Filtrar Pelicula
ventanaFiltrarPelicula = Toplevel(proyecto)
ventanaFiltrarPelicula.title("Filtrar películas")
ventanaFiltrarPelicula.geometry("450x230+440+170")
ventanaFiltrarPelicula.resizable(0,0)
ventanaFiltrarPelicula.protocol("WM_DELETE_WINDOW", "onexit")
ventanaFiltrarPelicula.withdraw()#Evita que la ventana se abra al iniciar el programa

Label(ventanaFiltrarPelicula,text="Por favor, marque la o las casillas para filtrar las películas:").place(x=75,y=36)
Button(ventanaFiltrarPelicula,text="   Filtrar   ",command=lambda: verificarChecks()).place(x=240,y=155)
Button(ventanaFiltrarPelicula,text="   Atras   ",command=lambda: cerrarVentana(ventanaFiltrarPelicula)).place(x=130,y=155)

checkNombre = IntVar()
checkNombre.set(0)

checkGenero = IntVar()
checkGenero.set(0)

checkActor = IntVar()
checkActor.set(0)

filtrarNombre = Checkbutton(ventanaFiltrarPelicula, variable=checkNombre, onvalue=1, offvalue=0,text="Nombre")
filtrarNombre.place(x=95,y=90)

filtrarGenero = Checkbutton(ventanaFiltrarPelicula, variable=checkGenero, onvalue=1, offvalue=0,text="Género")
filtrarGenero.place(x=195,y=90)

filtrarActor = Checkbutton(ventanaFiltrarPelicula, variable=checkActor, onvalue=1, offvalue=0,text="Actor")
filtrarActor.place(x=295,y=90)

def verificarChecks():
    if checkNombre.get() != 0:
        success = xml.LoadXmlFile("start.xml")
        hijosPelicula = (xml.get_NumChildren())
        #print("NumChildren = " + str(xml.get_NumChildren()))

        contador = 0
        while contador < xml.get_NumChildren():
            pelicula = xml.getChildTagByIndex(contador)
            xSearchRoot = xml.FindChild(pelicula)
            xBeginAfter = xSearchRoot.GetSelf()

            xSearch = xSearchRoot.GetSelf()
            types = xSearch.SearchForTag2(xBeginAfter,"title")
            nombrePelicula = xSearch.content()
            print (nombrePelicula)

            nombrePeliculaMOD = nombrePelicula.split()
            nombrePeliculaMOD = "_".join(nombrePeliculaMOD)

            insertarBotonEtiqueta(nombrePelicula,nombrePeliculaMOD)

            print(xml.getChildTagByIndex(contador))
            contador+=1
        messagebox.showinfo("¡Atención!","¡Nombre")
    if checkGenero.get() != 0:
        messagebox.showinfo("¡Atención!","¡Genero")
    if checkActor.get() != 0:
        messagebox.showinfo("¡Atención!","¡Actor")
            

#-------------------------------------------------------------Ventana de Inicio

menusBarra = Menu(proyecto) #Aquí van los submenús (Operaciones y Acerca de..)

menuOperaciones = Menu(menusBarra, tearoff = 0)
menusBarra.add_cascade(label="  Operaciones  ", menu = menuOperaciones)#Se añade a la barra del menú
menuOperaciones.add_command(label="Buscar película", command=lambda: abrirVentana(ventanaBuscarPelicula))
menuOperaciones.add_command(label="Filtrar lista de películas", command=lambda: abrirVentana(ventanaFiltrarPelicula))

acercaDeMenu = Menu(menusBarra, tearoff = 0)
menusBarra.add_cascade(label=" Acerca de..  ", menu = acercaDeMenu)#Se añade a la barra del menú
acercaDeMenu.add_command(label="Información", command = lambda: messagebox.showinfo("Acerca de..","Instituto Tecnológico de Costa Rica \nIngeniería en Computación \nIntroducción a la programación \n\nJosé Navarro Acuña \nJosúe Suárez Campos \n2016"))

comprobarExistencia(archivo)#Se necesita para crear el archivo 'start.xml' si es la primera vez que se ejecuta el programa
inicioXML()
proyecto.config(menu=menusBarra)

proyecto.mainloop()
