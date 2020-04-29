import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users
from model.publicacion import Publicacion
from model.like import Like

class MisPublicacionesHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        publicaciones = Publicacion.query(Publicacion.autor == user.email()).order(-Publicacion.fecha)
        likes = Like.query()

        jinja = jinja2.get_jinja2(app=self.app)

        valores = {
            "user": user,
            "publicaciones": publicaciones,
            "likes": likes
        }

        self.response.write(jinja.render_template("index.html", **valores))

app = webapp2.WSGIApplication([
    ('/publicaciones/misPublicaciones', MisPublicacionesHandler)
], debug=True)
