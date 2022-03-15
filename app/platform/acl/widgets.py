"""
Created on Oct 12, 2013

@author: Daniel Gaspar
"""

import logging

from flask.globals import _request_ctx_stack

from ....config import APP_TEMPLATE

# from . import get_template

log = logging.getLogger(__name__)


def get_template():
    template = ''
    try:
        # template = current_app.config['APP_TEMPLATE']
        template = APP_TEMPLATE
    except Exception as e:
        'philbert'
    return template


class RenderTemplateWidget(object):
    """
        Base template for every widget
        Enables the possibility of rendering a template
         inside a template with run time options
    """

    template = get_template() + "/general/widgets/render.html"
    template_args = None

    def __init__(self, **kwargs):
        self.template_args = kwargs

    def __call__(self, **kwargs):
        ctx = _request_ctx_stack.top
        jinja_env = ctx.app.jinja_env

        template = jinja_env.get_template(self.template)
        args = self.template_args.copy()
        args.update(kwargs)
        return template.render(args)


class ACLUserShowBlockWidget(RenderTemplateWidget):
    template = get_template() + "/general/widget/show.html"


class ACLUserListWidget(RenderTemplateWidget):
    """
        List Widget implements a Template as an widget.
        It takes the following arguments

        label_columns = []
        include_columns = []
        value_columns = []
        order_columns = []
        page = None
        page_size = None
        count = 0
        pks = []
        actions = None
        filters = {}
        modelview_name = ''
    """

    template = get_template() + "/general/widgets/list.html"
