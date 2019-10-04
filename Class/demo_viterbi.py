


def Viterbi(observations,states,start_p,trans_p,emis_p):
    """viterbi algorithm
    Output : labels estimated"""
    V = {} # present state

    for i in states:
        V[i] = (start_p[i]* emis_p[i][observations[0]],[i])
    for j in observations[1:]:
        V = next_state(j,states,V,trans_p,emis_p)
        print(V)

    prob,labels = max([V[i] for i in V])

    return prob,labels


def next_state(ob,states,V,tp,ep):

    U = {}
    for next_s in states:
        U[next_s] = (0,[])
        for now_s in states:
            p = V[now_s][0] * tp[now_s][next_s] * ep[next_s][ob]
            if p>U[next_s][0]:
                U[next_s] = [p,V[now_s][1]+[next_s]]
    return U

def main():
    states = ("F", "L")

    observations = 315116246446644245311321631164152133625144543631656626566666
    observations = str(observations)

    start_prob = {"F": 0.5, "L": 0.5}
    transit_prob = {"F": {"F": 0.95, "L": 0.05},
                    "L": {"F": 0.1, "L": 0.9}}
    emission_prob = {'F': {'1': 1 / 6, '2': 1 / 6, '3': 1 / 6, '4': 1 / 6, '5': 1 / 6, '6': 1 / 6},
                     'L': {'1': 1 / 10, '2': 1 / 10, '3': 1 / 10, '4': 1 / 10, '5': 1 / 10, '6': 1 / 2}}

    print (observations)
    probability,state = Viterbi(observations,states,
                  start_prob,transit_prob,emission_prob)
    print(''.join(map(str, state)))
    print (probability)

main()