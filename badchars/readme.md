# badchars

* chay chuong trinh ta thay cac char 'x', 'g', 'a', '.' co ve nhu khong dung duoc
* ![image](https://user-images.githubusercontent.com/93699926/224469610-ee71c765-ce27-4f40-b8a4-3f8e9550ac00.png)
* kiem tra cac che do bao ve cua chuong trinh
* ![image](https://user-images.githubusercontent.com/93699926/224469713-2cc7046f-91d0-48c8-ae6f-7cf63171c86f.png)
* kiem tra file thuc thi binary thi binary ta thay chuong trinh van co loi bof o pwnme
* dong thoi ta tim thay ham print_file() o trong usefulFunction
* ![image](https://user-images.githubusercontent.com/93699926/224469797-59271cca-8560-4197-94ae-96afc4063532.png)
![image](https://user-images.githubusercontent.com/93699926/224469843-536daf6b-a4bb-4960-8157-06e3207caeb3.png)
* su dung gdb ta tim duoc dia chi plt cua print_file

* Vay de khai thac chuong trinh ta can overflow return address cua pwnme 
* rdi can phai bang strings "flag.txt"
* sau do goi ham print_file

* sau khi viet scipt y tuong tren thi  cac ky tu da duoc canh bao ban dau da bien ky tu gi do

* vay  al chung ta can mot cach tiep can khac 
* sau khi kiem tra cac gadgets ben trong file thuc thi binary thi ta se khai thac theo huong sau
* ![image](https://user-images.githubusercontent.com/93699926/224470106-646df4f7-f3a3-42a3-9a94-a58f0e2a322e.png)
*  gadget phia tren se thuc hien phep tinh XOR  byte cua ptr r15 voi r14
*  nen ta se pop r15,(mot dia chi nao do trong binary cho phep read and write) dia chi do se co gia tri "flag.txt" sau khi XOR voi r14
*  ta can them mot gadgets nua de co the dua gia tri ("flag.txt" XOR r14) vao dia chi binary co quyen read and write
*   ![image](https://user-images.githubusercontent.com/93699926/224470477-ceca9eb3-fccc-4590-ad22-ea018efa742b.png)
* gadgets nay vo cung phu hop
* gio ta can tin dia chi co the ghi : kiem tra dia chi 0x601500 nam trong file binary co quyen read and write
* ![image](https://user-images.githubusercontent.com/93699926/224470591-07437c80-827f-4902-b354-7c17eab9f084.png)
* dia chi nay hien =0 nen ta co the ghi vo do ma khong so gay anh huong gi den chuong trinh

* ket luan:
* pop r13,dia chi binary co quyen read and write :0x601500
* pop r12 , ("flag.txt" XOR r14)
* mov ptr[r13],r12 ==> r13: 0x601500-> "flag.txt" XOR r14
* pop r15,dia chi binary co quyen read and write :0x601500
* pop r14,0x2  
* sau do ta se XOR tung byte mot cua ptr[r15] voi r14


* put it all together ta co script:
* ![image](https://user-images.githubusercontent.com/93699926/224470843-6671ae91-dbe9-40ce-9fb7-a2110f7e2656.png)

* chay script ta co:
* ![image](https://user-images.githubusercontent.com/93699926/224470858-5b696994-d511-41c9-9a47-b3c3a18a643b.png)

