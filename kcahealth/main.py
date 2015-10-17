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


class KCAPage(webapp2.RequestHandler):
	def proceed_with_user(self, ):
		user = users.get_current_user()
		if not user:
			return False
		return True

class GetPosts(KCAPage):
	def get(self):
		titles = ["title1","title2","title3"]
		bodies = ["body1","1234","qwer"]
		originalPosters = ["aaron","Abdullah","Jason"]
		points = [1,2,3]
		# post_list = map(lambda p:(GetUserFromEmail(p.user_email), p.post, p.votes, p.comments),Post.query().fetch(5))
		# res = json.dumps(post_list)
		res = json.dumps(zip(originalPosters,bodies,points,titles))
		self.response.write(res)


app = webapp2.WSGIApplication([
	('/getPosts.json', GetPosts)
], debug=True)
