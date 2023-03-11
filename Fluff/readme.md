# Fluff

* Kiem tra cac che do bao ve cua file binary
* ![image](https://user-images.githubusercontent.com/93699926/224471730-c09c06b0-7e0d-438e-9af7-90106fa21aed.png)
* kiem tra file binary thi ta thay file tiep tuc co loi bof o ham pwnme
* kiem tra usefulFuntion ta thay no goi ham print_file => vi pie khong bat nen ta co duoc dia chi plt cua print_file
* ![image](https://user-images.githubusercontent.com/93699926/224471780-2b95b092-50cd-4428-adf3-bb916c6bbc13.png)


* cac gadget su dung khai thac chuong trinh nhu sau
* ![image](https://user-images.githubusercontent.com/93699926/224471883-5a4c027c-2a2d-4890-a21e-c839435911c5.png)

* o gadget thu 3 ta thay sau mov ptr[rbp +0x48],edx; mov ebp, esp; call 0x400500 (day la dia chi plt pwnme)
* ![image](https://user-images.githubusercontent.com/93699926/224472007-e9e5b4e8-db18-49fc-ae0e-b05585172cdd.png)

* dung gadget tren nhu sau
* ta se chia "flag.txt" thanh hai doan
* o lan gui dau ta se pop edx ".txt"
* sau do mov ptr[rbp +0x48+4],edx
* chuong sau do chuong trinh se quy tro lai ham pwnme va ta co lan nhap thu 2 (call 0x400500)
* o lan gui thu 2 ta se pop edx ,"flag"
* sau do mov ptr[rbp +0x48+4],edx
* sau do pop rdi, dia chi rbp+0x48->"flag.txt"
* goi ham print_file
* va lay flag

* bay gio ta can tim dia chi de co the ghi string "flag.txt" vo
* dung cau lenh vmmap kiem tra :
* ![image](https://user-images.githubusercontent.com/93699926/224472364-93c7caf9-e4e2-4431-aad9-3406e31bbe1f.png)
* ta thay dia chi 0x601500 nam trong vung read and write rat phu hop
* de co the ghi "flag.txt"vo 0x601500 thi rbp phai =0x601500-0x48

* put it all together ta duoc script khai thac nhu sau:
* ![image](https://user-images.githubusercontent.com/93699926/224472440-501a0163-4676-42b0-8181-734a5bb124a8.png)

* chay script ta thay:
* ![image](https://user-images.githubusercontent.com/93699926/224472471-b8616d18-6c6d-437f-b8e3-5834e6e230bf.png)
