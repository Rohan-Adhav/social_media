from sqlalchemy import Column,Integer,String,create_engine,ForeignKey
from sqlalchemy.orm import declarative_base,sessionmaker,relationship
from pydantic import BaseModel
from fastapi import FastAPI,HTTPException
Base =declarative_base()

class User(Base):
    __tablename__ = "users"
    id= Column(Integer,primary_key=True)
    name = Column(String)
    email = Column(String , unique=True)
    posts = relationship("Post" , back_populates="user")
class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer , primary_key=True)
    title = Column(String)
    content = Column(String)
    user_id = Column(Integer , ForeignKey("users.id"))
    user = relationship("User" , back_populates="posts")

URL = "mysql+pymysql://root:RootPass123!@localhost/blog_db"
engine = create_engine(URL , echo=True)

Session = sessionmaker(bind=engine)
session =Session()

Base.metadata.create_all(engine)

# adding users
# new_user = User(name="rohan", email="rohanadhav@gmail.com")
# session.add(new_user)
# user2 = User(name="Priya", email="priya@example.com")
# user3 = User(name="Amit", email="amit@example.com")

# session.add_all([user2, user3])
# session.commit()
# #adding posts 

# post1 = Post(title="post1" ,content="my content1" , user=new_user)
# post2 = Post(title="post2" ,content="my conten2" , user=new_user)

# posts = [
#     Post(title="post3", content="my content3", user=new_user),
#     Post(title="post4", content="my content4", user=new_user),
#     Post(title="post5", content="my content5", user=new_user)
# ]
# posts = [
#     Post(title="Priya Post 1", content="Content 1", user=user2),
#     Post(title="Priya Post 2", content="Content 2", user=user2),
#     Post(title="Amit Post 1", content="Content 1", user=user3)
# ]

# session.add_all(posts)
# session.commit()

# session.add_all(posts)
# session.commit()

# fetching them

# user = session.query(User).filter_by(name="Priya").first()

# for post in user.posts:
#     print(post.title , post.content)



class CreateUser(BaseModel):
    name:str
    email:str
   

class CreatePost(BaseModel):
    title:str
    content:str

class ReadPosts(BaseModel):
    id:int
    title:str
    content:str
    user_id : int

class ReadUser(BaseModel):
    id:int
    name:str
    email:str
    posts:list[ReadPosts] =[]


app = FastAPI()

@app.get("/users",response_model=list[ReadUser])
def get_users():
    users = session.query(User).all()
    return users

@app.post("/users",response_model=CreateUser)
def add_users(users:CreateUser):
    existing_user = session.query(User).filter(User.email==users.email).first()
    if existing_user:
        raise HTTPException( status_code=400 , detail=f"{users.email} already exists")
    new_user = User(name=users.name,email=users.email)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user

@app.get("/posts",response_model=list[ReadPosts])
def get_posts():
    posts = session.query(Post).all()
    return posts

@app.post("/posts",response_model=CreatePost)
def add_posts(post:CreatePost,user_id = int):
    existing_user = session.query(User).filter(User.id==user_id).first()
    if not existing_user:
        raise HTTPException(status_code=400 , detail="User Not found")
    new_posts = Post(title=post.title , content = post.content)
    session.add(new_posts)
    session.commit()
    session.refresh(new_posts)
    return new_posts
    
    