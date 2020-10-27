from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField,SelectMultipleField
from wtforms.validators import DataRequired, Length, Email

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

class EmpregadoForm(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),Email()])
    phone = StringField('Telefone', validators=[DataRequired(), Length(9)])
    submit = SubmitField('Criar')


class EncaminhamentoForm(FlaskForm):
    fam_encaminhamento_id = SelectField(u'Familia Encaminhamento', coerce=int)
    servico_id = SelectField(u'Serviço', coerce=int)
    terminal_empregado_id = SelectField(u'Terminal Empregado', coerce=int)
    mesas=SelectMultipleField(u'Mesas',coerce=int)
    
    
    submit = SubmitField('Criar')
    
    
class SearchEncaminhamentoForm(FlaskForm):
    fam_encaminhamento_id = SelectField(u'Familia Encaminhamento', coerce=int)
    
    
   
    submit = SubmitField('submit')
    
    
class DefaultEncaminhamentoForm(FlaskForm):
    fam_encaminhamento_id = SelectField(u'Familia Teste', coerce=int)
    
    
   
    submit1 = SubmitField('Definir')
    
class Fam_atributos(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    tipo= SelectField(u'Tipo', coerce=int)
    submit = SubmitField('Criar')

class Atributos(FlaskForm):
    name = StringField('Nome', validators=[DataRequired()])
    
    submit = SubmitField('Criar')
    