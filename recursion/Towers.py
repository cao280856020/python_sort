def doTowers(topN,fromX,inter,to):
    if topN==1:
        print("Disk 1 from "+fromX+" to "+to)
    else:
        doTowers(topN-1,fromX,to,inter)
        print("Disk "+str(topN)+" from "+fromX+" to "+to)
        doTowers(topN-1,inter,fromX,to)


doTowers(3,'A','B','C')