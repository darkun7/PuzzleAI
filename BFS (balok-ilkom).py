# Reference Rahul Malviya
# Darkun7 aka Hartawan Bahari Mulyadi

list = {}                   #Dictionary graf yang terbentuk
level = 0                   #level dari pencarian saat ini (global var.)
found_value = []            #arrya nilai kanan dan kiri yang ditemukan
def getChild(l, r, limit):  #Fungsi untuk membuat node turunan
    value = 0               #nilai yang akan dikirim sebagai return/ return value
    if limit!=0 :           #nilai batas jumlah turunan yang akan dicari
        if r>=0:            #kondisi syarat
            value = (getChild(l, r+3, limit-1))     #untuk membuat note turunan dari node saat ini
        if l>=0:            #kondisi syarat
            value = (getChild(l+5, r, limit-1))     #untuk membuat note turunan dari node saat ini
        if r>=0 and l>=0:   #kondisi syarat
            value = (getChild(l+5, r+3, limit-1))   #untuk membuat note turunan dari node saat ini
        if r>=3:            #kondisi syarat
            val = (getChild(l, r-1, limit-1))       #untuk membuat note turunan dari node saat ini
        if l>=5:            #kondisi syarat
            value = (generate(l-3, r, limit-1))     #untuk membuat note turunan dari node saat ini
        if r>=3 and l>5:    #kondisi syarat
            value = (getChild(l-3, r-1, limit-1))   #untuk membuat note turunan dari node saat ini
    return value            #nilai yang didapat akan dikirim dan nantinya akan diproses lagi pada baris antara 11-21
def generate(l, r, lvl):    #Fungsi utama dari program BFS/LFS untuk pembatasan hasil
    global list, level      #pemanggilan global variable
    level += 1              #peningkatan jumlah level
    val = str(l)+','+str(r) #pengisian nilai val yang nantinya digunakan sebagai penamaan dari dictionary
    arr = []                #array kosong untuk menampung node yang didapat dari get child
    lim = lvl               #batas pencarian
    if l==r and l!=0:       #Syarat tujuan, dimana nilai l sama dengan r dan bukan merupakan nilai 0
        found_value.append(l+r)         #menyimpan nilai yang memenuhi syarat
        print('Ditemukan nilai ' + val) #menampilkan output hasil temuan
    if(level<lvl):          #batasan level
        if r>=0:            #kondisi syarat utama
            arr.append(getChild(l, r+3, lim))
        if l>=0:            #kondisi syarat utama
            arr.append(getChild(l+5, r, lim))
        if r>=0 and l>=0:   #kondisi syarat utama
            arr.append(getChild(l+5, r+3, lim))
        if r>=3:            #kondisi syarat utama
            arr.append(getChild(l, r-1, lim))
        if l>=5:            #kondisi syarat utama
            arr.append(getChild(l-3, r, lim))
        if r>=3 and l>5:    #kondisi syarat utama
            arr.append(generate(l-3, r-1, lim))
    list[val] = arr         #penyimpanan node induk dan anaknya
generate(0, 0, 2)           #pemanggilan fungsi BFS/LFS urutan fungsi parameter (start nilai alber, start nilai bima, batasan level pencarian)
print(list)                 #mencetak graf yang sudah dibentuk berupa dictionary
