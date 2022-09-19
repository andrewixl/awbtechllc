from __future__ import unicode_literals
from django.db import models
import re

class ContactManager(models.Manager):
	def registerVal(self, postData):
		results = {'status': True, 'errors': [], 'user': None}
		if len(postData['name']) < 2:
			results['status'] = False
			results['errors'].append('Name must be at least 3 characters - Account Not Created')

		if not re.match(r"[^@]+@[^@]+\.[^@]+", postData['email']):
			results['status'] = False
			results['errors'].append('Email entered is invalid  - Account Not Created')

		user = Contact.objects.filter(email = postData['email'].lower())

		#check to see if user is not in db
		return results
	def createContact(self, postData):
		contact = Contact.objects.create(
			name = postData['name'], 
			email = postData['email'].lower(), 
			subject = postData['subject'], 
            message = postData['message'],)
		return contact

class Contact(models.Model):
	name = models.CharField(verbose_name='Name', max_length = 50)
	email = models.EmailField(verbose_name='Email Address', max_length = 50)
	subject = models.CharField(verbose_name='Subject', max_length = 1000)
	message = models.TextField(verbose_name='Message', max_length = 5000)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = ContactManager()

	def __str__(self):
		return self.name

