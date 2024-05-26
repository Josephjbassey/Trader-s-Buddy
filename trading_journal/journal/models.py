from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class TradeEntry(Page):
    entry_time_date = models.DateTimeField()
    pair = models.CharField(max_length=100)
    long_short = models.CharField(max_length=10)
    lot = models.DecimalField(max_digits=10, decimal_places=2)
    entry_price = models.DecimalField(max_digits=10, decimal_places=4)
    stop_loss = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    take_profit = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    planned_rr = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    exit_price = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    exit_time_date = models.DateTimeField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    actual_rr = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    profit_loss = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    account_change = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    account_balance_before = models.DecimalField(max_digits=10, decimal_places=2)
    screenshot_before = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )
    screenshot_after = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )
    mistakes = models.TextField(null=True, blank=True)
    setup = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('entry_time_date'),
        FieldPanel('pair'),
        FieldPanel('long_short'),
        FieldPanel('lot'),
        FieldPanel('entry_price'),
        FieldPanel('stop_loss'),
        FieldPanel('take_profit'),
        FieldPanel('planned_rr'),
        FieldPanel('exit_price'),
        FieldPanel('exit_time_date'),
        FieldPanel('duration'),
        FieldPanel('actual_rr'),
        FieldPanel('profit_loss'),
        FieldPanel('account_change'),
        FieldPanel('account_balance_before'),
        ImageChooserPanel('screenshot_before'),
        ImageChooserPanel('screenshot_after'),
        FieldPanel('mistakes'),
        FieldPanel('setup'),
        FieldPanel('notes'),
    ]

    def __str__(self):
        return f"{self.pair} - {self.entry_time_date}"
