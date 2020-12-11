from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired, Length

# class RecommendationForm(FlaskForm):
#     race = StringField('Race', validators=[DataRequired(), Length(min=2, max=20)])
#     race = SelectField(u'Race', choices=[('cpp')])