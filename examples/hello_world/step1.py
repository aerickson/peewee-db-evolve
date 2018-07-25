import peeweedbevolve
# import peewee as pw
import peewee

from flask_security import UserMixin, RoleMixin


db = peewee.PostgresqlDatabase('example_hello_world')

# simple class

class Person(peewee.Model):
  first_name = peewee.CharField(null=True)
  birthday = peewee.DateField(null=True)
  is_relative = peewee.BooleanField(default=False)

  class Meta:
    database = db

# more complex: test with mixins and inheritance

class BaseModel(peewee.Model):
    class Meta:
        database = db

class Role(BaseModel, RoleMixin):
    name = peewee.CharField(unique=True)
    description = peewee.TextField(null=True)

# evolve

db.evolve(ignore_tables=['BaseModel']) # call this instead of db.create_tables([Person])
