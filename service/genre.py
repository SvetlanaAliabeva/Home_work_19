from dao.genre import GenreDAO

class GenreService:
	def __init__(self, dao: GenreDAO):
		self.dao = dao

	def get_one(self, gid):
		return self.dao.get_one(gid)

	def get_all(self):
		return self.dao.get_all()

	def create(self, data):
		return self.dao.create(data)

	def update(self, data):
		self.dao.update(data)
		return self.dao

	def delete(self, gid):
		self.dao.delete(gid)
