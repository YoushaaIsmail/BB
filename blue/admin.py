from django.contrib import admin
from .models import Contact
from .models import Product,profile,categoriesPRODUCT
# ,categoriesPRODUCT
admin.site.register(categoriesPRODUCT)
admin.site.register(profile)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')

admin.site.register(Contact, ContactAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'details']

admin.site.register(Product, ProductAdmin)


from django.contrib import admin
from .models import AboutUs

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title', 'description')
    fields = ('title', 'description', 'image')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return obj.image.url if obj.image else ''

