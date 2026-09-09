import basal_python_repetition

# Alle følgende funktioner er testfunktioner
# Din opgave er at oprette dem i filen basal_python_repetition.py
# fx. skal der oprettes en funktion navngivet return_hello
# return_hello-funktionen skal returnere en string "Hello, World!"
# når filen basal_python_repetition pushes til github vil testen køres
# Efterfølgende kan man se på github hvordan testen gik.
# når 100 points er givet på github er alle tests fuldført.

# OBS DENNE FIL MED TESTFUNKTIONERNE MÅ DER IKKE ÆNDRES I!

# lav funktionen return_hello, så at testen fuldføres
def test_return_hello():
    assert basal_python_repetition.return_hello() == "Hello, World!"
