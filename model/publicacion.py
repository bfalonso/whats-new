# Publicacion
from google.appengine.ext import ndb


class Publicacion(ndb.Model):
    url = ndb.StringProperty(required=True)
    comentario = ndb.StringProperty(required=True)
    autor = ndb.StringProperty(required=True)
    fecha = ndb.DateTimeProperty(auto_now_add=True, indexed=True)

    @staticmethod
    def recupera(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()
