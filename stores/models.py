from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("stores:detail", kwargs={"slug":self.slug})

def create_slug(instance,new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Store.objects.filter(slug=slug)
    if qs.exists():
        try:
            int(slug[-1])
            if "-" in slug:
                slug_list = slug.split("-")
                new_slug = "%s%s" % (slug[:-len(slug_list[-1])], int(slug_list[-1])+1)
            else:
                new_slug = "%s-1" % (slug)
        except:
            new_slug = "%s-1" % (slug)
        return create_slug(instance, new_slug=new_slug)
    return slug

def generate_slug(instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(generate_slug, sender=Store)
