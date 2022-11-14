from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated']
    list_display_links = ['id', 'first_name']
    search_fields = ['id', 'first_name', 'last_name', 'email',
                     'address', 'postal_code', 'city']
    list_filter = ['paid', 'created', 'updated']
    ordering = ("-created",)
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
