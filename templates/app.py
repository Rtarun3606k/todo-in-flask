from flask import Flask, render_template, url_for, request, redirect, flash ,send_from_directory,Response,send_file
from io import BytesIO
from flask_sqlalchemy import SQLAlchemy
import os

import time
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField , FileRequired , FileAllowed


from flask_uploads import UploadSet , IMAGES , configure_uploads
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from test_folder import *
from test_folder.gcheck import generator



app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///active_database.db"
# app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///projectsdatabases.db"
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS']= False
app.secret_key = "secreate_key"
app.config['UPLOADED_PHOTOS_DEST']='static'
db = SQLAlchemy(app)




def loga(f):
    
    def decorated_function(*args, **kwargs):
       return render_template('logadmin.html')
    return decorated_function



# # >>> from app import app , db
# # >>> app.app_context().push()
# # >>> db.create_all()   

class color_c(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body_color=db.Column(db.String(500))
    font=db.Column(db.String(500))
    font_style=db.Column(db.String(500))
    card_co_lor_bg=db.Column(db.String(500))
    project_card_color=db.Column(db.String(500))
    project_card_font=db.Column(db.String(500))
    project_card_button_color=db.Column(db.String(500))
    project_card_font_color=db.Column(db.String(500))
    certi_color=db.Column(db.String(500))
    certi_font =db.Column(db.String(500))
    certi_font_color=db.Column(db.String(500))
    adout_bg_color =db.Column(db.String(500))
    about_font_color=db.Column(db.String(500))
    contact_bg=db.Column(db.String(500))




class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500),nullable=False )
    email = db.Column(db.String(500),nullable=False )
    pa = db.Column(db.String(500),nullable=False )  #message
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.name} - {self.pa}"



class index_phara(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_para = db.Column(db.Text,nullable=True,unique=False)
    second_para = db.Column(db.Text,nullable=True,unique=False)



class about_phara(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_para = db.Column(db.Text,nullable=True,unique=False)



class projectdb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_name = db.Column(db.String(500),nullable=False )
    project_language = db.Column(db.String(500),nullable=False )
    img = db.Column(db.Text, unique=False, nullable=False)
    name = db.Column(db.Text, unique=False,nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    project_reach_link = db.Column(db.String(500),nullable=False )  
    project_description = db.Column(db.String(500),nullable=False )  
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.project_name} - {self.img}"


class certdb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, unique=False, nullable=False)
    name = db.Column(db.Text, unique=False,nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    name_certi = db.Column(db.String(500),nullable=True ,default = 12) 

    def __repr__(self) -> str:
        return f"{self.img} - {self.name_certi}"


class cIndex_img_big(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, unique=False, nullable=False)
    name = db.Column(db.Text, unique=False,nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    name_img = db.Column(db.String(500),nullable=True ,default = 12) 

    def __repr__(self) -> str:
        return f"{self.img} - {self.name_certi}"


class cIndex_img_self(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, unique=False, nullable=False)
    name = db.Column(db.Text, unique=False,nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    name_img = db.Column(db.String(500),nullable=True ,default = 12) 

    def __repr__(self) -> str:
        return f"{self.img} - {self.name_certi}"



class socials(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, unique=False, nullable=False)
    name = db.Column(db.Text, unique=False,nullable=False)
    mimetype = db.Column(db.Text, nullable=False)
    social = db.Column(db.String(500),nullable=True ,default = 12) 
    social_link = db.Column(db.String(500),nullable=True ,default = 12) 


class cIndex_name(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=False,nullable=True)
    full_name = db.Column(db.Text, unique=False,nullable=True)


class chat_bot_class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    query_asked = db.Column(db.Text, unique=False,nullable=True)
    response_made = db.Column(db.Text, unique=False,nullable=True)
    query_created = db.Column(db.Text, default=time.ctime())
    response_created = db.Column(db.Text, default=time.ctime())

    def __repr__(self) -> str:
        return f"{self.query} - {self.response}"

    
class Pdf(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(50))
    data =db.Column(db.LargeBinary)





@app.route('/')
@app.route('/home')
def hello_world():
    allinfo = index_phara.query.all()
    background_color = '#FF0000'  # Red color
    text_color = 'blue' 
    social = socials.query.all()
    names = cIndex_name.query.all()
    selfs=cIndex_img_self.query.all()
    bigs=cIndex_img_big.query.all()
    certificates=certdb.query.all()
    resume = Pdf.query.all()
    return render_template('cIndex.html',selfs=selfs,certificates=certificates,allinfo = allinfo,names = names,social = social,bigs=bigs ,background_color=background_color, text_r=text_color,resume=resume)


# @app.route('/')
# def hello_world():
#     allinfo=certdb.query.all()
#     social = socials.query.all()
#     names = cIndex_name.query.all()
#     return render_template('index.html',allinfo=allinfo, social = social,names=names)

@app.route("/admin")
def admin():
    allinfo=User.query.all()
    social = socials.query.all()
    names = cIndex_name.query.all()
    return render_template('admin.html',names=names, allinfo = allinfo,social = social)




@app.route('/base')
def base():
    background_color = '#0000'  # Red color
    text_color = 'blue' 
    allinfo=socials.query.all()
    names = cIndex_name.query.all()
    return render_template('base.html',allinfo=allinfo,names=names, background_color=background_color, text_r=background_color)

@app.route('/self',methods=['GET','POST'])
def self():
    status = False
    if request.method ==  "POST":

            # cIndex_img_self.__table__.create(db.engine)
        # allinfo = Img.qurey.all()
        print("sucess")
        pic = request.files['pic']
        filename = secure_filename(pic.filename)
        print(filename)
        mimetype = pic.mimetype
        name_img = request.form['upld_name']
        if not filename or not mimetype:
            flash("'No pic uploaded!', bad request ")
            return redirect('/self')
        else:
            with app.app_context():
                db.reflect()
                db.session.close()  # Close any existing sessions to avoid issues with dropping the table
                cIndex_img_self.__table__.drop(db.engine)
                db.create_all()
            

        flash(" updated SUCESSFULLY! ")
        allinfo = cIndex_img_self(img=pic.read(),mimetype=mimetype,name_img=name_img,name=filename)
        db.session.add(allinfo)
        db.session.commit()



    # allinfo = index_phara.query.all()
    allinfo= cIndex_img_self.query.all()
    social = socials.query.all()
    names = cIndex_name.query.all()
    return render_template('self.html',allinfo=allinfo,social = social,names=names)

@app.route('/big',methods=['GET','POST'])
def big():
    if request.method ==  "POST":
        with app.app_context():
            db.reflect()
            db.session.close()  # Close any existing sessions to avoid issues with dropping the table
            cIndex_img_big.__table__.drop(db.engine)
            db.create_all()
        # allinfo = Img.qurey.all()
        print("sucess")
        pic = request.files['pic']
        filename = secure_filename(pic.filename)
        print(filename)
        mimetype = pic.mimetype
        name_img = request.form['upld_name']
        if not filename or not mimetype:
            flash("'No pic uploaded!', bad request ")
            return redirect('/big')
        else:
            with app.app_context():
                db.reflect()
                db.session.close()  # Close any existing sessions to avoid issues with dropping the table
                cIndex_img_big.__table__.drop(db.engine)
                db.create_all()
            

        flash(" updated SUCESSFULLY! ")
        allinfo = cIndex_img_big(img=pic.read(),mimetype=mimetype,name_img=name_img,name=filename)
        db.session.add(allinfo)
        db.session.commit()

    # allinfo = index_phara.query.all()
    allinfo= cIndex_img_big.query.all()
    social = socials.query.all()
    names = cIndex_name.query.all()
    return render_template('big.html',allinfo=allinfo,social = social,names=names)

@app.route('/self/<int:id>')
def get_img_self(id):
    img = cIndex_img_self.query.filter_by(id=id).first()
    if not img:
        return 'Img Not Found!', 404

    return Response(img.img, mimetype=img.mimetype)

@app.route('/big/<int:id>')
def get_img_big(id):
    img = cIndex_img_big.query.filter_by(id=id).first()
    if not img:
        return 'Img Not Found!', 404

    return Response(img.img, mimetype=img.mimetype)


@app.route('/selfDel/<int:id>')
def delete_self(id):
    infos = cIndex_img_self.query.filter_by(id=id).first()
    db.session.delete(infos)
    db.session.commit()
    info = cIndex_img_self(id="id", name="name",mimetype="minetype",img="img",name_img="name_img")
    allinfo=cIndex_img_self.query.all()
    return redirect("/self")


@app.route('/bigDel/<int:id>')
def delete_big(id):
    infos = cIndex_img_big.query.filter_by(id=id).first()
    db.session.delete(infos)
    db.session.commit()
    info = cIndex_img_big(id="id", name="name",mimetype="minetype",img="img",name_img="name_img")
    allinfo=cIndex_img_big.query.all()
    return redirect("/big")


@app.route('/selfUpd/<int:id>',methods=['GET','POST'])
def selfUpd(id):
    if request.method ==  "POST":
        # allinfo = Img.qurey.all()
        print("sucess")
        pic = request.files['pic']
        filename = secure_filename(pic.filename)
        print(filename)
        mimetype = pic.mimetype
        name_img = request.form['upld_name']
        
        if not filename or not mimetype:
            flash("'No pic uploaded!', bad request ")
            

        flash(" updated SUCESSFULLY! ")
        infos=cIndex_img_self.query.filter_by(id=id).first()
        infos.img = pic.read()
        infos.name = filename
        infos.mimetype = mimetype
        infos.name_img = name_img
        # infos = Img(img=pic.read(),name=filename,mimetype=mimetype)
        db.session.add(infos)
        # print(infos.id,infos.name,infos.mimetype,infos.img,infos.name_certi)
        db.session.commit()
        
        return redirect('/self')
    infos=cIndex_img_self.query.filter_by(id=id).first()
    social = socials.query.all()
    names = cIndex_name.query.all()

    return render_template("selfUpdate.html",allinfo = infos,social = social,names=names)

@app.route('/bigUpd/<int:id>',methods=['GET','POST'])
def bigUpd(id):
    if request.method ==  "POST":
        # allinfo = Img.qurey.all()
        print("sucess")
        pic = request.files['pic']
        filename = secure_filename(pic.filename)
        print(filename)
        mimetype = pic.mimetype
        name_img = request.form['upld_name']
        
        if not filename or not mimetype:
            flash("'No pic uploaded!', bad request ")
            

        flash(" updated SUCESSFULLY! ")
        infos=cIndex_img_big.query.filter_by(id=id).first()
        infos.img = pic.read()
        infos.name = filename
        infos.mimetype = mimetype
        infos.name_img = name_img
        # infos = Img(img=pic.read(),name=filename,mimetype=mimetype)
        db.session.add(infos)
        # print(infos.id,infos.name,infos.mimetype,infos.img,infos.name_certi)
        db.session.commit()
        
        return redirect('/big')
    infos=cIndex_img_big.query.filter_by(id=id).first()
    social = socials.query.all()
    names = cIndex_name.query.all()

    return render_template("bigUpdate.html",allinfo = infos,social = social,names=names)



@app.route('/socials',methods=['GET','POST'])
def social():
    if request.method ==  "POST":
        # allinfo = Img.qurey.all()
        print("sucess")
        pic = request.files['pic']
        filename = secure_filename(pic.filename)
        print(filename)
        mimetype = pic.mimetype
        social = request.form['upld_name']
        social_link = request.form['social_link']
        if not filename or not mimetype:
            flash("'No pic uploaded!', bad request ")
            

        flash(" updated SUCESSFULLY! ")
        allinfo = socials(img=pic.read(),mimetype=mimetype,social=social,social_link=social_link,name=filename)
        db.session.add(allinfo)
        db.session.commit()

    # allinfo = index_phara.query.all()
    allinfo= socials.query.all()
    social = socials.query.all()
    names = cIndex_name.query.all()
    return render_template('socials.html',allinfo=allinfo,social = social,names=names)

@app.route('/socials/<int:id>')
def get_img_social(id):
    img = socials.query.filter_by(id=id).first()
    if not img:
        return 'Img Not Found!', 404

    return Response(img.img, mimetype=img.mimetype)

@app.route('/socialsUpd/<int:id>',methods=['GET','POST'])
def socialsUpd(id):
    if request.method ==  "POST":
        # allinfo = Img.qurey.all()
        print("sucess")
        pic = request.files['pic']
        filename = secure_filename(pic.filename)
        print(filename)
        mimetype = pic.mimetype
        social = request.form['upld_name']
        social_link = request.form['social_link']
        if not filename or not mimetype:
            flash("'No pic uploaded!', bad request ")
            

        flash(" updated SUCESSFULLY! ")
        infos=socials.query.filter_by(id=id).first()
        infos.img = pic.read()
        infos.name = filename
        infos.mimetype = mimetype
        infos.social = social
        infos.social_link = social_link
        # infos = Img(img=pic.read(),name=filename,mimetype=mimetype)
        db.session.add(infos)
        # print(infos.id,infos.name,infos.mimetype,infos.img,infos.name_certi)
        db.session.commit()
        
        return redirect('/socials')
    infos=socials.query.filter_by(id=id).first()
    social = socials.query.all()
    names = cIndex_name.query.all()

    return render_template("socialsUpdate.html",allinfo = infos,social = social,names=names)

    
@app.route('/socialsDel/<int:id>')
def delete_social(id):
    infos = socials.query.filter_by(id=id).first()
    db.session.delete(infos)
    db.session.commit()
    info = socials(id="id", name="name",mimetype="minetype",img="img",social="social",social_link="social_link")
    allinfo=socials.query.all()
    return redirect("/socials")


@app.route('/cIndex')
def cIndex():
    background_color = '#FF0000'  # Red color
    text_color = '#FFFFFF' 
    allinfo = index_phara.query.all()
    social = socials.query.all()
    names = cIndex_name.query.all()
    selfs=cIndex_img_self.query.all()
    bigs=cIndex_img_big.query.all()
    certificates=certdb.query.all()
    return render_template('cIndex.html',selfs=selfs,certificates=certificates,allinfo = allinfo,names = names,social = social,bigs=bigs, background_color=background_color, text_color=text_color)

@app.route('/cIndexName',methods=['GET','POST'])
def cIndexName():
    if request.method == 'POST':
        full_name = request.form['full-name']
        short_name = request.form['short-name']
        with app.app_context():
            db.reflect()
            # db.session.close()  # Close any existing sessions to avoid issues with dropping the table
            cIndex_name.__table__.drop(db.engine)
            db.create_all()
        info = cIndex_name(name = short_name, full_name=full_name)
        db.session.add(info)
        db.session.commit()
    allinfo = cIndex_name.query.all()
    social = socials.query.all()
    names = cIndex_name.query.all()
    return render_template("cIndexName.html",names=names,allinfo=allinfo,social = social)


@app.route('/cIndexNameDel/<int:id>',methods=['GET','POST'])
def cIndexNameDel(id):
    infos = cIndex_name.query.filter_by(id=id).first()
    db.session.delete(infos)
    db.session.commit()
    info = cIndex_name(name = "short_name", full_name="full_name")
    allinfo=cIndex_name.query.all()
    return redirect('/cIndexName')


@app.route('/cIndexNameUpd/<int:id>',methods=['GET','POST'])
def cIndexNameUpd(id):
    if request.method == "POST":
        full_name = request.form["full-name"]
        short_name = request.form["short-name"]
        info= cIndex_name.query.filter_by(id=id).first()
        info.name= short_name
        info.full_name= full_name
        db.session.add(info)
        db.session.commit()
        allinfo = cIndex_name.query.filter_by(id=id).first()
        return redirect('/cIndexName')
    allinfo = cIndex_name.query.filter_by(id=id).first()
    social = socials.query.all()
    names = cIndex_name.query.all()
    return render_template("cIndexNameUpd.html",names=names,allinfo=allinfo,social = social)



@app.route('/cIndexInp',methods=['GET','POST'])
def cIndexInp():
    print("sucesa")
    if request.method == 'POST':
        print("@sucesa@")
        print("@sucesa@")
        first_pa = request.form['first-pharagraph']
        second_pa = request.form['second-pharagraph']
        img  = index_phara(first_para=first_pa,second_para=second_pa)
        db.session.add(img)
        db.session.commit()
    allinfo = index_phara.query.all()
    social = socials.query.all()
    names = cIndex_name.query.all()

    return render_template('cIndexInp.html',names=names,allinfo = allinfo,social = social)


@app.route('/cIndexUpl/<int:id>',methods=['GET','POST'])
def cIndexUpl(id):
    if request.method == 'POST':
        first_pa = request.form['first-pharagraph']
        second_pa = request.form['second-pharagraph']
        infos = index_phara.query.filter_by(id=id).first()
        # img  = index_phara(first_para=first_pa,second_para=second_pa)
        infos.first_para=first_pa
        infos.second_para=second_pa
        db.session.add(infos)
        print(infos.first_para)
        print(infos.second_para)
        db.session.commit() 
        return redirect('/cIndexInp')
    infos = index_phara.query.filter_by(id=id).first()
    social = socials.query.all()
    names = cIndex_name.query.all()

    return render_template('cIndexUpl.html',names=names,infos = infos,social = social)

@app.route('/cIndexInp_del/<int:id>')
def cIndexDel(id):
    infos = index_phara.query.filter_by(id=id).first()
    db.session.delete(infos)
    db.session.commit()
    info = index_phara(first_para="first_para",second_para="second_para")
    allinfo=index_phara.query.all()
    return redirect('/cIndexInp')




@app.route('/upl',methods=['GET','POST'])
def upl():
    if request.method == 'POST':
        pic = request.files['pic']
        # print(dump(pic))
        if not pic:
            flash("'No pic uploaded!', bad request ")
            # return 'No pic uploaded!', 400

        filename = secure_filename(pic.filename)
        mimetype = pic.mimetype
        name_certi = request.form['upld_name']

        if not filename or not mimetype:
            flash("'No pic uploaded!', bad request ")
            # return 'Bad upload!', 400

        img = certdb(img=pic.read(), name=filename, mimetype=mimetype,name_certi=name_certi)
        db.session.add(img)
        db.session.commit()
        flash("IMAGE UPLOADED SUCESSFULLY! ")
        # return  'Img Uploaded!', 200
    allinfo=certdb.query.all()
    social = socials.query.all()
    names = cIndex_name.query.all()
    # infos=certdb.query.filter_by(id=id).first()
    return render_template('test.html',names=names,allinfo=allinfo,social = social)
        # db.session.commit()


@app.route('/upl/<int:id>')
def get_img(id):
    img = certdb.query.filter_by(id=id).first()
    if not img:
        return 'Img Not Found!', 404

    return Response(img.img, mimetype=img.mimetype)



# @app.route('/delete_cert/<int:id>')
@app.route('/<int:id>')
def delete_cert(id):
    infos = certdb.query.filter_by(id=id).first()
    db.session.delete(infos)
    db.session.commit()
    info = certdb(id="id", name="name",mimetype="minetype",img="img",name_certi="name_certi")
    allinfo=certdb.query.all()
    # if b():
    #     return redirect("test.html")
    # print(allinfo)
    # return render_template("/test.html" , allinfo = allinfo)
    return redirect("/upl")


@app.route("/upl_update/<int:id>",  methods=['GET','POST'])
def upl_update(id):
    if request.method ==  "POST":
        # allinfo = Img.qurey.all()
        print("sucess")
        pic = request.files['pic']
        filename = secure_filename(pic.filename)
        print(filename)
        mimetype = pic.mimetype
        name_certi = request.form['upld_name']
        if not filename or not mimetype:
            flash("'No pic uploaded!', bad request ")

            

        flash(" updated SUCESSFULLY! ")
        infos=certdb.query.filter_by(id=id).first()
        infos.img = pic.read()
        infos.name = filename
        infos.mimetype = mimetype
        infos.name_certi=name_certi
        # infos = Img(img=pic.read(),name=filename,mimetype=mimetype)
        db.session.add(infos)
        print(infos.id,infos.name,infos.mimetype,infos.img,infos.name_certi)
        db.session.commit()
        
        return redirect('/upl')
    # allinfo = Img.query.all()
    infos=certdb.query.filter_by(id=id).first()
    social = socials.query.all()
    names = cIndex_name.query.all()
    return render_template('update2.html',names=names, infos = infos,social = social)

@app.route("/update/<int:id>",  methods=['GET','POST'])
def update(id):
    if request.method ==  "POST":
        print("succcess")
        project_name = request.form['project_name']
        project_language = request.form['project_language']
        pic = request.files['pic']
        filename = secure_filename(pic.filename)
        print(filename)
        project_reach_link=request.form['project_reach_link']
        project_description = request.form['project_desc']
        mimetype = pic.mimetype
        if not filename or not mimetype:
            flash("'No pic uploaded!', bad request ")
        flash("' pic uploaded!' sucessufully ")
        infos = projectdb.query.filter_by(id=id).first()
        infos.project_name = project_name
        infos.project_language = project_language
        infos.img = pic.read()
        infos.name= filename
        infos.mimetype = mimetype
        infos.project_description = project_description
        infos.project_reach_link = project_reach_link
        db.session.add(infos)
        db.session.commit()
        # print(infos.id,infos.name,infos.mimetype,infos.img,infos.name_certi)
        db.session.commit()
        return redirect('/upload')
        
      
    # allinfo = Img.query.all()
    infos=projectdb.query.filter_by(id=id).first()
    social = socials.query.all()
    names = cIndex_name.query.all()
    return render_template('update.html',names=names, infos = infos,social = social)


    


@app.route('/contact' , methods=['GET','POST'])
def contact():
    if request.method == "POST":
        
        name = request.form['name']
        email = request.form['email']
        pa = request.form['pa']
        info = User(name=name, email=email, pa=pa)
        db.session.add(info)
        db.session.commit()
        if name=="" or email =="" or pa=="":
            flash("THIS FIELDS CANNOT BE EMPTY")
            info = User(name="name", email="email", pa="pa")
            allinfo=User.query.all()
            return render_template('contact.html' , allinfo =allinfo)
        if name == "tarun" and pa =="tarun" :
            info = User(name="name", email="email", pa="pa")
            allinfo=User.query.all()
            print("succcess")
            return render_template('admin.html', allinfo=allinfo)
        else:
            flash("MESSAGE SENT SUCESSFULLY! ")

    allinfo = User.query.all()
    social = socials.query.all()
    names = cIndex_name.query.all()
    return render_template('contact.html',names=names,  allinfo=allinfo,social = social)


@app.route('/delete/<int:id>')
def delete(id):
    infos = User.query.filter_by(id=id).first()
    db.session.delete(infos)
    db.session.commit()
    info = User(name="name", email="email", pa="pa")
    allinfo=User.query.all()
    # print(allinfo)
    return render_template("admin.html" , allinfo = allinfo)


@app.route('/deletee/<int:id>')
def deletee(id):
    infos = projectdb.query.filter_by(id=id).first()
    db.session.delete(infos)
    db.session.commit()
    info = projectdb(project_name="project_name", project_language="project_language", name="name",mimetype="minetype",img="img", project_description="project_description", project_reach_link="project_reach_link")
    allinfo=projectdb.query.all()
    # return render_template("upload.html" , allinfo = allinfo)
    return redirect("/upload")



@app.route('/logadmin' , methods=['GET','POST'])
def logadmin():
    if request.method == "POST":
        name = request.form['name']
        pa = request.form['pa']
        if name == "tarun" and pa =="tarun":
            allinfo=User.query.all()
            return render_template('admin.html', allinfo=allinfo)
    social = socials.query.all()
    names = cIndex_name.query.all()
    return render_template('logadmin.html',names=names,social = social)






@app.route("/about")
def about():
    social = socials.query.all()
    names = cIndex_name.query.all()
    allinfo= cIndex_img_self.query.all()
    pahara = about_phara.query.all()
    return render_template('about.html',names=names,social = social,allinfo=allinfo,pahara=pahara)



    
@app.route("/projects")
def projects():
    imge = os.path.join('static', 'Image')
    print("succcess")
    files = os.path.join(imge, 'coding.jpg')
    files1 = "static/coding.jpg"
    social = socials.query.all()
    allinfo = projectdb.query.all()
    names = cIndex_name.query.all()
    # print(allinfo)
    return render_template('project.html',names=names,allinfo=allinfo,social = social, image = files1)


@app.route("/certi")
def certi():
    social = socials.query.all()
    allinfo=certdb.query.all()
    names = cIndex_name.query.all()
    return render_template('certificate.html',names=names,allinfo=allinfo,social = social)





@app.route("/uploadUpd/<int:id>",  methods=['GET','POST'])
def uploadUpd(id):
    if request.method ==  "POST":
        print("succcess")
        project_name = request.form['project_name']
        project_language = request.form['project_language']
        pic = request.files['pic']
        filename = secure_filename(pic.filename)
        print(filename)
        mimetype = pic.mimetype
        if not filename or not mimetype:
            flash("'No pic uploaded!', bad request ")
        flash("' pic uploaded!' sucessufully ")
        project_description = request.form['project_desc']
        project_reach_link = request.form['project_reach_link']
        infos = projectdb.query.filter_by(id=id).first()
        infos.project_name = project_name
        infos.project_language = project_language
        infos.img = pic.read()
        infos.name= filename
        infos.mimetype = mimetype
        infos.project_description = project_description
        infos.project_reach_link = project_reach_link
        db.session.add(infos)
        db.session.commit()
        return redirect('upload.html')
    infos=projectdb.query.filter_by(id=id).first()
    social = socials.query.all()
    names = cIndex_name.query.all()
    return render_template('update.html',names=names, infos = infos,social = social)



@app.route("/upload",  methods=['GET','POST'])
def upload():
    files1 = "static/coding.jpg"
    if request.method ==  "POST":
        
        imge = os.path.join('static', 'Image')
        print("succcess")
        files = os.path.join(imge, 'coding.jpg')
        project_name = request.form['project_name']
        project_language = request.form['project_language']
        pic = request.files['pic']
        filename = secure_filename(pic.filename)
        print(filename)
        mimetype = pic.mimetype
        project_description = request.form['project_desc']
        project_reach_link = request.form['project_reach_link']
   
        if not filename or not mimetype:
            flash("'default pic uploaded!', bad request ")
        flash("' pic uploaded!' sucessufully ")
        allinfo = projectdb(project_name=project_name, project_language=project_language,name=filename,mimetype=mimetype,img=pic.read() , project_description= project_description, project_reach_link=project_reach_link)
        db.session.add(allinfo)
        db.session.commit()
        return redirect('upload')
    # infos=projectdb.query.filter_by(id=id).first()
    allinfo = projectdb.query.all()
    social = socials.query.all()
    names = cIndex_name.query.all()
    return render_template('upload.html',names=names, allinfo=allinfo,social = social,image = files1)



@app.route('/upload/<int:id>')
def get_img_project(id):
    img = projectdb.query.filter_by(id=id).first()
    if not img:
        flash("' Image Not found ")

    return Response(img.img, mimetype=img.mimetype)


@app.route("/chat_bot",  methods=['GET','POST'])
def chat_bot():
    s='trial'
    if request.method=='POST':
        query = request.form['query']
        query = str(query)
        # print(len(query),'query length')
        # print(,"hello")
        print(len(query),query)
        # string_without_spaces = query.replace(" ", "")
        for i in query:
            if i.isalnum():
                s= generator(query)
                response = s.text_generation()
                response = str(response)
                return render_template('chat_bot.html',response=response)  
                return render_template('chat_bot.html',response=s)
                break

            # return redirect('/home') 
        else:
            s="length prob"
            return render_template('chat_bot.html',response=s)  
    chat = chat_bot_class.query.all()
    img = cIndex_img_self.query.all()

        # return render_template('index.html',response=s)
    return render_template('chat_bot.html',response=s, chat=chat ,image_user=img)





@app.route('/chat_bot/<int:id>',methods=['GET','POST'])
def chat_bot_int(id):
    chat = chat_bot_class.query.filter_by(id=id).first()
    return render_template('chat_bot.html', chat = chat)


@app.route('/chat_bot_del/<int:id>',methods=['GET','POST'])
def chat_bot_upl(id):

    infos = chat_bot_class.query.filter_by(id=id).first()
    db.session.delete(infos)
    db.session.commit()

    return redirect('/chat_bot')



@app.route('/aboutInp',methods=['GET','POST'])
def aboutInp():
    if request.method == 'POST':
        first_pa = request.form['about_phara']
        data  = about_phara(first_para=first_pa)
        db.session.add(data)
        db.session.commit()
    allinfo = about_phara.query.all()
    social = socials.query.all()
    names = cIndex_name.query.all()

    return render_template('aboutInp.html',names=names,allinfo = allinfo,social = social)


@app.route('/aboutUpl/<int:id>',methods=['GET','POST'])
def aboutUpl(id):
    if request.method == 'POST':
        first_pa = request.form['about_phara']
        infos = about_phara.query.filter_by(id=id).first()
        infos.first_para=first_pa
        db.session.add(infos)
        db.session.commit() 
        return redirect('/aboutInp')
    infos = about_phara.query.filter_by(id=id).first()
    social = socials.query.all()
    names = cIndex_name.query.all()
    return render_template('about_update.html',names=names,infos = infos,social = social)

@app.route('/aboutInp_del/<int:id>')
def aboutDel(id):
    infos = about_phara.query.filter_by(id=id).first()
    db.session.delete(infos)
    db.session.commit()
    info = about_phara(first_para="first_para")
    allinfo=about_phara.query.all()
    return redirect('/aboutInp')



@app.route('/resume',methods=['GET','POST'])
def resume():
    if request.method=='POST':
        file = request.files['file']
        upload = Pdf(filename=file.filename,data=file.read())
        with app.app_context():
                db.reflect()
                db.session.close()  # Close any existing sessions to avoid issues with dropping the table
                cIndex_img_self.__table__.drop(db.engine)
                db.create_all()
        db.session.add(upload)
        db.session.commit()
        return redirect('/resume')
    resume = Pdf.query.all()
    return render_template('resume.html',resume=resume) 

@app.route("/download/resume/<upload_id>")
def download(upload_id):
    upload = Pdf.query.filter_by(id=upload_id).first()
    return send_file(BytesIO(upload.data),as_attachment=True,download_name=upload.filename)

@app.route('/delete/resume/<upload_id>')
def delete_pdf(upload_id):
    infos = Pdf.query.filter_by(id=upload_id).first()
    db.session.delete(infos)
    db.session.commit()
    return redirect("/resume")


@app.route("/color_c",methods=['GET','POST'])
def color_cc():
    if request.method=='POST':
        # test=request.form['color_test']
        body_color=request.form['body_color']
        font=request.form['font']
        font_style=request.form['font_style']
        card_color_bg=request.form['card_color_bg']
        project_card_color=request.form['project_card_color']
        project_card_font=request.form['project_card_font']
        project_card_button_color=request.form['project_card_button_color']
        project_card_font_color=request.form['project_card_font_color']
        certi_color=request.form['certi_color']
        certi_font=request.form['certi_font']
        certi_font_color=request.form['certi_font_color']
        adout_bg_color=request.form['adout_bg_color']
        about_font_color=request.form['about_font_color']
        contact_bg=request.form['contact_bg']
        info = color_c(body_color=body_color,font=font,font_style=font_style,card_co_lor_bg=card_color_bg,project_card_button_color=project_card_button_color,project_card_color=project_card_color,project_card_font=project_card_font,project_card_font_color=project_card_font_color,certi_color=certi_color,certi_font=certi_font,certi_font_color=certi_font_color,adout_bg_color=adout_bg_color,about_font_color=about_font_color,contact_bg=contact_bg)
        with app.app_context():
                db.reflect()
                # db.session.close()  # Close any existing sessions to avoid issues with dropping the table
                color_c.__table__.drop(db.engine)
                db.create_all()
        db.session.add(info)
        db.session.commit()
        return redirect('/color_c')
    flash('color deleted')
    colors=color_c.query.all()
    return render_template('color_c.html',colors=colors)

@app.route('/delete/color_c_del/<int:id>')
def color_c_Del(id):
    infos = color_c.query.filter_by(id=id).first()
    db.session.delete(infos)
    db.session.commit()
    
    return redirect('/color_c')


@app.route("/color_c_upd/<int:id>",methods=['GET','POST'])
def color_upd(id):
    if request.method=='POST':
        # test=request.form['color_test']
        body_color=request.form['body_color']
        font=request.form['font']
        font_style=request.form['font_style']
        card_color_bg=request.form['card_color_bg']
        project_card_color=request.form['project_card_color']
        project_card_font=request.form['project_card_font']
        project_card_button_color=request.form['project_card_button_color']
        project_card_font_color=request.form['project_card_font_color']
        certi_color=request.form['certi_color']
        certi_font=request.form['certi_font']
        certi_font_color=request.form['certi_font_color']
        adout_bg_color=request.form['adout_bg_color']
        about_font_color=request.form['about_font_color']
        contact_bg=request.form['contact_bg']
        infos = color_c.query.filter_by(id=id).first()
        infos.body_color=body_color
        infos.font=font
        infos.font_style=font_style
        infos.card_co_lor_bg=card_color_bg
        infos.project_card_button_color=project_card_button_color
        infos.project_card_color=project_card_color
        infos.project_card_font=project_card_font
        infos.project_card_font_color=project_card_font_color
        infos.certi_color=certi_color
        infos.certi_font=certi_font
        infos.certi_font_color=certi_font_color
        infos.adout_bg_color=adout_bg_color
        infos.about_font_color=about_font_color
        infos.contact_bg=contact_bg
        db.session.add(infos)
        db.session.commit()

        return redirect('/color_c')
    flash('color deleted')
    colors=color_c.query.filter_by(id=id).first()
    return render_template('color_c_upd.html',colors=colors)

if __name__=="__main__":

    app.run(debug=True, port=2000) 