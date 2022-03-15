from flask_appbuilder.fieldwidgets import BS3TextFieldWidget


class BS3TFROWidget(BS3TextFieldWidget):
    """
        BS3TFROWidget
        Bootstrap 3 read only widget
    """
    def __call__(self, field, **kwargs):
        kwargs['readonly'] = 'true'
        return super(BS3TFROWidget, self).__call__(field, **kwargs)
