from django.shortcuts import render
from ModelFormApp import forms

#Create your views here.
def student_view(request):
    sentdata = False;
    formObj=forms.StudentForm();
    if request.method=="POST":
        formObj=forms.StudentForm(request.POST);
        if formObj.is_valid():
            print('Given or Submitted Form data..!!')
            print('Name:', formObj.cleaned_data['name'])
            print('Marks:', formObj.cleaned_data['marks'])
            formObj.save(commit=True)
            sentdata = True;
            formObj = forms.StudentForm();
    return render(request, 'ModelFormApp/studentform.html',{"form1":formObj,'sentdata':sentdata });

