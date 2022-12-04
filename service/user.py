import hashlib
import base64
import hmac

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from dao.user import UserDAO

class UserService:
	def __init__(self, dao: UserDAO):
		self.dao = dao

	def get_one(self, uid):
		return self.dao.get_one(uid)

	def get_usser_name(self, username):
		return self.dao.get_by_username(username)


	def get_all(self):
		return self.dao.get_all()

	def create(self, data):
		data["password"] = self.get_hash(data.get("password"))
		return self.dao.create(data)

	def update(self, data):
		data["password"] = self.get_hash(data.get("password"))
		self.dao.update(data)
		return self.dao

	def delete(self, uid):
		self.dao.delete(uid)

	def get_hash(self, password):
		return base64.b64decode(hashlib.pbkdf2_hmac(
			'sha256',
			password.encode('utf-8'),  # Convert the password to bytes
			PWD_HASH_SALT,
			PWD_HASH_ITERATIONS
		))

	def compare_passwords(self, password_hash, request_password):
		return hmac.compare_digest(
			base64.b64decode(password_hash),
			hashlib.pbkdf2_hmac('sha256',
								request_password.encode('utf-8'),
								PWD_HASH_SALT,
								PWD_HASH_ITERATIONS)
								)
