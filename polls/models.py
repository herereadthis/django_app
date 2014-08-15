import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
# A model is a source of data about the data, containing the essential fields
# and behaviors of the data you're storing.
# Each model is represented by a class that subclasses django.db.models.Model
# Each model has class variables, which represent a database field in the
# model.
# The Poll model has a question and publication date.
# The Choice Model has a choice and vote tally.
# Each Choice is associated with a Poll


class Poll(models.Model):
    # Each field is represented by an instance of Field class (e.g. Charfield)
    question = models.CharField(max_length=200)
    # The name of each field instance is the name (aka Poll.pub_date)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    # this means each Choice is related to a single Poll
    # by convention, Django appens "_id" to foreign key field name (poll_id)
    poll = models.ForeignKey(Poll)
    # CharField requires giving a max_length, for database schema & validation.
    choice_text = models.CharField(max_length=200)
    # A Field can have optional arguments such setting default to 0.
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text
