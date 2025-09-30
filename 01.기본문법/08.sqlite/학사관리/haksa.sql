/*라인별 실행*/
/*학과*/
/*테이블 생성*/
create table dept(
       code integer primary key autoincrement,
       name char(200));
       
/*테이블 삭제*/
drop table dept;

/*데이터 입력*/
insert into dept(name) values('컴퓨터공학과');
insert into dept(name) values('전자공학과');
insert into dept(name) values('건축공학과');
insert into dept(name) values('의상다지안학과');

/*데이터 수정*/
update dept set name = '전기전자공학과' where code=2;


/*데이터 확인*/
select * from dept;


/*학생*/
/*테이블 생성*/
create table student(
       id char(4) primary key not null,
       dept integer not null,
       name char(50) not null,
--       birthday char(6) not null
       foreign key(dept) references dept(code)
       );
       
/*테이블 삭제*/
drop table student;
       
/*데이터 입력*/
insert into student(id, dept, name) 
values('2501', 1, '홍길동');
insert into student(id, dept, name) 
values('2502', 1, '심청이');
insert into student(id, dept, name) 
values('2503', 2, '강감찬');
insert into student(id, dept, name) 
values('2504', 3, '홍길동');

/*데이터 확인*/
select * from student;

/*테이블 조인-학과코드 내용 확인*별명공백 후or as붙인 뒤 -s.*/
select s.*, dept.name as dname from student s, dept
where s.dept = dept.code; 
--각테이블 코드 일치 확인

select s.*, d.name as dname from student as s, dept as d where s.dept=d.code;

/*원하는 정보 집합으로 뷰 생성*/
create view vstudent as
       select s.*, d.name as dname from student as s, dept as d where s.dept=d.code;

select * from vstudent;

/*max값+1*학번 증가*/
select max(id)+1 from student;

/*테이블 셋내용 수정* ex: 학번의 학과 수정*/
update student set dept = 4 where id ='2506';