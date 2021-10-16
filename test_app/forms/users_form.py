from flask_wtf import FlaskForm
from wtforms import StringField, ValidationError
from test_app.models.user import User

class UserForm(FlaskForm):
    username = StringField("username")
    password = StringField("password")

    def validate_username(self, username):
        if username.data == "":
            raise ValidationError("Please enter your username.")
        
        if User.query.filter_by(username=username.data).first():
            raise ValidationError("It has already been registered.")
    
    def validate_password(self, password):
        if password.data == "":
            raise ValidationError("Please enter your password.")
