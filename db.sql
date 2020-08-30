create table movie
(
id BIGINT PRIMARY KEY, 
popularity DOUBLE,
vote_count BIGINT,
video BOOLEAN,
poster_path LONGTEXT DEFAULT null,
adult BOOLEAN,
backdrop_path LONGTEXT DEFAULT null,
original_language VARCHAR(2),
original_title LONGTEXT,
genre_ids LONGTEXT,
title LONGTEXT,
vote_average INT,
overview LONGTEXT,
release_date DATE
);



mariadb current 10.1

json needed mariadb 10.2