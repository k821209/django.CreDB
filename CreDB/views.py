from django.shortcuts import render,get_object_or_404
from django import forms
from .models import DBmodel, final_comp,annotation

class NameForm(forms.ModelForm):
    class Meta:
        model = DBmodel
        fields = ('genename',)
class NameForm_plain(forms.Form):
    transcript_name = forms.CharField(label='transcript name', max_length=50)
class NameForm_gene(forms.Form):
    gene_name = forms.CharField(label='gene name', max_length=50)

def index(request):
    ex_genename   = final_comp.objects.order_by('?')[0].genename 
    final_comp_ex = final_comp.objects.filter(genename=ex_genename)
    annot         = annotation.objects.get(genename=ex_genename)
    if request.method=='POST':
        form = NameForm_gene(request.POST)
        if form.is_valid():
            query         = form.cleaned_data['gene_name']
            final_comp_ex = final_comp.objects.filter(genename=query)
            annot         = annotation.objects.get(genename=query)
            form          = NameForm_gene()
            return render(request, 'CreDB/index.html', {'final':final_comp_ex, 'form': form,'annotation':annot})
    else:
        form = NameForm_gene()
        return render(request, 'CreDB/index.html', {'final':final_comp_ex, 'form': form, 'annotation':annot})


def detail(request,transcript_name):
        DBex          = DBmodel.objects.get(genename=transcript_name)
        final_comp_ex = final_comp.objects.get(transcriptname=transcript_name)
        return render(request, 'CreDB/detail.html', {'DBex' : DBex,'final':final_comp_ex})

# Create your views here.
