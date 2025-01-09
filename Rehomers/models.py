from django.db import models
from django.conf import settings


# Rehomer Profile Model
class RehomerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rehomer_profile')
    bio = models.TextField(blank=True, null=True)
    rehome_history = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"

# Rehomer Application Model
class RehomerApplication(models.Model):
    rehomer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rehomer_applications')
    pet = models.ForeignKey('Pets.Pet', on_delete=models.CASCADE, related_name='rehomer_applications')
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending') 
    reason = models.TextField(blank=False, null=False, choices=[
            ('Behavioural issues', 'Behavioural issues'),
            ('Busy schedule', 'Busy schedule'),
            ('Change in family circumstances', 'Change in family circumstances'),
            ('Does not get along with another pet', 'Does not get along with another pet'),
            ('Fostered', 'Fostered'),
            ('Found', 'Found or abandoned'),
            ('Human health issues', 'Human health issues (e.g., allergies, sickness)'),
            ('Infant, young children or pregnancy', 'Infant, young children or pregnancy'),
            ('Landlord permission issues', 'Landlord permission issues'),
            ('Ongoing costs', 'Ongoing costs (e.g., lost job)'),
            ('Pet medical expenses', 'Pet medical expenses (e.g., vet procedure)')
        ],
        default='Busy schedule')  

    def __str__(self):
        return f"Application by {self.rehomer.email} for {self.pet}"