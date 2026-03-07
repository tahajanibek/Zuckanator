# Zuckanator ![Python](https://img.shields.io/badge/Python-3.11-blue)
Basic Instagram PP tool.

<div align="center">
<pre style="color:#00f7ff;"; font-weight:bold;">
███████╗██╗   ██╗ ██████╗██╗  ██╗ █████╗ ███╗   ██╗ █████╗ ████████╗ ██████╗ ██████╗
╚══███╔╝██║   ██║██╔════╝██║ ██╔╝██╔══██╗████╗  ██║██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
  ███╔╝ ██║   ██║██║     █████╔╝ ███████║██╔██╗ ██║███████║   ██║   ██║   ██║██████╔╝
 ███╔╝  ██║   ██║██║     ██╔═██╗ ██╔══██║██║╚██╗██║██╔══██║   ██║   ██║   ██║██╔══██╗
███████╗╚██████╔╝╚██████╗██║  ██╗██║  ██║██║ ╚████║██║  ██║   ██║   ╚██████╔╝██║  ██║
╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
</pre>
</div>

**Zuckanator**, Instagram profil fotoğraflarını HD olarak görüntülemek veya kaydetmek için basit bir Python aracıdır.

---

## Özellikler

- Instagram kullanıcılarının profil fotoğraflarını yüksek çözünürlükte çekme.
- Multi-endpoint RapidAPI desteği ile yüksek erişilebilirlik.
- Kolay ve temiz terminal arayüzü.
- İndirilen fotoğrafları kullanıcının klasörüne kaydetme.
- Hedef kullanıcı hakkında temel bilgiler gösterme: bio, takipçi sayısı, gönderi sayısı, doğrulama durumu.

---
## Gereksinimler ![Platform](https://img.shields.io/badge/Platform-Linux%2FmacOS%2FWindows%2FTermux-purple)

Python 3.10+ ve aşağıdaki paketler:

- `requests`
- `pyfiglet`

> Script, eksik paketleri otomatik olarak yükleyebilir.

---

## Kurulum

Repo’yu indirin:

```bash
git clone https://github.com/tahajanibek/Zuckanator.git
cd Zuckanator
pip install -r requirements.txt --break-system-packages
```

## Çalıştırın
```
python zuckanator.py
```
> Gerekli API'nin temin edilmesi: ![API](https://img.shields.io/badge/API-RapidAPI-green)
- `RapidAPI üzerinden aldığınız instagram120 API anahtarını girin.`
> Kullanım:
- `Hedef Instagram kullanıcı adını yazın (örn: @username).`

#### 🧃 Örnek Çıktı: 
```pgsql
TARGET  @juckfews
Full Name   Benjamin Zuckland
Bio         Buisness & Fund
User ID     6000000
Followers   586
Following   135
Posts       70
Private     🌐 No
Verified    ✓ Yes
URL         https://instagram.com/juckfews/bc597/ac70/PAX/ac580000/ac1933/
```

----
## Geliştirici Notları

TatNet tarafından geliştirilen bu yazılım, açık kaynaklı ve geliştirilmeye açıktır.  

---

# 📜 Lisans ![License](https://img.shields.io/badge/License-AGPL--3.0-red)

                  GNU AFFERO GENEL KAMU LİSANSI
                  Sürüm 3, 29 Haziran 2007
                       
    Copyright (C) 2007 Özgür Yazılım Vakfı, Inc. <https://fsf.org/>
    Copyright (C) 2025 Taha Janibek
    Copyright (C) 2025 TatNet

    Taha Janibek tarafından geliştirilen bu yazılım ve tüm betikleri (ör. zuckanator.py) aşağıdaki şartlarla lisanslanmıştır:

    Bu program özgür bir yazılımdır: onu yeniden dağıtabilir ve/veya
    GNU Affero Genel Kamu Lisansı'nın 3. versiyonu veya Özgür Yazılım Vakfı 
    tarafından yayınlanabilecek daha sonraki herhangi bir sürümü uyarınca değiştirebilirsiniz.

    Bu program, faydalı olacağı umuduyla dağıtılmaktadır,
    ancak HİÇBİR GARANTİ VERİLMEKSİZİN; satılabilirlik ya da
    belirli bir amaca uygunluk garantisi olmaksızın dağıtılmaktadır.
    Daha fazla ayrıntı için GNU Affero Genel Kamu Lisansı'na bakınız.

    Önemli fark: AGPL, bu programı ağ üzerinden kullanmanız durumunda
    değiştirilmiş sürümlerini kullanıcılarla paylaşmanızı zorunlu kılar.

    Bu lisansın aslı `LICENSE` ekinde verilmiştir. 
    Alternatif olarak <https://www.gnu.org/licenses/agpl-3.0.tr.html> 
    adresinden ulaşabilirsiniz.

*NOT: Bu Türkçe çeviri, bilgilendirme amaçlıdır. Yasal bağlayıcılığı olan sürüm, İngilizce olan `LICENSE` dosyası aslıdır, ayrıca buradan da göz atabilirsiniz: [GNU General Public License v3]([https:/www.gnu.org/licenses/gpl-3.0.html](https://www.gnu.org/licenses/agpl-3.0.html)

Bu proje, [GNU Affero Genel Kamu Lisansı v3](LICENSE) ile lisanslanmıştır.

---

# ⚠️ Sorumluluk Reddi Beyanı

Bu yazılım (Zuckanator) ve sağladığı tüm fonksiyonlar, kullanıcıya Instagram profil fotoğraflarını inceleme ve indirme imkânı sağlar.

Kullanıcı, bu yazılımı kullanarak yaptığı tüm işlemlerden tamamen kendisi sorumludur.

Geliştirici Taha Janibek ve TatNet, bu yazılımın kullanımı sırasında oluşabilecek herhangi bir veri kaybı, sistem hatası, hukuki durum veya kötüye kullanım nedeniyle hiçbir sorumluluk kabul etmez.

Önemli Uyarılar:

- Yazılım internete bağlı değildir ve veri iletimi yapmaz. Tüm işlemler, kullanıcının cihazında yerel olarak gerçekleşir.

- Kullanıcı tarafından girilen kullanıcı adları ve indirilen profil fotoğraflarının güvenliği tamamen kullanıcının sorumluluğundadır.

- Yazılımın üreteceği çıktı dosyaları (json, jpg, txt) gizli bilgiler içerebilir. Bu dosyaları yalnızca güvenli ve kontrollü ortamda kullanınız.

`Özetle: Kullanıcı, özel verilerini ve çıktıları güvenli şekilde yönetmekten sorumludur.`




---

## 👤 Geliştirici

**Taha Janibek**  
📧 tahajanibek@mail.ru  


