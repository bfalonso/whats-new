from google.appengine.ext import ndb

from publicacion import Publicacion

class Like(ndb.Model):
    autor = ndb.StringProperty(required=True)
    publicacion = ndb.KeyProperty(kind=Publicacion)
    fecha = ndb.DateTimeProperty(auto_now_add=True, indexed=True)

    @staticmethod
    def recupera(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()