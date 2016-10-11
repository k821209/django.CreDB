from CreDB.models import DBmodel


file_in = 'all.merged.bam.transcripts.all.txt'
for line in open(file_in):
    cell = line.strip().split('\t')
    DBmodel.objects.create(genename=cell[0], cov_1x=cell[1], cov_10x=cell[2], cov_30x=cell[3],depth_ratio=cell[4],depth=cell[5],match=cell[6],match_ratio=cell[7])

posts = DBmodel.objects.all()
for post in posts:
    post.publish()

