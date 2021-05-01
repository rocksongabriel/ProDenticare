from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class ServicesPage(Page):
    """Page model for the services page"""
    max_count = 1
    subpage_types = ["services.ServicePage"]
    template = "services/services_page.html"
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['services'] = ServicePage.objects.child_of(self).live()
        return context


class ServicePage(Page):
    """Page model for an individual service"""

    template = "services/service_page.html"

    parent_page_types = ["services.ServicesPage"]

    name = models.CharField(
        max_length=255,
        help_text="Enter the name of the service, this is the same as the title of the page",
        null=False,
        blank=False,
    )
    featured_image = models.ForeignKey(
        "wagtailimages.Image",
        help_text="Select an image to be featured on the service page, it will be used as a banner",
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
    )
    description = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel("name"),
        ImageChooserPanel("featured_image"),
        FieldPanel("description"),
    ]

    