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


        self.indexFile = open(self.themeAddress+'index.html', 'r+')

        #print(self.indexFile)
        self.index = self.indexFile.read()
        #print(self.index)
        self.indexArray = self.index.split(' ')
        print(self.indexArray)
        self.aboutPart()

    ## *** about ****


    def aboutPart(self):

        self.about_file = open(self.contentAddress + 'about_content.txt', 'r')
        self.about_file_reader = self.about_file.read()

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
                #print('Got inside')
                self.about += i + ' '

        print('self.about is : '+ self.about)
        #self.replacer('ID:#abouttext#', self.about)
        #self.scan_the_database_about('ABOUTCONTENT', self.about)
        self.scan_previous()

    def scan_previous(self):
        previous = open('../templates/' + themeName +'/Previous_Records/about_content.txt', 'r+')
        reader = previous.read()
        gotId = False
        gotDoubleColon = False
        newContent = ''

        if reader != self.about_file_reader :
            reader_array = reader.split(' ')
            print('Change found in about_content.txt')
            for word in reader_array :
                if word == 'ID:#abouttext#':
                    gotId = True
                if gotId == True:
                    if word == '::':
                        gotDoubleColon = True
                        continue
                if gotDoubleColon == True:
                    newContent += word + ' '

        self.replacer(self.about, newContent)


    def scan_the_database_about(self, name, content):
        cmd = 'select * from '+name+';'
        exe = connection.execute(cmd)
        previous = ''
        for i in exe:
            if i[0] == 2:
                previous = i[1]

        if previous != content:
            self.replacer(previous, content)
            cmd = 'UPDATE '+name + ' SET content = "'+str(content)+'" where No = 2;'
            connection.execute(cmd)

        connection.commit()

    def replacer(self, p, content):
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
        print(p + ' '+content)
        self.index = self.index.replace(p,content)
        #print(self.index.split(' '))
        self.indexFile_writer.write(self.index)


if __name__ == '__main__' :
    obj = Replace()
    obj.themeDetails()
