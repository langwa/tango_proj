from django.contrib import admin
from rango.models import Category, Page
from polls.models import Poll, Choice


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['question']}),
        ('Date Information',    {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['category']}),
        ('Title',               {'fields': ['title']}),
        ('URL',                 {'fields': ['url']}),
        ('Views',               {'fields': ['views']}),
    ]
    list_display = ('title', 'category', 'url', 'views')

admin.site.register(Poll, PollAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
