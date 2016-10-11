from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

class annotation(models.Model):
    genename   = models.CharField(max_length=50)
    annotation = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __unicode__(self):
        return self.genename

class DBmodel(models.Model):
    genename = models.CharField(max_length=50)
    cov_1x   = models.DecimalField(max_digits=4, decimal_places=3)
    cov_10x  = models.DecimalField(max_digits=4, decimal_places=3)
    cov_30x  = models.DecimalField(max_digits=4, decimal_places=3)     
    depth_ratio = models.DecimalField(max_digits=12, decimal_places=3)
    depth       =  models.DecimalField(max_digits=12, decimal_places=0)
    match       =  models.DecimalField(max_digits=12, decimal_places=0)
    match_ratio    =  models.DecimalField(max_digits=12, decimal_places=3)
    CDS            = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __unicode__(self): 
        return self.genename

class final_comp(models.Model):
    # genename        cov     st.=    st.c    st.j    td.=    td.c    td.j    transcriptname  score   length
    genename  = models.CharField(max_length=50)
    RNAseqcov = models.BinaryField()
    stringtie_complete = models.BinaryField()
    stringtie_partial  = models.BinaryField()
    stringtie_isoform  = models.BinaryField()
    ORFannot_complete  = models.BinaryField()
    ORFannot_partial   = models.BinaryField()
    ORFannot_isoform   = models.BinaryField()
    transcriptname     = models.CharField(max_length=50)
    score              = models.DecimalField(max_digits=4, decimal_places=0)
    length             = models.DecimalField(max_digits=10, decimal_places=0)
    published_date = models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __unicode__(self):
        return self.genename
     

# Create your models here.
