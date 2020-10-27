
from . import artigos
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from flask import Markup
from ..models import User, Role, Restaurant

from .forms import  FormArtigo, FormProcurarArtigo
from .. import db

@artigos.route('/')
@login_required
def index():
    
        
    return render_template('view.html', header='Artigos', columns =["Id","Producto","Familia","Serviço"],rows= lista, tabletype="striped", objecto="Artigos", titulo ="Artigos", form=form)
    
    
    


@artigos.route('/edit<id>')
@login_required
def edit(id):
    return str(id)
    
    
@artigos.route('/criar', methods=['GET', 'POST'])
@login_required
def criar():
    servicos = Servico.query.all()
    atributos=Fam_Caracterisitica.query.options(db.joinedload('caracteristicas')).all()
    lista=[]
    for atributo in atributos:
        a=[atributo.name]
        for caracteristicas in atributo.caracteristicas:
            a.append(caracteristicas)
        lista.append(a)
    
    if request.method == "POST":
        data = request.form
        artigo=Artigo(id_familia =1, id_servico =data["servico"], name=data["nome"] )
        
        #for cara in data:
            
        #caracteristicas
        print(data)
        for (key, val) in data.items():
            if key.startswith("atributo"):
                
                a=Artigo_Caracterisitica(id_caracteristica=int(val))
                artigo.artigos_caracteristicas.append(a)
        db.session.add(artigo)
        db.session.commit()
        return redirect(url_for('artigos.index'))
        
        
        
    
    return render_template('criar_artigo.html',id=3, tabtype="primary", header="Atributos", items=lista, servicos=servicos)
    


@artigos.route('/delete<id>')
@login_required
def delete(id):
    pass
    