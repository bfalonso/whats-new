from google.appengine.ext import ndb

from publicacion import Publicacion

class Like(ndb.Model):
    autor = ndb.StringProperty(reequired=True)
    fecha = ndb.DateTimeProperty(auto_now_add=True, indexed=True)
    publicacion = ndb.KeyProperty(kind=Publicacion)