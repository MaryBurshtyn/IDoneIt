from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, UnicodeUsernameValidator, UserManager
)


class AbstractUser(AbstractBaseUser, PermissionsMixin):
    """
    Абстрактный класс пользователя.
    """
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_('email address'), blank=True)
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    is_staff = models.BooleanField(_('is_staff'), default=True)
    is_superuser = models.BooleanField(_('is_superuser'), default=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        abstract = True
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)


class User(AbstractUser):
    """
    Класс Пользователь, который используется для аунтификации пользователей в системе.

    В отличие от базового класса поле email является обязательным.
    """
    email = models.EmailField(
        _('email address'),
        max_length=150,
        blank=False,
        help_text=_("Required.")
    )
    created_by_id = models.IntegerField(_('created_by_id'), default=0, blank=True, null=True)

    # При удалении пользователя, удаление зарегистрированных им пользователей.
    def delete(self, *args, **kwargs):
        User.objects.filter(created_by_id=self.id).delete()
        super(User, self).delete(*args, **kwargs)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
