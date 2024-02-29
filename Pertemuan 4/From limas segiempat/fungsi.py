def hitung_luas(txtluas_sisi1,txtluas_sisi2,txtluas_sisi3,txtluas_sisi4,txtluas_sisi5):
    ls_1 = float(txtluas_sisi1)
    ls_2 = float(txtluas_sisi2)
    ls_3 = float(txtluas_sisi3)
    ls_4 = float(txtluas_sisi4)
    ls_5 = float(txtluas_sisi5)
    
    L = round((ls_1 + ls_2 + ls_3 + ls_4 + ls_5), 2)
    return L

    
def hitung_volume(txtluas_alas,txttinggi):
    la = float(txtluas_alas)
    t = float(txttinggi)
    
    V = round((1/3 * la * t), 2)
    return V

