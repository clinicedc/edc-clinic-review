from django.db import models
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from edc_constants.choices import YES_NO_NA
from edc_constants.constants import NOT_APPLICABLE
from edc_model import models as edc_models

from ...utils import get_list_model_app


class ClinicalReviewHivModelMixin(models.Model):
    hiv_test = models.CharField(
        verbose_name="Since last seen, was the patient tested for HIV infection?",
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
        help_text=format_html(
            "{html}",
            html=mark_safe(
                "Note: Select `not applicable` if diagnosis previously reported. <BR>"
                "`Since last seen` includes today.<BR>"
                "If `yes', complete the initial review CRF<BR>"
                "If `not applicable`, complete the review CRF."
            ),  # nosec B308, B703
        ),
    )

    hiv_test_date = models.DateField(
        verbose_name="Date test requested",
        null=True,
        blank=True,
    )

    hiv_reason = models.ManyToManyField(
        f"{get_list_model_app()}.reasonsfortesting",
        related_name="hiv_test_reason",
        verbose_name="Why was the patient tested for HIV infection?",
        blank=True,
    )

    hiv_reason_other = edc_models.OtherCharField()

    hiv_dx = models.CharField(
        verbose_name=format_html(
            "As of today, was the patient <u>{text}</u> diagnosed with HIV infection?",
            text="newly",
        ),
        max_length=15,
        choices=YES_NO_NA,
        default=NOT_APPLICABLE,
    )

    class Meta:
        abstract = True
