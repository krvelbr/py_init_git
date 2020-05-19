# coding: utf-8
import os, subprocess
import pyperclip


#spam = pyperclip.paste()
#comando que faz o paste
def clear():
    print(os.name)
    if os.name in ('nt','dos'):
        os.system('cls')
    elif os.name in ('linux','osx','posix'):
        os.system('clear')
    else:
        print('\n') * 120

def init():
        
    print('\nThis utility will help you create the README.MD, \nand create a new repository in GitHub.')
    print('\n\nPress ^C at any time to quit.')

    project_name = input('\nProject Name: ')
    version = input('\nVersion: ')
    description = input('\nDescription: ')
    keywords = input('\nKeywords: ')
    author = input('\nAuthor Name: ')

    return 'retorno'

if __name__ =='__main__':
    clear()
    init()