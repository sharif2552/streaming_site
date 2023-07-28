from django.contrib import admin
from . models import video , comment, chategory
# Register your models here.
admin.site.register(video)
admin.site.register(comment)
admin.site.register(chategory)