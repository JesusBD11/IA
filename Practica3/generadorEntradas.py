import random

def writeFile(n_dias, n_tipos, n_platos, diasObligatorios, platosObligatorios, incomp, ext, exten):
    f = open("problema" + str(exten) + ".pddl","w")

    f.write("(define (problem problema1)\n")

    f.write("\t(:domain planificacion)\n")

    f.write("\t(:objects ")

    for i in range(n_platos):
        f.write("P" + str(i) + " ")
    f.write("- plato\n")
    f.write("\t")

    for i in range(n_dias):
        f.write("d" + str(i) + " ")
    f.write("- dia\n")
    f.write("\t")

    if ext >=2:
        for i in range(n_tipos):
            f.write(chr(i + 65) + " ")
        f.write("- tipoPlato")
    f.write(")\n\n")

    f.write("\t(:init\n\n")

    for el in incomp:
        f.write("\t\t(incompatibles P" + str(el[0]) + " P" + str(el[1]) +")\n")
    f.write("\n")

    aux = int(n_platos/2)
    for i in range(aux):
        f.write("\t\t(primerPlato P" + str(i) + ")\n")
    f.write("\n")

    for i in range(aux, n_platos):
        f.write("\t\t(segundoPlato P" + str(i) + ")\n")
    f.write("\n")

    if ext >=2:
        for i in range(n_platos):
            aux = random.randint(0, n_tipos - 1)
            f.write("\t\t(tipoDePlato P" + str(i) + " " + chr(aux + 65) + ")\n")
        f.write("\n")

    if ext >=2:
        for i in range(n_dias - 1):
            f.write("\t\t(consecutivos d"+str(i)+" d"+str(i+1)+")\n")
        f.write("\n")

    if ext >= 3:
        for i in range(0,len(diasObligatorios)):
            f.write("\t\t(platoObligatorio P" + str(platosObligatorios[i]) + " d" + str(diasObligatorios[i]) +")\n")
        f.write("\n")

        for i in range(0,len(diasObligatorios)):
            f.write("\t\t(diaObligatorio d" + str(diasObligatorios[i]) +")\n")
        f.write("\n")

    if ext >= 4:
        for i in range(n_platos):
            aux = random.randint(450, 900)
            f.write("\t\t(=(caloriasPlato P" + str(i) + " )" + str(aux) + ")\n")
        f.write("\n")


    if ext >= 5:
        f.write("(= (precio-Total) 0)\n")
        for i in range(n_platos):

            aux = random.randint(5, 30)
            f.write("\t\t(=(precioPlato P" + str(i) + " )" + str(aux) + ")\n")
        f.write("\n")

    f.write ("\t)\n\n")
    f.write ("(:goal ( forall (?d - dia) (diaPlanificado ?d) ) )\n")

    if ext == 5:
        f.write("(:metric minimize (precio-Total))")
    f.write ("\t)")


if __name__ == '__main__':
    for exten in range (0,12):
        ext = int (exten/2)
        n_dias = 5
        n_platos = random.randint(n_dias*2, n_dias*3)
        n_tipos = random.randint(int((2*n_platos)/3), n_platos)
        diasObligatorios = []
        platosObligatorios = []
        incomp = set()

        aux = random.randint(1, int(n_platos/3))
        for i in range(aux):
            aux2 = int(n_platos / 2)
            j = random.randint(0, aux2)
            k = random.randint(aux2 + 1, n_platos - 1)
            t = (j, k)
            incomp.add(t)

        aux = random.randint(1,2)
        for i in range(aux):
            j = random.randint(0,n_dias-1)
            while j in diasObligatorios:
                j = random.randint(0,n_dias-1)
            k = random.randint(0, n_platos-1)
            while k in platosObligatorios:
                k = random.randint(0, n_platos-1)
            diasObligatorios.append(j)
            platosObligatorios.append(k)

        writeFile(n_dias, n_tipos, n_platos, diasObligatorios, platosObligatorios, incomp, ext, exten)
