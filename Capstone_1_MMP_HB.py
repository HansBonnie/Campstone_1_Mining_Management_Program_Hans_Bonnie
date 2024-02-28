from tabulate import tabulate
import time

#============================================D I C T I O N A R Y ===============================================================

# Disini saya memilih penggunaan nested dictionary pada data dummy karena lebih mudah dalam pemanggilan value nya

data_site = {
    'RGR_01':{'Nama Site':'Satui','Jenis Batu Bara':'Bituminus','Volume Overburden':40000,'Cadangan Terukur':200000},
    'RGR_02':{'Nama Site':'Senakin','Jenis Batu Bara':'Sub-Bituminus','Volume Overburden':32000,'Cadangan Terukur':160000},
    'RGR_03':{'Nama Site':'Asam-Asam','Jenis Batu Bara':'Lignit','Volume Overburden':20000,'Cadangan Terukur':100000},
    'RGR_04':{'Nama Site':'Batulicin','Jenis Batu Bara':'Bituminus','Volume Overburden':50000,'Cadangan Terukur':300000}
}

data_hd ={
    'WL_01':{'Jenis':'Wheel Loader','Merk':'Caterpilar','Type':'Cat 980','Kapasitas':4,'Status':'Standby'},
    'WL_02':{'Jenis':'Wheel Loader','Merk':'Caterpilar','Type':'Cat 980','Kapasitas':7.4,'Status':'Operasonal'},
    'WL_03':{'Jenis':'Wheel Loader','Merk':'Volvo','Type':'L150','Kapasitas':4,'Status':'Operasonal'},
    'EX_01':{'Jenis':'Excavator','Merk':'Caterpilar','Type':'Cat 320','Kapasitas': 1,'Status':'Maintenance'},
    'EX_02':{'Jenis':'Excavator','Merk':'Komatsu','Type':'Cat 330','Kapasitas': 2.1,'Status':'Operasonal'},
    'EX_03':{'Jenis':'Excavator','Merk':'Komatsu','Type':'PC 300','Kapasitas': 2.3,'Status':'Operasonal'},
    'DT_01':{'Jenis':'Dump Truck','Merk':'Caterpilar','Type':'Cat 770','Kapasitas':98.2 ,'Status':'Standby'},
    'DT_02':{'Jenis':'Dump Truck','Merk':'Komatsu','Type':'HD 325','Kapasitas':40,'Status':'Operasonal'},
    'DT_03':{'Jenis':'Dump Truck','Merk':'Komatsu','Type':'A25','Kapasitas':25,'Status':'Operasonal'}
}

data_manpower = {
    'EP_01':{'Nama':'Rico Bana','Posisi':'Wheel Loader Operator','Usia':28,'Status':'On-duty'},
    'EP_02':{'Nama':'Cipta Kridatama','Posisi':'Wheel Loader Operator','Usia':29,'Status':'On-leave'},
    'EP_03':{'Nama':'Ronald Surapraja','Posisi':'Wheel Loader Operator','Usia':26,'Status':'On-duty'},
    'EP_04':{'Nama':'Giring Nidji','Posisi':'Excavator Operator','Usia':36,'Status':'On-leave'},
    'EP_05':{'Nama':'Amboy Nian','Posisi':'Excavator Operator','Usia':38,'Status':'On-duty'},
    'EP_06':{'Nama':'Ucok Piscok','Posisi':'Excavator Operator','Usia':37,'Status':'On-duty'},
    'EP_07':{'Nama':'Arutmin','Posisi':'Dumptruck Operator','Usia':35,'Status':'On-duty'},
    'EP_08':{'Nama':'Dono Doni','Posisi':'Dumptruck Operator','Usia':29,'Status':'On-leave'},
    'EP_09':{'Nama':'Brama Kumbala','Posisi':'Dumptruck Operator','Usia':28,'Status':'On-duty'},
    'EP_10':{'Nama':'Armando Mahler','Posisi':'Mine Planner','Usia':26,'Status':'On-duty'},
    'EP_11':{'Nama':'Angling Darma','Posisi':'Checker','Usia':30,'Status':'On-duty'},
    'EP_12':{'Nama':'Marina Marini','Posisi':'Admin','Usia':24,'Status':'On-duty'}
}



#===================================================S I T E=====================================================================
def tampilkan_site():
    '''
    Fungsi ini untuk menampilkan keseluruhan site  
    '''
    print (f"\n{' ':30}DAFTAR SITE RIANG GEMBIRA RESOURCES\n")
    rows =[]
    for id_site, info in data_site.items():
        row = [id_site,info['Nama Site'],info['Jenis Batu Bara'],info['Volume Overburden'],info['Cadangan Terukur']]
        rows.append(row)    
        # Kita melakukan append dari hasil looping agar data hasil looping tersebut berubah mnjadi list dan bisa diprint menggunakan tabulate
    print(tabulate(rows,headers=['ID Site','Nama Site','Jenis Batu Bara','Volume Overburden','Cadangan Terukur'],tablefmt='fancy_grid'))


def cadangan_terukur (item):
    '''
    Fungsi ini untuk mengambil nilai dari Data_Site
    
    [1] beartujuan untuk mengambil data dari dictionary index 1
        atau yang menjadi value dari key 'RGR_01','RGR_02',dsb
    
    ['Cadangan Terukur'] merupakan key yang ada didalam index 1
                         key yang akan kita pakai value nya
    '''
    return item[1]['Cadangan Terukur']

def tampilkan_site_tertentu():
    '''
    Fungsi ini berisi semua sub-menu yang bertujuan untuk
    melakukan sortir dan filter
    '''
    while True:
        print(f"{'='*90}")
        print('Menu Sortir:')
        print(f"{'-'*90}")
        print('1. Tampilkan Site dengan ID Site')
        print('2. Tampilkan Site Berdasarkan Jumlah Cadangan')
        print('3. Tampilkan Site dengan Jenis Batu Bara Tertentu')
        print('4. Kembali ke Menu Site Riang Gembira Resource')
        print(f"{'='*90}")

        task=input('Masukan Menu Sortir yang anda inginkan: ')
        if task =='1':
            task2 = input('\nHarap Masukan ID Site yang dicari: ').upper()
            
            if task2 in data_site:
                # Pada baris ini program akan memanggil seluruh value sesuai dengan input
                # Input berupa ID Site yang menjadi key utama dari Dictionary data_site
                # Value yang sudah dipanggil sesuai dengan key kemudian dijadikan list, karena program memakai Tabulate untuk menampilkan hasil

                print(f'\nInformasi Site dengan ID Site: {task2} adalah:')
                site_info = data_site[task2]
                rows = [[task2, site_info['Nama Site'], site_info['Jenis Batu Bara'], site_info['Volume Overburden'],site_info['Cadangan Terukur']]]
                print(tabulate(rows, headers=['ID Site', 'Nama Site', 'Jenis Batu Bara', 'Volume Overburden','Cadangan Terukur'], tablefmt='fancy_grid'))
                while True :
                    # Ketika memasukan input 'Ya' maka akan kembali ke 'Menu Sortir'
                    # Ketika memasukan input 'Tidak' maka akan kembali ke 'Menu Utama'
                    # Ketika  input yang dimasukan salah maka akan terus menampilkan pesan input sampai user memberikan input yang benar

                    
                    print ('\nApakah anda ingin kembali ke Menu Sortir? (Ya/Tidak): ')
                    input_task2 = input('')
                    if  input_task2.lower() == 'ya':
                        break
                    elif input_task2.lower() == 'tidak':
                        return
                    else :
                        print ('Anda memasukan input yang salah')
                        continue

            else:
                print("ID Site tidak ditemukan.")
            
        
        elif task == '2':
            # Pada bagian ini program melakukan sorting data berdasarkan 'Cadangan Terukur'
            # Program akan melakukan sort secara Descending, ditandai dengan penggunaan 'reverse=True'
            # Kita menyiapkan list kosong yang nanti akan di append dengan data baru yang dipanggil dari 
            # dari data yang telah tersortir dari 'sort_cadangan_terukur' agar bisa ditampilkan dengan tabulate
            while True :
                print ('\n1. Tampilkan secara Descending')
                print ('2. Tampilkan secara Ascending')
                Input_command = input('Silahkan Masukan Jenis yang anda inginkan :')
                if Input_command=='1':
                    sort_cadangan_terukur = sorted(data_site.items(), key=cadangan_terukur,reverse=True)
                    rows2 = []
                    for id_site,site_info in sort_cadangan_terukur:
                        row=[id_site,site_info['Nama Site'], site_info['Jenis Batu Bara'], site_info['Volume Overburden'],site_info['Cadangan Terukur']]
                        rows2.append(row)
                    print(tabulate(rows2, headers=['ID Site', 'Nama Site', 'Jenis Batu Bara', 'Volume Overburden','Cadangan Terukur'], tablefmt='fancy_grid'))
                    break

                elif Input_command=='2' :
                    sort_cadangan_terukur = sorted(data_site.items(), key=cadangan_terukur,reverse=False)
                    rows2 = []
                    for id_site,site_info in sort_cadangan_terukur:
                        row=[id_site,site_info['Nama Site'], site_info['Jenis Batu Bara'], site_info['Volume Overburden'],site_info['Cadangan Terukur']]
                        rows2.append(row)
                    print(tabulate(rows2, headers=['ID Site', 'Nama Site', 'Jenis Batu Bara', 'Volume Overburden','Cadangan Terukur'], tablefmt='fancy_grid'))
                    break 

                else :
                    print ('Harap masukan pilihan yang benar :')
                    continue
            
            while True :
                    # Ketika memasukan input 'Ya' maka akan kembali ke 'Menu Sortir'
                    # Ketika memasukan input 'Tidak' maka akan kembali ke 'Menu Utama'
                    # Ketika  input yang dimasukan salah maka akan terus menampilkan pesan input sampai user memberikan input yang benar

                    print ('\nApakah anda ingin kembali ke Menu Sortir? (Ya/Tidak): ')
                    input_task2 = input('')
                    if  input_task2.lower() == 'ya':
                        break
                    elif input_task2.lower() == 'tidak':
                        return
                    else :
                        print ('Anda memasukan input yang salah')
                        continue
        
        elif task == '3':
            # Pada bagian ini akan melakukan filter berdasarkan jenis batubara 
            # Pemilihan dilakukan dengan mengetikan jenis batu bara yang dicari
            # Pada program ini input yang dimasukan tidak perlu memperhatikan huruf besar atau kecil karena menggunakan fungsi UPPER
            # ini dilakukan agar menghindari eror saat program dijalankan 

            print ('\nJenis Batu Bara yang tersedia')
            print ('1. Bituminus')
            print ('2. Sub-Bituminus')
            print ('3. Lignit')
            time.sleep (1)
            jenis_bb=input ('\nMasukan Jenis Batu Bara yang ingin dicari:')
            filtered_data = []
            found = False
            # fungsi found disini dibuat defaultnya false, yang berguna sebagai penanda apakah jenis_bb nya ada di database
            for id_site, site_info in data_site.items() :
                if jenis_bb.capitalize() == site_info['Jenis Batu Bara']:
                    site_data = [id_site]+list(site_info.values())
                    filtered_data.append(site_data) 
                    found = True
                    # Jika jenis_bb ditemukan maka found akan bernilai True
                    
            if not found :
                print (f"Jenis Batu Bara : '{jenis_bb.upper()}' tidak ditemukan, harap periksa kembali")
                time.sleep (2)
            else :
                print((tabulate(filtered_data, headers=['ID Site', 'Nama Site', 'Jenis Batu Bara', 'Volume Overburden','Cadangan Terukur'], tablefmt='fancy_grid')))
                while True :
                    # Ketika memasukan input 'Ya' maka akan kembali ke 'Menu Sortir'
                    # Ketika memasukan input 'Tidak' maka akan kembali ke 'Menu Utama'
                    # Ketika input yang dimasukan salah maka akan terus menampilkan pesan input sampai user memberikan input yang benar

                    print ('\nApakah anda ingin kembali ke Menu Sortir? (Ya/Tidak): ')
                    input_task2 = input('')
                    if  input_task2.lower() == 'ya':
                        break
                    elif input_task2.lower() == 'tidak':
                        return
                    else :
                        print ('Anda memasukan input yang salah')
                        continue
        elif task == '4':
            break
        else :
            print("Masukan tidak valid. Silakan masukan nomor dari 1 hingga 4.")
           

def update_data_site():
    '''
    Ketika fungsi update_data_site dijalankan akan langsung menampilkan data seluruh site,
    agar mempermudah untuk melihat mana yang mau di update
    '''
    tampilkan_site()
    id_site = (input('\nMasukan ID Site yang ingin diperbarui: ')).upper()
    data_kosong ={
        'Nama Site': 'xxxx',
        'Jenis Batu Bara': 'xxxx',
        'Volume Overburden':00,
        'Cadangan Terukur':00

    }
    if id_site in data_site:
    # perintah ini untuk melakukan pengecekan apakah yang di input tersedia pada database
        print (f'ID Site : {id_site}')
        print ('Isi informasi baru: ')
        nama_site = input('Masukan Nama Site Baru :').title()
        jenis_bb = input('Masukan Jenis Batu Bara :').title()
        while True :
        # Looping ini berfugsi untuk memastikan input yang diberikan berupa bilangan bulat
        # Jika bukan bilang bulat maka akan menampilkan pesan error dan mengulangi looping kembali
            volume_ob = (input('Masukan Volume Overburden :'))
            if volume_ob.isdigit():
                volume_ob = int(volume_ob)
                break
            else :
                print('Maaf, Anda hanya bisa memasukan bilangn bulat positif')
                print('Silahkan ulangi lagi')
                time.sleep(1)
                continue
        while True :
        # Looping ini berfugsi untuk memastikan input yang diberikan berupa bilangan bulat
        # Jika bukan bilang bulat maka akan menampilkan pesan error dan mengulangi looping kembali
            cadangan = (input('Masukan Tonase Cadangan :'))
            if cadangan.isdigit():
                cadangan = int(cadangan)
                break
            else :
                print('Maaf, Anda hanya bisa memasukan bilangn bulat yang benar benar bulat')
                print('Silahkan ulangi lagi')
                time.sleep(1)
                continue

        data_kosong['Nama Site'] = nama_site
        data_kosong['Jenis Batu Bara'] = jenis_bb
        data_kosong['Volume Overburden'] = volume_ob
        data_kosong['Cadangan Terukur'] = cadangan
        
        while True :
            task3 = input('Apakah anda sudah yakin dengan data baru ? (Ya/Tidak)')
            if task3.lower() == 'ya' :
                data_site[id_site]=data_kosong
                print ('Berikut Data yang telah diperbarui')
                # Setelah melakukan konfirmasi penggantian data baru akan langsung mengganti data lama
                # dan akan ditampilkan dengan format tabulate seperti di fungsi tampilkan site 
                tampilkan_site()
                break
            elif task3.lower() == 'tidak' :
                print ('\nUpdate data anda dibatalkan\n')
                tampilkan_site()
                return
            else :
                print('\nInput tidak valid. Silakan masukkan "ya" atau "tidak".')
                continue
                
        while True:
            task4 = input('Apakah anda ingin mengganti yang lain? (Ya/Tidak)')
            if task4.lower() == 'ya' :
                update_data_site()
            elif task4.lower()=='tidak':
                break
            else :
                print ('Harap masukan input yang benar')
                continue
    else :
        print ('Harap Masukan ID Site sesuai dengan tabel')
        time.sleep (3)
        update_data_site()
    # Penambahan time.sleep bertujuan agar program dapat berjalan lebih ringan, dan memberi kesempatan pada user untuk membaca pesan error


#=============================================A L A T  B E R A T=====================================================================
def tampilkan_alat_berat():
    ''' 
    Fungsi ini sama seperti pada Tampilkan Seluruh Site,
    tetapi database nya menggunanakan data_hd
    '''
    print (f"\n{' ':20}DAFTAR ALAT BERAT RIANG GEMBIRA RESOURCES\n")
    rows_hd=[]
    for id_alat_berat,specs in data_hd.items():
        row1=[id_alat_berat,specs['Jenis'],specs['Merk'],specs['Type'],specs['Kapasitas'],specs['Status']]
        rows_hd.append(row1)
    print(tabulate(rows_hd,headers=['ID Alat','Jenis','Merk','Type','Kapasitas','Status'],tablefmt='fancy_grid'))

def tambahkan_alat_berat():
    ''' 
    Pada menu ini hanya tersedia 3 jenis pilihan alat berat yang bisa ditambahkan

    Pembatasan alat berat yang bisa ditambahkan karena pembuatan nomor index alat berat akan didasarkan pada jenis alat berat yang dimasukan

    Tiap jenis alat berat memiliki kode unik

    WL = Wheel Loader

    EX = Excavator

    DT = Dump Truck

    Pembuatan ID untuk alat berat dilakukan dengan melakukan split dari ID awal alat berat, split dari tanda penghubungnya ('_')

    Kemudian nomor index baru dibuat dengan penambahan dari nomor terakhir pada ID alat berat 


    '''
    print(f"{'='*90}")
    print ("Selamat Datang di Menu Tambah Alat Berat ")
    print ("Daftar Alat Berat yang Dapat Ditambahkan")
    print(f"{'-'*90}")
    print("1. Wheel Loader")
    print("2. Excavator")
    print("3. Dump Truck")
    print("4. Kembali ke Menu Inventaris Alat Berat")
    print(f"{'='*90}")
    input_jenis= input("Masukan Jenis Alat Barat : ")
    if input_jenis =='1':
        jenis = "Wheel Loader"
        if not data_hd:
            new_num = 0+1
            new_key = f"WL_{new_num:02}"
        else:
            last_num = int(list(data_hd.keys())[-1].split('_')[-1])
            new_num = last_num+1
            new_key = f"WL_{new_num:02}"
        # Disini diberikan :02 karena ingin format penulisannya menjadi contoh 'WL_09' sedangkan output yang dihasilkan dari new_key hanya 
        # berupa '9' sehinga perlu dibuat menjadi dua digit dengan :02
    elif input_jenis == '2':
        jenis = "Excavator"
        if not data_hd:
            new_num = 0+1
            new_key = f"EX_{new_num:02}"
        else :    
            last_num = int(list(data_hd.keys())[-1].split('_')[-1])
            new_num = last_num+1
            new_key = f"EX_{new_num:02}"
    elif input_jenis == '3' :
        jenis = "Dump Truck"
        if not data_hd:
            new_num = 0+1
            new_key = f"DT_{new_num:02}"
        else :
            last_num = int(list(data_hd.keys())[-1].split('_')[-1])
            new_num = last_num+1
            new_key = f"DT_{new_num:02}"
    elif input_jenis == '4' :
        return
    else :
        print ('\nAnda memasukan input yang salah')
        time.sleep (0.5)
        tambahkan_alat_berat()

    
    input_merk = input("Masukan Merk Alat Berat : ").title()
    input_type_AB = input("Masukan Type Alat Berat : ").upper()
    
    while True :
            input_kapasitas = (input ("Masukan Kapasitas Alat Berat : "))
            if input_kapasitas.isdigit():
                input_kapasitas = int(input_kapasitas)
                break
            else :
                print('Maaf, Anda hanya bisa memasukan bilangn bulat positif')
                print('Silahkan ulangi lagi')
                time.sleep(1)
                continue
    data_hd[new_key] = {'Jenis': jenis, 'Merk':input_merk,'Type':input_type_AB,'Kapasitas':input_kapasitas,'Status':'Standby'}
    # Pada menu tambah alat berat ini, semua alat berat baru akan memiliki default status berupa 'Standby',
    # karena sesuai dengan praktik di lapangan
    # Perubahan status dapat dilakukan pada fungsi 'update_alat_berat()'
    
    tampilkan_alat_berat()  

    while True :
        task_ab = input('\nApakah anda ingin menambahkan Alat Berat lainnya? (Ya/Tidak) : ')
        if task_ab.lower() == 'ya' :
            tambahkan_alat_berat()
            
        elif task_ab.lower() == 'tidak':
            break
        else :
            print ('Anda memasukan input yang salah')
            continue
        

def hapus_alat_berat() :
    '''
    Fungsi ini akan menghapus seluruh value dari key (ID Alat Berat) yang dimasukan pada input hapus_ab
    '''
    if not data_hd  :
        print('\nTidak ada data yang dapat diperbarui harap tambahkan Alat Berat dahulu')
        time.sleep(1)
    
    else :
        while True :
            tampilkan_alat_berat()
            print ('1. Hapus Data Berdasarkan ID')
            print ('2. Hapus Seluruh Data')
            print ('3. Kembali ke Menu Inventaris Alat Berat')
            menu_hapus = input('Silahkan masukan angka yang anda inginkan :')
            if menu_hapus == '1':
                hapus_ab = input('Silahkan Masukan ID Alat Berat yang ingin anda hapus : ').upper()
                if hapus_ab in data_hd :
                    task4 = input(f"Apakah anda sudah yakin akan menghapus '{hapus_ab}'? (Ya/Tidak) ")
                    if task4.lower() == 'ya':
                        del data_hd[hapus_ab]
                        tampilkan_alat_berat()
                    else:
                        print ('Input Anda Berhasil Dibatalkan')
                        time.sleep(1)
                        break
                else :
                    print(f"Alat Berat dengan ID {hapus_ab} tidak tersedia di Tambang Riang Gembira Resources")
                    time.sleep(1)
                    break


            elif menu_hapus == '2':
                print ('Apakah anda yakin menghapus semua alat berat? (Ya/Tidak)')
                hapus_hd_all = input('')
                if hapus_hd_all.lower() == 'ya':
                    data_hd.clear()
                    print ('Data Alat Berat Berhasil dihapus')
                    tampilkan_alat_berat()
                    break
                elif hapus_hd_all.lower() == 'tidak':
                    print('Input Anda Berhasil Dibatalkan')
                    time.sleep(2)
                    break
                else :
                    print('Anda Memasukan Input Yang Salah')
                    continue    
            elif menu_hapus == '3':
                return
            else :
                print('Anda Memasukan Input Yang Salah')
                continue

def update_alat_berat() :
    if not data_hd  :
        print('\nTidak ada data yang dapat diperbarui harap tambahkan Alat Berat dahulu')
        time.sleep(1)
    
    else :
        while True :
            tampilkan_alat_berat ()
            print ('Pilih angka yang anda inginkan : \n')
            print ('1. Update Status Alat Berat')
            print ('2. Update Data dan Spesifikasi Alat Berat')
            print ('3. Kembali ke Menu Inventaris Alat Berat')
            task5 = input('Silahkan Masukan Pilihan Anda : ')
            if task5 == '1' :
                id_update_status = input('Silahkan Masukan ID Alat Berat : ').upper()
                if id_update_status in data_hd :
                    print ("\nSilahkan Pilih Status Alat Berat :")
                    print ("1. Operasional")
                    print ("2. Standby")
                    print ("3. Maintenance")
                    task6 = input ("Masukan pilihan anda : ")
                    if task6 == '1':
                        status_upd = 'Operasional'
                        data_hd[id_update_status]['Status']=status_upd
                        tampilkan_alat_berat()
                        break
                    elif task6 == '2':
                        status_upd = 'Standby'
                        data_hd[id_update_status]['Status']=status_upd
                        tampilkan_alat_berat()
                        break
                    elif task6 == '3':
                        status_upd = 'Maintenance'
                        data_hd[id_update_status]['Status']=status_upd
                        tampilkan_alat_berat()
                        break
                    else :
                        print ('Silahkan Masukan Status Sesuai Pilihan yang Ada')
                        print ('Anda hanya bisa memasukan 1,2 atau 3')
                        time.sleep (1)
                        continue
                    
            elif task5 == '2' :
                id_ab = input("Silahkan Masukan ID Alat Berat yang ingin anda update : ").upper()
                data_kosong_hd = {
                    'Jenis': 'xxxx',
                    'Merk': 'xxxx',
                    'Type': 'xxxx',
                    'Kapasitas': 0000,
                    'Status': 'xxx'
                }
                
                if id_ab in data_hd :
                    print (f"ID Alat Berat = '{id_ab}'")
                    print ("Silahkan lengkapi data yang ingin anda perbaharui")
                    while True :
                        print("\n Jenis Alat Berat")
                        print("1. Wheel Loader")
                        print("2. Excavator")
                        print("3. Dump Truck")
                        input_jenis_ab = input ("Silahkan masukan jenis alat berat : ")
                        if input_jenis_ab == '1':
                            jenis_ab = 'Wheel Loader'
                            print('Jenis Alat Berat = Wheel Loader')
                            break
                        elif input_jenis_ab == '2':
                            jenis_ab = 'Excavator'
                            print('Jenis Alat Berat = Excavator')
                            break
                        elif input_jenis_ab == '3':
                            jenis_ab = 'Dump Truck'
                            print('Jenis Alat Berat = Dump Truck')
                            break
                        else :
                            print ('Anda Hanya Bisa Memilih 1 dari 3 Jenis Alat Berat yang Tersedia')
                            continue

                    merk_ab = input ("Silahkan masukan Merk alat berat : ").title()
                    type_ab = input ("Silahkan masukan Type alat berat : ").upper()
                    while True :
                        kapasitas_ab = (input ("Silahkan masukan kapasitas alat berat : "))
                        if kapasitas_ab.isdigit():
                            kapasitas_ab = int(kapasitas_ab)
                            break
                        else :
                            print('Maaf, Anda hanya bisa memasukan bilangn bulat positif')
                            print('Silahkan ulangi lagi')
                            time.sleep(1)
                            continue
                    while True :
                        status_ab = input("Silahkan masukan status alat berat : ").capitalize()
                        if status_ab.isalpha()==True :
                            break
                        else :
                            print ('Masukan status yang benar')
                            continue

                    data_kosong_hd['Jenis'] = jenis_ab
                    data_kosong_hd['Merk'] = merk_ab
                    data_kosong_hd['Type'] = type_ab
                    data_kosong_hd['Kapasitas'] = kapasitas_ab
                    data_kosong_hd['Status'] = status_ab

                    while True :
                        task7 = input('Apakah anda sudah yakin dengan data baru ? (Ya/Tidak)')
                        if task7.lower() == 'ya' :
                            data_hd[id_ab] = data_kosong_hd
                            print ('Berikut Data yang telah diperbarui')
                            tampilkan_alat_berat()
                            task8 = input('Apakah anda ingin mengganti yang lain? (Ya/Tidak)')
                            if task8.lower() == 'ya' :
                                update_alat_berat()
                            else :
                                return
                        elif task7.lower() == 'tidak' :
                            print ('\nUpdate data anda dibatalkan\n')
                            tampilkan_alat_berat()
                            break
                        else :
                            print('Input tidak valid. Silakan masukkan "ya" atau "tidak".')
                            update_alat_berat()
                else :
                    print ('Harap Masukan ID Alat Berat sesuai dengan tabel')
                    time.sleep (1)
                    update_alat_berat()
            
            elif task5 == '3':
                return
            else :
                print('Silahkan pilih menu dengan benar')
                time.sleep (1)
                continue


#============================================M A N  P O W E R=====================================================================
def tampilkan_man_power():
    print (f"\n{' ':20}DAFTAR MANPOWER RIANG GEMBIRA RESOURCES\n")
    rows_mp = []
    for id_pegawai,informasi in data_manpower.items():
        row2=[id_pegawai,informasi['Nama'],informasi['Posisi'],informasi['Usia'],informasi['Status']]
        rows_mp.append(row2)
    print(tabulate(rows_mp,headers=['ID Pegawai','Nama','Posisi','Usia','Status'],tablefmt='fancy_grid'))

def tambahkan_pekerja():
    
    input_nama = input("Masukan Nama Pegawai : ").title()
    input_posisi = input("Masukan Posisi Pegawai : ").title()
    while True :
        input_usia = (input ("Masukan Usia Pegawai : "))
        if input_usia.isdigit():
            input_usia =int (input_usia)
            break
        else :
            print ('\nAnda hanya dapat memsaukan bilangan bulat positif')
            print ('Silahkan ulangi lagi')
            continue
    while True :
        print("\n Status Pegawai : ")
        print("1.On-duty ")
        print("2.On-leave ")
        input_status = input ("Masukan Status Pegawai : ")
        if input_status=='1':
            input_status = 'On-duty'
            print('Status pegawai = On-duty')
            break
        elif input_status=='2':
            input_status = 'On-leave'
            print('Status pegawai = On-leave')
            break
        else :
            print ('\nAnda hanya bisa memasukan angka 1 atau 2:')
            continue
        
    if not data_manpower:
        new_num = 0+1
        new_key = f"EP_{new_num:02}"
    else :
        last_num = int(list(data_manpower.keys())[-1].split('_')[-1])
        new_num = last_num+1
        new_key = f"EP_{new_num:02}"
    
    data_manpower[new_key] = {'Nama': input_nama, 'Posisi':input_posisi,'Usia':input_usia,'Status':input_status}  

    while True :
        task_mp = input('Apakah Data Pegawai Baru Sudah Benar? (Ya/Tidak) : ')
        if task_mp.lower() == 'ya' :
            tampilkan_man_power()
            break
        elif task_mp.lower() == 'tidak':
            tambahkan_pekerja()
        else :
            print('Input yang anda masukan tidak valid')
            time.sleep(0.5)
            return

def hapus_pekerja() :
    '''
    Fungsi ini akan menghapus seluruh value dari key (ID Manpower) yang dimasukan pada input hapus_ab
    '''
    if not data_manpower :
        print ('Tidak ada data pegawai, harap tambahkan pegawai dulu')
        time.sleep(1)
    else :
        while True :
            tampilkan_man_power()
            print ('1. Hapus Data Berdasarkan ID')
            print ('2. Hapus Seluruh Data')
            print ('3. Kembali ke Menu Manajemen Manpower')
            menu_del_mp = input('Silahkan masukan menu yang anda inginkan : ')
            if menu_del_mp == '1':
                hapus_mp = input('Silahkan Masukan ID Pegawai yang ingin anda hapus : ').upper()
                if hapus_mp.upper() in data_manpower :
                    task8 = input(f"Apakah anda sudah yakin akan menghapus {hapus_mp}? (Ya/Tidak) ")
                    if task8.lower() == 'ya':
                        del data_manpower[hapus_mp]
                        tampilkan_man_power()
                    elif task8.lower() == 'tidak':
                        hapus_pekerja()
                    else:
                        print ('Harap Masukan Input yang benar')
                        time.sleep (1)
                        tampilkan_man_power()
                else :
                    print(f"Pegawai dengan ID {hapus_mp} tidak terdaftar di Tambang Riang Gembira Resources")
                    time.sleep(1)
                    hapus_pekerja()
            
            elif menu_del_mp == '2':
                print ('Apakah anda yakin menghapus semua data pegawai? (Ya/Tidak)')
                hapus_mp_all = input('')
                if hapus_mp_all.lower() == 'ya':
                    data_manpower.clear()
                    print ('Data Pegawai Berhasil dihapus')
                    tampilkan_man_power()
                    break
                elif hapus_mp_all.lower() == 'tidak':
                    print('Input Anda Berhasil Dibatalkan')
                    time.sleep(2)
                    break
                else :
                    print('Anda Memasukan Input Yang Salah')
                    continue    
            elif menu_del_mp == '3':
                return
            else :
                print('Anda Memasukan Input Yang Salah')
                continue


def usia_pegawai(item):
    '''
    Fungsi ini berguna untuk mengakses Value dari key 'Usia' ketika dipanggil
    '''
    return item[1]['Usia']

def filter_pekerja():
    '''
    Fungsi ini berisi semua sub-menu yang bertujuan untuk
    melakukan sortir dan filter
    '''
    if not data_manpower :
        print ('Tidak ada data pegawai, harap tambahkan pegawai dulu')
        time.sleep(1)
    else :       
        filtered_data =[]
        while True:
            print(f"{'-'*90}")
            print('\nFilter Pegawai:')
            print(f"{'.'*90}")
            print('1. Tampilkan Pegawai dengan ID Pegawai')
            print('2. Urutkan Pegawai Berdasarkan Usia')
            print('3. Tampilkan Pegawai Berdasarkan Posisi')
            print('4. Kembali ke Menu Manajemen Manpower')
            print(f"{'-'*90}")

            task3=input('Masukan Menu Filter Pegawai yang anda inginkan: ')
            if task3 =='1':
                task4 = input('\nHarap Masukan ID Pegawai yang dicari: ').upper()
                
                if task4 in data_manpower:
                    # Pada baris ini program akan memanggil seluruh value ses1uai dengan input
                    # Input berupa ID Pegawai yang menjadi key utama dari Dictionary data_mapower
                    # Value yang sudah dipanggil sesuai dengan key kemudian dijadikan list, karena program memakai Tabulate untuk menampilkan hasil

                    print(f'\nInformasi Pegawai dengan ID Pegawai: {task4} adalah:')
                    info_pegawai = data_manpower[task4]
                    rows = [[task4, info_pegawai['Nama'], info_pegawai['Posisi'], info_pegawai['Usia'],info_pegawai['Status']]]
                    print(tabulate(rows, headers=['ID Pegawai', 'Nama', 'Posisi', 'Usia','Status'], tablefmt='fancy_grid'))
                    while True :
                        # Ketika memasukan input 'Ya' maka akan kembali ke 'Menu Filter Pegawai'
                        # Ketika memasukan input 'Tidak' maka akan kembali ke 'Menu Utama'
                        # Ketika input yand dimasukan salah maka akan terus menampilkan pesan input sampai user memberikan input yang benar

                        print ('\nApakah anda ingin kembali ke Menu Filter Pegawai? (Ya/Tidak): ')
                        input_task4 = input('')
                        if  input_task4.lower() == 'ya':
                            break
                        elif input_task4.lower() == 'tidak':
                            return
                        else :
                            print ('Anda memasukan input yang salah')
                            continue

                else:
                    print("ID Pegwai tidak ditemukan.")
                
            
            elif task3 == '2':
                # Pada bagian ini program melakukan sorting data berdasarkan 'Usia'
                # Program akan melakukan sort secara Descending, ditandai dengan penggunaan 'reverse=T                                                         rue'
                # Kita menyiapkan list kosong yang nanti akan di append dengan data baru yang dipanggil dari 
                # dari data yang telah tersortir dari 'sort_usia_pegawai' agar bisa ditampilkan dengan tabulate

                sort_usia_pegawai = sorted(data_manpower.items(), key=usia_pegawai,reverse=True)
                rows2 = []
                for id_pegawai,detail_info_pegawai in sort_usia_pegawai:
                    row=[id_pegawai,detail_info_pegawai['Nama'], detail_info_pegawai['Posisi'], detail_info_pegawai['Usia'],detail_info_pegawai['Status']]
                    rows2.append(row)
                print(tabulate(rows2, headers=['ID Pegawai', 'Nama ', 'Posisi', 'Usia','Status'], tablefmt='fancy_grid'))
                while True :
                        # Ketika memasukan input 'Ya' maka akan kembali ke 'Menu Sortir'
                        # Ketika memasukan input 'Tidak' maka akan kembali ke 'Menu Utama'
                        # Ketika input yang dimasukan salah maka akan terus menampilkan pesan input sampai user memberikan input yang benar

                        print ('\nApakah anda ingin kembali ke Menu Filter Pegawai? (Ya/Tidak): ')
                        input_task2 = input('')
                        if  input_task2.lower() == 'ya':
                            break
                        elif input_task2.lower() == 'tidak':
                            return
                        else :
                            print ('Anda memasukan input yang salah')
                            continue
            
            elif task3 == '3':
                print(f"{'-'*90}")
                print ('Posisi Pegawai Riang Gembira Resources')
                print(f"{'.'*90}")
                print ('1. Wheel Loader Operator')
                print ('2. Excavator Operator')
                print ('3. Dumptruck Operator')
                print ('4. Mine Planner')
                print ('5. Checker')
                print ('6. Admin')
                print(f"{'-'*90}")
                time.sleep (1)
                posisi_pegawai=input ('\nMasukan Posisi Pegawai yang ingin dicari:')
                
                found = False
                if posisi_pegawai not in ['1','2','3','4','5','6']:
                    print ('Nomor Posisi Tidak Ditemukan')
                    print ('Harap Masukan 1, 2, 3, 4, 5 atau 6')
                    
                else :
                    detail_posisi = {
                        '1': 'Wheel Loader Operator',
                        '2': 'Excavator Operator',
                        '3': 'Dumptruck Operator',
                        '4': 'Mine Planner',
                        '5': 'Checker',
                        '6': 'Admin'
                    }

                    posisi_pegawai = detail_posisi[posisi_pegawai]
                    
                    for id_pegawai, value in data_manpower.items():
                        if posisi_pegawai == value['Posisi']:
                            bd_info = [id_pegawai]+list(value.values())
                            filtered_data.append(bd_info)
                            found = True
                    print((tabulate(filtered_data, headers=['ID Pegawai', 'Nama', 'Posisi', 'Usia','Status'], tablefmt='fancy_grid')))
                    filtered_data.clear()

                    while True :
                        # Ketika memasukan input 'Ya' maka akan kembali ke 'Menu Sortir'
                        # Ketika memasukan input 'Tidak' maka akan kembali ke 'Menu Utama'
                        # Ketika input yang dimasukan  maka akan terus menampilkan pesan input sampai user memberikan input yang benar
       
                        print ('\nApakah anda ingin kembali ke Menu Filter Pegawai? (Ya/Tidak): ')
                        input_task2 = input('')
                        if  input_task2.lower() == 'ya':
                            break
                        elif input_task2.lower() == 'tidak':
                            return
                        else :
                            print ('Anda memasukan input yang salah')
                            continue
            elif task3 == '4':
                break
            else :
                print("Masukan tidak valid. Silakan masukan nomor dari 1 hingga 4.")

def update_pekerja() :
    if not data_manpower :
        print ('Tidak ada data pegawai, harap tambahkan pegawai dulu')
        time.sleep(1)
    else :    
        while True :
            tampilkan_man_power ()
            print ('\nPilih angka yang anda inginkan :')
            print ('1. Update Status Pekerja')
            print ('2. Update Data Pekerja')
            print ('3. Kembali ke Menu Manajemen Man Power')
            task8 = input('Silahkan Masukan Pilihan Anda : ')
            if task8 == '1' :
                id_update_status = input('Silahkan Masukan ID Pegawai : ').upper()
                if id_update_status in data_manpower :
                    print ("\nSilahkan Pilih Status Pegawai :")
                    print ("1. On-duty")
                    print ("2. On-leave")
                    
                    task9 = input ("Masukan pilihan anda : ")
                    if task9 == '1':
                        status_upd = 'On-duty'
                        data_manpower[id_update_status]['Status']=status_upd
                        tampilkan_man_power()
                        print ('Apakah anda ingin melakukan update lain ?')
                        inp_upd = input('Ya atau Tidak? ').lower()
                        if inp_upd == 'ya':
                            continue
                        elif inp_upd == 'tidak' :
                            break
                        else :
                            print('Input yang anda masukan salah')
                            time.sleep(1)
                            return
                    elif task9 == '2':
                        status_upd = 'On-leave'
                        data_manpower[id_update_status]['Status']=status_upd
                        tampilkan_man_power()
                        while True :
                            print ('Apakah anda ingin melakukan update lain ?')
                            inp_upd = input('Ya atau Tidak? ').lower()
                            if inp_upd == '':
                                continue
                            elif inp_upd == 'tidak' :
                                break
                            else :
                                print('Input yang anda masukan salah')
                                time.sleep(1)
                                return
                    else :
                        print ('Silahkan Masukan Status Sesuai Pilihan yang Ada')
                        print ('Anda hanya bisa memasukan 1 atau 2')
                        time.sleep (1)
                        continue
                else :
                    print (f"\nKaryawan dengan ID : '{id_update_status}' TIDAK TERDAFTAR di Riang Gembira Resources")
                    break
                    
            elif task8 == '2' :
                id_mp = input("Silahkan Masukan ID Pegawai yang ingin anda update : ").upper()
                data_kosong_mp = {
                    'Nama':'xxxx',
                    'Posisi': 'xxxx',
                    'Usia':00,
                    'Status':'xxx'
                }
                
                if id_mp in data_manpower :
                    print (f"ID Pegawai = '{id_mp}'")
                    print ("Silahkan lengkapi data yang ingin anda perbaharui")
                    while True :
                        nama_mp = input ("Silahkan masukan Nama Pekerja : ").title()
                        if nama_mp.isalpha()==True:
                            break
                        else :
                            print ('Nama hanya bisa berupa alfabet')
                            continue
                    while True :
                        posisi_mp = input ("Silahkan masukan Posisi Pekerja : ").title()
                        if posisi_mp.isalpha()==True:
                            break
                        else :
                            print ('Posisi hanya bisa berupa alfabet')
                            continue   
                    
                    while True :
                    # loop ini berfungsi untuk memastikan bahwa user memasukan input berupa bilangan bulat
                        usia_mp = (input ("Silahkan masukan Usia Pekerja : "))
                        if usia_mp.isdigit() :
                            usia_mp = int(usia_mp)
                            break
                        else :
                            print('\nAnda hanya dapat memasukan bilang bulat yang benar benar bulat')
                            print ('Silahkan ulangi lagi')
                            return

                    while True :
                        status_mp = input("Silahkan masukan Status Pekerja : ").capitalize()
                        if status_mp.isalpha()==True:
                            break
                        else :
                            print ('Posisi hanya bisa berupa alfabet')
                            continue   

                    data_kosong_mp['Nama'] = nama_mp
                    data_kosong_mp['Posisi'] = posisi_mp
                    data_kosong_mp['Usia'] = usia_mp
                    data_kosong_mp['Status'] = status_mp

                    while True :    
                        task10 = input('Apakah anda sudah yakin dengan data baru ? (Ya/Tidak)')
                        if task10.lower() == 'ya' :
                            data_manpower[id_mp]=data_kosong_mp
                            print ('Berikut Data yang telah diperbarui')
                            tampilkan_man_power()
                            task11 = input('Apakah anda ingin mengganti yang lain? (Ya/Tidak)')
                            if task11.lower() == 'ya' :
                                update_pekerja()
                            else :
                                return
                        
                        elif task10.lower()=='tidak':
                            print('\n Update Anda Telah Dibatalka\n')
                            tampilkan_man_power()
                            break
                        else :
                            print('\nInput tidak valid. Silakan masukkan "ya" atau "tidak".')
                            update_pekerja()
                            continue
                else :
                    print (f"\nKaryawan dengan ID : '{id_mp}' TIDAK TERDAFTAR di Riang Gembira Resources")
                    time.sleep(1)
                    update_pekerja()
            
            elif task8 == '3':
                return
            
            else :
                print ('Harap Masukan ID Pegawai sesuai dengan tabel')
                time.sleep (5)
                update_pekerja()

#======================================P R O G R A M===================================================================
# Pada bagian program ini akan melakukan while loop, yang memungkinkan untuk program untuk running selama input bernilai True
# Pada sub-menu juga dilakukan while loop, karena ingin untuk program bisa terus berjalan tanpa limit tertentu
# kecuali input yang diberikan false, maka looping akan berhenti            
                        
while True:
    print(f"{'=-'*45}")
    print('SELAMAT DATANG DI RIANG GEMBIRA RESOURCES')
    print(f"{'-'*90}")
    print('Menu Utama:')
    print('1. Site Riang Gembira Resources')
    print('2. Inventaris Alat Berat')
    print('3. Manajemen Manpower')
    print('4. Exit program')
    print(f"{'=-'*45}")

    task = input('Masukan angka Menu yang ingin dijalankan :')

    if task == '1' :
        while True:
            print(f"\n{'+'*90}")
            print('SITE RIANG GEMBIRA RESOURCES')
            print('List Menu:')
            print(f"{'-'*90}")
            print('1. Tampilkan Seluruh Site')
            print('2. Tampilkan Site Tertentu')
            print('3. Update Data Site')
            print('4. Menu Utama')
            print(f"{'+'*90}")
            task1 = input('Masukan Menu yang ingin dijalankan :')

            if task1 == '1':
                tampilkan_site()
                print ('\nSilahkan Masukan Angka 1 atau 2: ')
                print ('1. Kembali ke Menu Site Riang Gembira Resource')
                print ('2. Menu Utama')
                task2 = input('Masukan Menu yang ingin dijalankan :')
                if task2 == '1':
                    continue
                elif task2 == '2':
                    break
                else :
                    print ('Input tidak valid, harap masukan input yang benar')
                    continue            
            elif task1 == '2' :
                tampilkan_site_tertentu()
            
            elif task1 == '3':    
                update_data_site()
            
            elif task1 == '4':
                break
            
            else :
                print ('HARAP MASUKAN INPUT YANG BENAR')
                print ('Anda dapat melakukan input lagi setelah 3 detik')
                time.sleep(3)
                continue
            
    elif task == '2' :
        while True:
            print(f"\n{'+'*90}")
            print('INVENTARIS ALAT BERAT')
            print('List Menu:')
            print(f"{'-'*90}")
            print('1. Tampilkan Seluruh Alat Berat')
            print('2. Tambahkan Alat Berat')
            print('3. Update Alat Berat')
            print('4. Hapus Alat Berat')
            print('5. Menu Utama')
            print(f"{'+'*90}")
            task3 = input('Masukan Menu yang ingin dijalankan :')

            if task3 == '1':
                tampilkan_alat_berat()
            
            elif task3 == '2':
                tambahkan_alat_berat()
            
            elif task3 == '3':
                update_alat_berat()
            
            elif task3 == '4':
                hapus_alat_berat()

            else :
                break
            
    elif task == '3' :
        while True:
            print(f"\n{'+'*90}")
            print('MANAJEMEN MANPOWER')
            print('List Menu:')
            print(f"{'-'*90}")
            print('1. Tampilkan Seluruh Pekerja')
            print('2. Update Status Pekerja')
            print('3. Filter Pekerja')
            print('4. Tambah Pekerja')
            print('5. Hapus Pekerja')
            print('6. Menu Utama')
            print(f"{'+'*90}")
            task3 = input('Masukan Menu yang ingin dijalankan :')

            if task3 == '1':
                tampilkan_man_power()
            
            elif task3 == '2':
                update_pekerja()
            
            elif task3 == '3':
                filter_pekerja()
            
            elif task3 == '4':
                tambahkan_pekerja()
            
            elif task3 == '5':
                hapus_pekerja()
            
            elif task3 == '6':
                break

            else :
                print ('Anda memasukan input yang salah')
                time.sleep(1)
                continue
    
    elif task == '4' :
        print (f"\n{' ':15}TERIMAKASIH")
        print (f"{' ':12}Sampai Bertemu lagi\n")
        print (f"{' ':13}Have a Nice Day ^^")
        break
    else :
        print("HARAP MASUKAN INPUT YANG BENAR")
        time.sleep (2)
    


    








            



        
    
    
    
    

