# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 19:50:14 2020

@author: My Pc
"""

class Artigo(db.Model):
    __tablename__ = 'artigos'
    id = db.Column(db.Integer, primary_key=True)
    id_sub_tipo_artigo =db.Column(db.Integer, db.ForeignKey('sub_tipo_artigos.id'))
    id_servico = db.Column(db.Integer, db.ForeignKey('servicos.id'))
    name = db.Column(db.String(64), unique=True)
    
    def __repr__(self):
        return '<Artigo %r>' % self.name
    

class Tipo_Artigo(db.Model):
    __tablename__ = 'tipo_artigos'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    
    def __repr__(self):
        return '<Tipo_artigo %r>' % self.name
    



class Sub_Tipo_Artigo(db.Model):
    __tablename__ = 'sub_tipo_artigos'
    id = db.Column(db.Integer, primary_key=True)
    id_tipo_artigo =db.Column(db.Integer, db.ForeignKey('tipo_artigos.id'))
    name = db.Column(db.String(64))
    
    def __repr__(self):
        return '<Sub_Tipo_Artigo %r>' % self.name

class Tipo_Caracterisitica(db.Model):
    __tablename__ = 'tipo_caracteristicas'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    def __repr__(self):
        return '<Tipo_Caracterisitica %r>' % self.name
    
        
class Fam_Caracterisitica(db.Model):
    __tablename__ = 'fam_caracteristicas'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    id_tipo_caracteristica = db.Column(db.Integer, db.ForeignKey('tipo_caracteristicas.id'))
    def __repr__(self):
        return '< Fam_Caracterisitica %r>' % self.name
    
    
class Caracterisitica(db.Model):
    __tablename__ = 'caracteristicas'
    id = db.Column(db.Integer, primary_key=True)
    id_fam_caracteristica = db.Column(db.Integer, db.ForeignKey('fam_caracteristicas.id'))
    name = db.Column(db.String(64))
    def __repr__(self):
        return 'Caracterisitica %r>' % self.name
    
    
    