from django.test import TestCase
from account.models import Account
from faker import Faker
from faker.providers.person.en import Provider


RANGE = 1000
f = Faker()
uuniq = []
u = []
firstNames = []
lastNames = []
usernames = []
emails = []
uniqueFirstNames = []
uniqueLastNames = []
uniqueUsernames = []
uniqueEmails = []
new_uniqueUsernames = []
new_uniqueEmails = []


# class TestUserModelNonUnique(TestCase):
# 	# * Most likely failing for 100+ RANGE
# 	# ! Unique Constrain Error
# 	@staticmethod
# 	def generateNonUniqe():
# 		for i in range(RANGE):
# 			firstNames.append(f.first_name())
# 			lastNames.append(f.last_name())
# 			usernames.append(f.user_name())
# 			emails.append(f.email())

# 	def setUp(self):
# 		self.generateNonUniqe()
# 		for i in range(RANGE):
# 			u.append(Account.objects.create(first_name=firstNames[i], last_name=lastNames[i], username=usernames[i], email=emails[i]))       

# 	def test(self):
# 		for i in range(RANGE):
# 			self.assertEqual(u[i].first_name, self.firstNames[i], 'First name failed')
# 			self.assertEqual(u[i].last_name, self.lastNames[i], 'Last name failed')
# 			self.assertEqual(u[i].username, self.usernames[i], 'Username failed')
# 			self.assertEqual(u[i].email, self.emails[i], 'E-mail failed')

# 	def tearDown(self):
# 		u.clear()


class TestUserModelUnique(TestCase):
	def_range = 0

	@staticmethod
	def generateUnique():
		uniqueFirstNames = list(set(Provider.first_names))
		uniqueLastNames = list(set(Provider.last_names))
		for i in range(RANGE):
			uniqueUsernames.append(f.user_name())
			uniqueEmails.append(f.email())
		new_uniqueUsernames = set(uniqueUsernames)
		new_uniqueEmails = set(uniqueEmails)
		unUname = len(new_uniqueUsernames)
		unEmail = len(new_uniqueEmails)
		def_range = unEmail if unUname > unEmail else unUname

	def setUp(self):
		self.generateUnique()
		for i in range(self.def_range):
			self.uuniq.append(Account.objects.create(first_name=uniqueFirstNames[i], last_name=uniqueLastNames[i], username=new_uniqueUsernames[i], email=new_uniqueEmails[i]))

	def test(self):
		for i in range(self.def_range):
			self.assertEqual(self.uuniq[i].first_name, self.uniqueFirstNames[i], 'First name failed')
			self.assertEqual(self.uuniq[i].last_name, self.uniqueLastNames[i], 'Last name failed')
			self.assertEqual(self.uuniq[i].username, self.new_uniqueUsernames[i], 'Username failed')
			self.assertEqual(self.uuniq[i].email, self.new_uniqueEmails[i], 'E-mail failed')

	def tearDown(self):
		uuniq.clear()
