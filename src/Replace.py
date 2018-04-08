from flask import Flask, render_template, redirect, url_for
import sys, subprocess
import codecs, sqlite3
themeName = 'graxpo'
connection = sqlite3.connect('../database/Record_'+themeName+'.db')

class Replace():

    def themeDetails(self):
        self.themeName = input('Enter theme name : ')
        self.themeAddress = '../templates/'+self.themeName+'/'
        self.contentAddress = self.themeAddress+'Content/'
        self.about_file =  open(self.contentAddress+'about_content.txt', 'r')
        self.about_file_reader = self.about_file.read()

        self.indexFile = open(self.themeAddress+'index.html', 'r+')

        #print(self.indexFile)
        self.index = self.indexFile.read()
        #print(self.index)
        self.indexArray = self.index.split(' ')
        print(self.indexArray)
        self.aboutPart()

    def aboutPart(self):

        self.about_Array = self.about_file_reader.split(' ')
        self.about = ''
        contentGot = False
        gotDColon = False
        print(self.about_Array)
        for i in self.about_Array:
            if i == 'ID:#abouttext#':
                contentGot = True

            if i == '::':
                gotDColon = True
                continue

            if gotDColon == True:
                print('Got inside')
                self.about += i + ' '

        print('self.about is : '+ self.about)
        self.replacer('ID:#abouttext#', self.about)


    def replacer(self, id, content):
        self.indexFile_writer = open(self.themeAddress + 'index.html', 'w')

        got_the_required_id = False
        '''
        for word in self.index:
            if word == id:
                got_the_required_id = True
                word.replace(word, content)
                print('Content is : '+content)
                print(word)
                print('Replaced with the required id ' + id)
                break
        '''
        print(id + ' '+content)
        self.index = self.index.replace(id,content)

        if got_the_required_id == False:
            print('Raw index.html doesnt have ID like this '+id)
        else:
            print('Got the ID : ' + id)
        print(self.index.split(' '))
        self.indexFile_writer.write(self.index)


if __name__ == '__main__' :
    obj = Replace()
    obj.themeDetails()
