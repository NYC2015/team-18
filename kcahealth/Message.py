from google.appengine.ext import ndb


#users to users
class Message(ndb.Model):
    sender = ndb.StringProperty()
    reciever = ndb.StringProperty()
    body = ndb.StringProperty()
