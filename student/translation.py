"""This is the prototype implementation of model translations
"""
from modeltranslation.translator import register, TranslationOptions
from ose.models import (
    AdmissionInstance, AdmissionMethod, AdmissionProcess, OpenHouse, OptOutChoice
)


@register(AdmissionProcess)
class AdmissionProcessTranslationOptions(TranslationOptions):
    """Defines the fields in AdmissionProcess that need translating.
    """
    fields = ('name', 'onboarding_copy', 'onboarding_start_search_copy',)
