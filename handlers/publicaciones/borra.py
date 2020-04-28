import webapp2
import time
from webapp2_extras.users import users
from model.publicacion import Publicacion


class BorraHandler(webapp2.RequestHandler):
    def get(self):
        p = Publicacion.recupera(self.request)
        if p.autor == users.get_current_user().email():
            p.key.delete()
            time.sleep(1)

        return self.redirect("/")



app = webapp2.WSGIApplication([
    ('/publicaciones/borra', BorraHandler)
], debug=True)
