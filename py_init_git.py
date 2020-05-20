# coding: utf-8
from datetime import date
import os, subprocess
#import pyperclip   #changed idea of the project


def clear():
    print(os.name)
    if os.name in ('nt','dos'):
        os.system('cls')
    elif os.name in ('linux','osx','posix'):
        os.system('clear')
    else:
        print('\n') * 120

class Body():
    def __init__(self):
        print('\nThis utility will help you create the README.MD, \nand create a new repository in GitHub.')
        print('\n\nPress ^C at any time to quit.')

        ask_again = True
        while ask_again:
            self.user_name = input('\nUser name on Github (required)*: ')
            if self.user_name:
                ask_again = False
            else:
                ask_again = True

        ask_again = True
        while ask_again:
            self.project_name = input('\nProject name (required)*:')
            if self.project_name:
                ask_again = False
            else:
                ask_again = True

        
        self.version = input('\nVersion (optional): ')
        self.description = input('\nDescription (optional): ')
        self.keywords = input('\nKeywords (optional): ')
        self.author = input('\nAuthor name (optional): ')
        self.initial_commit_message = input('\nCommit message (optional): ')
        print('\n\n\n')
        #return __self__

        ## sanitization of strings
        if not self.project_name:
            self.project_name = 'Project'

        if not self.version:
            self.version = '0.0.1'

        if not self.description:
            self.description = 'Description will fill later.'

        if not self.author:
            self.author = 'Unknown'

        if not self.initial_commit_message:
            self.initial_commit_message = 'Initial commit. Started on: {}'.format(str(date.today()))
        ## end sanitization
        
        


def message_mount(params):
    mb = params
    line = ''
    line += f'# {mb.project_name}\n\n'
    line += f'***Version: {mb.version}***\n'
    line += f'\nAuthor: *{mb.author}*\n'
    line += f'\nKeywords: *{mb.keywords}*\n'
    line += f'\nStart date: *{str(date.today())}*\n'
    line += f'\n------------\n'
    line += f'#### Description:\n\n'
    line += f'{mb.description}\n'

    return line

def process(content, url, commit_message):
    #create .gitignore file
    file_name = '.gitignore'
    try:
        f = open(file_name, 'w+')  # open file in append mode
        f.write('py_init_git.py')
    except IOError as err:
        print('error: {0}'.format(err))
    finally:
        f.close()
        print(f'Arquivo {file_name} criado e fechado com sucesso\n\n\n')


    #create Readme.md file
    file_name = 'readme.md'
    try:
        f = open(file_name, 'w+')  # open file in append mode
        f.write(content)
    except IOError as err:
        print('error: {0}'.format(err))
    finally:
        f.close()
        print(f'Arquivo {file_name} criado e fechado com sucesso\n\n\n')

    #process git commands
    cmd = []
    cmd.append(f'git init')
    cmd.append(f'git add readme.md')
    cmd.append(f'git add .')
    cmd.append(f'{commit_message}')
#    cmd.append(f'git checkout -b "master"')
    cmd.append(f'git remote add origin {url}')
    cmd.append(f'git push -u origin master')

    for cmds in cmd:
        
        try:
            #os.system(cmds)
            print(f'>>> {cmds}')
            command_run = subprocess.call(cmds)
        except OSError as err:
            print('error: {0}'.format(err))
        finally:
            if command_run == 0:
                print('Its worked!!\n')
            elif command_run == 128:
                print('\nRemote origin already exists. Do nothing.\n')
            else:
                #print(str(command_run))
                print(f'\nThere was a problem, exit code {(str(command_run))}. See error message on terminal.\n')
    pause = input('')

    


if __name__ =='__main__':
    clear()
    mb = Body()
    url = f'https://github.com/{mb.user_name}/{mb.project_name}.git'
    commit_message = f'git commit -m "{mb.initial_commit_message}"'

    process(message_mount(mb), url, commit_message)
    
    exit()





    #criar o arquivo .gitignore com o arquivo py_init_git.py dentro
    #criar o arquivo readme.md
    
    #print(message_mount(Body()))
    #print(message_mount(mb))