# daftar deklarasi fungsi
def baca_data(filename):
    file = open(filename,'r')

    toko = {}
    toko_salim = {} #key : nama barang, value : harga barang
    toko_toha = {} #key : nama barang, value : harga barang
    toko_ivan = {} #key : nama barang, value : harga barang
    toko_sutar = {} #key : nama barang, value : harga barang
    toko_karsono = {} #key : nama barang, value : harga barang
    toko_yatinah = {} #key : nama barang, value : harga barang
    


    
    teks = file.readline().replace("\n","")#menghilangkan spasi
    while teks != "" : #teks bukan EOF (end of file)
        list_kata = teks.split() # indeks 0 : nama barang, indeks 1 sampai 6 harga di toko-toko

    #Pengkongidisian untuk mencari dictionary value
        
        if list_kata[1] in toko_salim:
            toko_salim[list_kata[0]].append(list_kata[1])
        else :
            toko_salim[list_kata[0]]=list_kata[1]
            
        if list_kata[2] in toko_toha:
            toko_toha[list_kata[0]].append(list_kata[2])
        else :
            toko_toha[list_kata[0]]=list_kata[2]

        if list_kata[3] in toko_ivan:
            toko_ivan[list_kata[0]].append(list_kata[3])
        else :
            toko_ivan[list_kata[0]]=list_kata[3]
            
        if list_kata[4] in toko_sutar:
            toko_sutar[list_kata[0]].append(list_kata[4])
        else :
            toko_sutar[list_kata[0]]=list_kata[4]

        if list_kata[5] in toko_karsono:
            toko_karsono[list_kata[0]].append(list_kata[5])
        else :
            toko_karsono[list_kata[0]]=list_kata[5]

        if list_kata[6] in toko_yatinah:
            toko_yatinah[list_kata[0]].append(list_kata[6])
        else :
            toko_yatinah[list_kata[0]]=list_kata[6]


        nama_toko = ["toko_salim","toko_toha","toko_ivan","toko_sutar","toko_karsono","toko_yatinah"] #keys dictionary besar
        value_toko = [toko_salim,toko_toha,toko_ivan,toko_sutar,toko_karsono,toko_yatinah] #value dictionary besar
        

        #Perulangan untuk membuat dictionary besar
        
        for i in range(6):
            toko[nama_toko[i]]=value_toko[i]
        
        teks = file.readline().replace("\n","") #menghilangkan spasi 
    
    file.close()
    return toko
  

def termurah(data, nama_barang):
    list_namaToko = list(data.keys())#["toko_salim","toko_toha","toko_ivan","toko_sutar","toko_karsono","toko_yatinah"]
    list_hargaBarang = list(data.values()) #[{'Beras': '15.000', 'Minyak': '32.500', 'Gula': '12.000', 'Terigu': '7.000', 'Telur': '24.000'},'Beras': '14.500', 'Minyak': '32.500', 'Gula': '12.000', 'Terigu': '7.500', 'Telur': '24.000'} dst
    list_hargaDicari = [] #inisialisasi
    
    for i in range(len(data)):
        list_hargaDicari.append(list_hargaBarang[i][nama_barang]) #List harga barang tertentu yang akan dicari nilai termurahnya
        
    hargaMin = min(list_hargaDicari) #Harga termurah    

    IndeksMin = list_hargaDicari.index(hargaMin) # indeks atau posisi harga termurah tersebut di dalam list

    return list_namaToko[IndeksMin] #Nama toko yang memiliki barang yang dicari dengan harga termurah

def report(data, nama_barang):
    list_namaToko = list(data.keys())#["toko_salim","toko_toha","toko_ivan","toko_sutar","toko_karsono","toko_yatinah"]
    list_hargaBarang = list(data.values()) #[{'Beras': '15.000', 'Minyak': '32.500', 'Gula': '12.000', 'Terigu': '7.000', 'Telur': '24.000'},'Beras': '14.500', 'Minyak': '32.500', 'Gula': '12.000', 'Terigu': '7.500', 'Telur': '24.000'} dst
    list_hargaDicari = [] #inisialisasi 
    
    for i in range(len(data)):
        list_hargaDicari.append(list_hargaBarang[i][nama_barang]) # List harga barang tertentu yang akan dicari nilai rata-ratanya

    for j in range(len(data)):
        
        list_hargaDicari[j]=int(list_hargaDicari[j].replace(".","")) #casting tipe data dari list harga barang dicari dan mengganti . menjadi kosong

    hargaAvg = (sum(list_hargaDicari))/len(list_hargaDicari) # fungsi sum yang digunakan untuk menjumlahkan semua harga barang dibagi jumlah barang 

    return hargaAvg # harga rata-rata
   
# main program
file= "File_teks.txt"
dict_toko=baca_data(file)
print(dict_toko)
nama_barang = input()
print("Harga barang termurah ada di :" ,termurah(dict_toko,nama_barang)) 
print("Rata-rata harga barang di seluruh toko yaitu: Rp" ,"{:,.2f}".format(report(dict_toko,nama_barang)))





