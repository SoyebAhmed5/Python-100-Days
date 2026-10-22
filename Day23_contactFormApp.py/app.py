from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

app=Flask(__name__)
app.secret_key='@1234'

#Contact Form Class
class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Send Message')
    
# Route for Contact Form
@app.route('/',methods=['GET','POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash(f"Thank you, {form.name.data}! Your Message has been sent.", "success")
        return redirect(url_for('success'))
    return render_template("contact.html", form=form)

#Success Page
@app.route('/success')
def success():
    return render_template('success.html')

if __name__=='__main__':
    app.run(debug=True)
        