from jacco import *
from merijn import *
from dodo import *
from bey import *

def teamName():
    return "This is team READUS. We are: " + myName() + ", " + merijn() + ", " + function() + ", " + bey()

print(teamName())

char1 = char_1()
char2 = char_2()
char3 = char_3()
char4 = char_4()


print(paragraph1(char2, char3, char4), merijn_act_1(char1, char2, char4), act1p3(char1, char3, char4), dodo_act1(char1, char2, char3))
print(paragraph2(char2, char3, char4), merijn_act_2(char1, char2, char4), act2p3(char1, char3, char4), dodo_act2(char1, char2, char3))
print(paragraph3(char2, char3, char4), merijn_act_3(char1, char2, char4), act3p3(char1, char3, char4), dodo_act3(char1, char2, char3))