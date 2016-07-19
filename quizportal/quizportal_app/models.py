from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Quiz(models.Model):
	quiz_id= models.AutoField(primary_key= True)
	quiz_name= models.CharField(max_length= 35)
	quiz_startDateTime= models.DateTimeField()
	quiz_endDateTime= models.DateTimeField()
	quiz_maxMarks= models.IntegerField(default=0)
	def __unicode__(self):
		return u'%s' % (self.quiz_name)


class UserProfile(models.Model):
	user= models.OneToOneField(User)
	user_quizes= models.ManyToManyField(Quiz)
	def __unicode__(self):
		return u'%s' % (self.user.username)


class QuestionMC(models.Model):
	questionMC_id= models.AutoField(primary_key= True)
	question_text= models.TextField()
	questionMC_quiz= models.ForeignKey(Quiz)
	questionMC_maxMarks= models.IntegerField(default=0, null= False)
	questionMC_attempted= models.BooleanField(default= False)
	def __unicode__(self):
		return u'%s' % (self.questionMC_id)


class Choice(models.Model):
	choice_id= models.AutoField(primary_key=True)
	choice_answer= models.BooleanField(default=False)
	choice_questionMC= models.ForeignKey(QuestionMC)
	choice_text= models.TextField()
	def __unicode__(self):
		return u'%s' % (self.choice_text)


class QuestionSA(models.Model):
	questionSA_id= models.AutoField(primary_key=True)
	questionSA_text= models.TextField()
	questionSA_answer= models.TextField()
	questionSA_maxMarks= models.IntegerField(default=0, null= False)
	questionSA_attempted= models.BooleanField(default=False)
	def __unicode__(self):
		return u'%s' % (self.questionSA_id)


class User_QuizMarks(models.Model):
	marksScored= models.IntegerField(default=0)
	quizMarks_quiz= models.OneToOneField(Quiz, default=0)
	quizMarks_user= models.ForeignKey(User)
	quizMarks_completed= models.BooleanField()
	quizMarks_rank= models.IntegerField(null=True)
	def __unicode__(self):
		return u'%s' % (self.quizMarks_quiz.quiz_name)


