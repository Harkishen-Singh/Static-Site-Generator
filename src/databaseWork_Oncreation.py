import sqlite3
import datetime
time = datetime.datetime.now()
print(datetime.datetime.now())
themeName = 'graxpo'
connection = sqlite3.connect('../database/Record_'+themeName+'.db')
cmd ='';exe = ''

def createNecessaryTables():
    # general

    cmd = '''create table generalInformation(No integer, title varchar(1000), \
    BannerContent1 varchar(1000), BannerContent2 varchar(1000));'''

    connection.execute(cmd.upper())
    #about
    cmd = 'create table aboutContent(No integer, content varchar(10000), details date);'
    connection.execute(cmd.upper())
    #contact
    cmd = 'create table aboutContact(No integer,contactBrief varchar(10000), contactAdd1 varchar(10000), contactAdd2 varchar(10000),\
          contactMail varchar(1000), contactPhone varchar(1000),details datetime);'
    connection.execute(cmd.upper())
    #team brief
    cmd = 'create table aboutTeam(No integer, teamBrief varchar(10000), details datetime);'
    connection.execute(cmd.upper())
    #team members
    cmd = 'create table TeamMembers(No integer, Name varchar(1000), Position varchar(1000), Brief varchar(1000), details datetime);'
    connection.execute(cmd.upper())
    #footer
    cmd = 'create table aboutFooter(No integer, FooterContent varchar(10000), details datetime);'
    connection.execute(cmd.upper())

def defaultValues_toDatabase():
    cmd = "INSERT INTO GENERALINFORMATION (No, title, BannerContent1, bannercontent2) VALUES(1,'ID:#title#','ID:#htext#', 'ID:#htext2#');"
    connection.execute(cmd)

    cmd = '''INSERT INTO ABOUTCONTENT (No, content, details) VALUES(1,'ID:#abouttext#', ''' + str(time)[:9]+ ''');'''
    connection.execute(cmd)

    cmd = '''INSERT INTO ABOUTCONTACT (No, contactBrief, contactadd1, contactadd2, contactMail, ContactPhone, details) \
    VALUES(1,'ID:#contacttext#',  'ID:#contactaddress1#', 'ID:#contactaddress2#'\
     , 'ID:#contactmail#', ' ID:#contactphone# ','''+ str(time)[:9]+ ''');'''
    connection.execute(cmd)

    cmd = '''INSERT INTO ABOUTTEAM (No, teamBrief, details) VALUES(1, 'ID:#teambrief#', ''' + str(time)[:9]+ ''');'''
    connection.execute(cmd)

    cmd = '''INSERT INTO TEAMMEMBERS (No, name, Position, brief, details) VALUES(1, 'ID:#team1name#' , 'ID:#team1post#', 'ID:#team1content#', ''' +str(time)[:9]+ ''');'''
    connection.execute(cmd)

    cmd = '''INSERT INTO ABOUTFOOTER (No, footerContent, details) VALUES(1, 'ID:#footertext#', '''+str(time)[:9]+''');'''
    connection.execute(cmd)
    print('came here')
    connection.commit()


def defaultValues_toDatabase_secondtime():
    cmd = "INSERT INTO GENERALINFORMATION (No, title, BannerContent1, bannercontent2) VALUES(2,'ID:#title#','ID:#htext#', 'ID:#htext2#');"
    connection.execute(cmd)

    cmd = '''INSERT INTO ABOUTCONTENT (No, content, details) VALUES(2,'ID:#abouttext#', ''' + str(time)[:9]+ ''');'''
    connection.execute(cmd)

    cmd = '''INSERT INTO ABOUTCONTACT (No, contactBrief, contactadd1, contactadd2, contactMail, ContactPhone, details) \
    VALUES(2,'ID:#contacttext#',  'ID:#contactaddress1#', 'ID:#contactaddress2#'\
     , 'ID:#contactmail#', ' ID:#contactphone# ','''+ str(time)[:9]+ ''');'''
    connection.execute(cmd)

    cmd = '''INSERT INTO ABOUTTEAM (No, teamBrief, details) VALUES(2, 'ID:#teambrief#', ''' + str(time)[:9]+ ''');'''
    connection.execute(cmd)

    cmd = '''INSERT INTO TEAMMEMBERS (No, name, Position, brief, details) VALUES(2, 'ID:#team1name#' , 'ID:#team1post#', 'ID:#team1content#', ''' +str(time)[:9]+ ''');'''
    connection.execute(cmd)

    cmd = '''INSERT INTO ABOUTFOOTER (No, footerContent, details) VALUES(2, 'ID:#footertext#', '''+str(time)[:9]+''');'''
    connection.execute(cmd)
    print('came here')
    connection.commit()

#createNecessaryTables()

#defaultValues_toDatabase()
#defaultValues_toDatabase_secondtime()

'''
def about():
    cmd = connection.execute('')
'''

connection.close()