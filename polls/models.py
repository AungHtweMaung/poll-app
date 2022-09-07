import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    # admin ထဲမှာ question change page အတွက် pub_date ကို True, False ပြမယ့်အစား sign နဲ့ဖော်ပြပေးတာ။ 
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )

    def was_published_recently(self):
        # self.pub_date က current time 
        # timezone.now() ထဲက တစ်ရက်စာ အချိန်ကို နုတ်လိုက်တာ ၊ လွန်ခဲ့တဲ့ 1 ရက်က published လုပ်ခဲ့တာဆို True ဖြစ်မယ် 
        # 1 ရက်ကျော်သွားရင် False ပြမယ် 
        now = timezone.now()
        # question သည် လွန်ခဲ့တဲ့ တစ်ရက်အတွင်းက ဖြစ်ရမယ်။ ပြီးခဲ့တဲ့ တစ်ရက်ထက်ကျော်လို့လည်း မရ၊ လက်ရှိအချိန်ထက်လည်း ကျော်လို့မရ။ 
        # သတ်မှတ်ချက်နဲ့ မကိုက်ရင် False ပြမယ် 
        return now - datetime.timedelta(days=1) <= self.pub_date <= now 
        
        # return self.pub_date >= timezone.now() - \
        #     datetime.timedelta(days=1)
    
    def __str__(self):
        return self.question_text
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    