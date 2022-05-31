class MydbRouter():
	def db_for_read(model, **hint):
		if model._meta.app_label == "food_recommendation":
			return "mydb"
		else:
			return None

	def db_for_write(model, **hint):
		if model._meta.app_label == "food_recommendation":
			return "mydb"
		else:
			return None

	def allow_relation(obj1, obj2, **hint):
		if (obj1._meta.app_label == "food_recommendation" and obj2._meta.app_label):
			return True
		else:
			return None

	def allow_migrate(db, app_label, model_name=None, **hint):
		if app_label == "food_recommendation":
			return db == "mydb"
		elif db == "mydb":
			return False
		else:
			return None