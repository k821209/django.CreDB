from CreDB.models import final_comp 


for line in open('final.comp.txt'):
    cell = line.strip().split('\t')
    if cell[0] == 'genename':
        continue
    post = final_comp.objects.filter(genename=cell[0])
    post.update( RNAseqcov=cell[1], stringtie_complete=cell[2], stringtie_partial=cell[3], stringtie_isoform=cell[4], ORFannot_complete=cell[5], ORFannot_partial=cell[6], ORFannot_isoform=cell[7], transcriptname=cell[8], score=cell[9], length=cell[10])
   

    
