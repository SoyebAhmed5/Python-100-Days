from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = '@123'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    image = db.Column(db.String(200), nullable=False)
    link = db.Column(db.String(200), nullable=False)


def seed_projects():
    if Project.query.first():
        return

    projects = [
        Project(
            title='AI Blog Platform',
            description='A smart blogging dashboard for publishing and managing content with metadata and AI-based recommendations.',
            image='https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=900&q=80',
            link='https://github.com/'
        ),
        Project(
            title='E-Commerce Store',
            description='A full-stack storefront with product listings, cart logic, and a smooth checkout experience.',
            image='https://images.unsplash.com/photo-1524758631624-e2822e304c36?auto=format&fit=crop&w=900&q=80',
            link='https://github.com/'
        ),
        Project(
            title='Task Manager App',
            description='A productivity app for tracking goals, deadlines, and daily workflow with a clean dashboard.',
            image='https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=900&q=80',
            link='https://github.com/'
        )
    ]

    db.session.add_all(projects)
    db.session.commit()


with app.app_context():
    db.create_all()
    seed_projects()


@app.route('/')
def home():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/projects')
def projects():
    projects = Project.query.all()
    return render_template('project.html', projects=projects)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()

        if not name or not email or not message:
            flash('Please complete all fields before sending your message.', 'error')
            return redirect(url_for('contact'))

        flash(f'Thank you, {name}! Your message has been sent successfully.', 'success')
        return redirect(url_for('home'))

    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
