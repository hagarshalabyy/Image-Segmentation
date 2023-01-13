import PySimpleGUI as sg
import os
import io
from predict import predict
from PIL import Image

layout = [
    [sg.Text("Choose your image, supported files are PNG and GIF"), sg.Input(),sg.FileBrowse(key="-file-")],
    [sg.Button("Submit"),sg.Button("Detect Lane")],
    [sg.Text(key="-text-")],
    [sg.Image(key="-image-")]
]
window = sg.Window("Lane Detection Final Project", layout, margins=(200, 200))

while True:
    event, values = window.read()
    
    if event == "Exit":
        break
    
    if event == "Submit":
        print(values)
        if os.path.exists(values["-file-"]):
            image = values["-file-"]
            window["-image-"].update(image)
    
    if event == "Detect Lane":
        print(values)
        window["-text-"].update(predict(values["-file-"]))

window.close()
                                         