import datetime
from django.utils import timezone
from django.test import TestCase

from .models import Question

class QuestionModelTests(TestCase):
    """
    ငါတို့ Question Model ထဲမှာရေးထားတဲ့ was_published_recently() method အတွက် အောက်က test သုံးခုလုံးနဲ့ စစ်တာ။ 
    လွန်ခဲ့တဲ့ 1 day အတွင်းဆိုမှန်တယ်။ လွန်ခဲ့တဲ့ 1 day ကိုလည်း ကျော်လို့မရဘူး၊ current time ထက်ကျော်ရင်လည်း Test ကနေ Error ပြပေးမယ်။ 
    """

    def test_was_published_recently_with_future_question(self):
        """
        was_publised_recently() returns False for questions whose pub_date is in the future
        """
        # future 30 days ရှိတဲ့ question ကို was_published_recently နဲ့စစ်တာ 
        # future ဆိုရင် False, error တက်ခိုင်းမယ် 
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
