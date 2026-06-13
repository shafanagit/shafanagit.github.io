import FreeSimpleGUI as FSGUI
from datetime import datetime, timedelta

FSGUI.theme("DarkBlue3")

def decode_nic(nic):
    nic = nic.strip().upper()

    try:
        if len(nic) == 10 and nic[-1] in ["V", "X"]:
            year = int("19" + nic[:2])
            day_no = int(nic[2:5])

        elif len(nic) == 12 and nic.isdigit():
            year = int(nic[:4])
            day_no = int(nic[4:7])

        else:
            return "Invalid NIC format"

        gender = "Male"

        if day_no > 500:
            gender = "Female"
            day_no -= 500

        birth_date = datetime(year, 1, 1) + timedelta(days=day_no - 1)

        return (
            f"NIC Number : {nic}\n"
            f"Birth Year : {year}\n"
            f"Birth Date : {birth_date.strftime('%Y-%m-%d')}\n"
            f"Gender     : {gender}\n"
            f"Age        : {datetime.now().year - year}"
        )

    except Exception as e:
        return f"Error: {e}"

layout = [
    [FSGUI.Text("Sri Lankan NIC Decoder", font=("Arial", 16, "bold"))],
    [FSGUI.Text("NIC Number:"), FSGUI.Input(key="-NIC-", size=(25,1))],
    [FSGUI.Button("Decode"), FSGUI.Button("Clear"), FSGUI.Button("Exit")],
    [FSGUI.Multiline(
        size=(50,10),
        key="-RESULT-",
        disabled=True,
        autoscroll=True
    )]
]

window = FSGUI.Window(
    "NIC Decoder",
    layout,
    finalize=True
)

while True:
    event, values = window.read()

    if event in (FSGUI.WIN_CLOSED, "Exit"):
        break

    if event == "Decode":
        result = decode_nic(values["-NIC-"])
        window["-RESULT-"].update(result)

    if event == "Clear":
        window["-NIC-"].update("")
        window["-RESULT-"].update("")

window.close()