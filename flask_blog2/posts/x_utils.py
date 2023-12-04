import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flask_blog2 import mail


def save_blogpicture(form_blogpicture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_blogpicture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/blog_pics', picture_fn)

    output_size = (300 , 300)
    i = Image.open(form_blogpicture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn