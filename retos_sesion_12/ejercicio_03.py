# 3.- El usuario Jhon Doe esta en una red social sus amigos son:
#     {Alice, Bob, Charlie, David, Eve}
#  La usuaria Jess Doe tiene los siguientes amigos
#     {Alice, Bob,  Frank, Grace}
# ¿Tienen Jhon y Jess amigos en común?, ¿Cuáles son?

Jhon = {'Alice', 'Bob', 'Charlie', 'David', 'Eve'}
Jess = {'Alice', 'Bob',  'Frank', 'Grace'}

if Jhon.isdisjoint(Jess):  #  son distintos
    print("No tienen amigos en comun")
else:
    print("Jhon y Less, tienen amigos en comun y son:")
    print(Jhon.intersection(Jess))
