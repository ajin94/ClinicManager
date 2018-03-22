from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_sales_quantity(quantity):
    if quantity > 10:
        raise ValidationError(_("Quantity exceeds stock"))
    else:
        pass
