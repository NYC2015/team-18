from google.appengine.next import ndb

class kca_user(ndb.Model):
	user_email = ndb.StringProperty()
	is_expert = ndb.BooleanProperty(default=false)


#users to users
class Message(ndb.Model):
    sender = ndb.StringProperty()
    reciever = ndb.StringProperty()
    body = ndb.StringProperty()
