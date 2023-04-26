from django import forms
from ModelFormApp.models import Student

class StudentForm(forms.ModelForm):
    #fields with validations(Not-Required...)
	#model-field are taken-here automatically
    class Meta:
        model=Student;
        fields='__all__';