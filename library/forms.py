from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, ValidationError
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField("ユーザーID", validators=[DataRequired(), Length(min=2, max=80)])
    password = PasswordField("パスワード", validators=[DataRequired()])
    submit = SubmitField("ログイン")

class SearchForm(FlaskForm):
    search_term = StringField(
        "タイトルまたは著者",
        validators=[DataRequired()],
        render_kw={"placeholder": "キーワードを入力"},
    )
    submit = SubmitField("検索")


class BookRequestForm(FlaskForm):
    title = StringField("書名", validators=[DataRequired()])
    author = StringField("著者", validators=[DataRequired()])
    reason = TextAreaField("リクエスト理由", validators=[DataRequired()])
    submit = SubmitField("申請する")