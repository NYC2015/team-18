#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb
import json
from kca_models import *
import datetime
import math

class KCAPage(webapp2.RequestHandler):
	def proceed_with_user(self, ):
		user = users.get_current_user()
		if not user:
			self.redirect(users.create_login_url('/'))
			# greeting = ('<a href="%s">Sign in or register</a>.' %
                        # users.create_login_url('/'))
			# self.response.out.write('''
                # <html><body>%s %s id not authorized</body></html>'''
                # % (greeting, umail))
			return False
		return True


def distance_on_unit_sphere(lat1, lon1, lat2, lon2):
	# Convert latitude and longitude to 
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0
         
    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
         
    # theta = longitude
    theta1 = lon1*degrees_to_radians
    theta2 = lon2*degrees_to_radians
         
    # Compute spherical distance from spherical coordinates.
         
    # For two locations in spherical coordinates 
    # (1, theta, phi) and (1, theta', phi')
    # cosine( arc length ) = 
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length
     
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )
 
    # Remember to multiply arc by the radius of the earth 
    return arc*6378

def filterPosts(lat,lon,post):
	dist = distance_on_unit_sphere(lat,lon,post.lat,post.lon)
	if post.minDist:
		if dist < post.minDist:
			return False

	# if dist < 80:
		# return True
	return True


class GetPosts(KCAPage):
	def get(self):
		titles = ["title1","title2","title3"]
		bodies = ["body1","1234","qwer"]
		originalPosters = ["aaron","Abdullah","Jason"]
		points = [1,2,3]
		posts = Post.query().order(-Post.post_time).fetch(5)
		# self.response.write(self.request.get("lat"))
		# self.response.write(self.request.get("lat"))
		lat = float(self.request.get("lat"))
		lon = float(self.request.get("lon"))
		posts = filter(lambda p:filterPosts(lat,lon,p),posts)
		post_list = map(lambda p:(GetUserFromEmail(p.user_email).username, p.post, 0, p.comments,p.title),posts)
		res = json.dumps(post_list)
		# res = json.dumps(zip(originalPosters,bodies,points,titles))
		self.response.write(res)

class populateDB(KCAPage):
	def get(self):
		# return 0
	# 	user_email = ndb.StringProperty()
	# is_expert = ndb.BooleanProperty(default=False)
	# username = ndb.StringProperty()
	# password = ndb.StringProperty()
	# location = ndb.StringProperty()
	# age = ndb.IntegerProperty()
	# interests = ndb.JsonProperty()
	# gender = ndb.StringProperty()
		# populate users
		# kca_user(user_email="abdullah@ajkhan.me",is_expert = True, username="Abdullah Khan", password="password",location="Uganda",age=21,gender="M").put()
		# kca_user(user_email="acb257@cornell.edu",is_expert = True, username="Adam Bergere", password="password",location="Uganda",age=21,gender="M").put()
		# kca_user(user_email="ljh239@cornell.edu",is_expert = True, username="Lydia Holley", password="password",location="",age=21,gender="F").put()
		# kca_user(user_email="amf272@cornell.edu",is_expert = True, username="Aaron Ferber", password="password",location="Uganda",age=21,gender="M").put()
		# kca_user(user_email="jdeng1234@gmail.com",is_expert = True, username="Jason Deng", password="password",location="",age=21,gender="M").put()

		# populate messages
		# upvotes = json.dumps(["abdullah@ajkhan.me","acb257@cornell.edu"])
		# downvotes = json.dumps(["jdeng1234@gmail.com","amf272@cornell.edu"])
		# comments = json.dumps([["jdeng1234@gmail.com","totally great"],["amf272@cornell.edu","this is awesome"]])
		# Post(title="Took my pills today",post="omg I'm so great",user_email="ljh239@cornell.edu",upvotes=upvotes,downvotes=downvotes,comments=comments,post_time=datetime.datetime.now(),lat=0.3140103,lon=32.5290847).put()
		# Post(title="So empowered",post="team 18 number 1",user_email="amf272@cornell.edu",upvotes=downvotes,downvotes=upvotes,comments=comments,post_time=datetime.datetime.now(),lat=0.3140103,lon=32.5290747).put()
		# Post(title="I feel so depressed",post="not a good day",user_email="acb257@cornell.edu",upvotes=upvotes,downvotes=downvotes,comments=comments,post_time=datetime.datetime.now(),lat=0.3140003,lon=32.5290847).put()
		# Post(title="Bought a new sweater today",post="it is super warm",user_email="abdullah@ajkhan.me",upvotes=upvotes,downvotes=downvotes,comments=comments,post_time=datetime.datetime.now(),lat=-1.961540,lon=30.113753).put()
		# Post(title="I dont want people near me to know",post="I am in rwanda",user_email="jdeng1234@gmail.com",upvotes=upvotes,downvotes=downvotes,comments=comments,post_time=datetime.datetime.now(),lat=-1.961540,lon=30.113753, minDist=80).put()
		self.response.write(0)
		StoryParagraphs(text="I don't know how many meds I've taken in my life.",user="jdeng1234@gmail.com", post_time=datetime.datetime.now()).put()
		StoryParagraphs(text="I was adopted when I was 2 or 3.",user="abdullah@ajkhan.me",post_time=datetime.datetime.now()).put()
		StoryParagraphs(text="I don't really remember how my mom told me I had HIV or anything.",user="ljh239@cornell.edu",post_time=datetime.datetime.now()).put()
		StoryParagraphs(text="I think I used drugs as a way to escape all the feelings that came with that.",user="acb257@cornell.edu",post_time=datetime.datetime.now()).put()
		StoryParagraphs(text="But since then I've been sober for 3 years now.",user="amf272@cornell.edu",post_time=datetime.datetime.now()).put()
		StoryParagraphs(text="Haters gonna hate right?",user="jdeng1234@gmail.com",post_time=datetime.datetime.now()).put()

class BubbleData(KCAPage):
	def get(self):
		location_dict = {}
		for loc in kca_user.query().fetch():
			if loc.location == "":
				loc.location = "Anonymous"
			location_dict[loc.location] = 1+location_dict.get(loc.location,0)

		children = map(lambda (k,v):{"name":"something","children":[{"name":k,"size":v}]},location_dict.iteritems())
		res = {"name":"flare","children":children}
		self.response.write(json.dumps(res))

class GetStory(KCAPage):
	def get(self):
		paragraphs = StoryParagraphs.query().order(-StoryParagraphs.post_time).fetch(4)
		res = map(lambda x:x.text,paragraphs)
		res = map(lambda x:x.strip(),res)
		res.reverse()
		ans = " "
		for i in res:
			ans+=i + " "
		self.response.write(json.dumps(ans[:-1]))

	def post(self):
		return 0

class GetExperts(KCAPage):
	def get

app = webapp2.WSGIApplication([
	('/getPosts.json', GetPosts),
	('/populateDB',populateDB),
	('/bubbleData.json',BubbleData),
	('/getStory.json',GetStory),
	('/getExperts.json',GetExperts)

], debug=True)
