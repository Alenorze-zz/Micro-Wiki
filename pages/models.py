from django.db import models
from django.utils.translation import ugettext as _



class Article(models.Model):
    active     = models.BooleanField(default=False)
    created    = models.DateTimeField(auto_now_add=True)
    updated    = models.DateTimeField(auto_now=True)


class VersionManager(models.Manager):
    def get_active_object(self):
        try:
            return self.get(current=True)
        except models.ObjectDoesNotExist:
            return None


class Version(models.Model):
    article   = models.OneToOneField(Article, on_delete=models.CASCADE, default=None)
    release   = models.CharField(max_length=5)
    title     = models.CharField(max_length=128)
    text      = models.TextField(max_length=2048)
    created   = models.DateTimeField(auto_now_add=True)
    updated   = models.DateTimeField(auto_now=True)
    current   = models.BooleanField(_("Current"), default=False)

    objects = VersionManager()

    class Meta:
        ordering = ['-current']

    def save(self, *args, **kwargs):
        if self.current:
            try:
                currently_active = self.__class__.objects.get(current=True)
            except self.__class__.DoesNotExist:
                pass
            else:
                currently_active.current = False
                currently_active.save()
        return super(Version, self).save(*args, **kwargs)

    def get_state_string(self):
        if self.current:
            state = _("current")
        else:
            state = _("not current")
        return state
    
    def __str__(self):
        return self.release



