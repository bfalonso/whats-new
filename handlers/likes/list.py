import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users
from model.like import Like
from model.publicacion import Publicacion


class verLikesHandler(webapp2.RequestHandler):
    def get(self):
        publicacion = Publicacion.recupera(self.request)
        likes = Like.query(Like.publicacion == publicacion.key).order(-Like.fecha)
        user = users.get_current_user()

        jinja = jinja2.get_jinja2(app=self.app)

        valores = {
            "user": user,
            "likes": likes
        }

        self.response.write(jinja.render_template("listLikes.html", **valores))


app = webapp2.WSGIApplication([
    ('/likes/list', verLikesHandler)
], debug=True)
