import webapp2
import time
from webapp2_extras.users import users
from model.publicacion import Publicacion
from model.like import Like


class DarLikeHandler(webapp2.RequestHandler):
    def get(self):
        p = Publicacion.recupera(self.request)
        autor = users.get_current_user().email()
        yaMeGusta = Like.query(Like.autor == autor, Like.publicacion == p.key)

        if yaMeGusta.count() == 0:
            like = Like(autor=autor, publicacion=p.key)
            like.put()
            time.sleep(1)

        return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/likes/darLike', DarLikeHandler)
], debug=True)
