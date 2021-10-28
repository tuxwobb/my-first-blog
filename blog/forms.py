from django import forms
from .models import Post, Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'photo', 'category')
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description')