## Write 4

* sau khi kiem tra chuong trinh nhu cac challenge truoc thi  lan nay chung ta se khong string "/bin/cat flag.txt" hay system nao ca
* nhung file binary lai cung cap cho chung ta mot filelibwrite4.so va ben trong co mot ham dac biet laf ham print_file()
* kiem tra ham usefulFunction ta co the lay duoc dia chi plt cua ham print_file:
* ![image](https://user-images.githubusercontent.com/93699926/224462210-abc43668-52a0-456a-9ba8-3a9ba364137a.png)
* bay gio chung ta can tim kiem nhung gadget phu hop de thanh ghi rdi chua dia chi chi den chuoi "flag.txt"


* exploit plan nhu sau:
*   1. ta se tim kiem mot dia chi tren trong file thuc thi de co the gi chuoi "flag.txt"
*   2. pop dia chi do vo thanh ghi rdi 
*   3. goi ham print_file
*   ![image](https://user-images.githubusercontent.com/93699926/224462442-5118820f-4d8e-4ba8-b62e-e5a053bea80a.png)
* kiem tra dia chi 0x601500 nam trong vung duoc cap quyen read and write
*   ![image](https://user-images.githubusercontent.com/93699926/224462476-85b04e2f-7bf9-4886-8fbe-f387930c9fc7.png)
* Tiep theo la tim kiem cac gadget phu hop (su dung ropper)
*   ![image](https://user-images.githubusercontent.com/93699926/224462541-e7749509-30ad-4108-b3df-5d21030277c7.png)
*   ![image](https://user-images.githubusercontent.com/93699926/224462570-a76bb6ea-5e61-4b7c-a4d4-aef7cb8be62f.png)
* ==> tong ket :
* +) ta se pop r14 dia chi 0x601500 va r15 gia tri hex cua string "flag.txt"
* +) sau do ta se dua value cua r15="flag.txt" vo dia chi r14=0x601500 ==> r14 : 0x601500 -> "flag.txt"
* +)  cuoi cung la pop dia chi  0x601500 vo thanh ghi rdi
* +) cuoi cung la goi ham print_file()

* Script:
*   ![image](https://user-images.githubusercontent.com/93699926/224462943-a6fc22db-9fec-417a-9d30-b2c6627eb704.png)


* chay script:
* ![image](https://user-images.githubusercontent.com/93699926/224462842-48267f73-b48c-4850-a266-0d9df858f53e.png)
