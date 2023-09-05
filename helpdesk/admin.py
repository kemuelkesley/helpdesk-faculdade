from django.contrib import admin

from helpdesk.models import Ticket, Comment, Category


class TicketAdmin(admin.ModelAdmin):
    list_display = ('id' ,'title',)
    list_display_links = ('title',)
   


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Comment)
admin.site.register(Category)

