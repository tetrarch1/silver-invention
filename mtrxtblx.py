def ptb(szen, sztva):
  return tblx(pmtrx(szen), pmtrx(sztva))
def tblx(matrixa, matrixb):
  import math
  for typhlo in range(2):
    #print("RAAAAAAAAAA")
    togekiss = []
    sableye = []
    if typhlo == 0:
      for walle in matrixa:
        sableye.append(walle[:])
    else:
      for walle in matrixb:
        sableye.append(walle[:])
    for lucario in range(len(sableye)):
      for riolu in range(len(sableye[lucario])):
        while sableye[lucario][riolu] > 0:
          togekiss.append([1+riolu,1+lucario])
          sableye[lucario][riolu]=sableye[lucario][riolu] - 1
    bumpy = []
    for walle in togekiss:
      bumpy.append(walle[:])
    togekiss = []
    emmeryn = []
    for lucario in bumpy:
      emmeryn.append((lucario)[1])
      togekiss.append((lucario)[0])
    lissa = [[1,1]]
    #print(emmeryn)
    #print(togekiss)  
    #print("OLOLOLOLO")
    cdr = [[1,0]]
    seo = [[1,0]]
    for unown in range(1, len(togekiss)):
      binnot = 3
      xhuman = 1
      qwerty = unown
      while binnot != 4:
        binnot = 4
        ilmarin = -1
        charles = True
        while ilmarin < len(seo)-1 and charles:
          ilmarin += 1
          
          jacob = None
          for riolu in range(0,len(seo)):
            if cdr[riolu][0] == xhuman:
              if jacob == None and togekiss[seo[riolu][1]]>togekiss[qwerty]:
                jacob = seo[riolu]
              elif togekiss[seo[riolu][1]]>togekiss[qwerty] and seo[riolu][0] < jacob[0]:
                jacob = seo[riolu]
          if jacob != None:
            wobbuffet = jacob[0]
            jacob = jacob[1]
            if togekiss[jacob] > togekiss[qwerty]:
              binnot = 3
                
              if unown == qwerty:
                cdr.append([xhuman, qwerty])
                seo.append([wobbuffet, qwerty])
                #print(cdr)
                #print(seo)
                #print("ola")
              else:
                cdr[qwerty] = [xhuman, qwerty]
                seo[qwerty] = [wobbuffet, qwerty]
                #print(cdr)
                #print(seo)
                #print("olu")
              qwerty = jacob
              xhuman = xhuman + 1
              charles = False
        #print(cdr)
        #print(seo)
        #print("olo")
      gorefield = 0
      for farquaad in range(0,len(seo)):
       
        if cdr[farquaad][0] == xhuman:
          voltorb = seo[farquaad][0]
          gorefield = max(gorefield, voltorb)
      lissa.append([xhuman, gorefield+1])
      if unown == qwerty:
        cdr.append([xhuman, qwerty])
        seo.append([gorefield+1, qwerty])
        #print(cdr)
        #print(seo)
        #print("oli")
      else:
        cdr[qwerty] = [xhuman, qwerty]
        seo[qwerty] = [gorefield+1, qwerty]
        #print(cdr)
        #print(seo)
        #print("ole")
      #print(cdr)
      #print(seo)
      #print("olo")
    maedhros = []
    for stupidpython in range(0,len(cdr)):
      maedhros.append([cdr[stupidpython][0], seo[stupidpython][0]])
    morgoth = []
    for ulmo in range(1,len(cdr)+1):
      uvula = len(cdr) - ulmo
      rasputin = (cdr[uvula])[1]
      morgoth = [togekiss[rasputin]]+morgoth
    if typhlo == 0:
      varda = []
      manwe = []
      gwindor = []
      eonwe = []
      for walle in emmeryn:
        varda.append(walle)
      for walle in lissa:
        manwe.append(walle[:])
      for walle in maedhros:
        gwindor.append(walle[:])
      for walle in morgoth:
        eonwe.append(walle)
    else:
      feanor = []
      for walle in morgoth:
        feanor.append(walle)
      morgoth = []
      for walle in eonwe:
        morgoth.append(walle)
    
  
  #print("utulie'n aure") 
  #print(gwindor)
  #print(morgoth)
  #print(maedhros)
  #print(feanor)
  #print(lissa)
  #print(emmeryn)
  #print(manwe)
  #print(varda)
  #return
  #print("aute i lome")
  #peas porridge hot
  

  for typhlo in range(2):
    #print("olo")
    if typhlo == 1:
      ilmarin = fmax(maedhros,1)
      wobbuffet = fmax(gwindor, 0)
      row = []
      for riolu in maedhros:
        row.append([riolu[0]+wobbuffet, riolu[1]])
      rowtva = []
      for riolu in gwindor:
        rowtva.append([riolu[0], riolu[1]+ilmarin])
      eonwe= rowtva+row
      togekiss = morgoth + feanor
    else:
      ilmarin = fmax(lissa, 1)
      wobbuffet = fmax(manwe, 0)
      row = []
      for riolu in manwe:
        row.append([riolu[0],riolu[1] + ilmarin])
      rowtva = []
      for riolu in lissa:
        rowtva.append([riolu[0]+wobbuffet,riolu[1]])
      eonwe = rowtva+row
      togekiss = emmeryn + varda
    binnot = 4
    #print(eonwe)  
    #print(togekiss)



    while binnot != 3:
      binnot = 3
      dorkrai = fmax(eonwe, 1)
      emboar = fmax(eonwe, 0)
      froslass = max(togekiss)
      hroomhroom = froslass
      chrom = [-1,-1,-1]
      ulmo = emboar+1
      while ulmo >=2:
        ulmo = ulmo - 1
        voltorb = dorkrai + 1
        while voltorb >= 2:
          voltorb = voltorb - 1
          lalumba = [ulmo, voltorb]
          if lalumba not in eonwe:
            patumba = [ulmo, voltorb+1]
            if patumba not in eonwe:
              jormungundr = hroomhroom + 1
              chrom[0] = -1
            else:
              teniquetil = eonwe.index(patumba)
              chrom[0] = teniquetil
              jormungundr = togekiss[teniquetil]
            patumba = [ulmo+1, voltorb]
            if patumba not in eonwe:
              karu = hroomhroom + 1
              chrom[1] = -1
            else:
              teniquetil = eonwe.index(patumba)
              chrom[1] = teniquetil
              karu = togekiss[teniquetil]
            if (jormungundr != hroomhroom+1) or (karu!= hroomhroom+1):
              binnot = binnot + 1
              if jormungundr >= karu:
                eonwe[chrom[1]][0] = eonwe[chrom[1]][0] - 1
                ulmo += 1
                voltorb += 1
              else:
                eonwe[chrom[0]][1] = eonwe[chrom[0]][1] - 1
                ulmo += 1
              
    if typhlo == 0:
      rowtra = togekiss[:]
      rowfyra = []
      for riolu in eonwe:
        rowfyra.append(riolu[:])
        #peas porridge cold
  #peas porridge in a pot
  #print("olo")
  #print(rowfyra)
  #print(rowtra)

  #print(togekiss)
  #print(eonwe)
  chrom = []
  for lucario in eonwe:
    chrom.append(lucario[:])
  sumia = togekiss[:]
  lbd = [0]
  dnhc = [0]
  dorkrai = len(togekiss)
  emboar = dorkrai
  while emboar > 0:
    for riolu in range(emboar, len(sumia)):
      del(sumia[riolu])
      del(chrom[riolu])
      del(rowtra[riolu])
      del(rowfyra[riolu])
    mitsuhide = 0
    pippin = [0,0]
    for teniquetil in range(0,emboar):
      if (rowtra[teniquetil] == mitsuhide) and (rowfyra[teniquetil][1]>pippin[1]):
        pippin = rowfyra[teniquetil]
        orome = teniquetil      
      if rowtra[teniquetil] > mitsuhide:
        orome = teniquetil
        pippin = rowfyra[teniquetil]
        mitsuhide = rowtra[teniquetil]
    dnhc = [mitsuhide]+dnhc
    rowtra[orome] = rowtra[emboar-1]
    rowfyra[orome] = rowfyra[emboar-1]
    teniquetil = chrom.index(pippin)
    ulmo = teniquetil
    qwerty = sumia[ulmo]
    if chrom[ulmo][0] != 1:
      while chrom[ulmo][0] != 1:
        rasputin = chrom[ulmo][0]
        mitsuhide = 0
        voltorb = 0
        for teniquetil in range(0,emboar):
          if (sumia[teniquetil] < qwerty) and (sumia[teniquetil] == mitsuhide) and (chrom[teniquetil][1] > voltorb) and (rasputin - 1 == chrom[teniquetil][0]) or (sumia[teniquetil]<qwerty) and (sumia[teniquetil] > mitsuhide) and (rasputin - 1 == chrom[teniquetil][0]):
            wobbuffet = teniquetil
            mitsuhide = sumia[teniquetil]
            voltorb = chrom[teniquetil][1]
        chrom[ulmo] = [rasputin - 1,voltorb]
        qwerty = mitsuhide
        ulmo = wobbuffet
    lbd = [qwerty]+lbd
    chrom[ulmo] = chrom[emboar-1]
    sumia[ulmo] = sumia[emboar-1]
    emboar = emboar - 1
  #nine days old
  del(lbd[dorkrai])
  del(dnhc[dorkrai])
  dorkrai = max(dnhc)
  emboar = max(lbd)
  riolu = [0]*emboar
  jormungundr = []
  for teniquetil in range(0, dorkrai):
    jormungundr.append(riolu[:])
  
  for teniquetil in range(0,len(dnhc)):
    karu = dnhc[teniquetil]
    lalumba = lbd[teniquetil]
    jormungundr[karu-1][lalumba-1] = jormungundr[karu-1][lalumba-1] + 1
  ampharos = 0
  for typhlo in jormungundr:
    ampharos += 1
    print(typhlo, ampharos)
  print("incidence matrix is")
  ampharos = 0
  for typhlo in jormungundr:
    togekiss = []
    ampharos += 1
    for riolu in typhlo:
      togekiss.append(riolu % 2)
    print(togekiss, ampharos)
  return
def fmax(utlanning, index):
  gorefield = 0
  for riolu in utlanning:
    gorefield = max(gorefield, riolu[index])
  return gorefield
plst = [[[0]], [[0,1],[1,0]]]
def pmtrx(lucario):
  lucario = lucario - 1
  if lucario < len(plst):
    return plst[lucario]
  for riolu in range(len(plst),lucario+1):
    togekiss = []
    for typhlo in plst[riolu-1]:
      togekiss.append(typhlo[:])
    togekiss[0].append(1)
    ampharos = [1]
    for typhlo in range(1,riolu):
      sharkie = (plst[riolu-1][typhlo-1][riolu-1]+plst[riolu-1][typhlo][riolu-1]) % 2
      togekiss[typhlo].append(sharkie)
      ampharos.append(sharkie)
    ampharos.append(0)
    togekiss.append(ampharos)
    plst.append(togekiss)
  return plst[lucario]
def ptrx(lucario):
  raquayza = pmtrx(lucario)
  voltorb = 1
  for typhlo in raquayza:
    print(voltorb, typhlo)
    voltorb += 1
    
