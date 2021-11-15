
from wtforms.fields.core import IntegerField
from wtforms.fields.simple import TextField
from wtforms.widgets.core import Input
from project.views import *
from flask_wtf import FlaskForm
from wtforms.fields import HiddenField
from wtforms import SelectField, FloatField, SubmitField

from wtforms.validators import DataRequired, EqualTo, NumberRange
from project.models import MONEDAS




class Formulary(FlaskForm):
    
    date= HiddenField()
    time= HiddenField()
    moneda_from = SelectField(u"From:", choices=(MONEDAS), validators=[DataRequired(message="Tiene que indicar la moneda")])
    moneda_fromH= HiddenField()
    cantidad_from = FloatField("Q:", validators=[DataRequired(message="Tiene que indicar la cantidad"),NumberRange(min=0.0001, message="Debe de ser un importe positivo")])
    moneda_to= SelectField(u"To:", choices=MONEDAS, validators=[DataRequired(message="Tiene que indicar la moneda")])
    moneda_toH=HiddenField()
    pu= FloatField("P.U:", validators=[])
    puH= HiddenField()
    cantidad_to= FloatField("Q:")
    cantidad_toH= HiddenField()
    calculator = SubmitField("Calcular")
    submit = SubmitField('Aceptar')


   



class Formulary2(FlaskForm):
    invest= FloatField("Innversión:")
    investH = HiddenField()
    estado=FloatField("Valor actual:")
    estadoH= HiddenField()
