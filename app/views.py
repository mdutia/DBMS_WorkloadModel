from flask import render_template, redirect, session, url_for, g, request, make_response #, send_from_directory, current_app
from flask_login import login_user , logout_user , current_user , login_required
#from wtforms import widgets, SelectMultipleField

from app import app
from forms import LoginForm, ResearchRolesForm, AdminRolesForm, TeachingRolesForm #, NewUserForm, AddTestsForm, NewAdminForm, EditUserForm  #, ChoiceObj
from sqlalchemy import or_, and_

#from flask_mail import Message
#from app import mail    

import os, sys
from config import HOST  #, ADMIN

@app.route('/', methods = ['GET', 'POST'])
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if 'REMOTE_USER' in request.environ :
        session['this_user_name']= request.environ.get('REMOTE_USER')
        return redirect(url_for('process_login'))       
    else:
        return redirect(url_for('fake_EASE_login'))

    #if HOST!='EASE':  # working on either local or pythonanywhere. username=os.getenv("USERNAME") works only on localhost
        #return redirect(url_for('fake_EASE_login'))
    #else:
        #username = request.environ.get('REMOTE_USER')
        #session['this_user_name']= username
        #return redirect(url_for('process_login'))

@app.route('/fake_EASE_login', methods = ['GET', 'POST'])
def fake_EASE_login():
    form= LoginForm()
    if (request.method=='GET'):
        return render_template('fake_EASE_login.html', form=form)
    else:
        if not form.validate():
            return render_template('fake_EASE_login.html', form=form)
        else:
            session['this_user_name']= form.uname.data
            return redirect(url_for('process_login'))

@app.route('/process_login', methods = ['GET', 'POST'])
def process_login():
    from app import db, Admin # WLM_data, Admin, AdminRole, ResearchRole, TeachingRole
    try:
        username= session['this_user_name']  #this fails if not routed correctly, but is not 100% secure
    except:
        return redirect (url_for('login'))
    ad = Admin.query.filter_by(username=username).first()
    if ad is None:
        return redirect(url_for('unknown_admin'))
    login_user(ad)
    session['editable']= True    
    return redirect(url_for('dashboard'))

@app.route('/unknown_admin', methods = ['GET', 'POST'])
def unknown_admin():
    return render_template ('unknownuser.html', hostname= HOST)

@app.route('/finished', methods = ['GET', 'POST'])
@login_required
def finished():
    logout_user()
    return render_template ('finished.html')

#@app.route('/SetOptions', methods = ['GET', 'POST'])
#@login_required
#def SetOptions():
    #if request.method=='GET':
        ##selectedChoices = ChoiceObj('FiltersForm', session['facility'] )
        ##form = FiltersForm (obj=selectedChoices)
        #form=FiltersForm()
        #return render_template('set_options.html', form=form)
    
    #else: #'PUT'
        #form=FiltersForm()
        #session['facility']= form.sel_facility.data if form.sel_facility.data else ['All']
        
        #session['status']= form.sel_status.data
        #session['list_order']= form.list_order.data

        #session['current_pg']= 1                
        ##recs= get_filtered_recs()
        #return redirect (url_for('dashboard'))

@app.route('/dashboard', methods = ['GET'])
@login_required
def dashboard():  
    from app import WLM_data    
    if request.method=='GET':
    #if 'mode' in request.args:            
            #if request.args['mode']=='prev_page':
                #session['current_pg']-=1
                #if session['current_pg']<=0:
                    #session['current_pg']=1
                #form=FiltersForm()
                #recs= get_filtered_recs()
                #return render_template('show_recs.html', recs=recs, form=form) 
                
            #elif request.args['mode']=='next_page':
                #session['current_pg']+=1
                #form=FiltersForm()
                #recs= get_filtered_recs()
                #return render_template('show_recs.html', recs=recs, form=form) 

        #else:
            #form=FiltersForm()
            r= WLM_data.query.order_by(WLM_data.lastname)
            recs=[]
            for rr in r:
                recs.append ( ' '.join ( [rr.firstname, rr.lastname] ) )
            return render_template('WLM_staff_recs.html', recs=recs)   

@app.route('/show_one_rec', methods = ['GET'])
@login_required
def show_one_rec():  
    from app import WLM_data
    if 'idd' in request.args:
        firstname, lastname= request.args['idd'].split() 
        r= WLM_data.query.filter ( and_ ( WLM_data.firstname== firstname, WLM_data.lastname== lastname) ).first()
        session['selected_staff_id']= r.id
        session['selected_staff_name']= ' '.join ( [firstname, lastname] )
        return render_template('show_one_rec.html', rec=r, r_form= ResearchRolesForm(), ad_form= AdminRolesForm(), t_form= TeachingRolesForm()) 
    else:
        return render_template('WLM_error.html') 
        
@app.route('/update_research', methods = ['GET', 'POST'])
@login_required
def update_research():  
    from app import db, WLM_data, ResearchRole
    role= request.form.get('research_roles')
    n= int(request.form.get('number'))
    r= WLM_data.query.get(int(session['selected_staff_id']))
    activity= ResearchRole.query.filter_by (description=role).first()
    tot_tariff= n*activity.tariff
    rr=  ','.join ([role, request.form.get('number'), str(tot_tariff), ';']) 
    r.research+= rr
    r.tot_research+= tot_tariff
    r.total_hours+= tot_tariff
    db.session.merge (r)
    db.session.commit()
    #return redirect(url_for('dashboard'))
    return render_template('show_one_rec.html', rec=r, r_form= ResearchRolesForm(), ad_form= AdminRolesForm(), t_form= TeachingRolesForm())

@app.route('/update_admin', methods = ['GET', 'POST'])
@login_required
def update_admin():  
    from app import db, WLM_data, AdminRole
    role= request.form.get('admin_roles')
    n= int(request.form.get('number'))
    r= WLM_data.query.get(int(session['selected_staff_id']))
    activity= AdminRole.query.filter_by (description=role).first()
    tot_tariff= n*activity.tariff
    rr=  ','.join ([role, request.form.get('number'), str(tot_tariff), ';']) 
    r.admin+= rr 
    r.tot_admin+= tot_tariff
    r.total_hours+= tot_tariff
    db.session.merge (r)
    db.session.commit()
    #return redirect(url_for('dashboard'))
    return render_template('show_one_rec.html', rec=r, r_form= ResearchRolesForm(), ad_form= AdminRolesForm(), t_form= TeachingRolesForm()) 

@app.route('/update_teaching', methods = ['GET', 'POST'])
@login_required
def update_teaching():  
    from app import db, WLM_data, TeachingRole
    role= request.form.get('teaching_roles')
    course= request.form.get('course')
    n= int(request.form.get('number'))
    r= WLM_data.query.get(int(session['selected_staff_id']))
    activity= TeachingRole.query.filter_by (description=role).first()
    tot_tariff= n*activity.tariff
    rr=  ','.join ([role, course, request.form.get('number'), str(tot_tariff), ';']) 
    r.teaching+= rr
    r.tot_teaching+= tot_tariff
    r.total_hours+= tot_tariff
    db.session.merge (r)
    db.session.commit()
    #return redirect(url_for('dashboard'))
    return render_template('show_one_rec.html', rec=r, r_form= ResearchRolesForm(), ad_form= AdminRolesForm(), t_form= TeachingRolesForm())

            

#@app.route('/manage_admins', methods = ['GET', 'POST'])
#@login_required
#def manage_admins():
    #from app import db, Admin
    #ad= Admin.query.all()
    
    #adUUN= []
    #for a in ad:
        #adUUN.append(a.username)
    #form=NewAdminForm()

    ##if ('Manage' in request.form ['Button']):   #add authorised admins
    #if request.method=='GET':
        #return render_template('get_new_admin.html', ad=ad, form=form, err=False) 

    ##elif ('Admin' in request.form ['Button']): 
    #else: #POST
        #if (request.form ['Button']=='Add Admin'):
            #if (len(form.data['AdminUUN'])>=3) and not(form.data['AdminUUN'] in adUUN):
                #aa=Admin()
                #aa.username= form.data['AdminUUN']
                #db.session.add(aa)
                #db.session.commit()
            #else:
                #return render_template('get_new_admin.html', ad=ad, form=form, err=True)
            #ad= Admin.query.all() #refresh the list of admins
            #return render_template('get_new_admin.html', ad=ad, form=form, err=False)       
        #else:
            #return redirect (url_for('dashboard'))

            
#@app.route('/add_new_user', methods = ['GET', 'POST'])
#@login_required
#def add_new_user():
    #from app import db, Userdata
# ..........
