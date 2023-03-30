import os.path
from datetime import datetime

from django.db.models import Model, QuerySet, Q
from django.db.models import CharField, URLField, ForeignKey, DateTimeField, BooleanField, DO_NOTHING, IntegerField, \
    TextField, ManyToManyField
from django.contrib.auth.models import User
from django.utils import timezone
from wagtail.snippets.models import register_snippet
from wagtail.models import TranslatableMixin

CATEGORIES = [
    'Python',
    'Django',
    'DRF',
    'MySQL',
    'PostgresSQL',
    'PyQt',
    'Algorithms',
    'Software architecture',
    'Another tech',
    'Python libraries',
]


class Category(Model):
    name = CharField(max_length=100, blank=False, null=False)
    url = URLField(max_length=100),

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class PostsQuerySet(QuerySet):

    def published_posts(self):
        now = timezone.now()
        return self.filter(
            Q(publish_after__lt=now)
        )


def get_files_upload_path(app_name, prop_name, instance, current_filename, suffix=''):
    timestamp = int((datetime.now(tz=timezone.utc) - datetime(1970, 1, 1, tzinfo=timezone.utc)).total_seconds())

    filename = "{name}{suffix}_{timestamp}{ext}".format(
        name='blog',
        suffix=suffix,
        timestamp=str(timestamp),
        ext=os.path.splitext(current_filename)[1],
    )
    return f"images/{app_name}/{filename}"


@register_snippet
class Post(TranslatableMixin, Model):
    header = CharField(
        max_length=250,
        blank=False,
        help_text='This is header of your article or post',
    )
    date = DateTimeField(
        auto_now=True,
    )
    is_changed = BooleanField(
        default=False,
    )
    date_changed = DateTimeField(
        auto_now_add=True,
    )
    author = ForeignKey(
        User,
        on_delete=DO_NOTHING,
    )
    link = URLField(
        max_length=200,
        help_text='This is link to your post',
    )
    length = IntegerField()
    categories = ManyToManyField(
        Category,
        DO_NOTHING,
        choices=CATEGORIES,
    )
    body = TextField(
        max_length=1500,
        null=False,
        blank=False,
    )
    publish_after = DateTimeField(
        null=True,
        help_text='Post will be visible after this datetime'
    )
    contains_images_or_videos = BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    objects = PostsQuerySet.as_manager()

    class Meta(TranslatableMixin.Meta):
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ('-date',)

    def __str__(self):
        return self.header
