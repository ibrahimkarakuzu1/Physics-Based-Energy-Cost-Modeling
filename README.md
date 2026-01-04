#  Physics-Based Energy Estimator (Day 3)

**Day 3** focuses on replacing geometric heuristics with physics-based constraints.

## English

###  Objective
To develop a mathematical model that predicts energy consumption for a vehicle traversing 3D terrain, accounting for **Gravity** and **Friction**.

###  The Physics Model
We calculate the work ($W$) required to move a mass ($m$) across a distance ($d$) on a slope ($\theta$).

#### Key Equations:
1.  **Gravity Force:** $F_g = m \cdot g \cdot \sin(\theta)$
    * *Effect:* Penalizes elevation gain. Steeper angles require exponentially more torque/energy.
2.  **Friction Force:** $F_f = m \cdot g \cdot \cos(\theta) \cdot \mu$
    * *Effect:* Constant resistance based on surface type (sand, rock, asphalt).

#### Total Energy Cost:
$$Cost (Joules) = d \cdot (F_g + F_f)$$

###  Simulation Results
Comparing two paths of equal length (1000m):
* **Path A (Flat):** Only overcomes friction. Low energy cost.
* **Path B (Slope):** Must overcome gravity. Energy cost spikes by **+250%**.

---

## 🇹🇷

###  Amaç
3D arazide hareket eden bir aracın enerji tüketimini tahmin etmek için **Yerçekimi** ve **Sürtünme** kuvvetlerini hesaba katan matematiksel bir model geliştirmek.

### Fizik Modeli
Bir kütleyi ($m$) belirli bir eğimde ($\theta$) ve mesafede ($d$) hareket ettirmek için gereken işi ($W$) hesaplıyoruz.

#### Temel Denklemler:
1.  **Yerçekimi Kuvveti:** $F_g = m \cdot g \cdot \sin(\theta)$
    * *Etki:* Yükseklik kazanımını cezalandırır. Dik açılar katlanarak artan enerji gerektirir.
2.  **Sürtünme Kuvveti:** $F_f = m \cdot g \cdot \cos(\theta) \cdot \mu$
    * *Etki:* Yüzey tipine (kum, kaya, asfalt) bağlı sabit dirençtir.

#### Toplam Enerji Maliyeti:
$$Maliyet (Joule) = d \cdot (F_g + F_f)$$

###  Simülasyon Sonuçları
Eşit uzunluktaki (1000m) iki yolu karşılaştırdığımızda:
* **Yol A (Düz):** Sadece sürtünmeyi yener. Düşük enerji maliyeti.
* **Yol B (Eğimli):** Yerçekimini yenmek zorundadır. Enerji maliyeti **%250+** artar.

---
