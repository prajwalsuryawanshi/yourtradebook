from django.db import models
from django.contrib.auth.models import User

class Trade(models.Model):
    TRADE_TYPES = [
        ('buy', 'Buy'),
        ('sell', 'Sell'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_trade = models.DateField()
    script_name = models.CharField(max_length=100)
    trade_type = models.CharField(max_length=4, choices=TRADE_TYPES)
    buying_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.script_name} - {self.trade_type} on {self.date_of_trade}"

    def calculate_pl(self):
        if self.trade_type == 'buy' and self.selling_price:
            return (self.selling_price - self.buying_price) * self.quantity
        elif self.trade_type == 'sell' and self.selling_price:
            return (self.buying_price - self.selling_price) * self.quantity
        return 0

    @staticmethod
    def calculate_lifetime_pl(user):
        trades = Trade.objects.filter(user=user)
        lifetime_pl = sum(trade.calculate_pl() for trade in trades)
        return lifetime_pl
