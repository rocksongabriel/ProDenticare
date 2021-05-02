from django.db import models
from wagtail.admin.edit_handlers import (FieldPanel, MultiFieldPanel,
                                         StreamFieldPanel)
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from streams.blocks import TitleAndTextBlock


class DentistPage(Page):
    """This model creates the dentist page"""
    max_count = 1
    parent_page_types = ["home.HomePage"]
    template = "dentist/dentist_page.html"
    name = models.CharField(max_length=50, help_text="Enter name of the dentist")
    small_description = models.TextField(
        help_text="Enter a small description about the dentist"
    )
    about = StreamField([
       ("title_and_text", TitleAndTextBlock()),
    ])

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("name"),
            FieldPanel("small_description"),
        ], heading="Intro of About"),
        MultiFieldPanel([
            StreamFieldPanel("about"),
        ], heading="About of Dentist")
    ]
