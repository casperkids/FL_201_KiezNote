import os
import secrets
from PIL import Image
from datetime import datetime 
from flask import (render_template, url_for, flash, current_app, 
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename
from flask_blog2 import db
from flask_blog2.models import Post
from flask_blog2.posts.forms import PostForm


posts = Blueprint('posts', __name__)


@posts.route("/post/new",  methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    blogpicture = None
    if form.validate_on_submit():
        #picture
        blogpicture_file = save_blogpicture(form.blogpicture.data)
        post = Post(
            title=form.title.data,
            content=form.content.data,
            author=current_user,
            blogpicture=blogpicture_file
        )
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', form=form, legend='New Post')


@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        if form.blogpicture.data:
            blogpicture_file = save_blogpicture(form.blogpicture.data)
            post.blogpicture = blogpicture_file
        post.title = form.title.data
        post.content = form.content.data
        post.updated_at = datetime.utcnow()
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    blogpicture = url_for('static', filename=f'blog_pics/{post.blogpicture}')
    return render_template('create_post.html', title='Update Post', form=form, blogpicture=blogpicture, legend='Update Post')

@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
     post = Post.query.get_or_404(post_id)
     if post.author != current_user:
        abort(403)
     db.session.delete(post)
     db.session.commit()
     flash('Your post has been deleted!', 'success')
     return redirect(url_for('main.home'))


#savepicture
def save_blogpicture(form_blogpicture):
    if form_blogpicture:
        random_hex = secrets.token_hex(8)
        _, f_ext = os.path.splitext(secure_filename(form_blogpicture.filename))
        picture_fn = random_hex + f_ext
        picture_path = os.path.join(current_app.root_path, 'static/blog_pics', picture_fn)

        output_size = (300, 300)
        i = Image.open(form_blogpicture)
        i.thumbnail(output_size)
        i.save(picture_path)

        return picture_fn
   
