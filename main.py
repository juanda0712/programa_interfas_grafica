#LIBRARIES#
import tkinter as tk

#MAIN FUNCTION#
def main():
     #Window settings
     window = tk.Tk()
     window.title("Interfas grafica")
     window.geometry("800x580")
     window.resizable(False,False)
     window.iconbitmap('0x.ico')

     #Canvas creation
     left_canvas = tk.Canvas(window,height=580,width=400,bg="#424242")
     left_canvas.place(x=0,y=0)

     right_canvas = tk.Canvas(window,height=580,width=400,bg="#696969")
     right_canvas.place(x=400,y=0)
     

     #Button creation
     button = tk.Button(left_canvas,text="Fibonnaci",activebackground="#696969",
                        activeforeground="white",font=("Comic Sans",14),bg="#424242",fg="#B4B4B4",cursor="hand2")
     button.place(x=9,y=9)

     #Infinite loop#
     window.mainloop()

     
# EXECUTE THE MAIN #
main()

     
