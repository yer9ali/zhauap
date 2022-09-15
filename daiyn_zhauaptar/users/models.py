from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.templatetags.i18n import language
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Default custom user model for Daiyn Zhauaptar.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = CharField(_('username'), unique=True, max_length=100, null=False)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    language = CharField(_('язык'), max_length=2)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
