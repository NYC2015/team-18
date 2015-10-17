from google.appengine.next import ndb

class kca_user(ndb.Model):
	user_email = ndb.StringProperty()
	is_expert = ndb.BooleanProperty(default=false)
	username = ndb.StringProperty()
	password = ndb.StringProperty()

