from django.contrib import admin
from .models import Material, Media
# from .models import Material, Media

# class MaterialAdmin(admin.ModelAdmin):


# Register your models here.


class MediaInline(admin.TabularInline):
    model = Media
    extra = 1
    exclude = ('mime_type',)
    

class MaterialAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['material_text']}),
    ]
    inlines = [MediaInline]
    #list_display = ('material_text')
    

admin.site.register(Material, MaterialAdmin)