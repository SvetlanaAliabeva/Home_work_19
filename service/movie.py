# здесь бизнес логика, в виде классов или методов. сюда импортируются DAO классы из пакета dao и модели из dao.model
# некоторые методы могут оказаться просто прослойкой между dao и views,
# но чаще всего будет какая-то логика обработки данных сейчас или в будущем.


from dao.movie import MovieDAO

class MovieService:
	def __init__(self, dao: MovieDAO):
		self.dao = dao

	def get_one(self, uid):
		return self.dao.get_one(uid)

	def get_all(self, filters):
		if filters.get("director_id") is not None:
			movies = self.dao.get_by_director_id(filters.get("director_id"))

		elif filters.get("genre_id") is not None:
			movies = self.dao.get_by_genre_id(filters.get("genre_id"))

		elif filters.get("year") is not None:
			movies = self.dao.get_by_year(filters.get("year"))

		else:
			movies = self.dao.get_all()

		return movies

	def create(self, data):
		return self.dao.create(data)

	def update(self, data):
		self.dao.update(data)
		return self.dao

	def delete(self, uid):
		self.dao.delete(uid)
