from random import Random
from re import T
from DataGenerator import *
from DataGenerator.Generators import *
from DataGenerator.Table import *
from DataGenerator.Column import *
from datetime import date

db = Databases.Sqlite3DB(True)
db.connect("db.sqlite3")

sequences = [
	[i for i in range(1, 240)],
]

class SlugGenerator(Generator):
	def __init__(self):
		self.__faker = Faker()

	def generate(self):
		username = self.__faker.user_name()
		username = username.replace('\'', "")
		scnd_part = self.__faker.first_name() + "-" + self.__faker.street_name() + "-" + self.__faker.country()
		slug = f"{username}-{scnd_part}"
		return slug

class FDTG(Generator):
	def __init__(self):
		self

	def generate(self):
		name = "2015-03-21"
		return str(name)


accounts = Table("account_account")
accounts.addColumns([
	Column("id", SerialGenerator(4), True),
	Column("password", ConstantGenerator("pbkdf2_sha256$320000$FH7Fm1QsiecK7tW9CEcV6X$0yNuFTHD61ePG6WJyw5kBn7V7KRdWqDKWES9y8+Xojw=")),
	Column("first_name", FakeFirstNameGenerator()),
	Column("last_name", FakeLastNameGenerator()),
	Column("email", FakeEmailGenerator()),
	Column("username", FakeUsernameGenerator()),
	Column("date_joined", FDTG()),
	Column("last_login", FDTG()),
	Column("is_admin", ConstantGenerator(1)),
	Column("is_active", ConstantGenerator(0)),
	Column("is_staff", ConstantGenerator(1)),
	Column("is_superuser", ConstantGenerator(1)),
])

posts = Table("blog_blogpost")
posts.addColumns([
	Column("id", SerialGenerator(1), True),
	Column("title", RandomStringGenerator(30, True, False, False)),
	Column("body", RandomStringGenerator(3000, True, True, False)),
	Column("description", RandomStringGenerator(300, True, True, False)),
	Column("image", ConstantGenerator("blog/1/test-changePwdDean.gif")),
	Column("author_id", RandomIntegerGenerator(1, 50)),
	Column("pub_date", FDTG()),
	Column("slug", SlugGenerator()),
	Column("published", RandomIntegerGenerator(0, 1)),
	Column("likes", ConstantGenerator(0)),
	Column("upd_date", FDTG()),
])

#db.wipeTable(accounts)
#db.insertRows(accounts, 196)
db.wipeTable(posts)
db.insertRows(posts, 150)
