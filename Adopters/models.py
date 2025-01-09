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
        return f"{self.user.email} - Adopter Profile"

class AdoptionApplication(models.Model):
   
    adopter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='adoption_applications')
    pet = models.ForeignKey('Pets.Pet', on_delete=models.CASCADE, related_name='adoption_applications')  # assuming pets app with Pet model
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')
    motivation = models.TextField()  

    def __str__(self):
        return f"Application by {self.adopter.email} for {self.pet}"

class AdopterReference(models.Model):
    # References provided by adopters to validate their application
    adopter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='adopter_references')
    name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    relationship = models.CharField(max_length=100, blank=True, null=True)  # e.g., 'Friend', 'Colleague'
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Reference for {self.adopter.email} - {self.name}"