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

### 🏬 Render Host - deployment

- **Build command:** if all the commands are describe in production settings ex.-
  -  `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --no-input` 
  -  If you have more command include or remove as needed
- **Start command** `python manage.py runserver 0.0.0.0:8000` 
- **Env** check if envrionment variable available then then set it up 
- **Real-time Notification** `start command` would be different, check it carefully

### 🫙 Dump local Database `data` in a file
```bash
python3 manage.py dumpdata --output=data,json
```

# Issues

### CKEditor  

WARNINGS:
?: (ckeditor.W001) django-ckeditor bundles CKEditor 4.22.1 which isn't supported anymore and which does have unfixed security issues, see for example https://ckeditor.com/cke4/release/CKEditor-4.24.0-LTS . You should consider strongly switching to a different editor (maybe CKEditor 5 respectively django-ckeditor-5 after checking whether the CKEditor 5 license terms work for you) or switch to the non-free CKEditor 4 LTS package. See https://ckeditor.com/ckeditor-4-support/ for more on this. (Note! This notice has been added by the django-ckeditor developers and we are not affiliated with CKSource and were not involved in the licensing change, so please refrain from complaining to us. Thanks.)