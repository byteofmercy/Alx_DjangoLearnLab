from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    # add a default so migrations won't ask for a one-off value
    author = models.CharField(max_length=255, default='Unknown')
    published = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.title

    class Meta:
        # keep these exact codenames: can_view, can_create, can_edit, can_delete
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]


