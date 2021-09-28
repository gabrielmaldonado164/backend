from django.contrib import admin

# Register your models here.

from tickets.models.tickets import Ticket
from tickets.models.choices import Choices
from tickets.models.history import History
from tickets.models.comments import Comment

class TicketsAdmin(admin.ModelAdmin):
    list_display = ['id','domain','creation_date','area']
    list_display_links = ['id','domain']
    search_fields = ['id','domain','area']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','creation_date',]
    list_display_links = ['id', 'creation_date']

class HistoryAdmin(admin.ModelAdmin):
    list_display = ['id','creation_date',]

admin.site.register(Ticket,TicketsAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(History, HistoryAdmin)


