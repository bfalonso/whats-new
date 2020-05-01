# coding: utf-8
import webapp2
import time
from webapp2_extras import jinja2
from webapp2_extras.users import users
from model.publicacion import Publicacion


class AddPublicacionHandler(webapp2.RequestHandler):
    def get(self):
        jinja = jinja2.get_jinja2(app=self.app)
        user = users.get_current_user()
        email = user.email()

        if user:
            url_user = users.create_logout_url("/")
        else:
            url_user = users.create_login_url("/")

        valores = {
            "user": user,
            "url_user": url_user,
            "email": email
        }

        self.response.write(jinja.render_template("addPublicacion.html", **valores))

    def post(self):
        user = users.get_current_user()
        email = user.email()
        url = self.request.get("url")
        comentario = self.request.get("comentario")

        if not url or not comentario:
            return self.redirect("/")
        else:
            publicacion = Publicacion(url=url, comentario=comentario, autor=email)
            publicacion.put()
            time.sleep(1)
            return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/publicaciones/add', AddPublicacionHandler)
], debug=True)
