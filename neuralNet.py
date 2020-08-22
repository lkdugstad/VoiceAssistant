import re

# input stil (String, String) (Categeory, Sentence) Tuple
stop_words = {'aber', 'alle', 'allem', 'allen', 'aller', 'alles', 'als', 'also', 'am', 'an', 'ander', 'andere',
              'anderem', 'anderen', 'anderer', 'anderes', 'anderm', 'andern', 'anders', 'auch', 'auf', 'aus', 'bei',
              'bin', 'bis', 'bist', 'da', 'damit', 'dann', 'das', 'dass', 'dasselbe', 'dazu', 'daß', 'dein', 'deine',
              'deinem', 'deinen', 'deiner', 'deines', 'dem', 'demselben', 'den', 'denn', 'denselben', 'der', 'derer',
              'derselbe', 'derselben', 'des', 'desselben', 'dessen', 'dich', 'die', 'dies', 'diese', 'dieselbe',
              'dieselben', 'diesem', 'diesen', 'dieser', 'dieses', 'dir', 'doch', 'dort', 'du', 'durch', 'ein', 'eine',
              'einem', 'einen', 'einer', 'eines', 'einig', 'einige', 'einigem', 'einigen', 'einiger', 'einiges',
              'einmal', 'er', 'es', 'etwas', 'euch', 'euer', 'eure', 'eurem', 'euren', 'eurer', 'eures', 'für',
              'gegen', 'gewesen', 'hab', 'habe', 'haben', 'hat', 'hatte', 'hatten', 'hier', 'hin', 'hinter', 'ich',
              'ihm', 'ihn', 'ihnen', 'ihr', 'ihre', 'ihrem', 'ihren', 'ihrer', 'ihres', 'im', 'in', 'indem', 'ins',
              'ist', 'jede', 'jedem', 'jeden', 'jeder', 'jedes', 'jene', 'jenem', 'jenen', 'jener', 'jenes', 'jetzt',
              'kann', 'kein', 'keine', 'keinem', 'keinen', 'keiner', 'keines', 'können', 'könnte', 'machen', 'man',
              'manche', 'manchem', 'manchen', 'mancher', 'manches', 'mein', 'meine', 'meinem', 'meinen', 'meiner',
              'meines', 'mich', 'mir', 'mit', 'muss', 'musste', 'nach', 'nicht', 'nichts', 'noch', 'nun', 'nur', 'ob',
              'oder', 'ohne', 'sehr', 'sein', 'seine', 'seinem', 'seinen', 'seiner', 'seines', 'selbst', 'sich', 'sie',
              'sind', 'so', 'solche', 'solchem', 'solchen', 'solcher', 'solches', 'soll', 'sollte', 'sondern', 'sonst',
              'um', 'und', 'uns', 'unser', 'unsere', 'unserem', 'unseren', 'unserer', 'unseres', 'unter', 'viel',
              'vom', 'von', 'vor', 'war', 'waren', 'warst', 'was', 'weg', 'weil', 'weiter', 'welche', 'welchem',
              'welchen', 'welcher', 'welches', 'wenn', 'werde', 'werden', 'wie', 'wieder', 'will', 'wir', 'wird',
              'wirst', 'wo', 'wollen', 'wollte', 'während', 'würde', 'würden', 'zu', 'zum', 'zur', 'zwar', 'zwischen',
              'über'}

s = {'Today','is','my','lucky','day,','because','today','is','Thanksgiving','day!'}
s = ' '.join(s)
print(re.findall(r'[A-Z]',s))

# Vorherige Filterung nach Schlagwörtern könnte alles nochmal verbessern. Also wenn whatsapp kommt oder Licht, dass
# nur whatsapp bzw. Licht ins NN gegeben wird

categorien = {'licht', 'aktien', 'depot', 'plus', 'uhr', 'timer', 'whatsapp', 'depot'}
string = "Schalte das Licht im Wohnzimmer auf blau"
string = string.lower()
setA = set(string.split(" "))
# todo wörter sollten nicht in ihrere Reihenfolge geändert werden

erg = list(setA.difference(stop_words))

fullStr = ' '.join(erg)
print(fullStr)

output = ""
for x in fullStr:
    print(x)
    unPad = str(ord(x))
    if len(unPad) != 3:
        unPad = ('0'+unPad)
    output += unPad
if len(output) < 90:
    count = 120-len(output)
    for i in range (0, count):
        output += '0'
if len(output) > 90:
    print("Achtung", len(output))
print(output)


