# Django Analytics

Django analytics is an application that allows the website manager to store all the identifiers for his different analytics tools in a database in order to be used.

## Configuration

If you have created a custom admin site for your application, create `ADMIN_SITE` variable in your settings files pointing towards the admin site variable:

```python
# settings.py

ADMIN_SITE = 'accounts.sites'
```
