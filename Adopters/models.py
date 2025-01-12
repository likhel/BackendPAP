from django.db import models
from django.conf import settings

class AdopterProfile(models.Model):
    # Linking the profile to a user
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='adopter_profile')
    
    # Fields specific to adopter
    bio = models.TextField(blank=True, null=True)
    pet_preference = models.CharField(max_length=255, blank=True, null=True)  
    adoption_history = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - Adopter Profile"

class AdoptionApplication(models.Model):
    adopter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='adoption_applications',
    )
    pet = models.ForeignKey(
        'Pets.Pet',
        on_delete=models.CASCADE,
        related_name='adoption_applications'
    )
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')],
        default='pending'
    )
    motivation = models.TextField(default="") 
    district = models.CharField(max_length=100, default="Unknown District")  
    ward = models.PositiveIntegerField(default=1)  
    contact = models.CharField(max_length=15, default="")  
    garden = models.CharField(
        max_length=10,
        choices=[('yes', 'Yes'), ('no', 'No')],
        blank=True,
        default="no"
    )
    image = models.ImageField(
        upload_to='home_images/',
        blank=True,
        null=True
    )
    adults = models.PositiveIntegerField(default=0)  
    children = models.PositiveIntegerField(default=0)  
    visiting_children = models.CharField(
        max_length=10,
        choices=[('yes', 'Yes'), ('no', 'No')],
        blank=True,
        default="no"
    )
    other_animals = models.CharField(
        max_length=10,
        choices=[
            ('', 'Select'),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
            ('more', 'More than 3'),
        ],
        blank=True,
        default=""
    )
    home_type = models.TextField(blank=True, default="")
    household_activity = models.CharField(max_length=255, default="Moderate")  # Added
    work_pattern = models.TextField(default="")  # Added
    moving = models.CharField(
        max_length=10,
        choices=[('yes', 'Yes'), ('no', 'No')],
        default="no"
    )  # Added
    vehicle = models.CharField(
        max_length=10,
        choices=[('yes', 'Yes'), ('no', 'No')],
        default="no"
    )  # Added

    def __str__(self):
        return f"Application by {self.adopter.email} for {self.pet}"
