from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    searching = StringField('Поиск')
    sorting = SelectField('Агломерация', validators=[DataRequired()], choices=['По расстоянию', 'По цене'])
    submit = SubmitField('Поиск')