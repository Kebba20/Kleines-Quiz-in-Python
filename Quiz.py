from tkinter import *
from tkinter import messagebox
import vlc

import time


#A = vlc.MediaPlayer()
#A.play()


root = Tk()
root.title('Lernquiz')
root.geometry('1270x652+0+0')

root.config(bg = 'skyblue') 

img = PhotoImage(file = "C:\\Users\\moham\\OneDrive\\Desktop\\Zertifikate\\mainz.png")
label_img = Label(root, image = img)
label_img.place(x = 500 ,y = 80 )
img2 = PhotoImage(file = "C:\\Users\\moham\\OneDrive\\Desktop\\Zertifikate\\Ego.png")
img3 = PhotoImage(file = "C:\\Users\\moham\\OneDrive\\Desktop\\Zertifikate\\real.png")

E1 = Entry(root, width = 40)
E1.place(x = 500, y = 400)


count = 0


def function():
    Entry1 = E1.get()
    
    if Entry1 == "mainz 05":
        label_img.destroy()
        B1.destroy()
        E1.destroy()
        r = vlc.MediaPlayer("rantwort.mp3")
        r.play()
    

        
        #print("That's right!")
        

        
    else:
        label_img.destroy()
        E1.destroy()
        B1.destroy()
        w = vlc.MediaPlayer("fantwort.mp3")
        w.play()
            
        global count
        count += 1


    def function2():
        
        Button2.destroy()
        
        label_img2 = Label(root, image = img2)
        label_img2.place(x = 500 ,y = 80 )
        
        #B2 = Button(root, text = "okii", width = 5)
        #B2.place(x = 500, y = 450)        
    
        E2 = Entry(root, width = 40)
        E2.place(x = 500, y = 400)
        
    #Button2 = Button(text = 'next', command = function2)
    #Button2.place(x = 500, y = 470)
    
        def function3():
            Entry_2 = E2.get()
            
            if Entry_2 == "ego":
                
                label_img2.destroy()
                B2.destroy()
                E2.destroy()
                r = vlc.MediaPlayer("rantwort.mp3")
                r.play()
    
                
            else:
                label_img2.destroy()
                E2.destroy()
                B2.destroy()
                w = vlc.MediaPlayer("fantwort.mp3")
                w.play()
                
                global count
                count += 1
                
            def function4():
                
                Bttn.destroy()
                
                label_img3 = Label(root, image = img3)
                label_img3.place(x = 500 ,y = 80 )
                
                E3 = Entry(root, width = 40)
                E3.place(x = 500, y = 400)
                #Bton3 = Button(text ='alright', command = function5)
                #Bton3.place(x = 500, y = 450)
                
                def function5():
                    
                    Entry_3 = E3.get()
            
                    if Entry_3 == "real madrid":
                        #global count
                
                        label_img3.destroy()
                        Bton3.destroy()
                        E3.destroy()
                        r = vlc.MediaPlayer("rantwort.mp3")
                        r.play()
    

                    else:
                        label_img3.destroy()
                        E3.destroy()
                        Bton3.destroy()
                        w = vlc.MediaPlayer("fantwort.mp3")
                        w.play()
                        
                        global count
                        count += 1
                        
                        
                    def result():
                        global count
                        
                        L1.destroy()
                        bttn7.destroy()
                        
                        ergebnis = Label(root, text = 'Sie haben', font = ('Arial', 30))
                        ergebnis.place(x = 500, y = 400)
                        f = Label(text = count, font = ('Arial', 30))
                        f.place(x = 700, y = 400)
                        wrong = Label(text ='Fehler.', font = ('Arial', 30))
                        wrong.place(x = 750, y = 400)
                       
                    bttn7 = Button(text = 'Ergebnis anzeigen', command = result)
                    bttn7.place(x = 500, y = 450)
                    
                        
                        
                        
                        
                        
                        
                        
                        
                Bton3 = Button(text ='alright', command = function5)
                Bton3.place(x = 500, y = 450)
                    
                
                
                
            Bttn = Button(text = 'next1', command = function4)
            Bttn.place(x = 500, y = 450)
                
        B2 = Button(root, text = "okii", width = 5, command = function3)
        B2.place(x = 500, y = 450)
    Button2 = Button(text = 'next', command = function2)
    Button2.place(x = 500, y = 450)
                
        

        

        
        


        
L1 = Label(root, text = "Antwort: ", bg = "skyblue")
L1.place(x = 430, y = 400)

B1 = Button(root, text = "ok", width = 5,  command = function)
B1.place(x = 500, y = 450)





root.mainloop()