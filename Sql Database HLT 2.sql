use passenger_data;
drop table Passenger_Contact;
CREATE TABLE Passenger_Contact (
Passenger_id int , 	
Email varchar(25),
Name_id Varchar(15) not null,
Phone_Number integer , 
primary Key (Passenger_id),
Unique (Name_id));
explain Passenger_Contact;
insert into Passenger_Contact (Passenger_id, Email,Name_id,Phone_Number)
values ('000001','d.smith@gmail.com','Debbie Smith','0774564')
,('000002','R.Knowles@ymail.com','Richard Knowles','077457')
,('000003','SSmith1432@yahoo.co.uk','Sam Smith','077457')
,('000004','Petgra@gmail.com','Peter Grayam','07745')
,('000005','Lizzy123@mail.com','Liz Pike','0774')
,('000006','Spoles@googlemail.com','Stan Poles','07745')
,('000007','Isanchez@googlemail.com','Immi sanchez','077457')
,('000008','LT@mail.com','Luke Turner','077457')
,('000009','Ricky.gray@gmail.com','Ricky Gray','0774571')
,('000010','TNT@ymail.com','Timmy Turner','077457');
explain Passenger_Contact;
Select * from Passenger_Contact;

SELECT  passenger_info.Passenger_Id,passenger_info.Name_id, passenger_info.Dest, passenger_info.Assistance_Type, passenger_contact.Email,passenger_contact.Phone_Number
FROM Passenger_Info
JOIN passenger_contact
ON Passenger_Info.Passenger_id = passenger_contact.Passenger_id;

Select * from passenger_info
where Assistance_Type='WCHS';

SELECT  passenger_info.Passenger_Id,passenger_info.Name_id, passenger_info.Dest, passenger_info.Assistance_Type, passenger_contact.Email,passenger_contact.Phone_Number
FROM Passenger_Info
JOIN passenger_contact
ON Passenger_Info.Passenger_id = passenger_contact.Passenger_id
where Passenger_Info.Dest = 'Scotland' and Assistance_Type = 'WCHC' ; 

SELECT  passenger_info.Passenger_Id,passenger_info.Name_id, passenger_info.Dest, passenger_info.Assistance_Type, passenger_contact.Email,passenger_contact.Phone_Number
FROM Passenger_Info
JOIN passenger_contact
ON Passenger_Info.Passenger_id = passenger_contact.Passenger_id
where Passenger_Info.passenger_id between 4 and 8;