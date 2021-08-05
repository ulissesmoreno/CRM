from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Categoria, User
from . import db
import json
import pandas as pd

views = Blueprint('views', __name__)

@views.route('/lista_user', methods=['GET','POST'])
@login_required

def lista_user():
    cat = User.query.all()
    return render_template("lista_user.html", user=current_user, cat=cat)

@views.route('/fornec', methods=['GET','POST'])
@login_required
def fornec():
    if request.method == 'POST1': #mudar
        razaoSocial = request.form.get('cat')
        nomeFantasia = request.form.get('cat')
        cate = request.form.get('cat')

        if len(cat) < 1:
            flash('Categoria muito curta', category='error')
        else:
            new_cat = Categoria(data=cat)
            db.session.add(new_cat)
            db.session.commit()
            flash('Categoria Cadastrada', category='success')

    cat = Categoria.query.all()
    return render_template("fornec.html", user=current_user, cat=cat)

@views.route('/cat', methods=['GET','POST'])
@login_required
def cat():
    if request.method == 'POST':
        cat = request.form.get('cat')

        if len(cat) < 1:
            flash('Categoria muito curta', category='error')
        else:
            new_cat = Categoria(data=cat)
            db.session.add(new_cat)
            db.session.commit()
            flash('Categoria Cadastrada', category='success')

    cat = Categoria.query.all()
    return render_template("categorias.html", user=current_user, cat=cat)

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short.', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_cat():
    note = json.loads(request.data)
    noteId = note['catId']
    note = Note.query.get(catId)
    if note:
        #if note.user_id == current_user.id:
        db.session.delete(cat)
        db.session.commit()

    return jsonify({})