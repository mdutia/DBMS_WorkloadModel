from app import db, WLM_data, Admin, AdminRole, ResearchRole, TeachingRole, Course

db.drop_all()
db.create_all()

F= 'admins.csv'
with open (F) as f:
    classlist= f.readlines() # should only be one line, but can cope with more
for line in classlist:
    lin= line.strip().split(',')
    for u in lin:
        a=Admin()
        a.username=u
        db.session.add (a)
db.session.commit()


F= 'StaffList.csv'
with open (F) as f:
    classlist= f.readlines() 
for line in classlist:
    lin= line.strip().split(',')
    title, lastname, firstname, position= lin       
    u= WLM_data( title=title, firstname=firstname, lastname=lastname, position=position )
    db.session.add (u)
db.session.commit()


F= 'AdminRolesList.csv'
with open (F) as f:
    classlist= f.readlines() 
for line in classlist:
    lin= line.strip().split(',')
    description, tariff= lin       
    u= AdminRole( description= description, tariff= tariff ) #multiplier will be set by default=1
    db.session.add (u)
db.session.commit()

F= 'TeachingRolesList.csv'
with open (F) as f:
    classlist= f.readlines() 
for line in classlist:
    lin= line.strip().split(',')
    description, tariff= lin       
    u= TeachingRole( description= description, tariff= tariff ) #multiplier will be set by default=1
    db.session.add (u)
db.session.commit()

F= 'ResearchRolesList.csv'
with open (F) as f:
    classlist= f.readlines() 
for line in classlist:
    lin= line.strip().split(',')
    description, tariff= lin       
    u= ResearchRole( description= description, tariff= tariff ) #multiplier will be set by default=1
    db.session.add (u)
db.session.commit()

F= 'CoursesList.csv'
import csv

with open (F) as f:
    reader = csv.reader(f)    
    #rows= []
    for r in reader:
        u= Course( name= r[0], category= r[1] ) 
        db.session.add (u)
        #rows.append(r)
    # f.readlines() 
#for r in rows:
    #lin= line.strip().split(',')
    #description, tariff= lin       
    #u= Courses( name= r[0], category= r[1] ) 
    #db.session.add (u)
db.session.commit()


print "Done."