from flask_wtf import FlaskForm
from wtforms import StringField, FileField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class AddOfferForm(FlaskForm):
    name = StringField('Название', validators=[DataRequired()])
    description = TextAreaField('Описание', validators=[DataRequired()])
    image = FileField('Фотография товара', validators=[DataRequired()])
    submit = SubmitField('Добавить товар')