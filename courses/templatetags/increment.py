from django import template
from users.models import User
from kontest.models import Masala
from articles.models import Article
from django.utils.safestring import mark_safe

from ..models import CoursePart

from django.db.models import Avg, Q, Sum, Count


register = template.Library()

@register.filter
def next(obj):
    return f'/courses/detail/{obj+1}' if CoursePart.objects.filter(id=obj+1).exists() else '#'

@register.filter
def mmk(obj):
    return mark_safe(str(obj).replace('\n', '\n<br>\n'))

@register.filter
def get_mean_rate(obj):
    return Article.objects.get(id=obj).rates.aggregate(Avg('rate'))['rate__avg']

@register.filter
def get_user_kontest_ball(user_id, kontest_id):
    res = User.objects.get(id=user_id).ishlangan_masalalar.filter(state='🟢 Passed', masala__kontest_id=kontest_id).annotate(sum_ball=Sum('masala__ball', distinct=True)).first()
    if res:
        return res.sum_ball
    else:
        return 0

@register.filter
def get_user_masalalar_ball(user_id):
    res = User.objects.filter(
        ishlangan_masalalar__state='🟢 Passed',
        id=user_id
    ).annotate(
        num_passed=Count('ishlangan_masalalar', filter=Q(ishlangan_masalalar__state='🟢 Passed'), distinct=True),  # Count passed masalalar for each user
        total_ball=Sum('ishlangan_masalalar__masala__ball', filter=Q(ishlangan_masalalar__state='🟢 Passed'), distinct=True)  # Sum of balls for passed masalalar
    ).order_by(
        '-total_ball'  # Order by total_ball descending
    ).first()
    if res:
        return res.total_ball
    else:
        return 0

@register.filter
def user_has_related(user_id, kontest_id):
    try:
        return User.objects.get(id=user_id).kontests.filter(kontest__id=kontest_id).exists()
    except:
        return False
@register.filter
def togri_yechimlar_soni(user_id):
    return User.objects.get(id=user_id).ishlangan_masalalar.filter(state='🟢 Passed').count()

@register.filter
def notogri_yechimlar_soni(user_id):
    return User.objects.get(id=user_id).ishlangan_masalalar.filter(state='🔴 Failed').count()

@register.filter
def umumiy_yechimlar(user_id):
    user = User.objects.get(id=user_id)
    Masala.user = user
    # return Masala.objects.filter(umumiy_javoblar=True)
    filtered_objects = Masala.objects.annotate(
        passed_count=Count('ishlaganlar', filter=Q(ishlaganlar__state='🟢 Passed'))
    ).filter(passed_count__gte=4)

    return filtered_objects.count()
