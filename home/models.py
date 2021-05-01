from django.db import models
from wagtail.admin.edit_handlers import (FieldPanel, MultiFieldPanel,
                                         PageChooserPanel)
from wagtail.core.models import Page
from wagtail.images.edit_handlers import ImageChooserPanel
from services.models import ServicePage


class HomePage(Page):
    """Page model for the homepage"""
    max_count = 1

    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        related_name="+",
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        help_text="Pick an image that will displayed as the banner image"
    )
    banner_text = models.CharField(
        max_length=200,
        help_text="Enter text that will be displayed on the banner image",
        default="",
    )
    banner_button_text = models.CharField(
        max_length=20,
        help_text="Enter text that will appear on the button on the banner",
        default="",
    )
    banner_button_page = models.ForeignKey(
        "wagtailcore.Page",
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
        help_text="Select a page that this button leads to"
    )

    about_us_text = models.TextField(
        help_text="Enter a small description of the company",
        null=False,
        blank=False,
        default=""
    )

    about_us_image = models.ForeignKey(
        "wagtailimages.Image",
        related_name="+",
        help_text="Select an image to use for the about section on the homepage",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
    )

    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['services'] = ServicePage.objects.all().live()[:6]
        print(context['services'])
        return context
    
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel("banner_image"),
            FieldPanel("banner_text"),
        ], heading="Banner Information"),
        MultiFieldPanel([
            FieldPanel("banner_button_text"),
            PageChooserPanel("banner_button_page"),
        ], heading="Banner Button Information"),
        MultiFieldPanel([
            FieldPanel("about_us_text"),
            ImageChooserPanel("about_us_image"),
        ], heading="About Us Section Information"),
    ]