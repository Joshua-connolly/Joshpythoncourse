show databases;
use passenger_data;
drop table Passenger_Info;
CREATE TABLE Passenger_Info (
Passenger_id int , 	
Dest varchar(15),
Name_id Varchar(15) not null,
Assistance_Type varchar (4) not null, 
primary Key (Passenger_id),
Unique (Name_id));
explain Passenger_Info;
insert into Passenger_Info (Passenger_id, Dest,Name_id,Assistance_Type)
values ('000001','CORFU','Debbie Smith','WCHS')
,('000002','DUBAI','Richard Knowles','WCHS')
,('000003','POLAND','Sam Smith','WCHS')
,('000004','TENERIFE','Peter Grayam','WCHR')
,('000005','HOLLAND','Liz Pike','WCHR')
,('000006','SCOTLAND','Stan Poles','WCHC')
,('000007','ISTANBUL','Immi sanchez','WCHS')
,('000008','PAKISTAN','Luke Turner','WCHR')
,('000009','SPAIN','Ricky Gray','WCHS')
,('000010','DUBLIN','Timmy Turner','WCHR');

explain Passenger_Info;
Select * from Passenger_Info;

Update Passenger_Info
set Assistance_Type = 'DPNA'
where Passenger_id = '000001';
select * from Passenger_Info;

delete from Passenger_Info 
where Name_id = 'Ricky Gray';
select * from Passenger_Info;

Select Name_id from Passenger_Info;

Select Passenger_id, Name_Id From Passenger_Info;

Select * From Passenger_Info Order by Passenger_id;




