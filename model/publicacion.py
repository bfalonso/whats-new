from google.appengine.ext import ndb

class Publicacion(ndb.Model):
    autor = ndb.StringProperty(reequired=True)
    comentario = ndb.StringProperty(required=True)
    fecha = ndb.DateTimeProperty(auto_now_add=True, indexed=True)