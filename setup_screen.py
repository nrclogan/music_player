
# Import module
import tkinter
from tkinter import *
import os
import time
from PIL import Image, ImageTk
from pygame import mixer
import tkinter.messagebox
from tkinter import filedialog
from mutagen.mp3 import MP3

mixer.init()


def main():

    root = Tk()
    root.geometry("400x400")
    root.configure(background='white')
#    menu
    # root.menubar=Menu(root)
    # root.configure(menu=root.menubar)
    # root.submenu=Menu(root.menubar,tearoff=0)
    # root.menubar.add_cascade(label='file',menu=root.submenu)
    # root.menubar.add_command(label='open')
    # root.submenu2=Menu(root.menubar,tearoff=0)
    # root.menubar.add_cascade(label='Edit',menu=root.submenu)
    # root.menubar2.add_command(label='cut')

    def openfile():
        global filename
        filename = filedialog.askopenfilename()
    menubar = Menu(root)
    root.config(menu=menubar)
    file = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='File', menu=file)
    file.add_command(label='New File', command=None)
    file.add_command(label='Open...', command=openfile)
    file.add_command(label='Save', command=None)
    file.add_separator()
    file.add_command(label='Exit', command=root.destroy)
    # def edit():
    # tkinter.messagebox.showinfo('About us','Music player created by Kajal')
    edit = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Edit', menu=edit)
    edit.add_command(label='Cut', command=None)
    edit.add_command(label='Copy', command=None)
    edit.add_command(label='Paste', command=None)
    edit.add_command(label='Select All', command=None)
    edit.add_separator()
    edit.add_command(label='Find...', command=None)
    edit.add_command(label='Find again', command=None)
    root.config(menu=menubar)


# file
    root.filelabel = Label(text='Lets Begin The Music',
                           bg='black', fg='white', font=32)
    root.filelabel.place(x=0, y=30)

    def songinfo():
        root.filelabel['text'] = 'current music:-'+os.path.basename(filename)
    root.L_photo = ImageTk.PhotoImage(file='m1.jpg')
    L_photo = Label(root, image=root.L_photo).place(x=1100, y=15, height=550)
    # L_photo=Label(root,image=root.L_photo).place(x=5,y=60)
    root.photo = ImageTk.PhotoImage(file='music1.jpg')
    Photo = Label(root, image=root.photo, bg='white').place(
        x=0, y=60, height=400,width=1100)

    # label
    root.label1 = Label(root, text='Lets play it',
                        bg='black', fg='Red', font=32)
    root.label1.pack(side=BOTTOM, fill=X)
    # function

    # def playmusic():
        # try:
        #     paused
            
        # except NameError:

        #     try:

        #         mixer.music.load(filename)
        #         mixer.music.play()
        #         root.label1['text'] = 'Music_playing....'
        #         songinfo()
        #         length_bar()
        #     except:

        #         tkinter.messagebox.showerror( 'error', 'File could not found,Please Try Agin....')
        #         pass
        #     else:
        #         mixer.music.unpause()

        #     root.label1['text'] = 'Music_unpaused....'

    def length_bar():
                song_mut = MP3(filename)
                song_mut_length = song_mut.info.length
                convert_song_mut_length=time.strftime('%M:%S',time.gmtime(song_mut_length))
                print(song_mut_length)
                root.length_bar.config(text='Total_Length:-00:{convert_song_mut_length}')

                root.lengthbar = Label(
                root, text='Total_Length:-00:00', bg='black', fg='white', font=20)
                root.lengthbar.place(x=220, y=550)
    
    def playmusic():
        try:
            paused
            
        except NameError:

            try:

                mixer.music.load(filename)
                mixer.music.play()
                root.label1['text'] = 'Music_playing....'
                songinfo()
                length_bar()
            except:
            #   tkinter.messagebox.showerror( 'error', 'File could not found,Please Try Agin....')
               pass 
            else:
                mixer.music.unpause()

            root.label1['text'] = 'Music_unpaused....'

    # button
     # Creating Button Frame
    #  play button
    root.photo_B1 = ImageTk.PhotoImage(file='B1.jpg')
    photo_B1 = Button(root, image=root. photo_B1, bd=0, bg='white',
                      command=playmusic).place(x=75, y=550, height=150, width=150)

    def pausemusic():
        global paused
        paused = True
        mixer.music.pause()
        root.label1['text'] = 'Music_pasued....'

# pasue button
    root.photo_B2 = ImageTk.PhotoImage(file='B2.jpg')
    photo_B2 = Button(root, image=root. photo_B2, bd=0, bg='white',
                      command=pausemusic).place(x=300, y=550, height=150, width=150)

    def stopmusic():
        mixer.music.stop()
        root.label1['text'] = 'Music_stopped....'
#    stop button

    root.photo_B3 = ImageTk.PhotoImage(file='B3.jpg')
    photo_B3 = Button(root, image=root. photo_B3, bd=0, bg='white',
                      command=stopmusic).place(x=520, y=550, height=150, width=150)
    
    
    # def mute():
    # #     print('mute called')
    #  root.scale.set(0)
    # root.mute=ImageTk.PhotoImage(file='V1.jpg')
    # mute=Button(root,image=root.mute,command=unmute).place(x=750, y=550)
   
    # def unmute():
    #    root.scale.set(0)
    #    root.mute=ImageTk.PhotoImage(file='umnute.jpg')
    # mute=Button(root,image=root.unmute,command=mute).place(x=750, y=550)

# command=mute

    # volume img
    root.volimg = ImageTk.PhotoImage(file='V1.jpg')
    volimg = Button(root, image=root.volimg, bg='white', bd=0).place(x=900, y=650)


    # volumebar
    def volume(vol):
        volume = int (vol)/100
        mixer.music.set_volume(volume)
    
    # volumebar
    root.scale = Scale(root, from_=0, to=100, orient=HORIZONTAL,
                       bg='cyan', length=120, command=volume).place(x=950, y=650)
    

    #     mute();
    
# menubar

    root.mainloop()


main()

