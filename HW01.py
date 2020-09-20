for a in range(1,5):#將百位數字從1走到4
  for m in range(1,5):#將十位數字從走1到4
    for g in range(1,5):#將個位數字從走1到4
      if(a!=m)&(m!=g)&(a!=g):#如果三個數字都不一樣就印出來
        print (a,m,g)
