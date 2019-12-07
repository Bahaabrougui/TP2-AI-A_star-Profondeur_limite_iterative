from functions import *


# Function to check the existence of un predicat dans un tableaux de predicats
def exist(conclusion, predicats):
    if not predicats:
        return False
    verif = False
    for predicat in predicats:
        if predicat.vals[0] == conclusion.vals[0] and predicat.vals[1] == conclusion.vals[1]:
            return True

    return verif


base = BaseDeConnaissance("C:/Users/Kalelt'has/Desktop/My GL4/AI/Tp 2/cruches.txt")

# for regle in (genererConclusionUnifies(base, Predicat.extractPredicat('cruchesAetB(4,0)'))):
#     pass

EtatInit = base.faits[0].predicat
graphe = Graph(EtatInit)
closedStates = []
possibleStates = [EtatInit]
i = 0

# Graph construction
while possibleStates:

    state = possibleStates.pop(0)
    closedStates.append(state)
    base.faits = state
    possibleConclusions = genererConclusionUnifies(base.regles, state)

    for conclusion in possibleConclusions:
        graphe.addEdge(state, conclusion)
        if not exist(conclusion, closedStates) and not exist(conclusion, possibleStates):
            possibleStates.append(conclusion)
    i += 1

for key in graphe.graph:
    print("*********")
    print("Sommet: ", key.nom, '(', key.vals, ')')
    print("Values")
    for val in graphe.graph[key]:
        print("fils: ", val.nom, '(', val.vals, ')')

test = Predicat("cruchesAetB", ['4', '2'])
# chemin = []
# print(graphe.rechercheProfendeurLimiteIteratif(graphe.V, test, 10, chemin))
# chemin = functions.prepareChemin(chemin, graphe.V) # Function that modifies the path in order to get it in a good format
# for chem in chemin:
#     print(chem)

result, parcours = graphe.a_star_search(graphe.V, test)
for chem in parcours:
    print(chem)
# for key in came_from:
#     print(key, "came from", came_from[key])
