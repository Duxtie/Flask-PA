from flask import g, redirect
from flask_appbuilder import IndexView
from flask_appbuilder import expose


class MyIndexView(IndexView):
    index_template = 'philbert/index.html'

    @expose("/")
    # @has_access
    def index(self):
        self.update_redirect()

        if g.user is not None and g.user.is_authenticated:
            return self.render_template(self.index_template, appbuilder=self.appbuilder)
        else:
            return redirect('/login')
