from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = '+wwC8aWiq26eyDUgNZXVO/zcln/iRCCbxVupOlQl2IF+QYUwexllOw=='


class ExampleForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    submit = SubmitField('Отправить')


@app.get('/')
def index():
    form = ExampleForm()
    return render_template('index.html', form=form)


@app.post('/')
def post_index():
    form = ExampleForm()
    if form.validate_on_submit():
        name = form.name.data
        print(name)
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
