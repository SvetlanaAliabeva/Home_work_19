# это файл для классов доступа к данным (Data Access Object). Здесь должен быть класс с методами доступа к данным
# здесь в методах можно построить сложные запросы к БД
from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        return self.session.query(Director).get(did)

    def get_all(self):
        return self.session.query(Director).all()

    def create(self, data):
        director = Director(**data)

        self.session.add(director)
        self.session.commit()
        return director

    def update(self, data):
        did = data.get("id")
        director = self.get_one(did)

        self.session.add(director)
        self.session.commit()

    # def update_partial(self, data):
    #     uid = data.get("id")
    #     movie = self.session.query(Director).get(uid)
    #     return movie

    def delete(self, data):
        director = self.get_one(data.get("id"))
        director.name = data.get("name")

        self.session.delete(director)
        self.session.commit()
