
from project.views import *
from flask_wtf import FlaskForm
from wtforms.fields import HiddenField
from wtforms import SelectField, FloatField, SubmitField

from wtforms.validators import DataRequired, NumberRange
from project.__init__ import MONEDAS


class Formulary(FlaskForm):
    
    date= HiddenField()
    time= HiddenField()
    moneda_from = SelectField(u"From:", choices=(MONEDAS), validators=[DataRequired(message="Tiene que indicar la moneda")])
    cantidad_from = FloatField("Q:", validators=[DataRequired(message="Tiene que indicar la cantidad"),NumberRange(min=0.0001, message="Debe de ser un importe positivo")])
    moneda_to= SelectField(u"To:", choices=MONEDAS, validators=[DataRequired(message="Tiene que indicar la moneda")])
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
