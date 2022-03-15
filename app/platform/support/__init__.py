from flask import current_app


def get_template():
    template = 'philbert'
    try:
        template = current_app.config['APP_TEMPLATE']
    except Exception as e:
        ''
    return template
