from wagtail.core import blocks


class TitleAndTextBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=50, help_text="Enter title")
    text = blocks.RichTextBlock()

    class Meta:
        template = "streams/title_and_text_block.html"