from django.contrib import admin
from django.http import HttpResponseRedirect

from helpdesk.models import Ticket, Comment, Category
from django.utils import timezone
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode




class TicketAdmin(admin.ModelAdmin):
    list_display = ('numero_chamado', 'title', 'user', 'formatted_created_at','status', 'formatted_closed_at',)
   
    # Exclua o campo 'closed_at' do formulário de edição
    exclude = ('closed_at',) 

    list_display_links = ('numero_chamado', 'title',)
    list_filter = ('numero_chamado', 'user', 'status',)
    list_editable = ('user', 'status',)
    #search_fields = ('title', 'user__username', 'user__first_name', 'user__last_name', 'user__email', 'created_at',)
    # botão de ação para marcar como fechado ou aberto
    actions = ['mark_as_closed', 'mark_as_opened', 'mark_as_progress', 'view_closed_tickets',]
    readonly_fields = ('numero_chamado', 'created_at',)

    list_per_page = 10   

    fieldsets = (
        ('Dados do chamado', {
            'fields': ('numero_chamado', 'condominio', 'user', 'category'  ,'title', 'description', 'status', 'created_at',)
        }),
    )
        

    def formatted_created_at(self, obj):
        return obj.created_at.strftime("%d de %b %Y")

    formatted_created_at.short_description = "Data de Abertura"

    def formatted_closed_at(self, obj):
        return obj.closed_at.strftime("%d de %b %Y") if obj.closed_at else "-"

    formatted_closed_at.short_description = "Data de Fechamento"


    def mark_as_closed(self, request, queryset):
        # Atualize o status para "fechado" e defina a data de fechamento para os chamados selecionados
        queryset.update(status='fechado', closed_at=timezone.now())
        self.message_user(request, f'{queryset.count()} chamados foram marcados como fechados.')

    mark_as_closed.short_description = 'Marcar selecionados como Fechados'

    def view_closed_tickets(self, request, queryset):
        url = reverse('helpdesk_ticket_changelist') + '?' + urlencode({'status__exact': 'fechado'})
        return HttpResponseRedirect(url)

    view_closed_tickets.short_description = 'Visualizar Chamados Fechados'

    
        

class ClosedTicketAdmin(admin.ModelAdmin):
    list_display = ('numero_chamado', 'title', 'user', 'created_at', 'status', 'closed_at')

    list_filter = ('status',)  # Filtrar apenas chamados fechados


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Comment)
admin.site.register(Category)

