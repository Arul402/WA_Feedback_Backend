from django.db import models

class Feedbacks(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    rating = models.IntegerField(choices=[(i, f"{i} Star") for i in range(1, 6)])
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating} Stars"
