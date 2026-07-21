from django.db import models


class MenuOrder(models.Model):

    def __str__(self):
        first = self.details.first()
        if first:
            return first.value
        return f"Order #{self.id}"


class OrderDetail(models.Model):
    order = models.ForeignKey(
        MenuOrder,
        on_delete=models.CASCADE,
        related_name="details"
    )
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.key}: {self.value}"


class MenuSection(models.Model):
    menu_order = models.ForeignKey(
        MenuOrder,
        on_delete=models.CASCADE,
        related_name="sections"
    )

    category = models.CharField(max_length=100)
    items = models.TextField()

    def get_items(self):
        return [
            item.strip()
            for item in self.items.split("\n")
            if item.strip()
        ]


class Bill(models.Model):
    total = models.CharField(max_length=255, blank=True)

    def __str__(self):
        first = self.details.first()
        if first:
            return first.value
        return f"Bill #{self.id}"


class BillDetail(models.Model):
    bill = models.ForeignKey(
        Bill,
        on_delete=models.CASCADE,
        related_name="details"
    )
    key = models.CharField(max_length=100, blank=True)
    value = models.CharField(max_length=255, blank=True)


class BillItem(models.Model):
    bill = models.ForeignKey(
        Bill,
        on_delete=models.CASCADE,
        related_name="items"
    )
    key = models.CharField(max_length=200, blank=True)
    value = models.CharField(max_length=255, blank=True)