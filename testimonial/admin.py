from django.contrib import admin
from testimonial.models import Testimonial

# Register your models here.
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'company_name', 'published', 'pub_date')
    list_filter  = ['category', 'published', 'pub_date']

admin.site.register(Testimonial, TestimonialAdmin)
