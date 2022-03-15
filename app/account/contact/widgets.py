from ....app import get_template
from ....app.widgets import RenderTemplateWidget


class ContactEditBlockWidget(RenderTemplateWidget):
    template = get_template() + "/pages/account/contact/widget_edit.html"
