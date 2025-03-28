from django import forms
from .models import Comment, Review

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']