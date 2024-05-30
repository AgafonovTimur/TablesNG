from nicegui import ui
from nicegui.events import KeyEventArguments
import random

numbers_amount = [i for i in range(1, 10)]
rnd = random.shuffle(numbers_amount)
print(numbers_amount)
square_bgcolor = "#5e5e5e"
text_color = "#909090"
background_color = "#222222"
text1 = str(numbers_amount[0])
text2 = str(numbers_amount[1])
text3 = str(numbers_amount[2])
text4 = str(numbers_amount[3])
text5 = str(numbers_amount[4])
text6 = str(numbers_amount[5])
text7 = str(numbers_amount[6])
text8 = str(numbers_amount[7])
text9 = str(numbers_amount[8])

with ui.row():
    button1 = ui.button(text1, on_click=lambda: ui.notify('button was pressed'), color=square_bgcolor)
    button2 = ui.button(text2, on_click=lambda: ui.notify('button was pressed'), color=square_bgcolor)
    button3 = ui.button(text3, on_click=lambda: ui.notify('button was pressed'), color=square_bgcolor)
with ui.row():
    button4 = ui.button(text4, on_click=lambda: ui.notify('button was pressed'), color=square_bgcolor)
    button5 = ui.button(text5, on_click=lambda: ui.notify('button was pressed'), color=square_bgcolor)
    button6 = ui.button(text6, on_click=lambda: ui.notify('button was pressed'), color=square_bgcolor)
with ui.row():
    button7 = ui.button(text7, on_click=lambda: ui.notify('button was pressed'), color=square_bgcolor)
    button8 = ui.button(text8, on_click=lambda: ui.notify('button was pressed'), color=square_bgcolor)
    button9 = ui.button(text9, on_click=lambda: ui.notify('button was pressed'), color=square_bgcolor)


ui.query('body').style(f'background-color: {background_color}')
button1.style('height: 200px').classes('w-[200px]')
button2.style('height: 200px').classes('w-[200px]')
button3.style('height: 200px').classes('w-[200px]')
button4.style('height: 200px').classes('w-[200px]')
button5.style('height: 200px').classes('w-[200px]')
button6.style('height: 200px').classes('w-[200px]')
button7.style('height: 200px').classes('w-[200px]')
button8.style('height: 200px').classes('w-[200px]')
button9.style('height: 200px').classes('w-[200px]')


def handle_key(e: KeyEventArguments):
    if e.key == 'f' and not e.action.repeat:
        if e.action.keydown:
            global text1, text2, text3, text4, text5, text6, text7, text8, text9
            rnd = random.shuffle(numbers_amount)
            button1.text = str(numbers_amount[0])
            button2.text = str(numbers_amount[1])
            button3.text = str(numbers_amount[2])
            button4.text = str(numbers_amount[3])
            button5.text = str(numbers_amount[4])
            button6.text = str(numbers_amount[5])
            button7.text = str(numbers_amount[6])
            button8.text = str(numbers_amount[7])
            button9.text = str(numbers_amount[8])
            print(numbers_amount, "1231")


keyboard = ui.keyboard(on_key=handle_key)

ui.run(title='Shulte Game')
