from django.contrib import admin
from .models import Choice, Question

# Register your models here.
# choice တွေကို question ထဲမှာ ပေါ်အောင်ရေးတာ
class ChoiceInline(admin.TabularInline):  
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fieldsets => title တွေ သီးသန့် တပ်ပေးလိုက်တာ
    fieldsets = [
        ("Question Detial", {
            "fields": ['question_text']
        }),
        ("Date Information", {
            "fields": ["pub_date"],
            "classes": ["collapse"]  # date information ကို hide, show လုပ်လိုက်တာ
        })
    ]

    inlines = [ChoiceInline]   # choices တွေ question ထဲမှာ သုံးလို့ရအောင်။  

    list_display = ("question_text", "pub_date", "was_published_recently") # question အတွက် Column တွေ
    list_filter = ['pub_date'] # filter လုပ်လို့ရတဲ့ဟာ ပြပေးတယ် 

    search_fields = ["question_text"] # displaying search box to search question_text 
    
admin.site.register(Question, QuestionAdmin)

