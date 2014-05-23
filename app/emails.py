# -*- coding: utf-8 -*-
from flask.ext.mail import Message
from decorators import async
from app import mail, app


@async
def send_async_email(msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, recipients, text_body, html_body):
    """Sends mail from DEFAULT_MAIL_SENDER to given recipients"""
    msg = Message(subject, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    send_async_email(msg)


def send_all(messages):
    """Sends given messages over single connection"""
    with mail.connect() as conn:
        for msg in messages:
            conn.send(msg)
