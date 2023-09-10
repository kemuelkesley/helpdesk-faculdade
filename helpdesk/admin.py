from django.contrib import admin

from helpdesk.models import Ticket, Comment, Category
from django.utils import timezone


class TicketAdmin(admin.ModelAdmin):
    list_display = ('numero_chamado', 'title', 'user', 'created_at','status', 'closed_at',)

    # Exclua o campo 'closed_at' do formulário de edição
    exclude = ('closed_at',) 

    list_display_links = ('numero_chamado', 'title',)
    list_filter = ('user', 'status',)
    list_editable = ('user', 'status',)
    #search_fields = ('title', 'user__username', 'user__first_name', 'user__last_name', 'user__email', 'created_at',)
    # botão de ação para marcar como fechado ou aberto
    actions = ['mark_as_closed', 'mark_as_opened', 'mark_as_progress']
    readonly_fields = ('numero_chamado', 'created_at',)
   
    fieldsets = (
        ('Dados do chamado', {
            'fields': ('numero_chamado', 'condominio', 'user', 'title', 'description', 'status', 'created_at',)
        }),
    )

    # def mark_as_opened(self, request, queryset):
    #     queryset.update(status='Aberto')

    # def mark_as_closed(self, request, queryset):
    #     queryset.update(status='Fechado')

    # def mark_as_progress(self, request, queryset):
    #     queryset.update(status='Andamento')

    # def get_queryset(self, request):
    #     qs = super(TicketAdmin, self).get_queryset(request)
    #     if request.user.is_superuser:
    #         return qs
    #     return qs.filter(user=request.user)
   

    # mark_as_closed.short_description = 'Marcar como fechado'
    # mark_as_opened.short_description = 'Marcar como aberto'

    def mark_as_closed(self, request, queryset):
        # Atualize o status para "fechado" e defina a data de fechamento para os chamados selecionados
        queryset.update(status='fechado', closed_at=timezone.now())
        self.message_user(request, f'{queryset.count()} chamados foram marcados como fechados.')

    mark_as_closed.short_description = 'Marcar selecionados como Fechados'

   
    



admin.site.register(Ticket, TicketAdmin)
admin.site.register(Comment)
admin.site.register(Category)

