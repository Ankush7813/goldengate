---- create table hobbies
create table hobbies
(
hobbie_id number,
h_name varchar2(20),
constraint pk_hkid primary key (hobbie_id)
);
---- create table users
create table users
(id number  ,
U_name varchar2(20),
email_addr varchar(20),
constraint pk_uid primary key (id));

--- create table userhobbies
create table userhobbies
(u_id number,
h_id number ,
constraint fk_hfid foreign key (h_id) REFERENCES hobbies(hobbie_id),
constraint fk_ufid foreign key (u_id) REFERENCES users(id));

--- create user id seqenence
create sequence user_seq
MINVALUE 1
start with 1 
increment by 1
;
--- create Hobbie id seqenence
create sequence hobbie_seq
MINVALUE 10
start with 10 
increment by 10
;

-----procedure to insert data in above two main table and junction table
create or replace procedure Userhobbie_insert
( Uname in users.U_name%type,
 Hobbie in Hobbies.H_name%type
 email in users.email_addr%type)   --- parameters ## can be change according to length of table values
 is 
 UID users.id%type;
 HID hobbies.hobbie_id%type;
 begin 
 begin 
 select U.id
 into UID
 from users U 
 where U.email_addr =UPPER(email);
 exception 
 when no_data_found then 
 insert into users values (user_seq.nextval,Upper(Uname),UPPER(email))  -- insert data in users
 returning id into UID;
 end;
 begin
 select H.hobbie_id
 into HID 
 from hobbies H
 where H.H_name=UPPER(Hobbie);
 exception 
 when no_data_found then 
 insert into hobbies values (hobbie_seq.nextval,UPPER(Hobbie))  --- insert data in Hobbies
 returning Hobbie_id into HID;
 end;
 insert into userhobbies ---- insert data in userhobbies
 values(UID, HID);
 end;

--- run procedure
exec Userhobbie_insert ('Uname','Hobbie','email');---Hobbie as hobbies name value , Uname asuser name 
 
 -- to retrieve data for user having multiple same hobbie id

select 
U.u_name,U.id,U.email_addr,
H.h_name,H.hobbie_id 
from 
users U, 
userhobbies UH ,
hobbies H 
where 
U.id=UH.U_id 
and H.hobbie_id=UH.H_id 
and UH.H_id in (select H_id from userhobbies group by H_id having count(H_id) >1); --- to retrieve hobbies common in two users

select 
U.u_name,U.id,U.email_Addr,
H.h_name,H.hobbie_id 
from 
users U, 
userhobbies UH ,
hobbies H 
where 
U.id=UH.U_id 
and H.hobbie_id=UH.H_id 
and UH.H_id in (select H_id from userhobbies group by H_id having count(H_id) =1);  ---- to retrieve users having only one hobbie

select 
U.u_name,U.id,U.email_Addr,
H.h_name,H.hobbie_id 
from 
users U, 
userhobbies UH ,
hobbies H 
where
U.id=UH.U_id 
and H.hobbie_id=UH.H_id 
and UH.H_id in (select H_id from userhobbies ); --- to retrieve hobbies all users;



select 
U.u_name,U.id,U.email_Addr,
H.h_name,H.hobbie_id 
from 
users U, 
userhobbies UH ,
hobbies H 
where
U.id=UH.U_id 
and H.hobbie_id=UH.H_id 
and U.user_id='';--- to retrieve particular user hobbies details
 
