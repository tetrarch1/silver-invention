def ptb(szen, sztva):
  return tblx(pmtrx(szen), pmtrx(sztva))
def tblx(matrixa, matrixb):
  import math
  for pqcounter in range(2):

    listone = []
    listsab = []
    if pqcounter == 0:
      for listw in matrixa:
        listsab.append(listw[:])
    else:
      for listw in matrixb:
        listsab.append(listw[:])
    for twocounter in range(len(listsab)):
      for counter in range(len(listsab[twocounter])):
        while listsab[twocounter][counter] > 0:
          listone.append([1+counter,1+twocounter])
          listsab[twocounter][counter]=listsab[twocounter][counter] - 1
    interrim = []
    for listw in listone:
      interrim.append(listw[:])
    listone = []
    liste = []
    for twocounter in interrim:
      liste.append((twocounter)[1])
      listone.append((twocounter)[0])
    listl = [[1,1]]  
    clistone = [[1,0]]
    slistone = [[1,0]]
    for alphabet in range(1, len(listone)):
      b = 3
      x = 1
      qwerty = alphabet
      while b != 4:
        b = 4
        i = -1
        truth = True
        while i < len(slistone)-1 and truth:
          i += 1         
          j = None
          for counter in range(0,len(slistone)):
            if clistone[counter][0] == x:
              if j == None and listone[slistone[counter][1]]>listone[qwerty]:
                j = slistone[counter]
              elif listone[slistone[counter][1]]>listone[qwerty] and slistone[counter][0] < j[0]:
                j = slistone[counter]
          if j != None:
            w = j[0]
            j = j[1]
            if listone[j] > listone[qwerty]:
              b = 3               
              if alphabet == qwerty:
                clistone.append([x, qwerty])
                slistone.append([w, qwerty])
              else:
                clistone[qwerty] = [x, qwerty]
                slistone[qwerty] = [w, qwerty]
              qwerty = j
              x = x + 1
              truth = False
      maxim = 0
      for f in range(0,len(slistone)):
       
        if clistone[f][0] == x:
          v = slistone[f][0]
          maxim = max(maxim, v)
      listl.append([x, maxim+1])
      if alphabet == qwerty:
        clistone.append([x, qwerty])
        slistone.append([maxim+1, qwerty])
      else:
        clistone[qwerty] = [x, qwerty]
        slistone[qwerty] = [maxim+1, qwerty]
    listma = []
    for anothercounter in range(0,len(clistone)):
      listma.append([clistone[anothercounter][0], slistone[anothercounter][0]])
    listm = []
    for u in range(1,len(clistone)+1):
      utwo = len(clistone) - u
      ra = (clistone[utwo])[1]
      listm = [listone[ra]]+listm
    if pqcounter == 0:
      listv = []
      listmwe = []
      listg = []
      listthree = []
      for listw in liste:
        listv.append(listw)
      for listw in listl:
        listmwe.append(listw[:])
      for listw in listma:
        listg.append(listw[:])
      for listw in listm:
        listthree.append(listw)
    else:
      listf = []
      for listw in listm:
        listf.append(listw)
      listm = []
      for listw in listthree:
        listm.append(listw)
  for pqcounter in range(2):
    if pqcounter == 1:
      i = fmax(listma,1)
      w = fmax(listg, 0)
      row = []
      for counter in listma:
        row.append([counter[0]+w, counter[1]])
      rowtva = []
      for counter in listg:
        rowtva.append([counter[0], counter[1]+i])
      listthree= rowtva+row
      listone = listm + listf
    else:
      i = fmax(listl, 1)
      w = fmax(listmwe, 0)
      row = []
      for counter in listmwe:
        row.append([counter[0],counter[1] + i])
      rowtva = []
      for counter in listl:
        rowtva.append([counter[0]+w,counter[1]])
      listthree = rowtva+row
      listone = liste + listv
    b = 4
    while b != 3:
      b = 3
      d = fmax(listthree, 1)
      e = fmax(listthree, 0)
      froslass = max(listone)
      h = froslass
      slistone = [-1,-1,-1]
      u = e+1
      while u >=2:
        u = u - 1
        v = d + 1
        while v >= 2:
          v = v - 1
          lalumba = [u, v]
          if lalumba not in listthree:
            p = [u, v+1]
            if p not in listthree:
              j = h + 1
              slistone[0] = -1
            else:
              timer = listthree.index(p)
              slistone[0] = timer
              j = listone[timer]
            p = [u+1, v]
            if p not in listthree:
              karu = h + 1
              slistone[1] = -1
            else:
              timer = listthree.index(p)
              slistone[1] = timer
              karu = listone[timer]
            if (j != h+1) or (karu!= h+1):
              b = b + 1
              if j >= karu:
                listthree[slistone[1]][0] = listthree[slistone[1]][0] - 1
                u += 1
                v += 1
              else:
                listthree[slistone[0]][1] = listthree[slistone[0]][1] - 1
                u += 1              
    if pqcounter == 0:
      rowtra = listone[:]
      rowfyra = []
      for counter in listthree:
        rowfyra.append(counter[:])
  slistone = []
  for twocounter in listthree:
    slistone.append(twocounter[:])
  slisttwo = listone[:]
  lbd = [0]
  dnhc = [0]
  d = len(listone)
  e = d
  while e > 0:
    for counter in range(e, len(slisttwo)):
      del(slisttwo[counter])
      del(slistone[counter])
      del(rowtra[counter])
      del(rowfyra[counter])
    m = 0
    pippin = [0,0]
    for timer in range(0,e):
      if (rowtra[timer] == m) and (rowfyra[timer][1]>pippin[1]):
        pippin = rowfyra[timer]
        orome = timer      
      if rowtra[timer] > m:
        orome = timer
        pippin = rowfyra[timer]
        m = rowtra[timer]
    dnhc = [m]+dnhc
    rowtra[orome] = rowtra[e-1]
    rowfyra[orome] = rowfyra[e-1]
    timer = slistone.index(pippin)
    u = timer
    qwerty = slisttwo[u]
    if slistone[u][0] != 1:
      while slistone[u][0] != 1:
        ra = slistone[u][0]
        m = 0
        v = 0
        for timer in range(0,e):
          if (slisttwo[timer] < qwerty) and (slisttwo[timer] == m) and (slistone[timer][1] > v) and (ra - 1 == slistone[timer][0]) or (slisttwo[timer]<qwerty) and (slisttwo[timer] > m) and (ra - 1 == slistone[timer][0]):
            w = timer
            m = slisttwo[timer]
            v = slistone[timer][1]
        slistone[u] = [ra - 1,v]
        qwerty = m
        u = w
    lbd = [qwerty]+lbd
    slistone[u] = slistone[e-1]
    slisttwo[u] = slisttwo[e-1]
    e = e - 1
  del(lbd[d])
  del(dnhc[d])
  d = max(dnhc)
  e = max(lbd)
  counter = [0]*e
  j = []
  for timer in range(0, d):
    j.append(counter[:])
  
  for timer in range(0,len(dnhc)):
    karu = dnhc[timer]
    lalumba = lbd[timer]
    j[karu-1][lalumba-1] = j[karu-1][lalumba-1] + 1
  otherlist = 0
  for pqcounter in j:
    otherlist += 1
    print(pqcounter, otherlist)
  print("incidence matrix is")
  otherlist = 0
  for pqcounter in j:
    listone = []
    otherlist += 1
    for counter in pqcounter:
      listone.append(counter % 2)
    print(listone, otherlist)
  return
def fmax(somelist, index):
  maxim = 0
  for counter in somelist:
    maxim = max(maxim, counter[index])
  return maxim
plst = [[[0]], [[0,1],[1,0]]]
def pmtrx(twocounter):
  twocounter = twocounter - 1
  if twocounter < len(plst):
    return plst[twocounter]
  for counter in range(len(plst),twocounter+1):
    listone = []
    for pqcounter in plst[counter-1]:
      listone.append(pqcounter[:])
    listone[0].append(1)
    otherlist = [1]
    for pqcounter in range(1,counter):
      s = (plst[counter-1][pqcounter-1][counter-1]+plst[counter-1][pqcounter][counter-1]) % 2
      listone[pqcounter].append(s)
      otherlist.append(s)
    otherlist.append(0)
    listone.append(otherlist)
    plst.append(listone)
  return plst[twocounter]
def ptrx(twocounter):
  r = pmtrx(twocounter)
  v = 1
  for pqcounter in r:
    print(v, pqcounter)
    v += 1
    


