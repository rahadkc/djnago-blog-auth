# Deployment Basic

- Change `DEBUG=True` to `DEBUG=False`
- Check `staticfiles/` and `media/` file settings
    &nbsp;
  ```bash 
    STATIC_URL = 'static/'

    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
    ]
    # Location for collected static files
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 

    MEDIA_URL = 'media/'

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media') 
- if set `DEBUG=False` in **development** you have to run the project by this command 
  - **`python manage.py runserver --insecure`**
- `DEBUG=False` for **production** you have to configure **`Nginx`**
  -  We do not need to set up **`Nginx`** manually when deploying a Django app on Render.com.



- add `ALLOWED_HOSTS = []` for production ex. `ALLOWED_HOSTS = ['http://your-domain.com]`
- If app have `forms` need to set `CSRF_TRUSTED_ORIGINS` ex. 
    &nbsp;
    ```bash
    CSRF_TRUSTED_ORIGINS = [
        'http://localhost:8000', 
        'http://localhost:5085',                    
        'http://127.0.0.1:8000', 
        'http://127.0.0.1:5085', 
        'https://djnago-blog-auth.onrender.com'
    ]

#### Packages need for production

| Package      | Required? | Why?                                  |
| ------------ | --------- | ------------------------------------- |
| `gunicorn`   | ✅ Yes     | Runs your Django app in production    |
| `whitenoise` | ✅ Yes     | Serves static files (no Nginx needed) |
| `psycopg2-binary` | ✅ Yes     | postgreSql adapter  |
| `dj-database-url` | ✅ Yes     | To configure `DATABASE_URL` environment variable |



### 🏬 Render Host - deployment

- **Build command:** if all the commands are describe in production settings ex.-
  -  `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --no-input` 
  -  If you have more command include or remove as needed
- **Start command** **`python manage.py runserver 0.0.0.0:8000`** 
  - Though, Django development server (runserver) is intended for development purposes only and is not suitable for production use. It is not designed to handle multiple requests efficiently or securely.
  - When use **`DEBUG=False`** this command will not render `staticfiles/` 
  - We have to use `whitenoise` with `gunicorn`  
- **Env** check if envrionment variable available then then set it up 
- **Real-time Notification** `start command` would be different, check it carefully

### 🫙 Dump local Database `data` in a file
```bash
python3 manage.py dumpdata --output=data.json
```

### 🫙 load data from a `data.json` file to postgreSQL Database
```bash
python manage.py loaddata data.json
```
- It will replace all the existing data in postgreSQL database
- Be careful before running command, keep data backup by `python3 manage.py dumpdata --output=data_backup.json`


## To append data from `data.json` to your PostgreSQL database **without wiping existing records**, follow these steps:


### **1. Use `--append` Flag**
Run the `loaddata` command with the `--append` flag to preserve existing data:
```bash
python manage.py loaddata data.json --append
```
- This tells Django to **add new records** without deleting existing ones.
- **Note**: Ensure your JSON data has unique `pk` values to avoid conflicts.

---

### **2. Handle Primary Key Conflicts**
If your `data.json` contains duplicate primary keys (`pk`), use one of these options:

#### **Option A: Omit PKs in JSON**
Edit `data.json` to remove `"pk"` fields:
```json
[
  {
    "model": "app.model",
    "fields": {  // No "pk" here
      "name": "Example",
      ...
    }
  }
]
```
Then run:
```bash
python manage.py loaddata data.json
```
(PostgreSQL will auto-assign new PKs)

#### **Option B: Reset Sequences (For Django ≥ 3.1)**
After loading, reset PostgreSQL sequences to avoid future conflicts:
```bash
python manage.py sqlsequencereset app_name | python manage.py dbshell
```
Replace `app_name` with your Django app name.

---

### **3. For Large Datasets: Use Fixture Formatting**
Convert your data to **natural keys** to avoid PK dependencies:
```json
[
  {
    "model": "app.model",
    "fields": {
      "unique_field": "value",  // Use unique fields instead of PKs
      "foreign_key": ["natural_key_value"]  // For ForeignKey/M2M
    }
  }
]
```
Then load with:
```bash
python manage.py loaddata data.json --natural-foreign --natural-primary
```

---

### **4. Verify Data Integrity**
1. Check PostgreSQL **before** and **after** loading:
   ```bash
   python manage.py shell
   ```
   ```python
   from app.models import Model
   print(Model.objects.count())  # Compare counts
   ```

2. Inspect specific records:
   ```python
   Model.objects.filter(name__contains="Example").exists()
   ```

---

### **Key Notes**
- **Backup first!** Always dump your PostgreSQL data before loading:
  ```bash
  python manage.py dumpdata --output=backup.json
  ```
- **Fixtures are additive** when `--append` is used, but **unique constraints** (e.g., `slug`, `email`) may still cause errors.
- For **bulk inserts**, consider Django’s `bulk_create()` instead of fixtures.

---

### **Troubleshooting**
| Error | Solution |
|-------|----------|
| `IntegrityError` (duplicate PK) | Use `--append` or remove PKs from JSON |
| `UniqueViolation` | Edit JSON to avoid duplicate unique fields |
| `ForeignKey` missing | Load dependent models first (order matters) |

Example **correct load order**:
```bash
python manage.py loaddata auth.user.json  # Base model
python manage.py loaddata app.model.json  # Depends on User
```

# Issues

### CKEditor  

WARNINGS:
?: (ckeditor.W001) django-ckeditor bundles CKEditor 4.22.1 which isn't supported anymore and which does have unfixed security issues, see for example https://ckeditor.com/cke4/release/CKEditor-4.24.0-LTS . You should consider strongly switching to a different editor (maybe CKEditor 5 respectively django-ckeditor-5 after checking whether the CKEditor 5 license terms work for you) or switch to the non-free CKEditor 4 LTS package. See https://ckeditor.com/ckeditor-4-support/ for more on this. (Note! This notice has been added by the django-ckeditor developers and we are not affiliated with CKSource and were not involved in the licensing change, so please refrain from complaining to us. Thanks.)