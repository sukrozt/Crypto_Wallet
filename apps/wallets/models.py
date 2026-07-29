from django.db import models

class Wallet(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username}'s wallet"