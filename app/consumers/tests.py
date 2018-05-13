from django.test import TestCase
from .models import Consumer
from django.core.exceptions import ValidationError

class ConsumerModelTests(TestCase):

    def test_cannot_add_consumer_with_encorrect_email(self):
        """
        Invlid email for Consumer will raise ValidationError.
        """
        c = Consumer(name="correct name", email="invalidEmail")
        with self.assertRaises(ValidationError):
            c.full_clean()


    def test_cannot_add_consumer_with_encorrect_name(self):
        """
        Invlid name for Consumer will raise ValidationError. 
        Minimum length for name is 4 chars.
        """
        c = Consumer(name="inc", email="valid@email.com")
        with self.assertRaises(ValidationError):
            c.full_clean()

    def test_cannot_add_consumer_with_empty_name_email(self):
        """
        Name and email cannot be empty, It will raise ValidationError.
        """
        c = Consumer(name="", email="")
        with self.assertRaises(ValidationError):
            c.full_clean()

    def test_cannot_add_consumer_with_duplicate_email(self):
        """
        Email should be unique, else it will result in ValidationError.
        """
        #Adding user first time
        c1 = Consumer(name="correct name", email="duplicate@email.com")        
        c1.full_clean()
        #Saved in DB successfully
        c1.save()
        
        #Trying to add user with same email ID again
        c2 = Consumer(name="correct name", email="duplicate@email.com")
        #Validation Error is expected
        with self.assertRaises(ValidationError):
            c2.full_clean()


    def test_consumer_add_with_correct_data(self):
        """
        If email and name is correct.It should add consumer in database
        """
        c = Consumer(name="correct name", email="correct@email.com")
        c.full_clean()
        c.save()
        #Saved in DB successfully
        self.assertEqual((c.id >= 1), True)