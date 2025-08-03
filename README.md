## Implementation Notes

- In-memory storage with thread locks to ensure concurrency.
- Short codes are generated as random 6-character alphanumerics.
- URL validation uses regex.
- No persistent storage (as instructed).
- 5 tests covering:
    - Valid shortening
    - Invalid URL
    - Redirect working
    - Redirect 404
    - Analytics data
