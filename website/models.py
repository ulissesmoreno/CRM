from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    matricula = db.Column(db.String(150))
    id_clientes = db.relationship('Clientes')

class Clientes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_cadastro = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    data_nascimento = db.Column(db.DateTime(timezone=True))
    idade = (db.Integer)
    Empresa = db.Column(db.String(150))
    cargo = db.Column(db.String(150))
    Tratamento = db.Column(db.String(5))
    endereco_web = db.Column(db.String(150))
    telefone_comercial = db.Column(db.String(150))
    telefone_residencial = db.Column(db.String(150))
    telefone_celular = db.Column(db.String(150))
    rua = db.Column(db.String(150))
    uf = db.Column(db.String(2))
    cidade = db.Column(db.String(150))
    numero = db.Column(db.String(6))
    complemento = db.Column(db.String(150))
    cep = db.Column(db.String(9))

