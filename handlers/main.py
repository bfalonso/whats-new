import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users
from model.publicacion import Publicacion
from model.like import Like


class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        publicaciones = Publicacion.query().order(-Publicacion.fecha)
        likes = Like.query()

        if user:
            url_user = users.create_logout_url("/")
        else:
            url_user = users.create_login_url("/")

        jinja = jinja2.get_jinja2(app=self.app)

        valores = {
            "user": user,
            "url_user": url_user,
            "publicaciones": publicaciones,
            "likes": likes
        }

        self.response.write(jinja.render_template("index.html", **valores))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
