from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)


class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True)
    url = Column(String, unique=True)


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)


class UserLinkTag(Base):
    __tablename__ = "user_link_tag"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    link_id = Column(Integer, ForeignKey("links.id"))
    tag_id = Column(Integer, ForeignKey("tags.id"))

    user = relationship("User")
    link = relationship("Link")
    tag = relationship("Tag")


engine = create_engine("sqlite:///./db.db")
# Base.metadata.create_all(engine)
#
from sqlalchemy.orm import sessionmaker

#
Session = sessionmaker(bind=engine)
session = Session()
#
# user1 = User(username='user1', email='user1@example.com', password='password1')
# user2 = User(username='user2', email='user2@example.com', password='password2')
# link = Link(url='example.com')
#
# session.add(user1)
# session.add(user2)
# session.add(link)
#
# tag1 = Tag(name='tag1')
# tag2 = Tag(name='tag2')
# tag3 = Tag(name='tag3')
# tag4 = Tag(name='tag4')
#
# user_link_tag1 = UserLinkTag(user=user1, link=link, tag=tag1)
# user_link_tag2 = UserLinkTag(user=user1, link=link, tag=tag2)
# user_link_tag3 = UserLinkTag(user=user2, link=link, tag=tag3)
# user_link_tag4 = UserLinkTag(user=user2, link=link, tag=tag4)
#
# session.add(tag1)
# session.add(tag2)
# session.add(tag3)
# session.add(tag4)
#
# session.add(user_link_tag1)
# session.add(user_link_tag2)
# session.add(user_link_tag3)
# session.add(user_link_tag4)
#
# session.commit()


result = (
    session.query(Link)
    .join(UserLinkTag)
    .join(User)
    .join(Tag)
    .filter(User.username == "user1")
    .filter(Tag.name == "tag2")
    .all()
)
for link in result:
    print(link.__dict__)
