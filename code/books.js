import React, { useState, useEffect } from "react";

function Books() {
  const [books, setBooks] = useState([]);

  useEffect(() => {
    fetch("/api/books")
      .then((res) => res.json())
      .then((data) => setBooks(data));
  }, []);

  return (
    <div>
      <h1>Books</h1>
      <ul>
        {books.map((book) => (
          <li key={book.id}>
            <a href={`/books/${book.id}`}>{book.title}</a>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Books;