from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean

from .database import Base


user_link_association_table = Table(
    "user_link_association",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("link_id", Integer, ForeignKey("links.id")),
)
link_tag_association_table = Table(
    "link_tag_association",
    Base.metadata,
    Column("link_id", Integer, ForeignKey("links.id")),
    Column("tag_id", Integer, ForeignKey("tags.id")),
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    is_active = Column(Boolean, default=False)
    links = relationship("Link", secondary=user_link_association_table)


class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String, unique=True)

    tags = relationship("Tag", secondary=link_tag_association_table)


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)

    links = relationship("Link", secondary=link_tag_association_table)
