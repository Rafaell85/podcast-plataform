from django.db import models

class Podcast(models.Model):
    title = models.CharField(max_length=200)  # Título do podcast
    description = models.TextField()  # Descrição
    file = models.FileField(upload_to='podcasts/')  # Arquivo de áudio ou vídeo
    category = models.CharField(
        max_length=50,
        choices=[('Audio', 'Áudio'), ('Video', 'Vídeo')]
    )  # Tipo do podcast
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Data de upload

    def __str__(self):
        return self.title
