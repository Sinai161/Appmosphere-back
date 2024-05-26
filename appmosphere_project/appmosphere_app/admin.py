from django.contrib import admin
from .models import Profilepage
from .models import Comment
from .models import Feed
from .models import User
# Register your models here.

admin.site.register(Profilepage)
admin.site.register(Comment)
admin.site.register(Feed)
admin.site.register(User)