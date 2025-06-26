from django.db import models
from customers.models import Customer
from django.contrib.auth import get_user_model

User = get_user_model()

class Note(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='notes')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note for {self.customer} by {self.author}"

