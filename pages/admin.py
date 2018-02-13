from django.contrib import admin

from .models import Article, Version

class ArticleInline(admin.StackedInline):
    model = Version
    extra = 3

class AdminArticle(admin.ModelAdmin):
    inlines = [ArticleInline]


admin.site.register(Article, AdminArticle)
