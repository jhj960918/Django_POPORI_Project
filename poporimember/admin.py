from django.contrib import admin
from .models import CustomUser
# Register your models here.
class userAdmin(admin.ModelAdmin):
    list_display = ('username', 'password') # 관리자 사이트에서 보고싶은 필드


admin.site.register(CustomUser, userAdmin)