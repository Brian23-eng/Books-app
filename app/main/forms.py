from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class CommentForm(FlaskForm):
    
    title = StringField('Comment title', validators = [DataRequired()])

    comment = TextAreaField('Comment review')

    submit = SubmitField('Submit')
