from hashlib import md5

def code_generation(project_name, user_id):
	""" input proejoct name, pass in user id discreetly and printout the unique project code

	"""
	project_code = md5().update(project_name + user_id).hexdigest()
	return project_code
	

