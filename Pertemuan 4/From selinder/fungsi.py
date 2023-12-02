def hitung_luas_Selimut(JariJari,Tinggi):  
    r = float( JariJari)
    T = float( Tinggi)

    LS = round (2*22/7*r*T) 
    return LS


def hitung_luas_Permukaan(JariJari,Tinggi):
  
    r = float( JariJari)
    T = float( Tinggi)

    LP = round (2*(22/7)*r*T+2*(22/7)*(r*r)) 
    return LP


def hitung_Volume(JariJari,Tinggi):
    
    r = float( JariJari)
    T = float( Tinggi)

    V = round ((22/7)*(r*r)*T)
    return V
   


