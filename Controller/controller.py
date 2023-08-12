import UI.userMemuConsole as ui
import Controller.commands as com

"""Вызов пунктов меню для работы с заметками"""
def start():
    while True:
        ui.menu_console()
        user_input = input()
        if user_input == '1':
            com.show("all")
        elif user_input == '2':
            com.show("ID")
        elif user_input == '3':
            com.show("date")
        elif user_input == '4':
            com.show("all")
            com.change_note()
        elif user_input == '5':
            com.add_note()
        elif user_input == '6':
            com.show("all")
            com.del_notes()
        else:
            print("Программа для работы с заметками завершила свою работу")
            break