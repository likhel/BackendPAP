from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, Permission, Group
from core import settings





class PetCategory(models.Model):
    category_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name

# Create your models here.
class Pet(models.Model):

      

    # Linking the pet to a rehomer profile
    rehomer = models.ForeignKey('Rehomers.RehomerProfile', on_delete=models.CASCADE, related_name='pets', null=True)
    adopter = models.ForeignKey(
    'Adopters.AdopterProfile',  # Replace with the actual model name for adopters
    on_delete=models.SET_NULL,  # Allows the adopter field to be set to NULL if the adopter is deleted
    related_name='adopted_pets',  # Enables reverse querying
    null=True,  # Allows NULL values in the database
    blank=True ) # Makes the field optional in forms
    category = models.ForeignKey(PetCategory, on_delete=models.SET_NULL, null=True, related_name='pets')
   
    name = models.CharField(max_length=50) 
    age = models.IntegerField()  
    breed = models.CharField(max_length=50)  
    size = models.CharField(max_length=20, choices=[
            ('small', 'Small'),
            ('medium', 'Medium'),
            ('large', 'Large'),
        ],default='medium')  
    gender = models.CharField(max_length=10, choices=[
            ('male', 'Male'),
            ('female', 'Female'),
        ],default='male')  
    sterilization = models.CharField(max_length=10, choices=[('yes', 'Yes'), ('no', 'No')],default='yes')  # Spayed/neutered status
    description = models.TextField(blank=True)  
    pet_image = models.ImageField(upload_to="pets/", null=True, blank=True)  
    owned_time = models.CharField(max_length=50,choices=[
            ('less than 1 week', 'Less than 1 week'),
            ('1 week', '1 week'),
            ('2 weeks', '2 weeks'),
            ('3 weeks', '3 weeks'),
            ('1 month', '1 month'),
            ('2 months', '2 months'),
            ('over 2 months', 'Over 2 months')
        ],
        default='1 week')  # How long the pet has been owned
    source = models.CharField(max_length=50, choices=[
            ('Breeder', 'Breeder'),
            ('Friend/Family', 'Friend/Family'),
            ('Found', 'Found'),
            ('Fostered', 'Fostered'),
            ('Charity/RescueCenter', 'Charity/Rescue Center'),
            ('PetShop', 'Pet Shop'),
            ('OwnerSeller/Marketplace', 'Owner Seller/Marketplace'),
            ('Other', 'Other'),
        ],default='Breeder')  # Where did the pet come from
    color = models.CharField(max_length=50,choices=[   # Pet's choices=[
            ('Black', 'Black'),
            ('Brown/Chocolate', 'Brown/Chocolate'),
            ('Blue', 'Blue'),
            ('Cream/Fawn/Yellow', 'Cream/Fawn/Yellow'),
            ('Mixed Color', 'Mixed Color'),
            ('Red/Ginger', 'Red/Ginger'),
            ('White', 'White'),
            ('Silver/Grey', 'Silver/Grey'),
            ('Gold/Apricot', 'Gold/Apricot'),
            ('Other', 'Other'),
        ],default='Black',
        blank=True)
   
    # Household-specific fields
    household_activity = models.CharField(max_length=100,choices=[('Busy / Noisy', 'Busy / Noisy'),
        ('Moderate comings and goings', 'Moderate comings and goings'),
        ('Quiet with occasional guests', 'Quiet with occasional guests')],
        default='Moderate comings and goings',null=True,blank=True )  # Household activity level
    lives_with_other_pets = models.CharField(max_length=100,choices=[
            ('Yes, my pet lives with cats', 'Yes, my pet lives with cats'),
            ('Yes, my pet lives with dogs', 'Yes, my pet lives with dogs'),
            ('No, my pet does not live with other pets', 'No, my pet does not live with other pets')
        ],
        default='No, my pet does not live with other pets')  # Yes/No/Details of other pets
    household_environment = models.CharField(max_length=100 ,choices=[
            ('Busy urban', 'Busy urban'),
            ('Suburban', 'Suburban'),
            ('Quiet rural', 'Quiet rural'),
            ('Farm-like', 'Farm-like')
        ],
        default='Suburban',
        blank=True)
    socialization_issues = models.CharField(max_length=100,choices=[
        ("Reacts badly to people", "Reacts badly to people"),
        ("Rects badly to other dogs", "Rects badly to other dogs"),
        ("Is aggresive", "Is aggressive"),
        ("Is a barker(to the point of being problematic)", "Is a barker (to the point of being problematic)"),
        ("Has separation anxiety", "Has separation anxiety"),
        ("Bites or nips", "Bites or nips"),
        ("Has no or limited recall", "Has no or limited recall"),
        ("Cannot be walked off the leash", "Cannot be walked off the leash"),
        ("Pulls on the lead(to the point of being problematic)", "Pulls on the lead (to the point of being problematic)"),
        ("Jumps or lunges(to the point of being problematic)", "Jumps or lunges (to the point of being problematic)"),
        ("Can demonstrate resource guarding at times", "Can demonstrate resource guarding at times"),
    ],blank=True,default='Jumps or lunges(to the point of being problematic)') 
    
    behaviour = models.CharField(max_length=100, blank=True,choices= [
        ("Good with adults", "Good with adults"),
        ("Good with children", "Good with children"),
        ("Good with other dogs", "Good with other dogs"),
        ("Needs to be only PET in the home", "Needs to be only PET in the home"),
        ("Has lived with other dogs-it was fine", "Has lived with other dogs-it was fine"),
        ("Has lived with other dogs-it didn't go well", "Has lived with other dogs-it didn't go well"),
        ("is fairly relaxed", "Is fairly relaxed"),
        ("is active and lively", "Is active and lively"),
        ("is only walked on the leash", "Is only walked on the leash"),
        ("Can be left alone for short to medium periods", "Can be left alone for short to medium periods"),
        ("Has good recall", "Has good recall"),
        ("Travel well in cars", "Travel well in cars"),
        ("Needs more exercise than most dogs", "Needs more exercise than most dogs"),
    ]
    ,default='Good with adults')

    posted_at = models.DateTimeField(auto_now_add=True)  # When the pet was posted

    def __str__(self):
        return f"{self.name} ({self.breed})"


