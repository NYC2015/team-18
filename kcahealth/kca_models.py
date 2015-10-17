from google.appengine.ext import ndb

class kca_user(ndb.Model):
	user_email = ndb.StringProperty()
	is_expert = ndb.BooleanProperty(default=False)
	username = ndb.StringProperty()
	password = ndb.StringProperty()
	location = ndb.StringProperty()
	age = ndb.IntegerProperty()
	interests = ndb.JsonProperty()
	gender = ndb.StringProperty()

#users to users
class Message(ndb.Model):
    sender = ndb.StringProperty()
    reciever = ndb.StringProperty()
    body = ndb.StringProperty()

class Post(ndb.Model):
	title = ndb.StringProperty()
	post = ndb.StringProperty()
	user_email = ndb.StringProperty()
	votes = ndb.IntegerProperty()
	comments = ndb.JsonProperty()
	post_time = ndb.DateTimeProperty()

class Reminder(ndb.Model):
	user = ndb.StringProperty()
	text = ndb.StringProperty()
	frequency_hours = ndb.IntegerProperty()
	notifications = ndb.BooleanProperty()
	

def GetUserFromEmail(email):
	return list(kca_user.query(kca_user.user_email==email).iter())[1]
