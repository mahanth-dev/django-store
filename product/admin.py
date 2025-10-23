from django.contrib import admin

# Register your models here.

from .models import AttrbiuteProduct, Product, ProductImage ,Category ,ProdctPakage 

class AttributeInline(admin.TabularInline):
    list_display = ['product__title','name','value']
    model = AttrbiuteProduct
    extra = 2

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductCollerInline(admin.TabularInline):
    model = ProdctPakage
    extra = 1


class ProudctAdmin(admin.ModelAdmin):
    list_display = ["title"]
    inlines = [AttributeInline,ProductImageInline,ProductCollerInline]
    exclude = ['final_price']
    filter_horizontal =("categories",)
    
    



admin.site.register(Product,ProudctAdmin)


admin.site.register(ProductImage)
admin.site.register(AttrbiuteProduct)
admin.site.register(Category)
admin.site.register(ProdctPakage)

