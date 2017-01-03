from flask_wtf import Form
from wtforms import  widgets, SelectMultipleField
from wtforms import TextField, BooleanField, PasswordField, RadioField, TextAreaField, SelectField, IntegerField, SubmitField
from wtforms.validators import Required, NumberRange, Length
#from wtforms.fields.html5 import DateField

from config import ResearchRolesChoices, TeachingRolesChoices, AdminRolesChoices, CoursesChoices #

class LoginForm(Form):
    uname= TextField('username', validators = [Required()])

#class ChoiceObj(object):
    #def __init__(self, name, choices):
        ## this is needed so that BaseForm.process will accept the object for the named form,
        ## and eventually it will end up in SelectMultipleField.process_data and get assigned
        ## to .data
        #setattr(self, name, choices)

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(html_tag='ul',prefix_label=False)
    option_widget = widgets.CheckboxInput()
    
class NewUserForm (Form):
    title= SelectField(choices=[('Ms', 'Ms'), ('Mr', 'Mr'), ('Dr', 'Dr'), ('Prof', 'Prof') ])
    firstname= TextField(label='First name', validators= [Length(min=3, max=255, message='First name (max 40 chars)')])
    lastname= TextField(label='Last name', validators= [Length(min=3, max=255, message='Last name (max 40 chars)')])
    roll= IntegerField(label='StaffNo', validators = [Required()] ) #, validators= [Length(min=3, max=55, message='Staff number')])
    position= SelectField(choices=[('Staff', 'Staff'), ('Student', 'Student')], default='Staff')
    group= TextField(label='Group', validators= [Length(min=1, max=255, message='Group')])
    location= TextField(label='Location', validators= [Length(min=1, max=255, message='Location')])
    #facility1= SelectField (choices= FacilitiesListChoices)
    #facility2= SelectField (choices= FacilitiesListChoices)
    comment= TextAreaField()
    
class EditUserForm (Form):
    #title= SelectField(choices=[('Ms', 'Ms'), ('Mr', 'Mr'), ('Dr', 'Dr'), ('Prof', 'Prof') ])
    firstname= TextField(label='First name', validators= [Length(min=3, max=255, message='First name (max 40 chars)')])
    lastname= TextField(label='Last name', validators= [Length(min=3, max=255, message='Last name (max 40 chars)')])
    email= TextField(label='Email', validators= [Length(min=3, max=255, message='Email(max 40 chars)')])
    roll= IntegerField(label='StaffNo', validators = [Required()] ) #, validators= [Length(min=3, max=55, message='Staff number')])
    position= SelectField(choices=[('Staff', 'Staff'), ('Student', 'Student')], default='Staff')
    supervisor= TextField(label='Group', validators= [Length(min=1, max=255, message='Group')])
    location= TextField(label='Location', validators= [Length(min=1, max=255, message='Location')])
    #facility1= SelectField (choices= FacilitiesListChoices)
    #facility2= SelectField (choices= FacilitiesListChoices)
    comment= TextAreaField()
    
    
class ResearchRolesForm (Form):
    research_roles= SelectField (label= 'Research activity/role', choices= ResearchRolesChoices)
    number= IntegerField (label= 'Number', validators= [Required()])
    submit= SubmitField ('Add')

class TeachingRolesForm (Form):
    teaching_roles= SelectField (label= 'Teaching activity/role', choices= TeachingRolesChoices)
    course= SelectField (label= 'Course name', choices= CoursesChoices)
    number= IntegerField (label= 'Number', validators= [Required()])
    submit= SubmitField ('Add')

class AdminRolesForm (Form):
    admin_roles= SelectField (label= 'Admin activity/role', choices= AdminRolesChoices)
    number= IntegerField (label= 'Number', validators= [Required()])
    submit= SubmitField ('Add')
    
class NewAdminForm (Form):
    AdminUUN= TextField(label='UUN', validators= [Length(min=3, max=20, message='Please enter new admin UUN (max 20 chars)')])

    
class FiltersForm (Form):
    
    #sel_status= SelectField(choices= StatusListChoices)  #[ (c, c) for c in StatusList] )
                            
    list_order= SelectField(choices=[('Last name', 'List in order of Last name'),( 'Retest date', 'List in order of Expiry Date') ])
    #sel_facility= MultiCheckboxField('Facility', choices=[('All', 'All'), ('1GSQ','1GSQ'), ('Ash', 'Ash'), ('AWB', 'AWB'), ('CSQ', 'CSQ'), ('Evans', 'Evans'), ('HRB', 'HRB'),
                                   #('LF1', 'LF1'), ('LF2', 'LF2'), ('MacRH', 'MacRH'), ('SCRM', 'SCRM'), ('Teviot', 'Teviot'),('WGH', 'WGH'), 
                                   #('None', 'None'), ('Other', 'Other')  ])
    #sel_facility= MultiCheckboxField('Facility', choices= FacilitiesListChoices)
    
    #sel_facility= RadioField('Facility', choices= [
        #('1','All  '),
        #('2','LF1  '),
        #('3','LF2  '),
        #('4','HRB  '),
        #('5','CSQ  '),
        #('6','ASH  '),
        #('7','AWB  '),
        #('8','MACRH'),
        #('9','WGH  '),
        #('10','EVANS'),
    #] )
    #sel_status= RadioField('Facility', choices= [
        #('1','Active'),
        #('2','Not Active'),
    #] )
    
