import requests as req
import os
import json


real_path = os.path.dirname(__file__)

#Extrayendo json

res = req.get("https://datos.comunidad.madrid/catalogo/dataset/7da43feb-8d4d-47e0-abd5-3d022d29d09e/resource/ead67556-7e7d-45ee-9ae5-68765e1ebf7a/download/covid19_tia_muni_y_distritos.json").json()

with open (f"{real_path}/covid.json", "w", encoding="utf8") as file:
    json.dump(res, file, ensure_ascii=False, indent=4)

with open (f"{real_path}/covid.json", encoding="utf8") as file:
    data = json.load(file)["data"]

####################################

def get_muni(data):
    return(len(list(filter(lambda muni: muni["fecha_informe"] == "2020/07/01 09:00:00", data))))


def get_ccdate(data, date):
    cctotales = 0
    for muni in data:
        try:
            if muni["fecha_informe"].find(date) >= 0:
                cctotales += muni["casos_confirmados_totales"]
        
        except KeyError:
            cctotales += 0
    return cctotales

def top_ten(data):
    worst = []
    for muni in data:
        try:
            if muni["casos_confirmados_totales"] and muni["fecha_informe"] == "2020/07/01 09:00:00":
                worst.append(muni)
        except KeyError:
            continue
    
    tenworst = sorted(worst, key=lambda muni: muni["casos_confirmados_totales"], reverse=True)[0:10]

    for element in tenworst:
        print (element["municipio_distrito"])
        print (element["casos_confirmados_totales"])

def sum_tot_dia(data):
    lista_de_dias = []
    dict_total_por_dia = {}

    for muni in data:
        try:
            if muni["fecha_informe"].split(" ")[0] not in lista_de_dias:
                lista_de_dias.append(muni["fecha_informe"].split(" ")[0])
        except KeyError:
            continue
    
    for date in lista_de_dias:
        dict_total_por_dia[date] = get_ccdate(data,date)
    
    return(dict_total_por_dia)
    #return(list(dict_total_por_dia.values()))