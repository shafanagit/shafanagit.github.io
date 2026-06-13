import FreeSimpleGUI  as FSGUI
userinput_name = FSGUI.popup_get_text("what is your name?", title = "Name request")
FSGUI.popup(f"hello there, {userinput_name}", title ="My first desktop popup", button_color = "red", background_color= "yellow", text_color = "blue")