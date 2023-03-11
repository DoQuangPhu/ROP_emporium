#Split
* doc de ta thay duoc rang chuong trinh goi ham system va string "/bin/cat flag.txt" o dau do trong file binary

* Chay lenh strings de kiem tra thu 
* ![image](https://user-images.githubusercontent.com/93699926/224461167-4503c592-0b5a-4be4-8c81-98d480c76e4f.png)

* kiem tra cac che do bao ve cua file binary ta thay duoc :
* ![image](https://user-images.githubusercontent.com/93699926/224461222-c1099092-7b30-449d-bf08-c8415b2ec44d.png)
* che do pie khong bat tuc la ta co the xac dinh duoc dia chi cua ham system va string "/bin/cat flag.txt"
* kiem tra file binary bang ida :
* ![image](https://user-images.githubusercontent.com/93699926/224461404-e412ba34-3b46-4d41-aac5-76066a30562d.png)
* ta co the thay rang pwnme co loi buffer overfow 
* su dung cac ky nang co ban de tinh khoang cach tu phan input den saved return address ta tinh duoc offset=0x28 byte



* -exploit plan :
*   dau tien ta can lam day buffer voi 0x28 byte
*   sau do ta can load thanh rdi gia tri =string "/bin/cat flag.txt", su dung ropper ta co the kiem duoc gadget do:
* ![image](https://user-images.githubusercontent.com/93699926/224461613-3d2a4e7c-61f0-4ee9-af23-11f833f29d89.png)

*   bay gio ta can di kiem dia chi cua string  "/bin/cat flag.txt" va dia chi cau ham system 
*   ![image](https://user-images.githubusercontent.com/93699926/224461706-a5b7d223-6954-4cce-9e9e-e8812cda1431.png)

*   ![image](https://user-images.githubusercontent.com/93699926/224461721-378608aa-a362-4b5d-be13-0091c8fdcfaf.png)
 
 
* put it alltogether ta co script khai thac nhu sau
* ![image](https://user-images.githubusercontent.com/93699926/224461843-fd476194-c976-4e5e-813c-3ca0d30a4214.png)
* sau khi chay chuong trinh:
* ![image](https://user-images.githubusercontent.com/93699926/224461873-3bcbe8e1-4be4-4e7f-874f-ba0dbda2a22c.png)
