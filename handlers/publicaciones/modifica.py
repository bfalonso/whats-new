# coding: utf-8
import webapp2
import time
from webapp2_extras import jinja2
from webapp2_extras.users import users
from model.publicacion import Publicacion


class ModificarPublicacionHandler(webapp2.RequestHandler):
    def get(self):
        jinja = jinja2.get_jinja2(app=self.app)
        user = users.get_current_user()
        email = user.email()
        publicacion = Publicacion.recupera(self.request)

        if user:
            url_user = users.create_logout_url("/")
        else:
            url_user = users.create_login_url("/")

        valores = {
            "user": user,
            "url_user": url_user,
            "email": email,
            "p": publicacion
        }

        self.response.write(jinja.render_template("modificarPublicacion.html", **valores))

    def post(self):
        url = self.request.get("url")
        comentario = self.request.get("comentario")
        publicacion = Publicacion.recupera(self.request)

        if not url or not comentario:
            return self.redirect("/")
        else:
            publicacion.url = url
            publicacion.comentario = comentario
            publicacion.put()
            time.sleep(1)
            return self.redirect("/publicaciones/misPublicaciones")


app = webapp2.WSGIApplication([
    ('/publicaciones/modifica', ModificarPublicacionHandler)
], debug=True)
