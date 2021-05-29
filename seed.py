"""seed file to make a sample data"""

from models import User, Post, db
from app import app

"""Create table"""
db.drop_all()
db.create_all()


u1 = User(first_name='John', last_name="Butlor")
u2 = User(first_name='Joel', last_name="Paul")
u3 = User(first_name='Greta', last_name="Thunberg", img_url='https: // www.google.com/imgres?imgurl=https % 3A % 2F % 2Fwww.ft.com % 2F__origami % 2Fservice % 2Fimage % 2Fv2 % 2Fimages % 2Fraw % 2Fhttps % 3A % 2F % 2Fd1e00ek4ebabms.cloudfront.net % 2Fproduction % 2Ff2baf2aa-1f27-4ed9-b372-f3826bbae401.jpg % 3Fsource % 3Dnext % 26fit % 3Dscale-down % 26quality % 3Dhighest % 26width % 3D1067 & imgrefurl=https % 3A % 2F % 2Fwww.ft.com % 2Fcontent % 2F6ee4bb03-3039-446a-997f-91a7aef5f137 & tbnid=jFehmAj9APIkwM & vet=12ahUKEwjjmuySru3wAhWiKn0KHfmbBv4QMygHegUIARDIAQ..i & docid=M01bvxEfKBtQ9M & w=1067 & h=600 & itg=1 & q=greta % 20thunberg & ved=2ahUKEwjjmuySru3wAhWiKn0KHfmbBv4QMygHegUIARDIAQ')
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
