from django.contrib import admin
from .models import Service, Order, Review, Discount, Faq, Report
from django.contrib.auth.models import User
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.
def make_reviews_as_viewed(modeladmin, request, queryset):
    queryset.update(is_viewed=True)
make_reviews_as_viewed.short_description = "Отметить выбранные отзывы как просмотренные"

class ReviewResource(resources.ModelResource):
    class Meta:
        model = Review

@admin.register(Review)
class ReviewAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ordering = ['is_viewed']
    list_display = ('client', 'order', 'date_created', 'text', 'scores', 'is_viewed',)
    actions = [make_reviews_as_viewed]
    resource_class = ReviewResource


class ServiceResource(resources.ModelResource):
    class Meta:
        model = Service

@admin.register(Service)
class ServiceAdmin(ImportExportModelAdmin):
    resource_class = ServiceResource


class OrderResource(resources.ModelResource):
    class Meta:
        model = Order

@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    resource_class = OrderResource


class DiscountResource(resources.ModelResource):
    class Meta:
        model = Discount

@admin.register(Discount)
class DiscountAdmin(ImportExportModelAdmin):
    resource_class = DiscountResource


class FaqResource(resources.ModelResource):
    class Meta:
        model = Faq

@admin.register(Faq)
class FaqAdmin(ImportExportModelAdmin):
    resource_class = FaqResource


class ReportResource(resources.ModelResource):
    class Meta:
        model = Report

@admin.register(Report)
class ReportAdmin(ImportExportModelAdmin):
    resource_class = ReportResource


class OrderInline(admin.TabularInline):
    model = Order
    extra = 1

class ReportInline(admin.TabularInline):
    model = Report
    extra = 1

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1

class UserResource(resources.ModelResource):
    class Meta:
        model = User

admin.site.unregister(User)
@admin.register(User)
class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
   inlines = [OrderInline, ReportInline, ReviewInline]
   resource_class = UserResource