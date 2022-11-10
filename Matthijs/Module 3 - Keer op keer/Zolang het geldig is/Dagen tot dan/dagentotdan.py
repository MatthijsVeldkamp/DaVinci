print("Welke dag is het?")
dag = input("? ")
if dag.lower() == ("ma") or dag.lower() == ("maandag"):
    print("Maandag!")
elif dag.lower() == ("di") or dag.lower() == ("dinsdag"):
    print("Maandag, "+"dinsdag")
elif dag.lower() == ("wo") or dag.lower() == ("woensdag"):
    print("Maandag, "+"dinsdag, "+"woensdag")
elif dag.lower() == ("do") or dag.lower() == ("donderdag"):
    print("Maandag, "+"dinsdag, "+"woensdag, "+"donderdag")
elif dag.lower() == ("vr") or dag.lower() == ("vrijdag"):
    print("Maandag, "+"dinsdag, "+"woensdag, "+"donderdag, "+"vrijdag")
elif dag.lower() == ("za") or dag.lower() == ("zaterdag"):
    print("Maandag, "+"dinsdag, "+"woensdag, "+"donderdag, "+"vrijdag, "+"zaterdag")
elif dag.lower() == ("zo") or dag.lower() == ("zondag"):
    print("Maandag, "+"dinsdag, "+"woensdag, "+"donderdag, "+"vrijdag, "+"zaterdag, "+"zondag")
else:
    print("U heeft iets fout ingevuld.")