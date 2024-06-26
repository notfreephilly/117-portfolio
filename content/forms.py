from django import forms
from  .models import Project

class Projectform(forms.ModelForm):
    class Meta:
        model = Project
        field = ["name", "description", "year", "image", "repository", "technologies"]

        widgets = {
            "name": form.TextInput(attrs={"placeholder": "Project Name"}),

            "description": forms.TextInput(attrs={"placeholder": "Description"}),

            "year": forms.NumberInput(attrs={"placeholder": "yyyy"}),

            "image": forms.ClearableFileInput(attrs={"placeholder": "Select an Image"}),

            "repository": forms.URLInput(attrs={"placeholder": "GitHub URL"})
        }