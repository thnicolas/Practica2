from prettytable import PrettyTable
import sys
import os
sys.path.append(os.path.abspath("../src"))
from src.iniciar_ranking import iniciar_ranking
from src.imprimir_tabla import imprimir_tabla


def crear_ranking(r):
    nombres_jugadores = list(r[0].keys())
    rank_final = iniciar_ranking(nombres_jugadores)
    for i, ronda in enumerate(r):
        print(f"Ronda {i+1}")

        rank_rondas= iniciar_ranking(nombres_jugadores)

        for pj, stats in ronda.items():
            score = (stats["kills"] * 3) + stats["assists"] - int(stats["deaths"])
            rank_rondas[pj]["score"] = score
            rank_rondas[pj]["kills"] = stats["kills"]
            rank_rondas[pj]["assists"] = stats["assists"]
            rank_rondas[pj]["deaths"] = int(stats["deaths"])
            rank_final[pj]["score"]+=score        
            rank_final[pj]["kills"]+= stats["kills"] 
            rank_final[pj]["assists"]+=stats["assists"]
            rank_final[pj]["deaths"] += int(stats["deaths"])
      
        rank_rondas = dict(sorted(rank_rondas.items(), key=lambda item: item[1]["score"], reverse=True))
        jugadores = list(rank_rondas.items())
        if jugadores:
            mejor_jugador = jugadores[0][0]
            rank_rondas[mejor_jugador]["MVPs"] += 1
            rank_final[mejor_jugador]["MVPs"] += 1  
        
        imprimir_tabla(rank_rondas)

    rank_final= dict(sorted(rank_final.items(), key=lambda item: item[1]["score"], reverse=True))

    print ("Ranking Final")
    imprimir_tabla (rank_final)
       