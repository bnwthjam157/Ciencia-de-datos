import math


def promedio(lista):
    """
    calcula el promedio de una lista.
    
    parametros:
    -------------
    lista: lista de variables aleatorias
    
    retorna:
    ------------
    promedio : float
    """
    
    vals= []
    for v in lista:
        if math.isfinite(v):
            vals.append(v)
        
    promedio=sum(vals)/len(vals)
    return promedio

def mediana(vals_in):
    
    """
    calcula la mediana de una lista conteniendo una
    variable categoria nominal
    Parametros
    -----------
    vals: list
    lista de categotias
    Retorna
    -------
    moda: str
    la moda de la muestra
    """
    #se eliminan valores que sean NaNs
    vals=[]
    for v in vals_in:
        if math.isfinite(v):
            vals.append(v)
#ordenar la lista
    vals.sort()

    if len(vals)% 2!=0:
        k= len(vals)//2
        mediana= vals[k]            
    else: 
        k= len(vals)//2 
        mediana= (vals[k-1]+ vals[k])/2
    return mediana

def moda(vals):
    
    """
    calcula la moda de una lista conteniendo una
    variable categoriva nominal
    Parametros
    -----------
    vals: list
    lista de categotias
    Retorna
    -------
    moda: str
    la moda de la muestra
    """
    #encontrar el conjunto de elementos unicos
    categorias=[]
    for v in vals:
        if v not in categorias:
            categorias.append(v)
    #obtener el numero de cuentas en la muestra
    cuenta=[]
    #para cada una de las categorias
    
    
    for c in categorias:
        n=0
        for val in vals:
            if val==c:
                n=n+1
        cuenta.append(n)

    #guess and check
    i_max=0
    val_max=cuenta[0]
    for i in range(1,len(cuenta)):
        if cuenta[i]> val_max:
            i_max=i
            val_max=cuenta[i]
    #determinar todas las categorias que tengan el numero
    #maximo de cuentas
    
    modas= []
    for i in range(len(cuenta)):
        if cuenta[i]== val_max:
            modas.append(categorias[i])
    
    #retorno la moda
    #moda= categorias[i_max]
    return modas

def rango(vals_in):
    
    """
    calcula el rango de una lista conteniendos
    Parametros
    -----------
    vals: list
        lista de numeros
    Retorna
    -------
    rango: float
        rango de los valores (excluye nans)
    """
    
    vals=[]
    for v in vals_in:
        if math.isfinite(v):
            vals.append(v)
    return max(vals)-min(vals)

def varianza(vals_in):
    
    """
    calcula varianza de una lista de numeros
    Parametros
    -----------
    vals: list
        lista de numeros
    Retorna
    -------
    varianza: float
        varianza de los valores (excluye NaNs)
    """
    
    vals=[]
    for v in vals_in:
        if math.isfinite(v):
            vals.append(v)
    desviaciones=[]
    prom= promedio(vals)
    for i in vals:
        calculo= (i-prom)**(2)
        desviaciones.append(calculo)
    suma= sum(desviaciones)
    varianza= (1/len(vals)*suma)
        
    return varianza


        
def desviacion_estandar(vals_in):
    
    """
    calcula desviacion estandar de una lista de numeros
    Parametros
    -----------
    vals: list
        lista de numeros
    Retorna
    -------
    desviacion estandar: float
        desviacion de los valores (excluye NaNs)
    """
    
    vals=[]
    for v in vals_in:
        if math.isfinite(v):
            vals.append(v)

    return varianza(vals_in)**(1/2)

def percentil(vals_in,q,interpolacion="lineal"):
    """
    Calcula el percentil de una lista de numeros
    Detecta y elimina valores NaN
    
    Paràmetros
    ----------
    vals: lista
        lista con los numeros
        
    Retorna
    -------
    percentil:float
        percentil de los numeros (excluyendo NaNs)
    """
    
    
    #eliminamos los valores que sean NaNs
    vals=[]
    for v in vals_in:
        if math.isfinite(v):
            vals.append(v)

    # Ordenar la lista dada como input in-place
    vals.sort()

    if interpolacion=="lineal":
        #Distancia entre el primer y ultimo elemtno,
        #a ki kargi del eje de indices
        dist=len(vals)-1

        #calcular el indice efectio del percentil
        ieff=dist*q/100
        
        #parte fraccional
        fraction=ieff-int(ieff)
        
        #indice inferior
        i=int((ieff)//1)
        j=i+1

        #La interoplacion lineal se implementa con
        # val_inf + (val_sup)- val_inf)*fraction,
        percentile=vals[i]+vals[j]-vals[i]*fraction

        return percentile
        
        percentile=vals
    
def rango_intercuartilico(vals_in):
    """
    Calcula el rango intercuartilico de una lista de numeros
    Detecta y elimina valores NaN
    
    Parámetros
    ----------
    vals: lista
        lista con los numeros
        
    Retorna
    -------
    rango intercuartilico:float
        rango intercuartilico de los numeros (excluyendo NaNs)
    """
    
    
    #eliminamos los valores que sean NaNs
    vals=[]
    for v in vals_in:
        if math.isfinite(v):
            vals.append(vals_in)
    iqr=percentil(vals,75)-percentil(vals,25)
    return iqr

def MAD(vals_in):
    """
    calcula MAD de una lista de valores, ignora valores NaN
    
    Parámetros
    -----------
    vals_in: list
        lista de números
    Retorna
    -------
    MAD: float
        MAD de los valores
    """
    vals=[]
    for v in vals_in:
        if math.isfinite(v):
            vals.append(v)
    med = mediana(vals)
    desviaciones_med= []
    for v in vals:
        desviaciones_med.append(abs(v-med))
    mad = mediana(desviaciones_med)
    return mad
        

def covarianza(x,y):
    """
    calcula la covarianza de una lista de valores, ignora valores NaN
    
    Parámetros
    -----------
    x,y: list
        lista de números
    Retorna
    -------
    covarianza: float
        covarianza de los valores
    """
    x_vals=[]
    y_vals=[]
    if len(x) == len(y):
        for i in range(len(x)):
            if math.isfinite(x[i]) and math.isfinite(y[i]):
                x_vals.append(x[i])
                y_vals.append(y[i])
    else:
        print("los largos no coinciden")
            
    xmean= promedio(x_vals)
    ymean= promedio(y_vals)
    tt=[]                    
    for xv, yv in zip(x,y):
        tt.append((xv-xmean)*(yv-ymean))
    covarianza= sum(tt)/len(tt)
    return covarianza 
            
def correlacion(x,y):
    """
    calcula la correlación de una lista de valores, ignora valores NaN
    
    Parámetros
    -----------
    x,y: list
        lista de números
    Retorna
    -------
    correlacion: float
        covarianza de los valores
    """
    x_vals=[]
    y_vals=[]
    for i in range(len(x)):
        if math.isfinite(x[i]) & math.isfinite(y[i]):
            x_vals.append(x[i])
            y_vals.append(y[i])
            
    rxy = covarianza(x,y)/( varianza(x) * varianza(y) )
    return rxy                        