from . import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime



class Books:
    '''
    Books class to define the book objects
    '''
    def __init__(self, rank, title,author,poster, description, publisher):
        self.rank = rank
        self.title = title
        self.author = author
        self.poster = poster
        self.description = description
        self.publisher = publisher
        
class Preview:
    '''
    Show book previews
    
    '''
    
    def __init__(self,rank, title,author,poster, description, publisher):
        self.rank = rank
        self.title = title
        self.author = author
        self.poster = poster
        self.description = description
        self.publisher = publisher
        
        
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class User(UserMixin,db.Model):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)

    username = db.Column(db.String(255),index = True)

    email = db.Column(db.String(255),unique = True,index = True)

    image_file = db.Column(db.String(255), nullable=False, default='default.jpg')

    password_hash = db.Column(db.String(255))
    
    
    comment = db.relationship('Comment',backref = 'user',lazy = "dynamic")
    @property
    def password(self):
        raise AttributeError("You cannot read the password attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
   

   

    def __repr__(self):

        return f'User {self.username}'
    


class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)

    # book_rank = db.Column(db.Integer, db.ForeignKey("book.rank"))

    title = db.Column(db.String(255))

    comment = db.Column(db.String(255))

    posted = db.Column(db.DateTime,default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    @classmethod

    def get_comments(cls, id):

        comments = Comment.query.filter_by(book_rank = id).all()

        return comments

    def delete_comment(self):

        db.session.delete(self)

        db.session.commit()
        
        

