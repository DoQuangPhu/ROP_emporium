# Pivot

* kiem tra cac che do bao ve :
* ![image](https://user-images.githubusercontent.com/93699926/224468183-2240e7d8-bffc-4568-8994-bb83d0dfbbe3.png)

* kiem tra file binary thi challenge nay van co loi bof o ham pwnme 
* ![image](https://user-images.githubusercontent.com/93699926/224468248-54f70fec-9563-4197-b238-e74db6a06ca9.png)
* sau khi doc huong dan va kiem tra file libpivot.so
* ![image](https://user-images.githubusercontent.com/93699926/224468356-338452cc-6a88-4480-96f2-c9245aba3056.png)

* ta tim duoc ham ret2win o offset 0xa81 va foothold_function o offset 0x96a

* Chay thu chuong trinh thi ta thay co mot dia chi duoc in ra man hinh
* kiem tra source code  bang ida :
* ![image](https://user-images.githubusercontent.com/93699926/224468508-9834d82a-ded9-4a7b-83db-d2885a2d034d.png)
* dia chi duoc in ra man hinh chinh la dia chi cho lan nhap dau tien cua chuong trinh duoc khai bao trong ham main truoc do
* ta tiep tuc phat hien loi bof khi ma o lan nhap thu 2 t duoc nhap toi tan 64 byte vao bien s duoc khai bao 32 byte ban dau
* 
* 
* exploit plan:
* 1) ta se su dung lan nhap thu 2 de ghi de return adrress va dieu khien luong thuc thi cua chuong trinh 
* 2) nhung vi nhung vi o lan nhap thu 2 ta chi duoc nhap 64byte tuc la ta co chi co the su dung (64-0x28)/8 =3 gadgets de dieu khien chuong trinh
* 3) ta se tim cach pivot luong thuc thi chuong trinh stack cua lan nhap 1 qua dia chi cua lan nhap thu 1 da duoc leak ra
* 4)  sau khi kiem tra gadget cac gadget co the su dung thi y tuong khai thac chuong trinh nhu sau:
*         +)ta goi dia chi plt cua foothold_function de dia chi cua ham thuc thi foothold_funtion duoc load len bang got
*         +) sau do ta pop rax ,(dia chi got cua foothold_funtion).  rax : got.foothold_function --> dia chi thuc thi cua foothold_function
*         +) sau do ta se load gia tri cua ptr rax vo chinh rax . rax: dia chi thuc thi cua foothold_function
*         +) ta co the tinh duoc khoang cach giua foothold_function va ret2win =0xa81-0x96a
*         +) call rax
* --- Cac gadget can thiet de thuc thi y tuong la :
* ![image](https://user-images.githubusercontent.com/93699926/224469281-7ebb617a-137f-40d3-9b40-025566e4b34e.png)
* dia chi plt cua foothold_Function
* ![image](https://user-images.githubusercontent.com/93699926/224469329-cf0bd4c0-a506-49e0-a073-6a7fafb8cbbf.png)
* su dung gadget xchg rax,rsp de pivot
* ![image](https://user-images.githubusercontent.com/93699926/224469377-cfda8cc3-a0ea-4b60-bad1-21cb0eb1015d.png)
* ![image](https://user-images.githubusercontent.com/93699926/224469396-831cc388-7bfd-4559-90dc-5184c441d209.png)


* put it all together ta co script khai thac :
* ![image](https://user-images.githubusercontent.com/93699926/224469464-9430f022-d0b1-4db6-9839-6e208f059afd.png)
* chay script khai thac:
* ![image](https://user-images.githubusercontent.com/93699926/224469514-65b7e875-8816-42ee-a538-14c46c6ee2b7.png)

