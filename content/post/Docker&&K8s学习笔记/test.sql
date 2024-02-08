create database moviedb;
use moviedb;
CREATE TABLE Artist (
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
birthday DATE,
sex VARCHAR(100),
imdbnumber INT,
introduction VARCHAR(1000));

CREATE TABLE Movie (
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100),
releasedate DATE,
duration TIME,
language VARCHAR(100),
introduction VARCHAR(1000));

CREATE TABLE Participation (
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
artistid INT,
movieid INT,
rolename VARCHAR(100));

INSERT INTO Artist( name, birthday, sex, imdbnumber, introduction) VALUES("蓝萍",'1914-3-5','女','0156952',"Born to a family Li in Shandong province of China, Chiang Ching became a stage and film actress (stage name as Lanping) in Shanghai in left-wing groups and film companies in the 1930s. Her careers with the left-wing / pro-communist groups paved her way to become wife to Mao Tse-tung, leader of the Communist Party and subesequently as a political figure in the new People's Republic, where she was known as Chiang Ch'ing/Jiang Qing.");
INSERT INTO Movie( name, releasedate, duration, language, introduction) VALUES("狼山喋血记",'1936-11-01','01:10:00',"Chinese","Ostensibly a tale of a village attempting to fend off a pack of vicious wolves. In reality, the wolves were a euphemism for the Japanese army who had recently occupied Manchuria.");
INSERT INTO Participation(artistid, movieid, rolename) VALUES(1,1,"LiuSansao");

INSERT INTO Artist( name, birthday, sex, imdbnumber, introduction) VALUES("周星驰",'1962-6-22','男','0159507',"Stephen Chow was the only boy of his family, and has grown up as a Bruce Lee fan and a martial arts addict. His career started on TV, where he presented a children show ( 430 Space Shuttle(1983)) and started becoming popular. He got some supporting roles, after that, and won the Taiwanese Golden Horse award for best supporting actor.");
INSERT INTO Movie( name, releasedate, duration, language, introduction) VALUES("逃学威龙",'1991-7-18','01:40:00',"Chinese","(Cantonese with English subtitles) Classic, slapstick, all-out-ridiculous Hong Kong action-comedy delivered by the one-and-only Stephen Chow (Kung Fu Hustle, Shaolin Soccer), who plays a SWAT team leader going undercover at a high school to retrieve a stolen gun for his captain.");
INSERT INTO Participation(artistid, movieid, rolename) VALUES(2,2,"周警官");

INSERT INTO Artist( name, birthday, sex, imdbnumber, introduction) VALUES("刘德华",'1961-9-27','男','0490489',"Andy Lau Tak-wah, (born 27 September 1961) is a Hong Kong actor, singer-songwriter, presenter, and film producer. Lau has been one of Hong Kong's most commercially successful film actors since the mid-1980s, performing in more than 160 films while maintaining a successful singing career at the same time. In the 1990s, Lau was branded by the media as one of the Four Heavenly Kings of Cantopop. Lau was entered into the Guinness World Records for the Most Awards Won by a Cantopop Male Artist. By April 2000, he had already won a total unprecedented 292 awards. In 2005, Lau was awarded No.1 Box office Actor 1985-2005 of Hong Kong, yielding a total box office of HKD 1,733,275,816 for shooting 108 films in the past 20 years. In 2007, Lau was also awarded the Nielsen Box Office Star of Asia by the Nielsen Company.");
INSERT INTO Movie( name, releasedate, duration, language, introduction) VALUES("赌神",'1989-12-14','02:06:00',"Chinese","Do San (the God of gamblers) is a legendary gambler helped by his supernatural abilities. He undertakes to help a friend pay a debt by beating his friend's advisory at the card table. Despite being assigned a bodyguard Do San has a freak accident which leaves him with partial memory loss and at a mental stage of a child. The small time hustler Knife, his side-kick and his girl friend, being responsible for the accident takes care of the retarded Do San. After some time they discover that he has not lost all of his powers and takes him on a round at the local gambling halls. After being chased by both Knife's loan-shark and enemies closer to the home of Do San, a final showdown at the card tables may take place.");
INSERT INTO Participation(artistid, movieid, rolename) VALUES(3,3,"陈刀仔");

INSERT INTO Artist( name, birthday, sex, imdbnumber, introduction) VALUES("周润发",'1955-5-18','男','0000334',"Chow Yun Fat is a charismatic, athletically built and energetic Asian-born film star who first came to the attention of western audiences via his roles in the high-octane/blazing guns action films of maverick HK director John Woo.");
INSERT INTO Participation(artistid, movieid, rolename) VALUES(4,3,"高进");

INSERT INTO Artist( name, birthday, sex, imdbnumber, introduction) VALUES("沈腾	",'1979-10-23','男','7613067',"Shen Teng was born in Qiqihar, Heilongjiang, China in 1979. He attended the People's Liberation Army Academy of Art in 1999 and received a bachelor's degree in 2003. Shen was an actor for CCTV's several New Year Galas and played the leading role in the film Goodbye Mr. Loser in 2015.");
INSERT INTO Movie( name, releasedate, duration, language, introduction) VALUES("西虹市首富",'2018-7-27','01:58:00',"Chinese","A pathetic minor league Soccer Goalkeeper was given a task - to spend 1 Billion in thirty days, if successful he will get 30 Billion. However, he's not allowed to tell anyone about the task and he must not own any valuables by end of it.");
INSERT INTO Participation(artistid, movieid, rolename) VALUES(5,4,"王多鱼");

ALTER TABLE moviedb.Movie ADD rating DECIMAL(3,1);

UPDATE moviedb.Movie
SET rating=6.4
WHERE id=1;

UPDATE moviedb.Movie
SET rating=6.2
WHERE id=2;

UPDATE moviedb.Movie
SET rating=8.3
WHERE id=3;

UPDATE moviedb.Movie
SET rating=7.2
WHERE id=4;



