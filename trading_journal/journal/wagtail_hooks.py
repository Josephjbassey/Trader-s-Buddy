from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import TradeEntry, CompoundPlan, ToDoItem

class TradeEntryAdmin(ModelAdmin):
    model = TradeEntry
    menu_label = 'Trade Entries'
    menu_icon = 'doc-full'
    list_display = ('pair', 'entry_time_date', 'profit_loss')
    search_fields = ('pair', 'notes')

class CompoundPlanAdmin(ModelAdmin):
    model = CompoundPlan
    menu_label = 'Compound Plans'
    menu_icon = 'doc-full'
    list_display = ('goal_name', 'initial_balance', 'target_balance', 'target_date')
    search_fields = ('goal_name', 'notes')

class ToDoItemAdmin(ModelAdmin):
    model = ToDoItem
    menu_label = 'To-Do Items'
    menu_icon = 'doc-full'
    list_display = ('task_name', 'due_date', 'is_complete')
    search_fields = ('task_name',)

modeladmin_register(TradeEntryAdmin)
modeladmin_register(CompoundPlanAdmin)
modeladmin_register(ToDoItemAdmin)
