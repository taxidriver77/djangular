from django.contrib import admin

# Register your models here.
from .models import Customer,ListCustomer,Company

#admin.site.register(Customer)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
	fieldsets = [
		("Customer Details", {"fields": ["name", "companies"]}),
		("Review", {"fields": ["is_favourite", "review", "reviewed_by"]}),
	]

	#readonly_fields = ("date_reviewed",)

	def customer_companies(self, obj):
		return obj.list_companies()

	customer_companies.short_description = "Company(s)"

	list_display = ("name", "customer_companies", "is_favourite",)
	list_editable = ("is_favourite",)
	list_display_links = ("name",)
	list_filter = ("is_favourite",)
	search_fields = ("name", "companies__name",)

admin.site.register(ListCustomer)
admin.site.register(Company)