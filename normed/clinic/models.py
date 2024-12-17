from django.db import models

class Doctor(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    middle_name = models.CharField('Отчество', max_length=50, blank=True)
    specialty = models.CharField('Специальность', max_length=100)
    education = models.CharField('Образование', max_length=100)
    experience_years = models.IntegerField('Опыт работы', default=0)
    biography = models.TextField('О враче', blank=True)
    photo = models.ImageField('Фото', upload_to='doctors_images/', blank=True)

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
