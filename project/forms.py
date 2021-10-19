from flask_wtf import FlaskForm
from wtforms.fields import HiddenField
from wtforms import SelectField, FloatField, SubmitField, DateField, TimeField
from wtforms.validators import NumberRange
from project.models import *

class Formulary(FlaskForm):
    date= DateField("date")
    time= TimeField("time")
    moneda_from = SelectField(u"From", choices=['Monedas','EUR', 'ETH', 'LTC','BNB', 'EOS', 'XLM', 'TRX', 'BTC', 'XRP', 'BCH', 'USDT', 'BSV', 'ADA'])
    cantidad_from = FloatField("Q", validators=[NumberRange(message="Debe de ser un importe positivo")])
    moneda_to= SelectField("To", choices=['Monedas','EUR', 'ETH', 'LTC','BNB', 'EOS', 'XLM', 'TRX', 'BTC', 'XRP', 'BCH', 'USDT', 'BSV', 'ADA'])
    pu= FloatField("P.U", validators=[])
    puH= HiddenField()
    cantidad_to= FloatField("Q:", validators=[])
    cantidad_toH= HiddenField()
    calculator = SubmitField("Calcular")
    submit = SubmitField('Aceptar')