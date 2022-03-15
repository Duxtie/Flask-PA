from flask_appbuilder import expose, BaseView, IndexView

from etas.app import appbuilder, get_template


class BaseIndexView(IndexView):
    """
        A simple view that implements the index for the site
    """

    route_base = ""
    default_view = "index"
    index_template = get_template() + '/index.html'

    @expose("/")
    def index(self):
        self.update_redirect()
        return self.render_template(self.index_template, appbuilder=self.appbuilder)


appbuilder.add_view_no_menu(BaseIndexView())
