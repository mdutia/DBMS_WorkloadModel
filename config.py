CSRF_ENABLED = True
TEMPLATES_AUTO_RELOAD=True

SECRET_KEY = 'Cjq0nz2@kWl2Pm#c'
SQLALCHEMY_DATABASE_URI = 'sqlite:///WLM_data.db'
SQLALCHEMY_BINDS = {
    'admins':      'sqlite:///WLM_admins.db'
}

F= 'ResearchRolesList.csv'
with open (F) as f:
    classlist= f.readlines()
ResearchRolesList=[]
for line in classlist:
    lin= line.strip().split(',')
    description, tariff= lin
    ResearchRolesList.append (description)
ResearchRolesChoices= [ (c, c) for c in ResearchRolesList]

F= 'AdminRolesList.csv'
with open (F) as f:
    classlist= f.readlines() 
AdminRolesList=[]
for line in classlist:
    lin= line.strip().split(',')
    description, tariff= lin       
    AdminRolesList.append (description)
AdminRolesChoices= [ (c, c) for c in AdminRolesList]

F= 'TeachingRolesList.csv'
with open (F) as f:
    classlist= f.readlines() 
TeachingRolesList=[]
for line in classlist:
    lin= line.strip().split(',')
    description, tariff= lin       
    TeachingRolesList.append (description)
TeachingRolesChoices= [ (c, c) for c in TeachingRolesList]

F= 'CoursesList.csv'
import csv
CoursesList=[]
with open (F) as f:
    reader = csv.reader(f)    
    #rows= []
    for r in reader:
        CoursesList.append (r[0])
CoursesChoices= [ (c, c) for c in CoursesList]


#MAIL_SERVER='smtp.staffmail.ed.ac.uk'
#MAIL_USERNAME= "mdutia@staffmail.ed.ac.uk"

#MAIL_SERVER='smtp.gmail.com'
#MAIL_PORT = 465
#MAIL_USERNAME= "sbms.bmto@gmail.com"
#MAIL_PASSWORD= "t3stingsyst3m1"
#MAIL_USE_TLS = False
#MAIL_USE_SSL = True

MAIL_SERVER='smtp.office365.com'
MAIL_PORT = 587
MAIL_USERNAME= "mdutia@ed.ac.uk"
MAIL_PASSWORD= "password"
MAIL_USE_TLS = True
MAIL_USE_SSL = False


HOST='Local' #EASE 
#ADMINS= ['mdutia','kharris']
