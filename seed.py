"""seed file to make a sample data"""

from models import User, Post, db
from app import app

"""Create table"""
db.drop_all()
db.create_all()


u1 = User(first_name='John', last_name="Butlor")
u2 = User(first_name='Joel', last_name="Paul")
u3 = User(first_name='Greta', last_name="Thunberg",
          img_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJc55b62rSWDtwHGbNrGjLyAGsa6S4GCn3LHE2Yxe1qBsreWcA0vpEeNoojxkmGAhUbOw&usqp=CAU')
u4 = User(first_name='Samuel', last_name="James")


db.session.add(u1)
db.session.add(u2)
db.session.add(u3)
db.session.add(u4)
db.session.commit()

p1 = Post(title='See John Post',
          content='This is my very first post nothing much to write', user_id=1)

p2 = Post(title='See Joel Post',
          content='This is my very first post nothing much to write', user_id=2)

p3 = Post(title='See Greta Post',
          content='This is my very first post nothing much to write', user_id=3)


db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.commit()
