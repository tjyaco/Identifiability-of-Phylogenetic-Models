from sage.matroids.advanced import *
import random
# A Sage Implementation of Hollering and Sullivant's Exact Algorithm
def matroidSeparate(phi_1, varlist1, phi_2,varlist2, dim_1, dim_2, t):
    certset = Set({})
    jacphi1 = jacobian(phi_1,varlist1).transpose()
    jacphi2  = jacobian(phi_2,varlist2).transpose()
    vallist1 = [randrange(10) for j in range(len(varlist1))]
    vallist2 = [randrange(10) for j in range(len(varlist2))]
    numJac1 = Matrix(W,jacphi1.subs({varlist1[k]:vallist1[k] for k in range(len(varlist1))}))
    numJac2 = Matrix(W,jacphi2.subs({varlist2[k]:vallist2[k] for k in range(len(varlist2))}))
    LM1 = LinearMatroid(numJac1)
    LM2 = LinearMatroid(numJac2)
    IS1 = LM1.independent_sets()
    IS2 = LM2.independent_sets() 
    breakoutflag=False
    for j in range(1,dim_2+1):
        print(j)

        for i in range(0,t+1):
            print(i)
            trialSet = Set({})
            while len(trialSet)< j:
                y=randint(0,jacphi1.ncols()-1)
                if y not in trialSet:
                    trialSet = trialSet.union(Set({y}))
            if (trialSet in IS2) and not (trialSet in IS1):
                print((trialSet in IS2) and not (trialSet in IS1))
                if (trialSet in LinearMatroid(jacphi2).independent_sets()) and not (trialSet in LinearMatroid(jacphi1).independent_sets()):                  
                    foundCert = True
                    certset = trialSet
                    breakoutflag=True
                    break
        if breakoutflag:
            break
    return certset 
    
# A Sage Implementation of Hollering and Sullivant's Probabilistic Algorithm 
def matroidSeparateSZ(phi_1, varlist1, phi_2,varlist2, maxdeg,dim_1, dim_2, t,e):
    certset = Set({})
    jacphi1 = jacobian(phi_1,varlist1).transpose()
    jacphi2  = jacobian(phi_2,varlist2).transpose()
    vallist1 = [randrange(next_prime(3*8^18)) for j in range(len(varlist1))]
    vallist2 = [randrange(next_prime(3*8^18)) for j in range(len(varlist2))]
    numJac1 = Matrix(W,jacphi1.subs({varlist1[k]:vallist1[k] for k in range(len(varlist1))}))
    numJac2 = Matrix(W,jacphi2.subs({varlist2[k]:vallist2[k] for k in range(len(varlist2))}))
    print('matrices initialized')
    
    breakoutflag=False
    j=1
    while (j in range(1,dim_2+1)) and not breakoutflag :
        print(j)

        for i in range(0,t+1):
            print(i)
            trialSet = Set({})
            while len(trialSet)< j:
                y=randint(0,jacphi1.ncols()-1)
                if y not in trialSet:
                    trialSet = trialSet.union(Set({y}))
            if (trialSet in IS2) and not (trialSet in IS1):
                print((trialSet in IS2) and not (trialSet in IS1))
                l = ceil(log(e)/log(maxdeg/next_prime(3*8^18)))
                for k in range(1,l+1):
                    vallist1 = [randrange(next_prime(3*8^18)) for j in range(len(varlist1))]
                    numJac1 = Matrix(W,jacphi1.subs({varlist1[k]:vallist1[k] for k in range(len(varlist1))}))
                    LM1 = LinearMatroid(numJac1)
                    IS1 = LM1.independent_sets()
                    if trialSet in IS1:
                        break
                certset = trialSet
                breakoutflag=True
        j=j+1
                
    return certset    
