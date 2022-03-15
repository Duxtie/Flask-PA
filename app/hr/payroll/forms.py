from flask_appbuilder.fieldwidgets import BS3TextFieldWidget
from wtforms import StringField, FileField, SelectField
from wtforms.validators import DataRequired

from etas.app.forms import BaseDynamicForm as DynamicForm


class PayrollImportForm(DynamicForm):
    name = StringField(
        "Name",
        description="Your field number one!",
        validators=[DataRequired()],
        widget=BS3TextFieldWidget(),
    )
    language = SelectField(
        u'Programming Language',
        choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')]
    )
    field1 = StringField(
        "Field1",
        description="Your field number one!",
        validators=[DataRequired()],
        widget=BS3TextFieldWidget(),
    )
    field2 = StringField(
        "Field2",
        description="Your field number two!",
        widget=BS3TextFieldWidget()
    )

    file = FileField()
