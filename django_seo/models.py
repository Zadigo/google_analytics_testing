from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch.dispatcher import receiver
from django.utils.functional import cached_property
from django.utils.translation import gettext_lazy as _
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from django_seo.managers import GlobalManager


class BaseAbstract(models.Model):
    version = models.PositiveIntegerField(default=0)
    modified_on = models.DateField(auto_now_add=True)
    created_on = models.DateField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['version']

    def full_name(self):
        return f'Version {self.version}'


class SEOVersion(BaseAbstract):
    """Stores all the SEO versions for a website"""
    author = models.CharField(
        max_length=100,
        help_text='Author or founder of the company',
        blank=True,
        null=True
    )
    company_name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    keywords = models.CharField(
        max_length=100,
        help_text='Meta keywords',
        blank=True,
        null=True
    )
    description = models.TextField(
        max_length=155,
        help_text=_("Description of the company which should "
                    "ideally be between a 100 and 155 characters"),
        blank=True,
        null=True
    )
    theme_color = models.CharField(
        max_length=20,
        default='2d2d2d',
        blank=True,
        null=True
    )

    objects = GlobalManager.as_manager()

    def __str__(self):
        return f'SEO Version: {self.version}'


class LegalBusiness(BaseAbstract):
    legal_name = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    # knows_about = models.CharField(max_length=100, blank=True, null=True)
    # founding_date = models.DateField(blank=True, null=True)
    general_email = models.EmailField(
        validators=[],
        blank=True,
        null=True
    )
    customer_service_email = models.EmailField(
        validators=[],
        blank=True,
        null=True
    )
    telephone = models.CharField(
        max_length=100,
        validators=[],
        blank=True,
        null=True
    )
    address_line = models.CharField(
        max_length=300,
        blank=True,
        null=True
    )
    locality = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    region = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    postal_code = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    country = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    logo = models.ImageField(
        blank=True,
        null=True
    )
    square_image = ImageSpecField(
        source='logo',
        processors=[ResizeToFill(100, 100)],
        options={'quality': 100},
        format='PNG'
    )
    linkedin = models.URLField(
        help_text=_('LinkedIn business page'),
        blank=True,
        null=True
    )
    facebook = models.URLField(
        help_text=_('Facebook business page'),
        blank=True,
        null=True
    )
    instagram = models.URLField(
        help_text=_('Instagram profile page'),
        blank=True,
        null=True
    )
    twitter = models.URLField(
        help_text=_('Twitter business page'),
        blank=True,
        null=True
    )
    youtube = models.URLField(
        help_text=_('YouTube channel'),
        blank=True,
        null=True
    )
    tiktok = models.URLField(
        help_text=_('Tiktok page'),
        blank=True,
        null=True
    )

    objects = GlobalManager.as_manager()

    class Meta:
        verbose_name_plural = _('legal businesses')
        ordering = ['version']

    def __str__(self):
        return f'Business Version: {self.version}'

    @cached_property
    def get_socials(self):
        return {
            'facebook': self.facebook,
            'twitter': self.twitter,
            'instagram': self.instagram,
            'linkedin': self.linkedin,
            'youtube': self.youtube,
            'tiktok': self.tiktok
        }


@receiver(post_save, sender=SEOVersion)
def update_version(instance, created, **kwargs):
    if created:
        result = SEOVersion.objects.latest('created_on')
        instance.version = result.version + 1
        instance.save()


# @receiver(pre_save, sender=LegalBusiness)
def validate_address(instance, **kwargs):
    pass
