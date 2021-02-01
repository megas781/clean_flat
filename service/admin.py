from django.contrib import admin
from .models import Service, Order, Review, Discount, Faq, Report
from django.contrib.auth.models import User

# Register your models here.
def make_reviews_as_viewed(modeladmin, request, queryset):
    queryset.update(is_viewed=True)
make_reviews_as_viewed.short_description = "Отметить выбранные отзывы как просмотренные"

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    ordering = ['is_viewed']
    list_display = ('client', 'order', 'date_created', 'text', 'scores', 'is_viewed',)
    actions = [make_reviews_as_viewed]

class OrderInline(admin.TabularInline):
    model = Order
    extra = 1

class ReportInline(admin.TabularInline):
    model = Report
    extra = 1

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1

class UserAdmin(admin.ModelAdmin):
   inlines = [OrderInline, ReportInline, ReviewInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Service)
admin.site.register(Order)
admin.site.register(Discount)
admin.site.register(Faq)
admin.site.register(Report)