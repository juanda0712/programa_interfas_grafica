#LIBRARIES#
import tkinter as tk
from tkinter import messagebox
from winsound import *



#Fibonacci Funtion#
def fibonacci():
     #win settings
     secwin=tk.Toplevel()
     secwin.geometry("275x300")
     secwin.resizable(False,False)
     secwin.config(bg="#424242")
     
     #Labels creation
     label_title = tk.Label(secwin, text="Fibonacci",font=("Comic Sans",14),bg="#424242",             #title
     fg="#B4B4B4") 
     label_title.pack()
     label_title.place(x=90,y=13)

     label_entry= tk.Label(secwin,text="Ingresar Numero:",font=("Comic Sans",12),bg="#424242",   #entry
     fg="#B4B4B4")
     label_entry.pack()
     label_entry.place(x=3,y=56)

     tail_recursive= tk.Label(secwin,text="Recursividad de cola:",font=("Comic Sans",12),bg="#424242", #tail
     fg="#B4B4B4")
     tail_recursive.pack()
     tail_recursive.place(x=3,y=120)

     pile_recursive= tk.Label(secwin,text="Recursividad de pila:",font=("Comic Sans",12),bg="#424242", #pile
     fg="#B4B4B4")
     pile_recursive.pack()
     pile_recursive.place(x=3,y=160)

     time = tk.Label(secwin,text="Duración:",font=("Comic Sans",12),bg="#424242",fg="#B4B4B4")    #time
     time.pack()
     time.place(x=3,y=200)

     #entry#
     entry = tk.Entry(secwin,bg="#696969",font=("Comic Sans",12),fg="white")
     entry.pack()
     entry.place(x=125,y=60)

     finalResult=tk.StringVar()
     result=tk.Entry(secwin,bg="#424242",font=("Comic Sans",12),fg="white",textvariable=finalResult,relief="flat")
     result.pack()
     result.place(x=125,y=90)

     #buttons#
     cancelButton = tk.Button(secwin,text="Cancelar",bg="#696969",fg="#D1CFCF",font=("Comic Sans",11),
     cursor="hand2",activebackground="#696969",activeforeground="white",command=secwin.destroy)
     cancelButton.pack()
     cancelButton.place(x=195,y=265)
     
     acceptButton= tk.Button(secwin,text="Aceptar",bg="#696969",fg="#D1CFCF",font=("Comic Sans",11),
     cursor="hand2",activebackground="#696969",activeforeground="white",command=lambda:fib(int(entry.get())))
     acceptButton.pack()
     acceptButton.place(x=120,y=265)
     
     #pile recursive funtion#
     def fib(num):
          if isinstance(num,int) and num >0:
               finalResult.set(fib_aux(num))
          else:
               finalResult.set("Numero invalido")
     def fib_aux(num):
          if num == 0:
               return 0
          elif num ==1:
               return 1
          else:
               return fib_aux(num-1)+ fib_aux(num-2)


#MAIN FUNCTION#
def main():
     #Window settings
     window = tk.Tk()
     window.title("Interfas grafica")
     window.geometry("800x580")
     window.resizable(False,False)
     window.iconbitmap('./images/0x.ico')

     #Canvas creation
     information_canvas = tk.Canvas(window,height=580,width=400,bg="#424242")
     information_canvas.place(x=0,y=0)

     fibonacci_canvas = tk.Canvas(information_canvas,height=60,width=120,bg="#696969")
     fibonacci_canvas.place(x=0,y=0)

     animation_canvas = tk.Canvas(window,height=580,width=400,bg="#696969")
     animation_canvas.place(x=400,y=0)
     

     #Button creation
     button = tk.Button(fibonacci_canvas,text="Fibonacci",activebackground="#696969",
                        activeforeground="white",font=("Comic Sans",14),bg="#424242",fg="#B4B4B4",cursor="hand2",
                        command=fibonacci)
     button.place(x=9,y=9)




     #Personal Information#

     #play function#
     def play_ledzepplin():   #sound function
          return PlaySound(r'.\music\sound.wav',SND_ASYNC)

     playButton = tk.Button(information_canvas,text="Play",activebackground="#696969",   #Button play
     activeforeground="white",font=("Comic Sans",14),bg="#424242",fg="#B4B4B4",cursor="hand2",
     command=play_ledzepplin,relief="flat")
     playButton.place(x=255,y=475)

     #Photographys#
     facePhoto = tk.PhotoImage(file = "./images/photo.png")   #myphoto
     mapPhoto = tk.PhotoImage(file = "./images/mapa.png") #map
     albumPhoto = tk.PhotoImage(file = "./images/Led Zeppelin.png") #album
     
     #Labels#
     photoLabel = tk.Label(information_canvas,image=facePhoto) #personal photo label
     photoLabel.pack()
     photoLabel.place(x=270,y=6)

     mapLabel = tk.Label(information_canvas,image=mapPhoto) #map label
     mapLabel.pack()
     mapLabel.place(x=10,y=265)

     albumLabel = tk.Label(information_canvas,image=albumPhoto) #album label
     albumLabel.pack()
     albumLabel.place(x=10,y=385)

     nameLabel = tk.Label(information_canvas,text="Juan Daniel Rodríguez Montero",  #name
     bg="#424242",font=("Comic Sans",12),fg="white")
     nameLabel.pack()
     nameLabel.place(x=10,y=80)

     idLabel = tk.Label(information_canvas,text="2020426163",  #ID
     bg="#424242",font=("Comic Sans",12),fg="white")
     idLabel.pack()
     idLabel.place(x=10,y=115)

     genderLabel = tk.Label(information_canvas,text="Masculino",  #Gender
     bg="#424242",font=("Comic Sans",12),fg="white")
     genderLabel.pack()
     genderLabel.place(x=10,y=155)

     ageLabel = tk.Label(information_canvas,text="20 años",  #Age
     bg="#424242",font=("Comic Sans",12),fg="white")
     ageLabel.pack()
     ageLabel.place(x=10,y=195)

     addressLabel = tk.Label(information_canvas,text="Quebradilla, Cartago, Costa Rica",  #address
     bg="#424242",font=("Comic Sans",12),fg="white")
     addressLabel.pack()
     addressLabel.place(x=10,y=235)

     drescription1 = tk.Label(information_canvas,text="-Es un lugar muy tranquilo",  #description 1
     bg="#424242",font=("Comic Sans",12),fg="white")
     drescription1.pack()
     drescription1.place(x=200,y=270)

     drescription2 = tk.Label(information_canvas,text="-Tiene mucha naturaleza",  #description 2
     bg="#424242",font=("Comic Sans",12),fg="white")
     drescription2.pack()
     drescription2.place(x=200,y=310)

     drescription3 = tk.Label(information_canvas,text="-La gente es muy amable",  #description 3
     bg="#424242",font=("Comic Sans",12),fg="white")
     drescription3.pack()
     drescription3.place(x=200,y=350)

     musicalGroup = tk.Label(information_canvas,text="Led Zeppelin",  #musical group 
     bg="#424242",font=("Comic Sans",16),fg="#B80606")
     musicalGroup.pack()
     musicalGroup.place(x=220,y=400)

     musicalGenre = tk.Label(information_canvas,text="Hard Rock",  #musical genre
     bg="#424242",font=("Comic Sans",12),fg="white")
     musicalGenre.pack()
     musicalGenre.place(x=245,y=440)
     

     #Infinite loop#
     window.mainloop()

     
# EXECUTE THE MAIN #
main()

     
