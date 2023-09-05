from django.contrib import admin

from helpdesk.models import Ticket, Comment, Category


class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'created_at','status',)
    list_display_links = ('title',)
    list_filter = ('user', 'status',)
   


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Comment)
admin.site.register(Category)

