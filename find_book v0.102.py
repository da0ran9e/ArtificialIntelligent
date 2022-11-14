#app
"""

"""


import PySimpleGUI as sg
import PIL
from PIL import Image
import io
import base64
import random
import pandas as pd
import requests
from io import BytesIO
from urllib.request import urlopen

books = pd.read_csv('BX-Books.csv' , encoding='latin-1' , on_bad_lines='skip' , sep=';' , low_memory=False, escapechar='\\')
rating = pd.read_csv('BX-Book-Ratings.csv' , encoding='latin-1' , on_bad_lines='skip' , sep=';')
user = pd.read_csv('BX-Users.csv' , encoding='latin-1' ,  on_bad_lines='skip' , sep=';')

def main():

        # image = random_image()
        # size = (500,500)
        # image = convert_to_bytes(image, size, fill=False)

        infor_layout =  [
            # [sg.Button('+', size=(4,2)), sg.Button('-', size=(4,2)), sg.B('Next', size=(4,2)), sg.T(size, size=(10,1), k='-SIZE-')],
            # [sg.Button(image_data=image, key='-BUTTON IMAGE-')],
            [sg.Text("Information of the book:")],
            {sg.Text(size=(40, 1))}
        ]
        
        thumb_layout =  [
            [sg.Text("Pick a book to view the image")],
            [sg.Text(size=(40, 1), key="-TEXT-")],
            [sg.Image(key="-IMAGE-")],
        ]

        list_layout = [
            [sg.Text("User ID:")],
            [sg.Input(size=(25, 1), enable_events=True, key="-IN-"), sg.Button('Go')],
            [sg.Text("Information of the reader here:")],
            [sg.Text('Location: ')],
            [sg.Text(size= (25, 5), key="-UID-")],
            [sg.Listbox(values=[], enable_events=True, size=(40,20), key="-LIST-")],
            
        ]

        layout = [
            [
                sg.Column(list_layout),
                sg.VSeparator(),
                sg.Column(infor_layout),
                sg.VSeparator(),
                sg.Column(thumb_layout),
            ]
        ]

        window = sg.Window('Window Title', layout)
        #toolbar = make_toolbar()
        # u_loc = user.loc[user['User-ID'] == wd.values("-IN-"), 'Location'].values[0]

def run():
        while True:             # Event Loop
            event, values = window.read()
            if event in (sg.WIN_CLOSED, 'Exit'):
                break

            if event == 'Go':
                button_go()
        
        window.close()
    
def button_go():
        u_loc = user.loc[user['User-ID'] == values("-IN-"), 'Location'].values[0]
        window['-UID-'].update(u_loc)


        # event_window, event, values = sg.read_all_windows()
        # if event == sg.WIN_CLOSED or event == 'Exit':
        #     break
        # if event == '+':
        #     size = (size[0]+20, size[1]+20)
        # elif event == '-':
        #     if size[0] > 20:
        #         size = (size[0]-20, size[1]-20)
        # elif event in ('Next', '-BUTTON IMAGE-'):
        #     image = random.choice(img_list)
        # elif event_window == toolbar:
        #     image = event_window[event].ImageData

        # Resize image and update the window
        # image = convert_to_bytes(image, fill=True)
        # window['-IMAGE-'].update(data=image)
        # window['-BUTTON IMAGE-'].update(image_data=image)
        # window['-SIZE-'].update(size)