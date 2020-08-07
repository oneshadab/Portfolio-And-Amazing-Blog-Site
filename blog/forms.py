from django.forms import ModelForm
from .models import UserBlog 


#Form class for userBlog model
class UserBlogForm(ModelForm):
    class Meta:
        model = UserBlog
        fields = ["title", 'content', 'images']