import sys
def isValidChessBoard(boardname):
    if 'wking' and 'bking' not in boardname.values():
        print(False)
        return False
        sys.exit()
    else:
        bking=0
        wking=0
        bknight=0
        wknight=0
        bbishop=0
        wbishop=0
        brook=0
        wrook=0
        bqueen=0
        wqueen=0
        bpawn=0
        wpawn=0
        pass
    for i in boardname.keys():
        if i[0]=='b' or i[0]=='a' or i[0]=='c' or i[0]=='d' or i[0]=='e' or i[0]=='f' or i[0]=='h' or i[0]=='g':
            pass
        else:
            print(False)
            return False
            sys.exit()
        if i[1]=='1' or i[1]=='2' or i[1]=='3' or i[1]=='4' or i[1]=='5' or i[1]=='6' or i[1]=='7' or i[1]=='8':
            pass
        else:
            print(False)
            return False
            sys.exit()
        if len(i)>=3:
            print(False)
            return False
            sys.exit()
        if boardname[i]=='wking' or boardname[i]=='bking' or boardname[i]=='wqueen' or boardname[i]=='bqueen' or boardname[i]=='wknight' or boardname[i]=='bknight'or boardname[i]=='wbishop' or boardname[i]=='bbishop' or boardname[i]=='wrook' or boardname[i]=='brook' or boardname[i]=='wpawn' or boardname[i]=='bpawn':
            pass
        else:
            print(False)
            return False
            sys.exit()
        if boardname[i]=='wking':
            wking=wking+1
        if boardname[i]=='bking':
            bking=bking+1
        if boardname[i]=='wknight':
            wknight=wknight+1
        if boardname[i]=='bknight':
            bknight=bknight+1
        if boardname[i]=='wbishop':
            wbishop=wbishop+1
        if boardname[i]=='bbishop':
            bbishop=bbishop+1
        if boardname[i]=='wqueen':
            wqueen=wqueen+1
        if boardname[i]=='bqueen':
            bqueen=bqueen+1
        if boardname[i]=='wrook':
            wrook=wrook+1
        if boardname[i]=='brook':
            brook=brook+1
        if boardname[i]=='wpawn':
            wpawn=wpawn+1
        if boardname[i]=='bpawn':
            bpawn=bpawn+1
            
    if bking  >=2 or wking  >=2:
        print(False)
        return False
        sys.exit()
    else:
        pass
    if bqueen  >=2 or wqueen  >=2:
        print(False)
        return False
        sys.exit()
    else:
        pass
    if bknight  >=3 or wknight  >=3:
        print(False)
        return False
        sys.exit()
    else:
        pass
    if bbishop  >=3 or wbishop  >=3:
        print(False)
        return False
        sys.exit()
    else:
        pass
    if brook >=3 or wrook  >=3:
        print(False)
        return False
        sys.exit()
    else:
        pass
    if bpawn  >=9 or wpawn  >=9:
        print(False)
        return False
        sys.exit()
    else:
        pass
    
    print(True)    
    return True
##chessboard={'a1':'wrook','a2':'wpawn','a7':'bpawn','a8':'brook',
##            'b1':'wknight','b2':'wpawn','b7':'bpawn','b8':'bknight',
##            'c1':'wbishop','c2':'wpawn','c7':'bpawn','c8':'bbishop',
##            'd1':'wqueen','d2':'wpawn','d7':'bpawn','d8':'bqueen',
##            'e1':'wking','e2':'wpawn','e7':'bpawn','e8':'bking',
##            'f1':'wbishop','f2':'wpawn','f7':'bpawn','f8':'bbishop',
##            'g1':'wknight','g2':'wpawn','g7':'bpawn','g8':'bknight',
##            'h1':'wrook','h2':'wpawn','h7':'bpawn','h8':'brook'}

        
        
        
    

