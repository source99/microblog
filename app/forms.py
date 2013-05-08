import re
from flask.ext.wtf import Form, TextField, BooleanField, TextAreaField
from flask.ext.wtf import Required, Length
from app.models import User

class LoginForm(Form):
	email = TextField('email', validators = [Required()])
	password = TextField('password', validators = [Required()])
	

class EditForm(Form):
	nickname = TextField('nickname', validators = [Required()])
	about_me = TextAreaField('about_me', validators = [Length(min = 0, max = 140)])

	def __init__(self, original_nickname, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)
		self.original_nickname = original_nickname

	def validate(self):
		if not Form.validate(self):
			return False
		if self.nickname.data == self.original_nickname:
			return True
		user = User.query.filter_by(nickname = self.nickname.data).first()
		if user != None:
			self.nickname.errors.append('This nickname is already in use. Please choose another one.')
			return False
		return True		
	
	
class signupForm(Form):
	email = TextField('email', validators = [Required()])
	password = TextField('password', validators = [Required()])


#	def __init__(self, original_email, *args, **kwargs):
#		Form.__init__(self, *args, **kwargs)
#		self.original_email = original_email
	
	def validate(self):
		print "executing validate inside of signupForm class"
		if not Form.validate(self):
			return False
		#check its valid email form
		email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
		if not email_regex.match(self.email.data):
			self.email.errors.append('This is not a valid email address format')
			print "invalid email - False"
			return False
		#check the email address doesn't exist already
		user = User.query.filter_by(email = self.email.data).first()
		if user != None:
			self.email.errors.append('This email is already used')
			print "email already exists"
			return False
		#check its a valid passowrd
		password_regex = re.compile(r"[a-z]")
		if not password_regex.match(self.password.data):
			self.password.errors.append('This password is not valid even though the proper rules have not been defined')
			print "password not valid"
			return False
		return True
	
class PostForm(Form):
	post = TextField('post', validators = [Required()])

class SearchForm(Form):
	search = TextField('search', validators = [Required()])			
		
			