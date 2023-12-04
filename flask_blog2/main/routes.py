from flask import render_template, request, Blueprint
from flask_blog2.models import Post, User
#from flask import flash

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.updated_at.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')

#index
@main.route("/index")
def index():
    users = User.query.all()
    page = request.args.get('page', 1, type=int)
    users = User.query.paginate(page=page, per_page=5)
    #print(users)
    #flash(f'Number of users: {len(users)}', 'info')
    return render_template('index.html', title='Index', users=users)