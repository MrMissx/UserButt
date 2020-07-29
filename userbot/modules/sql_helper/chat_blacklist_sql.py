try:
    from userbot.modules.sql_helper import SESSION, BASE
except ImportError:
    raise AttributeError
from sqlalchemy import Column, String


class BlChat(BASE):
    __tablename__ = "chat_blacklist"
    blacklisted = Column(String(14), primary_key=True)


BlChat.__table__.create(checkfirst=True)


def get_chatlist(chat_id):
    try:
        return SESSION.query(BlChat).get(blacklisted)
    finally:
        SESSION.clone()


def add_chatlist(chat_id):
    adder = BlChat(blacklisted)
    SESSION.add(adder)
    SESSION.commit()


def rm_chatlist(chat_id):
    rem = SESSION.query(BlChat).get(blacklisted)
    if rem:
        SESSION.delete(rem)
        SESSION.commit()