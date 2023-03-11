# Ret2csu
* ![image](https://user-images.githubusercontent.com/93699926/224463394-c7d80713-b610-4cd0-bcc4-6c7de60579f4.png)

* doc tieu de cua challenge ta cung cung co the thay ranh challenge nay giong voi callme
* ta can goi ham ret2win voi cac argument=0xdeadbeefdeadbeef, 0xcafebabecafebabe, 0xd00df00dd00df00d lan luot
*  nhung kho hon call me o cho tim mai trong cac gadget cau file binary chung ta khong he nao tim duoc gadget nao de dua rdx=0xd00df00dd00df00d

* sau khi tim hieu thi chung ta se su dung ky thuat ret to csu 
* kiem tra ham __libc_csu_init
* ![image](https://user-images.githubusercontent.com/93699926/224463494-0c1c3b09-278c-4dbf-a7ea-18aaaa966691.png)
* dac biet quan tam tu phan nay tro di:
* ![image](https://user-images.githubusercontent.com/93699926/224463600-8d7f193b-0999-4c09-8628-bc56245e0a50.png)
* ta co the thay rang no se dua gia tri cua r15 vo rdx , r14 vo rsi ,ta chi can tim kiem them gadget pop rdi nua thi co the thoa man 3 arg cua ret2win
* nhung o dong 73 ta thay chuong trinh call   QWORD PTR [r12+rbx*8] 
* vay nen ta can thiet lap r12+rbx*8 = (dia chi nao do) -> (gadget nao do) khong lam anh huong toi rdi,rsi,rdx
* sau khi tim kiem thi ta co the thay ham _fini kha la phu hop voi muc dich cua chung ta:
* ![image](https://user-images.githubusercontent.com/93699926/224463884-08320a34-b6f0-4fa2-a209-a0d191ce3f5e.png)
* tiep do ta can tim kiem dia chi chua ham _fini:
 * ![image](https://user-images.githubusercontent.com/93699926/224463951-809db177-1edc-499f-894f-84f4b2cf3c4a.png)

* ta se su dung dia chi 0x400e48 ==> rbx =0 rbp=0x1(can set 2 thanh nay nhu vay de no pass qua lan so sanh tiep theo) va r12=0x400e48
* sau do thi r12+rbx*8 : 0x400e48 -> _fini



* put it all together ta co script 
* ![image](https://user-images.githubusercontent.com/93699926/224464203-57c50bdf-15e9-4679-a28d-62c649657e4d.png)
* chay script ta duoc flag:
* ![image](https://user-images.githubusercontent.com/93699926/224464246-320d1f9b-a8a4-4101-9ab9-8f538337ca24.png)

