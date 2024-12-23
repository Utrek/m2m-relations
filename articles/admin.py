from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from.models import Article, Scope, Tag



class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        count = 0
        name_list =[]
        for form in self.forms:
            tag = form.cleaned_data.get('tag')
            print(tag)
            if form.cleaned_data.get('is_main') == True:
                count += 1
            if tag not in name_list:
                name_list.append(tag)
                print (name_list)
            else:
                name_list =[]
                raise ValidationError("Теги не должны повторяться") 
                   
        if count > 1:
            raise ValidationError("Вы можете выбрать только один основной тег")
        elif count == 0:
            raise ValidationError("Выберите основной тег")
         
        return super().clean() 


class RelationshipInline(admin.TabularInline):
    model = Scope
    extra = 0
    formset = RelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]
    

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

