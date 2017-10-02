'''
Compiler Construction - UCS704

Anshul Aggarwal
101410007

Converting Thompson's Construction NFA to DFA using Subset construction
Regular Expression      (a|b)*abb

e -> epsilon
'''

#NFA Tranition table for given Regular Expression

#      a   b   e
T = [[[], [], [1,7]],    #0
     [[], [], [2,4]],    #1
     [[3], [], []],      #2
     [[], [], [6]],      #3
     [[], [5], []],      #4
     [[], [], [6]],      #5
     [[], [], [1,7]],    #6
     [[8], [], []],      #7
     [[], [9], []],      #8
     [[], [10], []],     #9
     [[], [], []],       #10
    ]

S_0 = 0   #Start state
finalNFAstate = 10
highest_stateno = 0
S = []
DFA = []
DFA_finalstates = []

def epsilon_closure(state, closure):
    closure = closure + [state]
    for i in T[state][2]:
        closure = closure + epsilon_closure(i, closure)
    return closure

def stateset_compare(stateset):
    global highest_stateno, S
    flag = -1
    for i in range(0,len(S)):
        if set(S[i]) == set(stateset):
            return i
        else:
             flag = i
    if flag == len(S)-1:
        S.append(stateset)
        highest_stateno = flag + 1
        #print(str(highest_stateno) + "\tHello\t" + str(stateset))
        return (highest_stateno) 

def move(stateset, transition):
    index = -1
    if transition == 'a':
        index = 0
    elif transition == 'b':
        index = 1
    newstate = []
    for state in stateset:
        for j in range(len(T[state][index])):
            newstate = newstate + list(set(epsilon_closure(T[state][index][j], [])))
            #print(stateset, transition, state, j, newstate)
    targetstate = stateset_compare(newstate)
    return targetstate

def find_Final_DFA_states():
    final_list = []
    for i in range(len(S)):
        if finalNFAstate in S[i]:
            final_list.append(i)
    return final_list
        
def string_test(test_str, indx, cur_state):
    a = 0
    charid = 0
    if test_str[indx] == 'b':
        charid = 1
    new_state = DFA[cur_state][charid]
    print("S" + str(new_state),end='')
    if (indx + 1) < len(test_str):
        print(" -> ",end='')
        string_test(test_str, indx + 1, new_state)
    else:
        if new_state in DFA_finalstates:
            print("\nString accepted")
        else:
            print("\nString not accepted")

init_state = list(set(epsilon_closure(S_0, [])))
highest_stateno = stateset_compare(init_state)

ctr = 0
while(True):
    DFA.append([])
    target_a = move(S[ctr], 'a')
    DFA[ctr].append(target_a)
    print("Move S" + str(ctr) + ", a to S" + str(target_a))
    target_b = move(S[ctr], 'b')
    DFA[ctr].append(target_b)
    print("Move S" + str(ctr) + ", b to S" + str(target_b))
    if ctr == highest_stateno:
        break
    ctr = ctr + 1

print("\n\nSt\ta\tb\n-------------------")
for i in range(len(DFA)):
    print("S"+ str(i) + "\tS" + str(DFA[i][0]) + "\tS" + str(DFA[i][1]))

DFA_finalstates = find_Final_DFA_states()

test_str = input("\n\nPlease enter a string to test: ")
print("S0 -> ",end='')
string_test(test_str, 0, 0)
