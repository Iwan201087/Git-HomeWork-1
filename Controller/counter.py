"""Создание специального счетчика, для автоматического  формирования id заметки"""
count = 0
def counter():
    global count
    count += 1
    return count