import sys
import PySimpleGUI as sg


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def get_name() -> str:
    # All the stuff inside your window.
    layout = [[sg.Text("What's your name?")],
              [sg.InputText()],
              [sg.Button('Ok'), sg.Button('Cancel')]]

    # Create the Window
    window = sg.Window('Hello Example', layout)

    # Event Loop to process "events" and get the "values" of the inputs
    name: str = None

    event, values = window.read()

    # if user closes window or clicks cancel
    if event == sg.WIN_CLOSED or event == 'Cancel':
        name = None
    else:
        name = values[0]

    window.close()
    window = None
    return name


def main():
    name = get_name()
    if name is None:
        msg = 'No name was entered'
    else:
        msg = f'Hello {name}!'

    sg.popup(msg, title='Result', keep_on_top=True)
    print(msg)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(f'Python version {get_python_version()}')
    main()
