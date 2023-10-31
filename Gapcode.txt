# GAP Code Verifing Computation in Hollering and Sullivant
G:=Group((1,2,3,5,7,88)(4,6,9,13,20,31)(8,12,18,28,41,57)(10,15,23,35,48,64)(11,17,26,39,53,68)(14,22,34,46,58,72)(16,25,37,50,60,24)(19,30,43,61,74,36)(21,33,45,54,69,81)(27,40,55,70,82,84)(29,42,59)(32,44,51,90,78,87)(38,52,66)(47,63,73,62,75,85)(49,65,76,79,67,80)(56,71,83)(77,86,89)(91,92)(93,94,95,97,100,103)(96,99,102)(98,101,104),  (2,4)(5,8)(6,10)(7,11)(9,14)(12,19)(13,21)(15,24)(16,88)(17,27)(18,29)(20,32)(22,33)(23,36)(25,38)(30,31)(34,47)(35,49)(37,51)(39,54)(40,56)(41,58)(42,60)(44,62)(45,48)(46,55)(52,67)(57,71)(59,73)(61,69)(63,72)(65,77)(68,80)(74,84)(75,78)(79,90)(81,87)(82,86)(85,89)(92,93)(94,96)(95,98)(99,103)(100,101)(104,105));;

PairsOfTrees:=UnorderedTuples([1..105],2);;

PairsOfPairs:=IteratorOfTuples(PairsOfTrees,2);;

PairEqual := function(P1,P2)

   return (P1 = P2) or ((P1[1] = P2[2]) and (P1[2] = P2[1]));
   end;;

PairPairEqual:=function(PP1,PP2)

   return (PairEqual(PP1[1],PP2[1]) and PairEqual(PP1[2],PP2[2])) or (PairEqual(PP1[1],PP2[2]) and PairEqual(PP1[2],PP2[1]));
   end;;
   
TotalFixed:=0;;
Elts:=Elements(G);;
for g in Elts do
  PairsOfPairs:=IteratorOfCombinations(PairsOfTrees,2);;
  NFix:=0;
  for PP in PairsOfPairs do
         PPg:=OnTuplesTuples(PP,g);
         if (PPg = PP) or ((PPg[1] = PP[2]) and (PPg[2] = PP[1])) then
             NFix:=NFix + 1;
         fi;  
  od;
  if not(NFix = 0) then
      Print(g,NFix);
  fi;
  TotalFixed:=TotalFixed+NFix;;
od;
c = (1,2,3,4,5,6);
perm:= 
  PairsOfPairs:=IteratorOfCombinations(PairsOfTrees,2);;
  NFix:=0;
  for PP in PairsOfPairs do
         PPg:=OnTuplesTuples(PP,perm);
         if PairPairEqual(PP,PPg) then
         Print(PP);
             NFix:=NFix + 1;
             
         fi;  
  od;
  NFix;
  
  PairsOfPairs:=IteratorOfCombinations(PairsOfTrees,2);;
  NFix:=0;
  for PP in PairsOfPairs do
         PPg:=OnTuplesTuples(PP,perm);
         if PairPairEqual(PP,PPg) then
             NFix:=NFix + 1;
             
         fi;  
  od;
  NFix;
  
  PairsOfPairs:=IteratorOfCombinations(PairsOfTrees,2);;
  NFix:=0;
  for PP in PairsOfPairs do
         PPg:=OnTuplesTuples(PP,t*c*t*c^5);
         if PairPairEqual(PP,PPg) then
             NFix:=NFix + 1;
             
         fi;  
  od;
  NFix;
  
   PairsOfPairs:=IteratorOfCombinations(PairsOfTrees,2);;
  NFix:=0;
  for PP in PairsOfPairs do
         PPg:=OnTuplesTuples(PP,t*c^2*t*c^4);
         if PairPairEqual(PP,PPg) then
             NFix:=NFix + 1;
             
         fi;  
  od;
  NFix;
  
  PairsOfPairs:=IteratorOfCombinations(PairsOfTrees,2);;
  NFix:=0;
  for PP in PairsOfPairs do
         PPg:=OnTuplesTuples(PP,t*c*t*c*t*c*t*c^3);
         if PairPairEqual(PP,PPg) then
             NFix:=NFix + 1;
             
         fi;  
  od;
  NFix;
  
  
  PairsOfPairs:=IteratorOfCombinations(PairsOfTrees,2);;
  NFix:=0;
  for PP in PairsOfPairs do
         PPg:=OnTuplesTuples(PP,t*c*t*c^2*t*c^3);
         if PairPairEqual(PP,PPg) then
             NFix:=NFix + 1;
             
         fi;  
  od;
  NFix;
  
  PairsOfPairs:=IteratorOfCombinations(PairsOfTrees,2);;
  NFix:=0;
  for PP in PairsOfPairs do
         PPg:=OnTuplesTuples(PP,t*c*t*c*t*c^4);
         if PairPairEqual(PP,PPg) then
             NFix:=NFix + 1;
             
         fi;  
  od;
  NFix;
  
  PairsOfPairs:=IteratorOfCombinations(PairsOfTrees,2);;
  NFix:=0;
  for PP in PairsOfPairs do
         PPg:=OnTuplesTuples(PP,t*c*t*c*t*c^2*t*c^2);
         if PairPairEqual(PP,PPg) then
             NFix:=NFix + 1;
             
         fi;  
  od;
  NFix;
