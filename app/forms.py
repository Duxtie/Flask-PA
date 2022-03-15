from flask_appbuilder.forms import DynamicForm

from . import appbuilder, db, get_template


class BaseDynamicForm(DynamicForm):

    form_template = get_template() + '/general/model/edit.html'
