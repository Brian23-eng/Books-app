from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Email,Length,EqualTo, DataRequired,ValidationError
from ..models import User



class LoginForm(FlaskForm):

    email = StringField('Your Email Address',validators=[Required(),Email()])

    password = PasswordField('Password',validators =[Required()])

    remember = BooleanField('Remember me')

    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):

    email = StringField('Your Email Address',validators=[Required(),Email()])

    username = StringField('Enter your username',validators = [Required()])

    password = PasswordField('Password',validators = [Required(),

    EqualTo('confirm_password',message = 'Passwords must match')])

    confirm_password = PasswordField('Confirm Passwords',validators = [Required()])

    submit = SubmitField('Sign Up')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('That username is already taken.')

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('An account by that email already exists.')
    
class RequestResetForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('There is no account with that email. You must register first.')
        
class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')

