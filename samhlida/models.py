from django.db import models


class Corpus(models.Model):
    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name


class Entry(models.Model):
    corpus = models.ForeignKey(Corpus, on_delete=models.CASCADE, related_name="entries")
    number = models.IntegerField()
    isl_text = models.TextField()
    other_text = models.TextField()

    def __str__(self):
        return f'{self.corpus}-{self.number}'


