from django.urls import path

from .views import kontest, musobaqalar, masalalar, kontest_detail, kontest_urinishlar, kontest_masalalar, kontest_qatnashuvchilar, masala_detail, turnir_jadvali,reyting, masalalar_ballari


urlpatterns = [
    path('', kontest, name='kontest'),
    path('musobaqalar/', musobaqalar, name='musobaqalar'),
    path('masalalar/', masalalar, name='masalalar'),
    path('<int:kontest_id>/', kontest_detail, name='kontest-detail'),
    path('kontest-try/<int:kontest_id>/', kontest_urinishlar, name='kontest-urinishlar'),
    path('kontest-masalalar/<int:kontest_id>/', kontest_masalalar, name='kontest-masalalar'),
    path('kontest-qatnashuvchilar/<int:kontest_id>/', kontest_qatnashuvchilar, name='kontest-qatnashuvchilar'),
    path('masala/<int:masala_id>/', masala_detail, name='masala-detail'),
    path('turnir-jadvali/<int:kontest_id>/', turnir_jadvali, name='turnir_jadvali'),
    path('reyting/', reyting, name='reyting'),
    path("masalalar_ballari/<int:k_id>/", masalalar_ballari, name="masalalar_ballari"),
]
