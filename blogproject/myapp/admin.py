from django.contrib import admin
from myapp.models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status']
    prepopulated_fields={'slug':('title',)}
    list_filter=('status','created','publish','author')
    search_fields=['title','body']
    raw_id_fields=('author',)
    ordering=['status','publish']
    date_hirearchy=('publish',)
admin.site.register(Post,PostAdmin)
