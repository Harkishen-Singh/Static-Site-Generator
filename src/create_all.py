'''creates all the required files for the theme chosen. these can be customised to change the feel.'''
import sys, subprocess

class Create_all:

    def __init__(self):

        a=0
        self.themeName = 'Graxpo'
        self.general = open('../templates/'+self.themeName+'/content/general.txt', 'r')

        self.making_files()

    def making_files(self):
        self.general.write('Title : \n')

        part = '**** Navigation Bar ****\n\n' \
               'add the elements wanted in Navigation within these curly brackets strictly in form of array.\n' \
               '{"Home", }'
        self.general.write(part + '\n**** Navigation Bar End ****\n')

        self.file_save()


    def file_save(self):
        a = 1









object = Create_all()
