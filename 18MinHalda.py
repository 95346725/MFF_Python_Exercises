class MinHalda:
    def __init__(self):
        self.halda = []

    def swap(self,a,b):
      (self.halda[a], self.halda[b]) = (self.halda[b], self.halda[a])

    def bublej_nahoru(self, i):
      while i>0:
        j = (i-1)//2 #index rodice
        if self.halda[i]>=self.halda[j]: #dite vetsi nez rodic, tak je to 
            break
        self.swap(i,j)
        i=j #posouvame se na rodice

    def bublej_dolu(self,N,i): #po odebrani korene a nahrazeni poslednim
        while 2*i+1<N: # dokud existuje leve dite, ted je ta halda o prvek vetsi
            j=2*i+1 #index leveho ditete
            if j+1<N and self.halda[j] > self.halda[j+1]: #pokud je prave dite mensi (a existuje)
                j+=1 #budeme nahrazovat nej
            if self.halda[i]>self.halda[j]: #pokud je rodic vetsi nez mensi z deti
                self.swap(i,j)
            i=j #pokracuju s novou pozici


    #vymaz koren
    def pop(self):
        koren = self.halda[0]
        self.halda[0] = self.halda[-1] #na koren dej posledni prvek z haldy
        self.halda.pop() #smaž poslední prvek z haldy
        self.bublej_dolu(0) #probublej prvek na spravne misto
        return koren
    
    #vloz novy prvek
    def vloz(self,prvek):
      # Vložíme prvek na konec
      self.halda.append(prvek)
      i = len(self.halda) - 1 #soused/rodic
      self.bublej_nahoru(i)

    def heapsort(pole):
      N = len(pole)
      for i in range(N//2, -1, -1): #N//2 = (pole-1)//2, jedeme od poloviny (nejblizsi rodic) do zacatku (tzn prvni polovinu, kde maj byt rodice)
        bublej_dolu(pole,N, i) #bublame dolu prvni polovinu pole, od stredu -> pak mame spravnou strukturu minheap
      # Výběr maxima a jeho přesun nakonec
      for i in range(N - 1, 0, -1): #ted tim prozeneme postupne vsechny prvky, at zapadnou do spravnych kolonek
        (pole[0], pole[i]) = (pole[i], pole[0])
        bublej_dolu(pole,i, 0) #vždy jen do momentu, kdy to mame srovnane, zbytek nema cenu zatim bublat
      return pole

  
