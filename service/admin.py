from django.contrib import admin
from .models import Service, Order, Review, Discount, Faq, Report
from django.contrib.auth.models import User
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.
def make_reviews_as_viewed(modeladmin, request, queryset):
    queryset.update(is_viewed=True)
make_reviews_as_viewed.short_description = "Отметить выбранные отзывы как просмотренные"

def make_reviews_as_unviewed(modeladmin, request, queryset):
    queryset.update(is_viewed=False)
make_reviews_as_unviewed.short_description = "Отметить выбранные отзывы как непросмотренные"

class ReviewResource(resources.ModelResource):
    class Meta:
        model = Review

@admin.register(Review)
class ReviewAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    date_hierarchy = 'date_created'
    list_filter = ('date_created', 'scores', 'is_viewed',)
    ordering = ['is_viewed']
    list_display = ('client', 'order', 'get_text', 'date_created', 'scores', 'is_viewed',)
    actions = [make_reviews_as_viewed, make_reviews_as_unviewed]
    resource_class = ReviewResource

    def get_text(self, obj):
        return u"%s..." % (obj.text[:50],)
    get_text.short_description = 'Текст'

class ServiceResource(resources.ModelResource):
    class Meta:
        model = Service

@admin.register(Service)
class ServiceAdmin(ImportExportModelAdmin):
    resource_class = ServiceResource
    date_hierarchy = 'date_created'
    # search_fields = ('user',)
    list_display = ('title', 'get_description', 'initial_price', 'add_room_price', 'add_bathroom_price', 'date_created')

    def get_description(self, obj):
        return u"%s..." % (obj.description[:50],)
    get_description.short_description = 'Описание'


class OrderResource(resources.ModelResource):
    class Meta:
        model = Order

@admin.register(Order)
class OrderAdmin(ImportExportModelAdmin):
    date_hierarchy = 'date_created'
    list_filter = ('order_date', 'date_created', 'service_type', 'room_count', 'bathroom_count')
    # search_fields = ('user',)
    list_display = ('get_order_name', 'order_date', 'date_created', 'service_type', 'room_count', 'bathroom_count', 'get_all_price')
    resource_class = OrderResource

    def get_all_price(self, obj):
        queryset = obj.all_price()
        return queryset
    get_all_price.short_description = 'Стоимость (руб)'

    def get_order_name(self, obj):
        queryset = obj.__str__()
        return queryset
    get_order_name.short_description = 'Название'



class DiscountResource(resources.ModelResource):
    class Meta:
        model = Discount

@admin.register(Discount)
class DiscountAdmin(ImportExportModelAdmin):
    date_hierarchy = 'date_end'
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
    date_hierarchy = 'date_created'
    list_filter = ('date_created',)
    list_display = ('client', 'get_text', 'date_created')
    resource_class = ReportResource

    def get_text(self, obj):
        return u"%s..." % (obj.text[:50],)
    get_text.short_description = 'Текст'


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
    date_hierarchy = 'date_joined'
    list_filter = ('last_login', 'is_staff', 'is_superuser')