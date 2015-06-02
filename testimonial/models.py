from django.db import models

# Create your models here.
class Testimonial(models.Model):
    customer_name = models.CharField('Customer', max_length=50)
    company_name  = models.CharField('Company', max_length=50)
    text_snippet  = models.CharField('Summary', max_length=200)
    text_body     = models.TextField('Body')
    image_logo    = models.ImageField('Logo', upload_to='media/logos/', blank=True, null=True)
    image_person  = models.ImageField('Photo', upload_to='media/photos', blank=True, null=True)
    designation   = models.CharField('Designation', max_length=50)
    published     = models.BooleanField('published', default=False)
    category      = models.CharField('Category', max_length=20)
    pub_date      = models.DateTimeField('Published date')

    def __unicode__(self):
        return self.customer_name
