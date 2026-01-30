from tkinter import Widget
from django import forms
from .models import workAssignments, Requests

class workform(forms.ModelForm):
    
    def __init__(self,*args,**kwargs):
            current_user=kwargs.pop("current_user",None)
            super().__init__(*args, **kwargs)

            if current_user:
                self.fields["taskerId"].queryset=(
                    self.fields["taskerId"].queryset.exclude(
                        eID=current_user.username
                    )
                )
    class Meta:
        model=workAssignments
        widgets={
            "assignDate" : forms.DateInput(attrs={'type':'datetime-local'}),
            "dueDate" : forms.DateInput(attrs={'type':'datetime-local'}),
            }
        labels={"assignerId" : "Select Your Id"}
        
        fields=[
            "assignerId",
            "work",
            "assignDate",
            "dueDate",
            "taskerId",

        ]

class workStatusForm(forms.ModelForm):
    class Meta:
        model=workAssignments
        fields=["workStatus"]
        
class makeRequestForm(forms.ModelForm):
    class Meta:
        model=Requests
        widgets={
            "requestDate" : forms.DateInput(attrs={'type':'datetime-local'}),
            }
        labels={"requesterId" : "Select Your Id"}
        
        fields=[
            "requesterId",
            "requestMessage",
            "requestDate",
            "requestStatus",
            "destinationEmployeeId",
        ]