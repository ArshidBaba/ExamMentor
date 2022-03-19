from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ['id']

    # question = models.ForeignKey(Questions, related_name='category', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Questions(models.Model):

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['id']
         
    TYPE = (
        (0, _("Multiple Choice")),
    )
    title = models.CharField(max_length=255, verbose_name=_("Title"), default="Question")
    question = models.CharField(max_length=255, verbose_name="Question")
    exam_year = models.IntegerField(verbose_name="Year")
    exam_name = models.CharField(max_length=255, verbose_name="Exam")
    category = models.ForeignKey(Category, related_name='Subject', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.question  

class Answers(models.Model):
    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ['id']
    # category = models.ForeignKey(Category, related_name='Category', on_delete=models.DO_NOTHING)
    question = models.ForeignKey(Questions, related_name='answer', on_delete=models.DO_NOTHING)
    answer_text = models.CharField(max_length=255, verbose_name="Answer")
    is_right = models.BooleanField(default=False) 

    def __str__(self):
        return self.answer_text
