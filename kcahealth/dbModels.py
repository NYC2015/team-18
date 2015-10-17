from google.appengine.ext import ndb


class PreRushUserModel(ndb.Model):
    email = ndb.StringProperty()
    is_admin = ndb.BooleanProperty(default=False)

class PreRushStationModel(ndb.Model):
    stat_id = ndb.IntegerProperty()
    location = ndb.StringProperty()
    latitude = ndb.FloatProperty()
    longitude = ndb.FloatProperty()
    neverdie = ndb.BooleanProperty()
    on_street = ndb.BooleanProperty()
    station_notes = ndb.StringProperty()
    # fill percentages
    hidden = ndb.BooleanProperty()
    wkday_10am_1 = ndb.FloatProperty()
    wkday_2pm_5 = ndb.FloatProperty()
    wkday_6pm_9 = ndb.FloatProperty()
    wkday_10pm_9 = ndb.FloatProperty()

    wkend_10am_1 = ndb.FloatProperty()
    wkend_2pm_5 = ndb.FloatProperty()
    wkend_6pm_9 = ndb.FloatProperty()
    wkend_10pm_9 = ndb.FloatProperty()

class PlanningSettingsModel(ndb.Model):
	threshold = ndb.IntegerProperty()

def queryStationsAsDict(stats):
    stat_ids = map(lambda x: x.id, stats)
    stations = PreRushStationModel.query(PreRushStationModel.stat_id.IN(stat_ids))
    return dict([(x.stat_id, x) for x in stations])

class PreRushFuelModel(ndb.Model):
    location = ndb.StringProperty()
    latitude = ndb.FloatProperty()
    longitude = ndb.FloatProperty()
    is_diesel = ndb.BooleanProperty()