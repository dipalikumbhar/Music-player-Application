def unmutemusic():
    global currentvol
    root.BrowseUnMute.grid_remove()
    root.BrowseMute.grid()
    mixer.music.set_volume(currentvol)
def mutemusic():
    global currentvol

    root.BrowseMute.grid_remove()
    root.BrowseUnMute.grid()
    currentvol=mixer.music.get_volume()
    mixer.music.set_volume(0)
def volumeup():
    vol=mixer.music.get_volume()

    mixer.music.set_volume(vol + 0.05)
    ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    ProgressbarVolume['value']=mixer.music.get_volume()*100


def resumemusic():
    root.BrowseResume.grid_remove()
    root.BrowsePause.grid()
    mixer.music.unpause()
    AudioStatusLabel.configure(text="Playing.........")


def volumedown():
    vol = mixer.music.get_volume()
    mixer.music.set_volume(vol - 0.05)
    ProgressbarVolumeLabel.configure(text='{}%'.format(int(mixer.music.get_volume() * 100)))
    ProgressbarVolume['value'] = mixer.music.get_volume() * 100


def stopmusic():
    mixer.music.stop()
    AudioStatusLabel.configure(text="Stopped.........")
def pausemusic():
    mixer.music.pause()
    root.BrowsePause.grid_remove()
    root.BrowseResume.grid()
    AudioStatusLabel.configure(text="Paused.........")
def playmusic():
    ad=audiotrack.get()
    mixer.music.load(ad)
    ProgressbarLabel.grid()
    root.BrowseMute.grid()
    ProgressbarMusicLabel.grid()
    mixer.music.set_volume(0.4)
    ProgressbarVolume['value']=40
    ProgressbarVolumeLabel['text']='40%'
    mixer.music.play()
    AudioStatusLabel.configure(text="Playing.........")

    song=MP3(ad)
    totalsonglength=int(song.info.length)
    ProgressbarMusic['maximum']=totalsonglength
    ProgressbarMusicEndTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=totalsonglength))))
    def Progressbarmusictick():
        currentsonglength=mixer.music.get_pos()//1000
        ProgressbarMusic['value']=currentsonglength
        ProgressbarMusicStartTimeLabel.configure(text='{}'.format(str(datetime.timedelta(seconds=currentsonglength))))
        ProgressbarMusic.after(2,Progressbarmusictick)
    Progressbarmusictick()
def musicurl():
    try:

        dd=filedialog.askopenfilename(initialdir='',title='select audio file',

                                      filetype=(('MP3','*.mp3'),('WAV','*.wav')))
    except:
        dd = filedialog.askopenfilename(title='select audio file',filetype=(('MP3','*.mp3'),('WAV','*.wav')))


    audiotrack.set(dd)







def createwidthes():
    global imbrowsing,immute,ProgressbarMusicLabel,ProgressbarLabel,ProgressbarVolume,ProgressbarVolumeLabel,imunmute,impasue,imresume,imvloumeup,imvloumedown,implay,imstop
    global AudioStatusLabel,ProgressbarMusicStartTimeLabel,ProgressbarMusic,ProgressbarMusic,ProgressbarMusicEndTimeLabel
    #######Images Register##########
    imbrowsing = PhotoImage(file='browsing.png')
    implay=PhotoImage(file='play-button.png')
    impasue = PhotoImage(file='pause (3).png')
    imresume = PhotoImage(file="play-button.png")
    imvloumeup = PhotoImage(file='volume-up.png')
    imstop=PhotoImage(file='stop.png')
    immute = PhotoImage(file='mute.png')
    imunmute = PhotoImage(file='volume.png')
    imvloumedown = PhotoImage(file='volume-down.png')



    ############change size of images###########
    imbrowsing=imbrowsing.subsample(15,15)
    implay = implay.subsample(15,15)
    impasue = impasue.subsample(15,15)
    imresume = imresume.subsample(15, 15)
    imvloumeup = imvloumeup.subsample(15,15)
    imstop=imstop.subsample(15,15)
    immute = immute.subsample(15, 15)
    imunmute = imunmute.subsample(15, 15)
    imvloumedown = imvloumedown.subsample(15,15)





    #######labels#######
    TrackLabel=Label(root,text="Select Audio Track:",bg='lightskyblue',font=('arial',15,'italic bold'))
    TrackLabel.grid(row=0,column=0,padx=20,pady=20)

    AudioStatusLabel = Label(root, text="paused", bg='lightskyblue', font=('arial', 15, 'italic bold'),width=20)

    AudioStatusLabel.grid(row=2, column=1, padx=20, pady=20)
    ##### Entry Box#####
    TrackLabelEntry=Entry(root,font=('arial',15,'italic bold'),width=35,textvariable=audiotrack)
    TrackLabelEntry.grid(row=0,column=1,padx=20,pady=20)
    ######Button#######
    BrowseButton=Button(root,text='Search',bg='deeppink',font=('arial',13,'italic bold'),width=200,bd=5,
                        activebackground='purple4',image=imbrowsing,compound=RIGHT,command=musicurl)
    BrowseButton.grid(row=0,column=2,padx=20,pady=20)

    BrowsePlay = Button(root, text='Play', bg='green2', font=('arial', 13, 'italic bold'), width=200, bd=5,
                        activebackground='purple4',image=implay,compound=RIGHT,command=playmusic)
    BrowsePlay.grid(row=1, column=0, padx=20, pady=20)

    root.BrowsePause = Button(root, text='Pause', bg='yellow', font=('arial', 13, 'italic bold'), width=200, bd=5,
                         activebackground='purple4',image=impasue,compound=RIGHT,command=pausemusic)
    root.BrowsePause.grid(row=1, column=1, padx=20, pady=20)

    root.BrowseResume = Button(root, text='Resume', bg='yellow', font=('arial', 13, 'italic bold'), width=200, bd=5,
                         activebackground='purple4', image=imresume, compound=RIGHT,command=resumemusic)
    root.BrowseResume.grid(row=1, column=1, padx=20, pady=20)
    root.BrowseResume.grid_remove()

    root.BrowseMute=Button(root,text='Mute',width=100,bg='yellow',activebackground='purple4',bd=5,image=immute,compound=RIGHT,command=mutemusic)
    root.BrowseMute.grid(row=3,column=3)
    root.BrowseMute.grid_remove()

    root.BrowseUnMute = Button(root, text='UnMute', width=100, bg='yellow', activebackground='purple4', bd=5, image=imunmute,
                             compound=RIGHT,command=unmutemusic)
    root.BrowseUnMute.grid(row=3, column=3)


    BrowseVolumeUp = Button(root, text='VolumeUp', bg='blue', font=('arial', 13, 'italic bold'), width=200, bd=5,
                            activebackground='purple4',image=imvloumeup,compound=RIGHT,command=volumeup)
    BrowseVolumeUp.grid(row=1, column=2, padx=20, pady=20)

    BrowseStop = Button(root, text='Stop', bg='red', font=('arial', 13, 'italic bold'), width=200, bd=5,
                        activebackground='purple4',image=imstop,compound=RIGHT,command=stopmusic)
    BrowseStop.grid(row=2, column=0, padx=20, pady=20)

    BrowseVolumeDown = Button(root, text='VolumeDown', bg='blue', font=('arial', 13, 'italic bold'), width=200, bd=5,
                              activebackground='purple4',image=imvloumedown,compound=RIGHT,command=volumedown)
    BrowseVolumeDown.grid(row=2, column=2, padx=20, pady=20)

    ##################3progressbar valume######################3333333
    ProgressbarLabel=Label(root,text='',bg='red')
    ProgressbarLabel.grid(row=0,column=3,rowspan=3,padx=20,pady=20)
    ProgressbarLabel.grid_remove()

    ProgressbarVolume=Progressbar(ProgressbarLabel,orient=VERTICAL,mode='determinate'
                                  ,value=0,length=190)
    ProgressbarVolume.grid(row=0,column=0,ipadx=5)

    ############################
    ProgressbarVolumeLabel=Label(ProgressbarLabel,text='0%',bg='lightgray',width=3)
    ProgressbarVolumeLabel.grid(row=0,column=0)

    ##########################Progressbarmusic################################
    ProgressbarMusicLabel=Label(root,text='',bg='red')
    ProgressbarMusicLabel.grid(row=3,column=0,columnspan=3,padx=20,pady=20)
    ProgressbarMusicLabel.grid_remove()
    ProgressbarMusicStartTimeLabel = Label(ProgressbarMusicLabel, text='0:00:0', bg='red',width=6)
    ProgressbarMusicStartTimeLabel.grid(row=0,column=0)

    ProgressbarMusic=Progressbar(ProgressbarMusicLabel,orient=HORIZONTAL,
                                 mode='determinate',value=0)
    ProgressbarMusic.grid(row=0,column=1,ipadx=370,ipady=3)


    ProgressbarMusicEndTimeLabel = Label(ProgressbarMusicLabel, text='0:00:0', bg='red')
    ProgressbarMusicEndTimeLabel.grid(row=0,column=2)

from tkinter import *
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
import datetime
from mutagen.mp3 import MP3
root=Tk()
root.geometry('1100x500+200+50')  #x mean multiplication 200 is width 500 from height which display screen that perticular location of screen x=1100 y=500
root.title("Simple Music Player...")
root.iconbitmap('music.ico')#this image only in the format of ico
root.resizable(False,False)# stop increasing size of window
root.configure(bg='lightskyblue')# confiure means modify
################global varaible###############
audiotrack=StringVar()
currentvol=0
totalsonglength=0
count=0
text=''
##################### create silder#######################
ss='Music Player.....'

sliderlabel=Label(root,text='',bg='lightskyblue',fg='black',font=('arial',40,'italic bold'))
sliderlabel.grid(row=4,column=0,padx=20,pady=20,columnspan=3)
def IntroLabelTrick():
    global count,text
    if(count>=len(ss)):
        count=-1
        text=""
        sliderlabel.configure(text=text)
    else:
        text=text+ss[count]
        sliderlabel.configure(text=text)
    count+=1
    sliderlabel.after(200,IntroLabelTrick)
IntroLabelTrick()
mixer.init()
createwidthes()

root.mainloop()
