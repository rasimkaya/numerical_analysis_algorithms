<div align="center">
  <h1>🧮 Lineer Olmayan Denklemlerin Nümerik Çözümleri</h1>
  <p><i>Python ile Nümerik Analiz Algoritmaları, İterasyon Görselleştirmeleri ve Kök Bulma Yöntemleri</i></p>

  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Numpy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="Numpy" />
  <img src="https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white" alt="Matplotlib" />
  <img src="https://img.shields.io/badge/Sympy-3B5526?style=for-the-badge&logo=python&logoColor=white" alt="Sympy" />
</div>

<br>

> **Kurum:** T.C. Gazi Üniversitesi | Fen Fakültesi | Matematik Bölümü <br>
> **Hazırlayan:** Rasim Kaya <br>

---

## 📖 Proje Hakkında
Bu proje, lineer olmayan denklemlerin köklerini bulmak için kullanılan temel nümerik analiz yöntemlerinin **Python** ile algoritmik olarak uygulanmasını ve **Matplotlib** kullanılarak adım adım görselleştirilmesini içermektedir. Projede kod mimarisine özen gösterilmiş, `DRY` prensibi ile ortak fonksiyonlar modüler hale getirilmiştir.

---

## 🔬 Temel Teoremler (Kök Varlığı)

Sayısal bir yöntem oluşturabilmemiz için kökün varlığından, yani varlığını bildiğimiz bir aralığa ihtiyacımız vardır. Algoritmaların dayandığı temel teoremler şunlardır:

### 1. Rolle Teoremi
Bir f fonksiyonu [a,b] aralığında sürekli ve (a,b) aralığında türevlenebilir olsun. Eğer f(a) = f(b) ise;
$$f'(c) = 0$$
olacak şekilde en az bir c ∈ (a,b) vardır.

### 2. Ortalama Değer Teoremi
f fonksiyonu [a,b] aralığında sürekli ve (a,b) aralığında türevlenebilir olsun.
$$f'(c) = \frac{f(b) - f(a)}{b - a}$$
olacak şekilde bir c ∈ (a,b) vardır.

### 3. Ara Değer Teoremi
f fonksiyonu [a,b] aralığında sürekli olsun. Eğer bir K sayısı f(a) ile f(b)'nin arasında ise;
$$f(c) = K$$
olacak şekilde bir c ∈ (a,b) vardır.

### 4. Bolzano Teoremi
f fonksiyonu [a,b] aralığında sürekli olsun. Eğer uç noktaların işaretleri zıt ise, yani;
$$f(a) \cdot f(b) < 0$$
ise, f(c) = 0 olacak şekilde bir c ∈ (a,b) vardır. *(Bu durum, aralıkta en az bir kök olduğunu garanti eder ve Aralık Yarılama yönteminin temelini oluşturur.)*

---

