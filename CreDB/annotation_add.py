from CreDB.models import annotation
file_in  = 'Creinhardtii_281_v5.5.description.txt'
file_in1 = 'Creinhardtii_281_v5.5.annotation_info.txt' 
dicG2D = {}
done   = []
for line in open(file_in):
    cell       = line.strip().split('\t')
    e_genename = '.'.join(cell[0].split('.')[0:2]) 
    e_annot    = cell[1]
    if e_genename in set(done):
        continue
    else: done.append(e_genename)
    dicG2D[e_genename] = e_annot

done = []
for line in open(file_in1):
    cell       = line.strip().split('\t')
    e_genename = cell[1] 
    if e_genename in set(done):
        continue
    else: done.append(e_genename)

    try:
        e_annotation = dicG2D[e_genename]
    except KeyError:
        try:
            e_annotation = cell[12]
        except IndexError:
            e_annotation = 'None'

    post = annotation.objects.create(genename=e_genename,  annotation=e_annotation)
    post.publish()

