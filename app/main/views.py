from flask import Markup
from sqlalchemy import and_
from . import main
from . import auth
from ..models import User, Role, Restaurant
from flask_login import login_user, logout_user, login_required
from .forms import EmpregadoForm,  EncaminhamentoForm, SearchEncaminhamentoForm, DefaultEncaminhamentoForm, Fam_atributos, Atributos
from .. import db
from flask import render_template, redirect, request, url_for, flash
import datetime
@main.route('/index')
@login_required
def index():
    return render_template('index.html')

@main.route('/')
@login_required
def indexx():
    return render_template('index.html')


@main.route('/establecimentos')
@login_required
def establecimentos():
    esta= Restaurant.query.all()
    lista=[]
    for a in esta:
        lista.append([a.name,a.address,a.all_reviews_count, a.phone_numbers, a.average_cost_for_two])
    return render_template('establecimentos.html',header='Pedidos', columns =["Nome","Morada",'# Reviews','Telefone', 'Custo médio'],rows= lista, tabletype="striped")



@main.route('/familia_artigos')
@login_required
def familia_artigos():
    tipo_artigos= Tipo_Artigo.query.all()
    lista=[]
    for Empregados in tipo_artigos:
        
        
        lista.append([Empregados.id, Empregados.name])
        
    return render_template('fam_artigos.html', header='Familias Artigos', columns =["Id","Serviço"],rows= lista, tabletype="striped", objecto="familia_artigos", objectos="/familia_artigos/sub_familia_artigos/")
    
    
    


@main.route('/familia_artigos_edit/<id>')
@login_required
def artigos_edit(id):
    return render_template('index.html')




@main.route('/familia_artigos/sub_familia_artigos/<id>')
@login_required
def sub_familia_artigos(id):
    sub_tipo_artigos = Sub_Tipo_Artigo.query.filter_by(id_tipo_artigo=id)
    
    lista=[]
    for Empregados in sub_tipo_artigos:
        
        
        lista.append([Empregados.id, Empregados.name])
        
    return render_template('sub_fam_artigos.html', header='', columns =["Id","Serviço"],rows= lista, tabletype="striped", objecto="familia_artigos")


