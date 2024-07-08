from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from data import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\dell\Tkinter-Designer-master\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Agamine")

window.geometry("1000x550")
window.configure(bg = "#000000")


canvas = Canvas(
    window,
    bg = "#000000",
    height = 550,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    171.0,
    46.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    169.0,
    153.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    169.0,
    375.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    500.0,
    375.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    831.0,
    375.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    500.0,
    153.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    831.0,
    152.0,
    image=image_image_7
)

canvas.create_text(
    87.0,
    124.0,
    anchor="nw",
    text="Tension \nélectrique",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    435.0,
    124.0,
    anchor="nw",
    text="Consommation \nd'énergie",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    760.0,
    124.0,
    anchor="nw",
    text="état du module \nsolaire",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    62.0,
    152.0,
    image=image_image_8
)

image_image_9 = PhotoImage(
    file=relative_to_assets("image_9.png"))
image_9 = canvas.create_image(
    402.0,
    152.0,
    image=image_image_9
)

image_image_10 = PhotoImage(
    file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(
    726.0,
    151.0,
    image=image_image_10
)

image_image_11 = PhotoImage(
    file=relative_to_assets("image_11.png"))
image_11 = canvas.create_image(
    499.0,
    82.0,
    image=image_image_11
)

revenue_data = pd.DataFrame(revenue)
revenue_data["date"] = pd.to_datetime(revenue_data['date'])

fig_1 = Figure(figsize=(2.5, 2.2), facecolor='#E9E8E8')
ax_1 = fig_1.add_subplot()
# BackGround Color
ax_1.set_facecolor("#E9E8E8")
# identify axis
ax_1.fill_between(x=revenue_data['date'], y1=revenue_data["amount"], alpha=0.7)


canvas = FigureCanvasTkAgg(figure = fig_1, master = window)
canvas.draw()
canvas.get_tk_widget().place(x=40, y=220)


window.resizable(False, False)
window.mainloop()


