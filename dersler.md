# V08
Edited for testing purposes

# Video Tutorials
https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH&index=2

# Environment Variables
https://www.youtube.com/watch?v=IolxqkL7cD8
Şifre ve kullanıcı adı gibi blgilerin kendi bilgisayarımda tutulması için yapılması şart.
Böylelikle benden başka kimse kullanamaz. Bu environment Variables'ı yazdığımız kodun içerisinde çekiyoruz.
Örnek:

# Requirements.txt
Bunu oluşturmak için önce virtual environment tarafında pip freeze ile kütüphaneleri ve veriyonlarını görüyoruz.
pip freeze

bunu requirements.txt tarafına eklemek için (Lünux ve Mac => Windows'ta denemek lazım):
pip freeze > requirements.txt


# Server için Command Line Süreci
C:\Users\emres
λ cd C:\xampp\htdocs\testler\python\flask\corey\Flask_Blog

C:\xampp\htdocs\testler\python\flask\corey\Flask_Blog
λ py -3 -m venv venv

C:\xampp\htdocs\testler\python\flask\corey\Flask_Blog
λ venv\Scripts\activate

C:\xampp\htdocs\testler\python\flask\corey\Flask_Blog
(venv) λ atom .

C:\xampp\htdocs\testler\python\flask\corey\Flask_Blog
(venv) λ set FLASK_APP=run.py

C:\xampp\htdocs\testler\python\flask\corey\Flask_Blog
(venv) λ set FLASK_DEBUG=1

C:\xampp\htdocs\testler\python\flask\corey\Flask_Blog
(venv) λ flask run

# Virtual environment oluşturma
py -3 -m venv venv

# Environment'i aktif hale getirme
venv\Scripts\activate

# Modül install etme
(venv) λ pip install flask -- (venv) aktif edilince otomatik geliyor

# Flask App tanımlama
(venv) λ set FLASK_APP=flaskblog.py
* Mac'te ve Linux'ta set yerine export kullanılıyor

# Sunucuyu çalıştırma
(venv) λ flask run

# Reload Page
Değişiklikler yapıldığında sayfayı reload ettiğimizde değişiklikler görünmüyor, o yüzden debug moduna geçmemiz lazım:

(venv) λ set FLASK_DEBUG=1

# Direkt olarak çalıştırmak için (Environment'te değil)
if __name__ == '__main__':
    app.run(debug=True)

# Templating
Template işi jinja ile yapılıyor. Jinja2 de varmış. Bir bakmak lazım.

# Forms
Formlar için bir eklenti kurmak en doğrusu. Çünkü o tüm işi hallediyor.
- pip install flask-wtf

# Secret key
 Kolay oluşturmak için python içinde olan bir fonksiyonu kullanabiliriz. Çok önemli değil biz de kendimiz yazabiliriz, ama böyle daha janjanlı oluyor.
 <!--

 (venv) λ python
 Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
 Type "help", "copyright", "credits" or "license" for more information.
 >>> import secrets
 >>> secrets.token_hex(16)
 '7bce2ca88c6b82065a42a4ca1bd2ccf6'

  -->

# Linkler
Linkleri url_for('approute_fonksiyonu') ile veriyoruz. Daha sağlıklıymış.
parantez içindeki route adı değil, route'a bağlı olan fonksiyon.

# VERİTABANI
Veritabanı için SQLAlchemy kullanmak çok faydalı. Bir çok sorguyu bununla kolaylıkla çalıştırabiliyoruz.

Örnek:
>>> from flaskblog import db
>>> from flaskblog._models.test import User, Post
>>> user_1 = User(username='Corey', email='C@demo.com', password='password')
>>> db.session.add(user_1)
>>> user_2 = User(username='JohnDoe', email='Cjd@demo.com', password='password')
>>> db.session.add(user_2)
>>> db.session.commit()
>>> User.query.all()
[User('Corey','C@demo.com','default.jpg'), User('JohnDoe','Cjd@demo.com','default.jpg')]
>>> User.query.first()
User('Corey','C@demo.com','default.jpg')
>>> User.query.filter_by(username='Corey').all()
[User('Corey','C@demo.com','default.jpg')]
>>> User.query.filter_by(username='Corey').first()
User('Corey','C@demo.com','default.jpg')
>>> user = User.query.filter_by(username='Corey').first()
>>> user
User('Corey','C@demo.com','default.jpg')
>>> user.id
1
>>> post_1 = Post(title='Blog 1', content='First Post Content!', user_id=user.id)

Özellikle flaskblog.py'daki relationship süper bir şey.
