from flask_wtf import FlaskForm
from wtforms import SelectField, FloatField, SubmitField, DateField, TimeField
from wtforms.validators import NumberRange

class MovimientosFormulario(FlaskForm):
    date= DateField("date")
    hora= TimeField("time")
    moneda1 = SelectField("From", choices=['EUR', 'ETH', 'LTC','BNB', 'EOS', 'XLM', 'TRX', 'BTC', 'XRP', 'BCH', 'USDT', 'BSV', 'ADA'])
    cantidad = FloatField("Q", validators=[NumberRange(message="Debe de ser un importe positivo")])
    moneda2= SelectField("To", choices=['EUR', 'ETH', 'LTC','BNB', 'EOS', 'XLM', 'TRX', 'BTC', 'XRP', 'BCH', 'USDT', 'BSV', 'ADA'])
    calculator = SubmitField("Calculator")
    submit = SubmitField('Aceptar')