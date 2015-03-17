from django.db import models
from django.contrib.auth.models import User

class Tahun_Akademik(models.Model):
	SEMESTER_CHOICES = (
		('1', 'Ganjil'),
		('0', 'Genap'),
	)
	STATUS_CHOICES = (
		('A', 'Aktif'),
		('N', 'Tidak Aktif'),
	)
	kode_tahun_akademik = models.AutoField(primary_key=True)
	nama_tahun_akademik = models.CharField(max_length=9)
	semester = models.CharField(max_length=1, choices=SEMESTER_CHOICES, default='1')
	status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='N')
	created_by = models.ForeignKey(User, null=True, blank=True)
	updated_by = models.IntegerField(null=True, blank=True)
	created_at = models.DateTimeField('Tgl Dibuat', auto_now_add=True)
	updated_at = models.DateTimeField('Tgl Diubah', auto_now=True)
	# Komentar Akhir