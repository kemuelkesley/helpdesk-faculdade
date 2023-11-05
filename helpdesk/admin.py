from django.contrib import admin
from django.http import HttpResponse, HttpResponseRedirect

from helpdesk.models import Ticket, Comentario, Categoria
from django.utils import timezone
from django.urls import reverse
from django.utils.http import urlencode

from import_export.admin import ImportExportModelAdmin
from .models import Ticket

# Register your models here.



class TicketAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    list_display = ('numero_chamado', 'titulo', 'condominio' , 'user', 'status', 'created_at', 'closed_at',)
    # Exclua o campo 'closed_at' do formulário de edição
    exclude = ('closed_at',) 

    list_display_links = ('numero_chamado', 'titulo', 'condominio')
    list_filter = ('numero_chamado', 'user', 'status',)
    list_editable = ('user', 'status',)
      
    readonly_fields = ('numero_chamado', 'created_at', 'status',)

    list_per_page = 10   

    fieldsets = (
        ('Dados do chamado', {
            'fields': ('numero_chamado', 'condominio', 'user', 'categoria'  ,'titulo', 'descricao', 'status', 'created_at', )
        }),
    )
        


    def mark_as_closed(self, request, queryset):
        # Atualize o status para "fechado" e defina a data de fechamento para os chamados selecionados
        queryset.update(status='fechado', closed_at=timezone.now())
        self.message_user(request, f'{queryset.count()} chamados foram marcados como fechados.')

    mark_as_closed.short_description = 'Marcar selecionados como Fechados'

    def view_closed_tickets(self, request, queryset):
        url = reverse('helpdesk_ticket_changelist') + '?' + urlencode({'status__exact': 'fechado'})
        return HttpResponseRedirect(url)

    view_closed_tickets.short_description = 'Visualizar Chamados Fechados'

   


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('get_numero_chamado','ticket', 'user', 'created_at',)
    list_filter = ('id','ticket', 'user',  'comentario',)
    list_display_links = ('ticket', 'user', 'created_at',)
    readonly_fields = ('get_numero_chamado', 'categoria', 'status')

   
    def get_numero_chamado(self, obj):
        return obj.ticket.numero_chamado
    
    get_numero_chamado.short_description = 'Número do Chamado'
    # Deixa o link clicavel
    get_numero_chamado.admin_order_field = 'ticket__numero_chamado'

 



    # def has_add_permission(self, request):
    #     return False

    # def has_change_permission(self, request, obj=None):
    #     return False


admin.site.register(Ticket, TicketAdmin)
admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(Categoria)

