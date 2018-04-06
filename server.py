from flask import Flask, render_template, redirect, url_for
import sys, subprocess


## console works below
fromConsole = sys.argv
toConsole = ''
newthemeName = ''
if fromConsole[1] == 'new':
    sys.stdout.write('\n\nPlease save the downloaded theme from the Git repository in the themes folder created by the\
 software\n\n')
    newthemeName = input('Name of the theme : ')

elif fromConsole[1] == 'help':
    toConsole = 'This is the documentation portal\n\n'
    sys.stdout.write(toConsole)

    helpDoc = 'keyword and their following functions below:\n\n' \
              '------------------------------------------------------------------------------\n\n' \
              '' \
              'new \t choosing new theme\n' \
              'help \t details for the keywords and their meanings'
    sys.stdout.write(helpDoc)














app = Flask(__name__)


@app.route('/')
def homePage():
    return render_template()