# -*- coding: utf-8 -*-
from django.contrib import admin
from yatranslate.models import Translate


class TranslateAdmin(admin.ModelAdmin):
    model = Translate


admin.site.register(Translate, TranslateAdmin)
