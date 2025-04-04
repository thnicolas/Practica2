
from prettytable import PrettyTable

def imprimir_tabla (ranking):
     table = PrettyTable()
     table.field_names = ["Jugador", "Kills", "Assists", "Deaths", "MVPs", "Score"]
     for player, stats in ranking.items():
        table.add_row([player, stats['kills'], stats['assists'], stats['deaths'], stats['MVPs'], stats['score']])
     print(table)