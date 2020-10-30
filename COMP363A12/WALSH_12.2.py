from heapq import heappush, heappop
from math import inf

RP = {'Howard_Western': {'A2': 60, 'B1': 10},
'A2': {'Howard_Western': 60, 'A3': 60, 'B2': 60},
'A3': {'A2': 60, 'Howard_Ridge': 60, 'B3': 60},
'Howard_Ridge': {'A3': 60, 'A5': 60, 'B4': 60},
'A5': {'Howard_Ridge': 60, 'A6': 60, 'B5': 60},
'A6': {'A5': 60, 'A7': 60, 'B6': 60},
'A7': {'A6': 60, 'A8': 60, 'B7': 60},
'A8': {'A7': 60, 'A9': 60, 'B8': 60},
'A9': {'A8': 60, 'Howard_L': 60, 'B9': 10},
'Howard_L': {'A9': 60, 'A11': 60, 'B10': 60, 'Jarvis_L': 20},
'A11': {'Howard_L': 60, 'A12': 60, 'B11': 60},
'A12': {'A11': 60, 'A13': 60, 'B12': 60},
'A13': {'A12': 60, 'A14': 60, 'B13': 60},
'A14': {'A13': 60, 'A15': 60, 'B14': 60},
'A15': {'A14': 60, 'A16': 60, 'B15': 60},
'A16': {'A15': 60, 'B16': 10},
'B1': {'Howard_Western': 10, 'B2': 60, 'C1': 10},
'B2': {'A2': 60, 'B1': 60, 'B3': 60, 'C2': 60},
'B3': {'A3': 60, 'B2': 60, 'B4': 60, 'C3': 60},
'B4': {'Howard_Ridge': 60, 'B3': 60, 'B5': 60, 'C4': 60},
'B5': {'A5': 60, 'B4': 60, 'B6': 60, 'C5': 60},
'B6': {'A6': 60, 'B5': 60, 'B7': 60, 'C6': 60},
'B7': {'A7': 60, 'B6': 60, 'B8': 60, 'C7': 60},
'B8': {'A8': 60, 'B7': 60, 'B9': 60, 'C8': 60},
'B9': {'A9': 10, 'B8': 60, 'B10': 60, 'Jarvis_Clark': 10},
'B10': {'Howard_L': 60, 'B9': 60, 'B11': 60, 'C10': 60},
'B11': {'A11': 60, 'B10': 60, 'B12': 60, 'C11': 60},
'B12': {'A12': 60, 'B11': 60, 'B13': 60, 'Jarvis_L': 60},
'B13': {'A13': 60, 'B12': 60, 'B14': 60, 'C13': 60},
'B14': {'A14': 60, 'B13': 60, 'B15': 60, 'C14': 60},
'B15': {'A15': 60, 'B14': 60, 'B16': 60, 'C15': 60},
'B16': {'A16': 10, 'B15': 60, 'C16': 10},
'C1': {'B1': 10, 'C2': 60, 'D1': 10},
'C2': {'B2': 60, 'C1': 60, 'C3': 60, 'D2': 60},
'C3': {'B3': 60, 'C2': 60, 'C4': 60, 'D3': 60},
'C4': {'B4': 60, 'C3': 60, 'C5': 60, 'D4': 60},
'C5': {'B5': 60, 'C4': 60, 'C6': 60, 'D5': 60},
'C6': {'B6': 60, 'C5': 60, 'C7': 60, 'D6': 60},
'C7': {'B7': 60, 'C6': 60, 'C8': 60, 'D7': 60},
'C8': {'B8': 60, 'C7': 60, 'Jarvis_Clark': 60, 'D8': 60},
'Jarvis_Clark': {'B9': 10, 'C8': 60, 'C10': 60, 'D9': 10},
'C10': {'B10': 60, 'Jarvis_Clark': 60, 'C11': 60, 'D10': 60},
'C11': {'B11': 60, 'C10': 60, 'Jarvis_L': 60, 'D11': 60},
'Jarvis_L': {'B12': 60, 'C11': 60, 'C13': 60, 'D12': 60, 'Howard_L': 20, 'Morse_L': 20},
'C13': {'B13': 60, 'Jarvis_L': 60, 'C14': 60, 'D13': 60},
'C14': {'B14': 60, 'C13': 60, 'C15': 60, 'D14': 60},
'C15': {'B15': 60, 'C14': 60, 'C16': 60, 'D15': 60},
'C16': {'B16': 10, 'C15': 60, 'D16': 10},
'D1': {'C1': 10, 'D2': 60, 'E1': 10},
'D2': {'C2': 60, 'D1': 60, 'D3': 60, 'E2': 60},
'D3': {'C3': 60, 'D2': 60, 'D4': 60, 'E3': 60},
'D4': {'C4': 60, 'D3': 60, 'D5': 60, 'E4': 60},
'D5': {'C5': 60, 'D4': 60, 'D6': 60, 'E5': 60},
'D6': {'C6': 60, 'D5': 60, 'D7': 60, 'E6': 60},
'D7': {'C7': 60, 'D6': 60, 'D8': 60, 'E7': 60},
'D8': {'C8': 60, 'D7': 60, 'D9': 60, 'E8': 60},
'D9': {'Jarvis_Clark': 10, 'D8': 60, 'D10': 60, 'Touhy_Clark': 10},
'D10': {'C10': 60, 'D9': 60, 'D11': 60, 'E10': 60},
'D11': {'C11': 60, 'D10': 60, 'D12': 60, 'E11': 60},
'D12': {'Jarvis_L': 60, 'D11': 60, 'D13': 60, 'E12': 60},
'D13': {'C13': 60, 'D12': 60, 'D14': 60, 'E13': 60},
'D14': {'C14': 60, 'D13': 60, 'D15': 60, 'Touhy_Glenwood': 60},
'D15': {'C15': 60, 'D14': 60, 'D16': 60, 'E15': 60},
'D16': {'C16': 10, 'D15': 60, 'E16': 10},
'E1': {'D1': 10, 'E2': 60, 'F1': 10},
'E2': {'D2': 60, 'E1': 60, 'E3': 60, 'F2': 60},
'E3': {'D3': 60, 'E2': 60, 'E4': 60, 'F3': 60},
'E4': {'D4': 60, 'E3': 60, 'E5': 60, 'F4': 60},
'E5': {'D5': 60, 'E4': 60, 'E6': 60, 'F5': 60},
'E6': {'D6': 60, 'E5': 60, 'E7': 60, 'F6': 60},
'E7': {'D7': 60, 'E6': 60, 'E8': 60, 'F7': 60},
'E8': {'D8': 60, 'E7': 60, 'Touhy_Clark': 60, 'F8': 60},
'Touhy_Clark': {'D9': 10, 'E8': 60, 'E10': 60, 'F9': 10},
'E10': {'D10': 60, 'Touhy_Clark': 60, 'E11': 60, 'F10': 60},
'E11': {'D11': 60, 'E10': 60, 'E12': 60, 'F11': 60},
'E12': {'D12': 60, 'E11': 60, 'E13': 60, 'F12': 60},
'E13': {'D13': 60, 'E12': 60, 'Touhy_Glenwood': 60, 'F13': 60},
'Touhy_Glenwood': {'D14': 60, 'E13': 60, 'E15': 60, 'F14': 60},
'E15': {'D15': 60, 'Touhy_Glenwood': 60, 'E16': 60, 'F15': 60},
'E16': {'D16': 10, 'E15': 60, 'F16': 10},
'F1': {'E1': 10, 'F2': 60, 'G1': 10},
'F2': {'E2': 60, 'F1': 60, 'F3': 60, 'G2': 60},
'F3': {'E3': 60, 'F2': 60, 'F4': 60, 'G3': 60},
'F4': {'E4': 60, 'F3': 60, 'F5': 60, 'G4': 60},
'F5': {'E5': 60, 'F4': 60, 'F6': 60, 'G5': 60},
'F6': {'E6': 60, 'F5': 60, 'F7': 60, 'G6': 60},
'F7': {'E7': 60, 'F6': 60, 'F8': 60, 'G7': 60},
'F8': {'E8': 60, 'F7': 60, 'F9': 60, 'G8': 60},
'F9': {'Touhy_Clark': 10, 'F8': 60, 'F10': 60, 'G9': 10},
'F10': {'E10': 60, 'F9': 60, 'F11': 60, 'G10': 60},
'F11': {'E11': 60, 'F10': 60, 'F12': 60, 'G11': 60},
'F12': {'E12': 60, 'F11': 60, 'F13': 60, 'G12': 60},
'F13': {'E13': 60, 'F12': 60, 'F14': 60, 'G13': 60},
'F14': {'Touhy_Glenwood': 60, 'F13': 60, 'F15': 60, 'G14': 60},
'F15': {'E15': 60, 'F14': 60, 'F16': 60, 'G15': 60},
'F16': {'E16': 10, 'F15': 60, 'Greenleaf_Sheridan': 10},
'G1': {'F1': 10, 'G2': 60, 'Lunt_Western': 10},
'G2': {'F2': 60, 'G1': 60, 'G3': 60, 'H2': 60},
'G3': {'F3': 60, 'G2': 60, 'G4': 60, 'H3': 60},
'G4': {'F4': 60, 'G3': 60, 'G5': 60, 'H4': 60},
'G5': {'F5': 60, 'G4': 60, 'G6': 60, 'H5': 60},
'G6': {'F6': 60, 'G5': 60, 'G7': 60, 'H6': 60},
'G7': {'F7': 60, 'G6': 60, 'G8': 60, 'H7': 60},
'G8': {'F8': 60, 'G7': 60, 'G9': 60, 'H8': 60},
'G9': {'F9': 10, 'G8': 60, 'G10': 60, 'Lunt_Clark': 10},
'G10': {'F10': 60, 'G9': 60, 'G11': 60, 'H10': 60},
'G11': {'F11': 60, 'G10': 60, 'G12': 60, 'H11': 60},
'G12': {'F12': 60, 'G11': 60, 'G13': 60, 'H12': 60},
'G13': {'F13': 60, 'G12': 60, 'G14': 60, 'H13': 60},
'G14': {'F14': 60, 'G13': 60, 'G15': 60, 'H14': 60},
'G15': {'F15': 60, 'G14': 60, 'Greenleaf_Sheridan': 60, 'H15': 60},
'Greenleaf_Sheridan': {'F16': 10, 'G15': 60, 'H16': 10},
'Lunt_Western': {'G1': 10, 'H2': 10, 'I1': 10},
'H2': {'G2': 60, 'Lunt_Western': 10, 'H3': 10, 'I2': 60},
'H3': {'G3': 60, 'H2': 10, 'H4': 10, 'I3': 60},
'H4': {'G4': 60, 'H3': 10, 'H5': 10, 'I4': 60},
'H5': {'G5': 60, 'H4': 10, 'H6': 10, 'I5': 60},
'H6': {'G6': 60, 'H5': 10, 'H7': 10, 'I6': 60},
'H7': {'G7': 60, 'H6': 10, 'H8': 10, 'I7': 60},
'H8': {'G8': 60, 'H7': 10, 'Lunt_Clark': 10, 'I8': 60},
'Lunt_Clark': {'G9': 10, 'H8': 10, 'H10': 10, 'I9': 10},
'H10': {'G10': 60, 'Lunt_Clark': 10, 'H11': 10, 'I10': 60},
'H11': {'G11': 60, 'H10': 10, 'H12': 10, 'I11': 60},
'H12': {'G12': 60, 'H11': 10, 'H13': 10, 'I12': 60},
'H13': {'G13': 60, 'H12': 10, 'H14': 10, 'I13': 60},
'H14': {'G14': 60, 'H13': 10, 'H15': 10, 'Morse_L': 60},
'H15': {'G15': 60, 'H14': 10, 'H16': 10, 'I15': 60},
'H16': {'Greenleaf_Sheridan': 10, 'H15': 10, 'I16': 10},
'I1': {'Lunt_Western': 10, 'I2': 60, 'J1': 10},
'I2': {'H2': 60, 'I1': 60, 'I3': 60, 'J2': 60},
'I3': {'H3': 60, 'I2': 60, 'I4': 60, 'J3': 60},
'I4': {'H4': 60, 'I3': 60, 'I5': 60, 'J4': 60},
'I5': {'H5': 60, 'I4': 60, 'I6': 60, 'J5': 60},
'I6': {'H6': 60, 'I5': 60, 'I7': 60, 'J6': 60},
'I7': {'H7': 60, 'I6': 60, 'I8': 60, 'J7': 60},
'I8': {'H8': 60, 'I7': 60, 'I9': 60, 'J8': 60},
'I9': {'Lunt_Clark': 10, 'I8': 60, 'I10': 60, 'J9': 10},
'I10': {'H10': 60, 'I9': 60, 'I11': 60, 'J10': 60},
'I11': {'H11': 60, 'I10': 60, 'I12': 60, 'J11': 60},
'I12': {'H12': 60, 'I11': 60, 'I13': 60, 'J12': 60},
'I13': {'H13': 60, 'I12': 60, 'Morse_L': 60, 'J13': 60},
'Morse_L': {'H14': 60, 'I13': 60, 'I15': 60, 'J14': 60, 'Jarvis_L': 20},
'I15': {'H15': 60, 'Morse_L': 60, 'I16': 60, 'J15': 60},
'I16': {'H16': 10, 'I15': 60, 'J16': 10},
'J1': {'I1': 10, 'J2': 60, 'K1': 10},
'J2': {'I2': 60, 'J1': 60, 'J3': 60, 'K2': 60},
'J3': {'I3': 60, 'J2': 60, 'J4': 60, 'K3': 60},
'J4': {'I4': 60, 'J3': 60, 'J5': 60, 'Pratt_Ridge': 60},
'J5': {'I5': 60, 'J4': 60, 'J6': 60, 'K5': 60},
'J6': {'I6': 60, 'J5': 60, 'J7': 60, 'K6': 60},
'J7': {'I7': 60, 'J6': 60, 'J8': 60, 'K7': 60},
'J8': {'I8': 60, 'J7': 60, 'J9': 60, 'K8': 60},
'J9': {'I9': 10, 'J8': 60, 'J10': 60, 'K9': 10},
'J10': {'I10': 60, 'J9': 60, 'J11': 60, 'K10': 60},
'J11': {'I11': 60, 'J10': 60, 'J12': 60, 'K11': 60},
'J12': {'I12': 60, 'J11': 60, 'J13': 60, 'K12': 60},
'J13': {'I13': 60, 'J12': 60, 'J14': 60, 'Home': 60},
'J14': {'Morse_L': 60, 'J13': 60, 'J15': 60, 'K14': 60},
'J15': {'I15': 60, 'J14': 60, 'J16': 60, 'K15': 60},
'J16': {'I16': 10, 'J15': 60, 'K16': 10},
'K1': {'J1': 10, 'K2': 10, 'L1': 10},
'K2': {'J2': 60, 'K1': 10, 'K3': 10, 'L2': 60},
'K3': {'J3': 60, 'K2': 10, 'Pratt_Ridge': 10, 'L3': 60},
'Pratt_Ridge': {'J4': 60, 'K3': 10, 'K5': 10, 'L4': 60},
'K5': {'J5': 60, 'Pratt_Ridge': 10, 'K6': 10, 'L5': 60},
'K6': {'J6': 60, 'K5': 10, 'K7': 10, 'L6': 60},
'K7': {'J7': 60, 'K6': 10, 'K8': 10, 'L7': 60},
'K8': {'J8': 60, 'K7': 10, 'K9': 10, 'L8': 60},
'K9': {'J9': 10, 'K8': 10, 'K10': 10, 'Columbia_Clark': 10},
'K10': {'J10': 60, 'K9': 10, 'K11': 10, 'L10': 60},
'K11': {'J11': 60, 'K10': 10, 'K12': 10, 'L11': 60},
'K12': {'J12': 60, 'K11': 10, 'Home': 10, 'L12': 60},
'Home': {'J13': 60, 'K12': 10, 'K14': 10, 'L13': 60},
'K14': {'J14': 60, 'Home': 10, 'K15': 10, 'L14': 60},
'K15': {'J15': 60, 'K14': 10, 'K16': 10, 'L15': 60},
'K16': {'J16': 10, 'K15': 10, 'Columbia_Sheridan': 10},
'L1': {'K1': 10, 'L2': 60},
'L2': {'K2': 60, 'L1': 60, 'L3': 60},
'L3': {'K3': 60, 'L2': 60, 'L4': 60},
'L4': {'Pratt_Ridge': 60, 'L3': 60, 'L5': 60},
'L5': {'K5': 60, 'L4': 60, 'L6': 60},
'L6': {'K6': 60, 'L5': 60, 'L7': 60},
'L7': {'K7': 60, 'L6': 60, 'L8': 60},
'L8': {'K8': 60, 'L7': 60, 'Columbia_Clark': 60},
'Columbia_Clark': {'K9': 10, 'L8': 60, 'L10': 60},
'L10': {'K10': 60, 'Columbia_Clark': 60, 'L11': 60},
'L11': {'K11': 60, 'L10': 60, 'L12': 60},
'L12': {'K12': 60, 'L11': 60, 'L13': 60},
'L13': {'Home': 60, 'L12': 60, 'L14': 60},
'L14': {'K14': 60, 'L13': 60, 'L15': 60},
'L15': {'K15': 60, 'L14': 60, 'Columbia_Sheridan': 60},
'Columbia_Sheridan': {'K16': 10, 'L15': 60}}

#dijkstra method from slides repurposed
def dijkstra(G, s):
    D, P, Q, S = {s:0}, {}, [(0,s)], set()
    while Q:
        _,u=heappop(Q)
        if u in S: continue
        S.add(u)
        for v in G[u]:
            relax(G,u,v,D,P)
            heappush(Q,(D[v],v))
            #print(u,v,D)
    return D

inf = float('inf')
#Relax method from slides repurposed
def relax(graph, startNode, endNode, Distances, Pred):
    d = Distances.get(startNode, inf) + graph[startNode][endNode]
    if d < Distances.get(endNode, inf):
        Distances[endNode], Pred[endNode] = d, object
        return True
    
print(dijkstra(RP, "Home"))
