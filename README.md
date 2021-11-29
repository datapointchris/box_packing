Full-text search works out of the box:
```sql
create virtual table books_fts
using fts5(title, author, publisher);

insert into books_fts
select title, author, publisher from books;

select
  author,
  substr(title, 1, 30) as title,
  substr(publisher, 1, 10) as publisher
from books_fts
where books_fts match 'ann'
limit 5;
```