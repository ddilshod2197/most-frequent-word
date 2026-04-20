def eng_ko_p_takrorlangan_sozni_top(sozlar):
    sozlar = sozlar.lower().split()
    sozlar_soni = {}
    for soz in sozlar:
        if soz in sozlar_soni:
            sozlar_soni[soz] += 1
        else:
            sozlar_soni[soz] = 1
    max_soz = max(sozlar_soni, key=sozlar_soni.get)
    return max_soz

sozlar = "Bu sozlar eng ko'p takrorlangan sozni topish uchun ishlatiladi. Bu sozlar eng ko'p takrorlangan sozni topish uchun ishlatiladi."
print(eng_ko_p_takrorlangan_sozni_top(sozlar))
