from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        error_messages={
            'unique': 'Bu foydalanuvchi nomi band. Iltimos, boshqa nom kiriting.',
        }
    )
    profile_image = models.ImageField(upload_to="pfiles/", null=True, blank=True)
    telefon = models.CharField(max_length=20, default="Kiritilmagan")
    telegram = models.CharField(max_length=150, default="Kiritilmagan")
    viloyat = models.CharField(max_length=100, default="Kiritilmagan")
    tuman = models.CharField(max_length=100, default="Kiritilmagan")
    maktab = models.CharField(max_length=300, default="Kiritilmagan")
    def __str__(self):
        return self.first_name
    
    def get_all_balls(self):
        res = self.ishlangan_masalalar.filter(state='🟢 Passed').aggregate(models.Sum('masala__ball', distinct=True))['masala__ball__sum']
        # self.ishlangan_masalalar.filter(state='🟢 Passed').annotate(sum_ball=Sum('masala__ball')).first()
        res = self.ishlangan_masalalar.filter(state__contains="Passed").values("masala").distinct().aggregate(models.Sum("masala__ball"))["masala__ball__sum"]
        return res if res else 0
    
    def get_kontest_masala_status(self, k_id=None):
        result = []
        kontests = self.kontests.all()
        for k in kontests:
            if k_id:
                if k_id != k.kontest.id:
                    continue
            k_masalalar_ball = []
            k_masalalar = k.kontest.masalalar.all()
            for m in k_masalalar:
                ball = 0
                try:
                    ball = m.ishlaganlar.filter(user=self,state="🟢 Passed").first().masala.ball
                except:
                    pass
                k_masalalar_ball.append(ball)
        result.append((k.kontest.id,k_masalalar_ball, len(k_masalalar_ball)-k_masalalar_ball.count(0)))
        return result
