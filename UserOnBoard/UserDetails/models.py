import uuid

from django.db import models


# Create your models here.

# Create your models here.
class BaseModel(models.Model):
    #   uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4())
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class UserDetails(BaseModel):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4())
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = 'UserDetails'


class UserAddress(BaseModel):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4())
    address = models.TextField(max_length=2000, blank=True, null=True)
    country = models.CharField(max_length=50)
    userDetails = models.OneToOneField(UserDetails, on_delete=models.CASCADE)

    def __str__(self):
        return self.address
