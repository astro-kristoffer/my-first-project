#!/usr/bin/env python3

import os
import psutil
import shutil
import sys


def duplicate_file(filename):
    if os.path.isfile(filename):
        newfile1 = filename + '.dupl'
        shutil.copy(src=filename, dst=newfile1)  # можно просто через запятую, без src и dst!
        if os.path.exists(newfile1):
            print("Файл", filename, " продублирован!")
            return True
        else:
            print("Ошибка при копировании")
            return False


def del_dupl(dir_name):
    dupl_files = os.listdir(dir_name)
    dupl_count = 0
    for f in dupl_files:
        fullname = os.path.join(dir_name, f)
        if fullname.endswith(".dupl"):
            os.remove(fullname)
            if not os.path.exists(fullname):
                dupl_count += 1
                print("Файл", fullname, "был успешно удален!")
    return dupl_count


print("Это Величайшая из когда-либо созданных программ!")

UserName = input("Юный падаван, впиши имя свое:")

print(UserName, ", Совет джедаев приветствует тебя!")

answer = " "

# PEP-8

while answer != "q":
    answer = input("Хочешь присоединиться к Совету разработчиков? \n[y]- да \n[n]- нет \n[q]- выход\n")
    if answer == "y":
        print("Правильный путь ты выбрал, юный падаван! Посмотрим, чем могу помочь я!")
        print("[1]- выведу список файлов")
        print("[2]- выведу информацию о системе")
        print("[3]- выведу список процессов")
        print("[4]- продублирую файлы в текущей директории")
        print("[5]- продублирую указанный файл")
        print("[6]- удалю все продублированные файлы в указанной директории")
        do = int(input("Укажи номер действия: "))

        if do == 1:
            print(os.listdir())
        elif do == 2:
            print("Имя текущей директории: ", os.getcwd())
            print("Платформа (ОС): ", sys.platform)
            print("Кодировка файловой системы: ", sys.getfilesystemencoding())
            print("Логин пользователя: ", os.getlogin())
            print("Количество CPU: ", os.cpu_count())
        elif do == 3:
                print(psutil.pids())
        elif do == 4:
            print("=Дублирование файлов с помощью Силы=")
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                    duplicate_file(file_list[i])
                    i += 1

        elif do == 5:
            print("=Дублирование указанного файла=")
            filename = input("Введи имя файла:")
            duplicate_file(filename)

        elif do == 6:
            print("=Сила джедая удалит все продублированные файлы в указанной директории=")
            dir_name = input("Введи имя директории: ")
            count = del_dupl(dir_name)
            print("--Удалено файлов: ", count)

        else:
            pass
    elif answer == "n":
        print("Эх... не видна взгляду Темная сторона.")
    elif answer == "q":
        print("Да прибудет с тобой сила!")
    else:
        print("Это не те дроиды!")
