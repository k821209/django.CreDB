from CreDB.models import DBmodel

def Fasta2dic(file_fasta):
    dic       = {}
    bulk      = open(file_fasta).read()
    bulk_list = bulk.split('>')
    for each in bulk_list:
        if each == '':
            continue
        strHD  = each.split('\n')[0].split()[0]
        strSeq = ''.join(each.split('\n')[1:])
        dic[strHD] = strSeq
    return dic


dicfa = Fasta2dic('/ref/analysis/References/Creinhardtii/annotation/Creinhardtii_281_v5.5.cds.fa')
i = 0 
for transcript in dicfa:
    if i == 0 :
        print transcript
        i += 1
    DBmodel.objects.filter(genename=transcript+'.v5.5').update(CDS=dicfa[transcript])
    
