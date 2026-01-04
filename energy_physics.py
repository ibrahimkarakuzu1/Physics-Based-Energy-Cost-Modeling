import math

# -----------------SABİTLER----------------
# aracın donanım özellikleri

MASS = 900.0             # kg aracın kütlesi
GRAVITY = 3.721          # m/s^2 mars yerçekimi
FRICTION_COEFF = 0.04    # µ Tekerlek ile kumlu zemin arasındaki sürtünme

def calculate_slope_physics(p1, p2):
    """
    3D Uzayda iki nokta arasındaki geometriyi çözer
    Girdi: x, y, elevation
    Çıktı: 3D Mesafe, Eğim Açısı
    """
    # 1 Yatay Mesafe (Delta D) - Kuş bakışı uzaklık (Pisagor)
    dist_2d = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
   
    # 2 Yükseklik farkı (DElta H)
    delta_h = p2[2] - p1[2]

    #3 Hipotenüs 
    # Araç haritadaki düz çizgiyi değil bu eğimli hipotenüsü gider
    dist_3d = math.sqrt(dist_2d**2 + delta_h**2)

    #4 Eğim Açısı 
    # Trigonometri -> Karşı / Komşu  arctan bize açıyı verir.
    if dist_2d == 0:
        theta_rad = 0
    else:
        theta_rad = math.atan2(delta_h, dist_2d)
    
    return dist_3d, theta_rad

def estimate_energy_cost(dist_3d, theta_rad):
    """
    İş (Joule) = Kuvvet (Newton) x Yol (Metre)
    Motorun yenmesi gereken toplam direnç kuvvetlerini hesaplar.
    """

    # YERÇEKİMİ KUVVETİ
    # F = m * g * sin(θ)
    # yokuş ne kadar dikse sin(θ) artar, motor o kdar zorlanır 
    gravity_force = MASS * GRAVITY * math.sin(theta_rad)

    #SÜRTÜNME KUVVETİ
    #F = m * g * cos(θ) * µ
    #Yüzeye ne kadar dik basarsak cos(θ), sürtünme o kadar etkilidir.
    friction_force = MASS *  GRAVITY * math.cos(theta_rad) * FRICTION_COEFF

    # TOPLAM KUVVET 
    total_force = gravity_force + friction_force


    # Eğer yokuş aşağı iniyorsak (negatif kuvvet), araç kendi kendine hızlanır.
    # Biz burada 'Rejeneratif Frenleme' ile enerji geri kazanımını yok sayıyoruz (0 kabul ediyoruz).
    if total_force < 0:
        total_force = 0.0

    # SONUÇ harcanan enerji
    return total_force * dist_3d

# -------------- SİMÜLASYON -------------------
if __name__ == "__main__":
    print("\n PHYSICS-BASED ENERGY ANALYSIS - MARS ROVER")
    print("-" * 50)
    
    # Senaryo: İki farklı yoldan 1000 metre gidilecek.
    
    # YOL 1 Dümdüz ova - 0 metre tırmanış
    path_flat_start = (0, 0, 100)
    path_flat_end   = (1000, 0, 100)
    
    # YOL 2 Dik yokuş 100 metre tırmanış %10 eğim
    path_steep_start = (0, 0, 100)
    path_steep_end   = (1000, 0, 200) 
    

    # Hesaplama 1 Düz yol
    d_flat, angle_flat = calculate_slope_physics(path_flat_start, path_flat_end)
    cost_flat = estimate_energy_cost(d_flat, angle_flat)
    
    # Hesaplama 2 Yokuşlu yol
    d_steep, angle_steep = calculate_slope_physics(path_steep_start, path_steep_end)
    cost_steep = estimate_energy_cost(d_steep, angle_steep)
    
    # Çıktılar
    print(f" FLAT PATH (Delta H: 0m)")
    print(f" Distance: {d_flat:.2f} m | Angle: {math.degrees(angle_flat):.2f}°")
    print(f" Energy  : {cost_flat:.2f} Joules")
    print("-" * 30)
    
    print(f" STEEP PATH (Delta H: +100m)")
    print(f" Distance: {d_steep:.2f} m | Angle: {math.degrees(angle_steep):.2f}°")
    print(f" Energy  : {cost_steep:.2f} Joules")
    print("-" * 30)
    
    # Karşılaştırma
    increase = ((cost_steep - cost_flat) / cost_flat) * 100
    print(f" RESULT: A {math.degrees(angle_steep):.1f}° slope increases energy consumption by +{increase:.1f}%")








