# SQLInspector Middleware for Django

[![Version](https://img.shields.io/badge/version-0.5-brightgreen)](https://pypi.org/project/sqlinspector/)

## Description

SQLInspector is a Django middleware that provides developers with insights into the SQL queries generated by Django's ORM. By integrating SQLInspector into your Django project, you can:

- Monitor and capture all SQL queries in real-time.
- Analyze the efficiency and performance of database operations.
- Understand the underlying SQL interactions even when using Django's ORM for database operations.
- Ensure that the application's database interactions are optimized for scalability and performance.

SQLInspector acts as a valuable tool for developers aiming to ensure the optimal performance of their Django applications, especially when dealing with complex database operations and multiple related models.

## Features

- **Monitor and Log SQL Queries:** Every SQL query made by your Django application is recorded.
  
- **Performance Optimization:** Get insights into the most efficient ways of fetching data from your database and optimizing your queries accordingly.
  
- **Diagnostic Aid:** Helps in diagnosing non-performant SQL queries and offers insights into potential optimizations.
  
- **Ease of Integration:** Being a middleware, it seamlessly integrates into any Django project.

## Installation

To install the SQLInspector middleware via pip, use:

```bash
pip install -i https://test.pypi.org/simple/ sql-inspector
```

## How to Use

Integrating SQLInspector into your Django project is straightforward. Once you've installed the middleware, the next steps ensure its proper functioning:

### Integration Steps:

1. **Add to MIDDLEWARE in settings.py:**

    After you have installed the SQLInspector via pip, you need to add it to your Django application's `MIDDLEWARE` settings. 

    Open your `settings.py` file and locate the `MIDDLEWARE` section. Add the following line:

    ```python
    'sql-inspector.middleware.querychecker_middleware',
    ```

    Ensure you add it in the appropriate order. For instance, if you have other middleware that processes database queries, you might want to adjust the order to ensure SQLInspector captures the raw queries before any other processing takes place.

2. **Monitor Your Queries:**

    With SQLInspector now integrated, you can monitor, analyze, and optimize your SQL queries in real-time as your application runs.

Remember, SQLInspector doesn't just capture the queries; it provides valuable insights into their performance and efficiency. By understanding the underlying SQL, you can make the necessary adjustments to your Django ORM operations, ensuring optimal database interactions.

Happy optimizing!

## Contributor:

### Aryaman Awasthi

- **GitHub:** [aryaman-awasthi](https://github.com/aryaman-awasthi)
- **LinkedIn:** [Aryaman Awasthi](https://www.linkedin.com/in/aryaman-awasthi/)

