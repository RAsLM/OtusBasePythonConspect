DROP TABLE IF EXISTS users, author, articles;


CREATE TABLE users(
  id SERIAL UNIQUE PRIMARY KEY,
  username VARCHAR NOT NULL,
  email VARCHAR UNIQUE
);

INSERT INTO users VALUES (DEFAULT ,'rus', NULL);
INSERT INTO users VALUES (DEFAULT ,'test', NULL);

CREATE TABLE author(
    id SERIAL UNIQUE PRIMARY KEY,
    nickname VARCHAR UNIQUE NOT NULL
);

INSERT INTO author VALUES (DEFAULT ,'Dos');
INSERT INTO author VALUES (DEFAULT ,'Tres');
INSERT INTO author VALUES (DEFAULT ,'rus');
INSERT INTO author VALUES (DEFAULT ,'test');

CREATE TABLE articles(
    id SERIAL UNIQUE PRIMARY KEY,
    title VARCHAR NOT NULL,
    body TEXT NOT NULL,
    author_id INT NOT NULL,
    CONSTRAINT fk_author
        FOREIGN KEY (author_id)
            REFERENCES author(id)
);

INSERT INTO articles VALUES (DEFAULT ,'New1', 'some1', 2);
INSERT INTO articles VALUES (DEFAULT ,'new2', 'some2', 1);
INSERT INTO articles VALUES (DEFAULT ,'New3', 'some3', 3);
INSERT INTO articles VALUES (DEFAULT ,'New4', 'some4', 1);

SELECT au.id as author_id, au.nickname, ar.id as article_id, ar.title
       FROM author au
JOIN articles ar ON au.id = ar.author_id
WHERE au.nickname = 'Dos';

/*
subquery
*/
SELECT id, username FROM users
    WHERE id = (SELECT MAX(Id) FROM users);

/*
JSONB
*/

SELECT * FROM articles
WHERE articles.raw_data ->> 'english' = 'WAR and Peace';

SELECT * from articles
WHERE  articles.raw_data IS NOT NULL OR NOT (articles.raw_data ? 'english');