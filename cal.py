import FreeSimpleGUI as FSGUI

FSGUI.theme("DarkBlue3")

layout = [
    [FSGUI.Input(
        key="-DISPLAY-",
        size=(20, 1),
        justification="right",
        font=("Arial", 20),
        readonly=True
    )],

    [
        FSGUI.Button("7", size=(5, 2)),
        FSGUI.Button("8", size=(5, 2)),
        FSGUI.Button("9", size=(5, 2)),
        FSGUI.Button("/", size=(5, 2))
    ],

    [
        FSGUI.Button("4", size=(5, 2)),
        FSGUI.Button("5", size=(5, 2)),
        FSGUI.Button("6", size=(5, 2)),
        FSGUI.Button("*", size=(5, 2))
    ],

    [
        FSGUI.Button("1", size=(5, 2)),
        FSGUI.Button("2", size=(5, 2)),
        FSGUI.Button("3", size=(5, 2)),
        FSGUI.Button("-", size=(5, 2))
    ],

    [
        FSGUI.Button("0", size=(5, 2)),
        FSGUI.Button(".", size=(5, 2)),
        FSGUI.Button("=", size=(5, 2)),
        FSGUI.Button("+", size=(5, 2))
    ],

    [
        FSGUI.Button("Clear", size=(22, 2))
    ]
]

window = FSGUI.Window(
    "Simple Calculator",
    layout,
    resizable=False
)

expression = ""

while True:
    event, values = window.read()

    if event == FSGUI.WIN_CLOSED:
        break

    if event == "Clear":
        expression = ""

    elif event == "=":
        try:
            expression = str(eval(expression))
        except Exception:
            expression = "Error"

    elif event in "0123456789.+-*/":
        expression += event

    window["-DISPLAY-"].update(expression)

window.close()