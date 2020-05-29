#LIBRARIES#
import tkinter as tk
from winsound import *
from threading import Thread
import time
import random
from timeit import default_timer



#Fibonacci Funtion#
def fibonacci():
     #win settings
     secwin=tk.Toplevel()
     secwin.geometry("300x365")
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

     tail_recursive= tk.Label(secwin,text="Cola:",font=("Comic Sans",12),bg="#424242", #tail
     fg="#B4B4B4")
     tail_recursive.pack()
     tail_recursive.place(x=3,y=110)

     pile_recursive= tk.Label(secwin,text="Pila:",font=("Comic Sans",12),bg="#424242", #pile
     fg="#B4B4B4")
     pile_recursive.pack()
     pile_recursive.place(x=3,y=195)

     timePile = tk.Label(secwin,text="Duración:",font=("Comic Sans",12),bg="#424242",fg="#B4B4B4")    #Pile time
     timePile.pack()
     timePile.place(x=3,y=220)

     timeTail = tk.Label(secwin,text="Duración:",font=("Comic Sans",12),bg="#424242",fg="#B4B4B4")    #Tail time
     timeTail.pack()
     timeTail.place(x=3,y=135)

     loopPile = tk.Label(secwin,text="Vueltas:",font=("Comic Sans",12),bg="#424242",fg="#B4B4B4")    #Pile loop
     loopPile.pack()
     loopPile.place(x=3,y=245)

     loopTail = tk.Label(secwin,text="Vueltas:",font=("Comic Sans",12),bg="#424242",fg="#B4B4B4")    #Tail loop
     loopTail.pack()
     loopTail.place(x=3,y=161)

     #entry#
     entry = tk.Entry(secwin,bg="#696969",font=("Comic Sans",12),fg="white")   #Entry number
     entry.pack()
     entry.place(x=125,y=60)

     finalResultPile=tk.StringVar()  
     pileResult=tk.Entry(secwin,bg="#424242",font=("Comic Sans",12),fg="white",textvariable=finalResultPile,relief="flat")   #Pile result
     pileResult.pack()
     pileResult.place(x=50,y=195)

     finalResultTail=tk.StringVar()
     tailResult=tk.Entry(secwin,bg="#424242",font=("Comic Sans",12),fg="white",textvariable=finalResultTail,relief="flat")  #Tail result
     tailResult.pack()
     tailResult.place(x=50,y=110)

     resultTimePile=tk.StringVar()
     pileTime=tk.Entry(secwin,bg="#424242",font=("Comic Sans",12),fg="white",textvariable=resultTimePile,relief="flat")  #Pile time
     pileTime.pack()
     pileTime.place(x=75,y=220)

     resultTimeTail=tk.StringVar()
     tailTime=tk.Entry(secwin,bg="#424242",font=("Comic Sans",12),fg="white",textvariable=resultTimeTail,relief="flat")  #Tail time
     tailTime.pack()
     tailTime.place(x=75,y=135)

     resultLootPile=tk.StringVar()
     lootPile=tk.Entry(secwin,bg="#424242",font=("Comic Sans",12),fg="white",textvariable=resultLootPile,relief="flat")  #Pile recursions
     lootPile.pack()
     lootPile.place(x=65,y=245)

     resultLootTail=tk.StringVar()
     tailResult=tk.Entry(secwin,bg="#424242",font=("Comic Sans",12),fg="white",textvariable=resultLootTail,relief="flat")  #Tail recursions
     tailResult.pack()
     tailResult.place(x=65,y=161)

     #buttons#
     cancelButton = tk.Button(secwin,text="Cancelar",bg="#696969",fg="#D1CFCF",font=("Comic Sans",11),   #cancel button
     cursor="hand2",activebackground="#696969",activeforeground="white",command=secwin.destroy)
     cancelButton.pack()
     cancelButton.place(x=210,y=320)
     
     acceptButton= tk.Button(secwin,text="Aceptar",bg="#696969",fg="#D1CFCF",font=("Comic Sans",11),    #Accept button
     cursor="hand2",activebackground="#696969",activeforeground="white",command=lambda:fib(int(entry.get())))
     acceptButton.pack()
     acceptButton.place(x=135,y=320)
     
     #pile recursive funtion | timer | number of recursions 
     def fib(num): #principal function
          start = default_timer()
          fib2(num)
          if isinstance(num,int) and num >0:
               finalResultPile.set(fib_aux(num,0,start))
          else:
               finalResultPile.set("Numero invalido")
     def fib_aux(num,veces,start): #Auxiliary function
          if num == 0:  #base case
               end = default_timer()
               resultTimePile.set(end-start)
               resultLootPile.set(veces)
               return 0
          elif num ==1:
               return 1
          else:
               veces = veces + 1
               return fib_aux(num-1,veces,start)+ fib_aux(num-2,veces,start)

     #Tail resursive function | timer | number of recursions 
     def fib2(num): #principal function
          start = default_timer()
          if isinstance(num,int) and num > 0:
               return finalResultTail.set(fib2_aux(num,0,1,0,0,start))
          else:
               return -1    
     def fib2_aux(num,count,n1,n2,veces,start):
          if count == num: #base case
               end = default_timer()
               resultTimeTail.set(end - start)
               resultLootTail.set(veces)
               return n2
          else:
               veces = veces+1
               return fib2_aux(num,count+1,n2,n1+n2,veces,start)

         
#Animation#
#Ball#
class Balls:
     
    def __init__(self, canvas):                #Constructor __init__
        self.canvas = canvas
        self.x = random.randint(10, 300)
        self.y = 0
        self.r = 5
        self.speed = 4
        self.falling = True
        self.top_y = 25
        self.oval = canvas.create_oval(self.x, self.y, self.x + 30, 30, fill="white",outline="red")  #create oval

    #move funcion#
    def move(self):               
        while self.x < 600:
            if self.y >= 575 - self.r*2 and self.falling:       
                self.falling = False

            if self.falling:                                   
                self.y += self.r
                self.canvas.move(self.oval, 3, 8)
            else:
                self.y -= self.r
                self.canvas.move(self.oval, 3, -8)
                
            self.x += self.speed                       

            time.sleep(0.05)

#Square#
class Squares:
    def __init__(self, canvas):                #Constructor __init__
        self.canvas = canvas
        self.x = random.randint(0, 300)
        self.y = 600
        self.r = 5
        self.speed = 3
        self.falling = False
        self.top_y = 25
        self.oval = canvas.create_rectangle(self.x,self.y,self.x+35,self.y+35, fill="black",outline="white") #create square
        
    #move function
    def move(self):                                             
        while self.x < 600:
            if self.y >= 575 - self.r*2 and self.falling:       
                self.falling = False

            if self.falling:                                   
                self.y += self.r
                self.canvas.move(self.oval, 3, 8)
            else:
                self.y -= self.r
                self.canvas.move(self.oval, 3, -8)
                
            self.x += self.speed                              

            time.sleep(0.05)


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



     #animation function#
     def create_circle():
        circle = Balls(animation_canvas)
        circle_thread = Thread(target=circle.move)
        circle_thread.daemon = True
        circle_thread.start()

     def create_squares():
        square = Squares(animation_canvas)
        square_thread = Thread(target=square.move)
        square_thread.daemon = True
        square_thread.start()

     #animation buttons#
     button_animation = tk.Button(animation_canvas,cursor="hand2", text="Circles", font=("Comic Sans",16), bg="#991010", command=create_circle,fg="white")
     button_animation.place(x=10,y=10)

     button_animation = tk.Button(animation_canvas,cursor="hand2", text="Squares", font=("Comic Sans",16), bg="#991010", command=create_squares,fg="white")
     button_animation.place(x=10,y=530)

     #Infinite loop#
     window.mainloop()

     
# EXECUTE THE MAIN #
main()

     
