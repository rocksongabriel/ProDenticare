from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class ServicesPage(Page):
    """Page model for the services page"""
    max_count = 1
    subpage_types = ["services.ServicePage"]
    template = "services/services_page.html"
    pass


class ServicePage(Page):
    """Page model for an individual service"""
    parent_page_types = ["services.ServicesPage"]

    name = models.CharField(
        max_length=255,
        help_text="Enter the name of the service, this is the same as the title of the page",
        null=False,
        blank=False,
    )
    description = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("name"),
        
    ]