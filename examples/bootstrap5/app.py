# -*- coding: utf-8 -*-
from enum import Enum
from flask import Flask, render_template, request, flash, redirect, url_for
from markupsafe import Markup
from flask_wtf import FlaskForm, CSRFProtect
from wtforms.validators import DataRequired, Length, Regexp
from wtforms.fields import *
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5, SwitchField

app = Flask(__name__)
app.secret_key = 'dev'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

# serve locally for faster and offline development
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

# set default button sytle and size, will be overwritten by macro parameters
app.config['BOOTSTRAP_BTN_STYLE'] = 'primary'
app.config['BOOTSTRAP_BTN_SIZE'] = 'sm'

# set default icon title of table actions
app.config['BOOTSTRAP_TABLE_VIEW_TITLE'] = 'Read'
app.config['BOOTSTRAP_TABLE_EDIT_TITLE'] = 'Update'
app.config['BOOTSTRAP_TABLE_DELETE_TITLE'] = 'Remove'
app.config['BOOTSTRAP_TABLE_NEW_TITLE'] = 'Create'

bootstrap = Bootstrap5(app)
db = SQLAlchemy(app)
csrf = CSRFProtect(app)


class ExampleForm(FlaskForm):
    """An example form that contains all the supported bootstrap style form fields."""

    date = DateField(description="We'll never share your email with anyone else.")  # add help text with `description`
    datetime = DateTimeField(render_kw={'placeholder': 'this is a placeholder'})  # add HTML attribute with `render_kw`
    datetime_local = DateTimeLocalField()
    time = TimeField(description='This is private', render_kw={'description_class': 'fst-italic text-decoration-underline'})
    month = MonthField()
    color = ColorField()
    floating = FloatField()
    integer = IntegerField()
    decimal_slider = DecimalRangeField()
    integer_slider = IntegerRangeField(render_kw={'min': '0', 'max': '4'})
    email = EmailField()
    url = URLField()
    telephone = TelField()
    image = FileField(render_kw={'class': 'my-class'}, validators=[Regexp('.+\.jpg$')])  # add your class
    option = RadioField(choices=[('dog', 'Dog'), ('cat', 'Cat'), ('bird', 'Bird'), ('alien', 'Alien')], render_kw={'label_class': 'text-decoration-underline', 'radio_class': 'text-decoration-line-through'})
    select = SelectField(choices=[('dog', 'Dog'), ('cat', 'Cat'), ('bird', 'Bird'), ('alien', 'Alien')])
    select_multiple = SelectMultipleField(choices=[('dog', 'Dog'), ('cat', 'Cat'), ('bird', 'Bird'), ('alien', 'Alien')])
    bio = TextAreaField()
    search = SearchField()  # will autocapitalize on mobile
    title = StringField()  # will not autocapitalize on mobile
    secret = PasswordField()
    remember = BooleanField('Remember me')
    submit = SubmitField()


class ExampleFormInline(FlaskForm):
    """An example inline form."""
    floating = FloatField(description='a float', render_kw={'label_class': 'text-decoration-underline'})
    integer = IntegerField(description='an int', render_kw={'description_class': 'text-decoration-line-through'})
    option = RadioField(description='Choose one', choices=[('dog', 'Dog'), ('cat', 'Cat'), ('bird', 'Bird'), ('alien', 'Alien')], render_kw={'radio_class': 'text-decoration-line-through', 'description_class': 'fw-bold'})
    submit = SubmitField()


class ExampleFormHorizontal(FlaskForm):
    """An example horizontal form."""
    floating = FloatField(description='a float', render_kw={'label_class': 'text-decoration-underline'})
    integer = IntegerField(description='an int', render_kw={'description_class': 'text-decoration-line-through'})
    option = RadioField(description='choose 1', choices=[('dog', 'Dog'), ('cat', 'Cat'), ('bird', 'Bird'), ('alien', 'Alien')], render_kw={'label_class': 'text-decoration-underline'})
    submit = SubmitField()


class HelloForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 150)])
    remember = BooleanField('Remember me', description='Rember me on my next visit', render_kw={'description_class': 'fw-bold text-decoration-line-through'})
    submit = SubmitField()


class ButtonForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    confirm = SwitchField('Confirmation', description='Are you sure?', render_kw={'label_class': 'font-monospace text-decoration-underline'})
    submit = SubmitField()
    delete = SubmitField()
    cancel = SubmitField()


class TelephoneForm(FlaskForm):
    country_code = IntegerField('Country Code')
    area_code = IntegerField('Area Code/Exchange')
    number = StringField('Number')


class IMForm(FlaskForm):
    protocol = SelectField(choices=[('aim', 'AIM'), ('msn', 'MSN')])
    username = StringField()


class ContactForm(FlaskForm):
    first_name = StringField()
    last_name = StringField()
    mobile_phone = FormField(TelephoneForm)
    office_phone = FormField(TelephoneForm)
    emails = FieldList(StringField("Email"), min_entries=3)
    im_accounts = FieldList(FormField(IMForm), min_entries=2)


class BootswatchForm(FlaskForm):
    """Form to test Bootswatch."""

    # DO NOT EDIT! Use list_bootswatch.py to generate the Radiofield below.
    theme_name = RadioField(
        default='default',
        choices=[
            ('default', 'none'),
            ('brite', 'Brite 5.3.5'),
            ('cerulean', 'Cerulean 5.3.5'),
            ('cosmo', 'Cosmo 5.3.5'),
            ('cyborg', 'Cyborg 5.3.5'),
            ('darkly', 'Darkly 5.3.5'),
            ('flatly', 'Flatly 5.3.5'),
            ('journal', 'Journal 5.3.5'),
            ('litera', 'Litera 5.3.5'),
            ('lumen', 'Lumen 5.3.5'),
            ('lux', 'Lux 5.3.5'),
            ('materia', 'Materia 5.3.5'),
            ('minty', 'Minty 5.3.5'),
            ('morph', 'Morph 5.3.5'),
            ('pulse', 'Pulse 5.3.5'),
            ('quartz', 'Quartz 5.3.5'),
            ('sandstone', 'Sandstone 5.3.5'),
            ('simplex', 'Simplex 5.3.5'),
            ('sketchy', 'Sketchy 5.3.5'),
            ('slate', 'Slate 5.3.5'),
            ('solar', 'Solar 5.3.5'),
            ('spacelab', 'Spacelab 5.3.5'),
            ('superhero', 'Superhero 5.3.5'),
            ('united', 'United 5.3.5'),
            ('vapor', 'Vapor 5.3.5'),
            ('yeti', 'Yeti 5.3.5'),
            ('zephyr', 'Zephyr 5.3.5'),
        ]
    )
    submit = SubmitField()


class MyCategory(Enum):
    CAT1 = 'Category 1'
    CAT2 = 'Category 2'


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), nullable=False)
    category = db.Column(db.Enum(MyCategory), default=MyCategory.CAT1, nullable=False)
    draft = db.Column(db.Boolean, default=False, nullable=False)
    create_time = db.Column(db.Integer, nullable=False, unique=True)


with app.app_context():
    db.drop_all()
    db.create_all()
    for i in range(20):
        url = 'mailto:x@t.me'
        if i % 7 == 0:
            url = 'www.t.me'
        elif i % 7 == 1:
            url = 'https://t.me'
        elif i % 7 == 2:
            url = 'http://t.me'
        elif i % 7 == 3:
            url = 'http://t'
        elif i % 7 == 4:
            url = 'http://'
        elif i % 7 == 5:
            url = 'x@t.me'
        m = Message(
            text=f'Message {i+1} {url}',
            author=f'Author {i+1}',
            create_time=4321*(i+1)
            )
        if i % 2:
            m.category = MyCategory.CAT2
        if i % 4:
            m.draft = True
        db.session.add(m)
    db.session.commit()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/form', methods=['GET', 'POST'])
def test_form():
    form = HelloForm()
    if form.validate_on_submit():
        flash('Form validated!')
        return redirect(url_for('index'))
    return render_template(
        'form.html',
        form=form,
        telephone_form=TelephoneForm(),
        contact_form=ContactForm(),
        im_form=IMForm(),
        button_form=ButtonForm(),
        example_form=ExampleForm(),
        inline_form=ExampleFormInline(),
        horizontal_form=ExampleFormHorizontal()
    )


@app.route('/nav', methods=['GET', 'POST'])
def test_nav():
    return render_template('nav.html')


@app.route('/bootswatch', methods=['GET', 'POST'])
def test_bootswatch():
    form = BootswatchForm()
    if form.validate_on_submit():
        if form.theme_name.data == 'default':
            app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = None
        else:
            app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = form.theme_name.data
        flash(f'Render style has been set to {form.theme_name.data}.')
    else:
        if app.config['BOOTSTRAP_BOOTSWATCH_THEME'] is not None:
            form.theme_name.data = app.config['BOOTSTRAP_BOOTSWATCH_THEME']
    return render_template('bootswatch.html', form=form)


@app.route('/pagination', methods=['GET', 'POST'])
def test_pagination():
    page = request.args.get('page', 1, type=int)
    pagination = Message.query.paginate(page=page, per_page=10)
    messages = pagination.items
    return render_template('pagination.html', pagination=pagination, messages=messages)


@app.route('/flash', methods=['GET', 'POST'])
def test_flash():
    flash('A simple default alert—check it out!')
    flash('A simple primary alert—check it out!', 'primary')
    flash('A simple secondary alert—check it out!', 'secondary')
    flash('A simple success alert—check it out!', 'success')
    flash('A simple danger alert—check it out!', 'danger')
    flash('A simple warning alert—check it out!', 'warning')
    flash('A simple info alert—check it out!', 'info')
    flash('A simple light alert—check it out!', 'light')
    flash('A simple dark alert—check it out!', 'dark')
    flash(Markup('A simple success alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.'), 'success')
    return render_template('flash.html')


@app.route('/table')
def test_table():
    page = request.args.get('page', 1, type=int)
    pagination = Message.query.paginate(page=page, per_page=10)
    messages = pagination.items
    titles = [('id', '#'), ('text', 'Message'), ('author', 'Author'), ('category', 'Category'), ('draft', 'Draft'), ('create_time', 'Create Time')]
    data = []
    for msg in messages:
        data.append({'id': msg.id, 'text': msg.text, 'author': msg.author, 'category': msg.category, 'draft': msg.draft, 'create_time': msg.create_time})
    return render_template('table.html', messages=messages, titles=titles, Message=Message, data=data)


@app.route('/table/<int:message_id>/view')
def view_message(message_id):
    message = Message.query.get(message_id)
    if message:
        return f'Viewing {message_id} with text "{message.text}". Return to <a href="/table">table</a>.'
    return f'Could not view message {message_id} as it does not exist. Return to <a href="/table">table</a>.'


@app.route('/table/<int:message_id>/edit')
def edit_message(message_id):
    message = Message.query.get(message_id)
    if message:
        message.draft = not message.draft
        db.session.commit()
        return f'Message {message_id} has been editted by toggling draft status. Return to <a href="/table">table</a>.'
    return f'Message {message_id} did not exist and could therefore not be edited. Return to <a href="/table">table</a>.'


@app.route('/table/<int:message_id>/delete', methods=['POST'])
def delete_message(message_id):
    message = Message.query.get(message_id)
    if message:
        db.session.delete(message)
        db.session.commit()
        return f'Message {message_id} has been deleted. Return to <a href="/table">table</a>.'
    return f'Message {message_id} did not exist and could therefore not be deleted. Return to <a href="/table">table</a>.'


@app.route('/table/<int:message_id>/like')
def like_message(message_id):
    return f'Liked the message {message_id}. Return to <a href="/table">table</a>.'


@app.route('/table/new-message')
def new_message():
    return 'Here is the new message page. Return to <a href="/table">table</a>.'


@app.route('/icon')
def test_icon():
    return render_template('icon.html')


@app.route('/icons')
def test_icons():
    return render_template('icons.html')


if __name__ == '__main__':
    app.run(debug=True)
