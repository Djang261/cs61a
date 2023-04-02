from ants import *
beehive, layout = Hive(AssaultPlan()), dry_layout
dimensions = (1, 9)
gamestate = GameState(None, beehive, ant_types(), layout, dimensions)

# case 8
# scary = ScaryThrower()
# slow = SlowThrower()
# bee = Bee(3)
# gamestate.places["tunnel_0_0"].add_insect(scary)
# gamestate.places["tunnel_0_1"].add_insect(slow)
# gamestate.places["tunnel_0_3"].add_insect(bee)
# scary.action(gamestate) # scare bee once

# print(bee.pre_actions)

# gamestate.time = 0
# bee.action(gamestate) # scared
# print(bee.place.name)      #'tunnel_0_4'
# for _ in range(3): # slow bee three times
#    slow.action(gamestate)

# print(bee.slow_turn, bee.scare_turn)
# print(bee.pre_actions)

# gamestate.time = 1
# bee.action(gamestate) # scared, but also slowed thrice
# print("time1\n" + bee.place.name)      #'tunnel_0_4'
# print(bee.slow_turn, bee.scare_turn)
# print(bee.pre_actions)

# gamestate.time = 2
# bee.action(gamestate) # scared and slowed thrice
# print("\ntime2\n" + bee.place.name)      #'tunnel_0_5'
# print(bee.slow_turn, bee.scare_turn)
# print(bee.pre_actions)

# gamestate.time = 3
# bee.action(gamestate) # slowed thrice
# print("\ntime3\n" + bee.place.name)      #'tunnel_0_5'
# print(bee.slow_turn, bee.scare_turn)
# print(bee.pre_actions)

# gamestate.time = 4
# bee.action(gamestate) # slowed twice
# print("\ntime4\n" + bee.place.name)      #'tunnel_0_4'
# print(bee.slow_turn, bee.scare_turn)
# print(bee.pre_actions)

# gamestate.time = 5
# bee.action(gamestate) # slowed twice
# print("\ntime5\n" + bee.place.name)      #'tunnel_0_4'
# print(bee.slow_turn, bee.scare_turn)
# print(bee.pre_actions)

# gamestate.time = 6
# bee.action(gamestate) # slowed once
# print("\ntime6\n" + bee.place.name)      #'tunnel_0_3'
# print(bee.slow_turn, bee.scare_turn)
# print(bee.pre_actions)

# gamestate.time = 7
# bee.action(gamestate) # statuses have worn off
# print("\ntime7\n" + bee.place.name)      #'tunnel_0_2'
# print(bee.slow_turn, bee.scare_turn)
# print(bee.pre_actions)


# case 9
# scary = ScaryThrower()  # suit 1 case 9
# slow = SlowThrower()
# bee = Bee(3)
# gamestate.places["tunnel_0_0"].add_insect(scary)
# gamestate.places["tunnel_0_1"].add_insect(slow)
# gamestate.places["tunnel_0_3"].add_insect(bee)
# slow.action(gamestate) # slow bee
# scary.action(gamestate) # scare bee

# print(bee.place.name)   #'tunnel_0_3'
# # print(bee.pre_actions)
# print(bee.slow_turn, bee.scare_turn)
# print("\n")

# gamestate.time = 0
# bee.action(gamestate) # scared and slowed
# print("time0\n" + bee.place.name)   #'tunnel_0_4'
# print(bee.slow_turn, bee.scare_turn)
# print("\n")

# gamestate.time = 1
# bee.action(gamestate) # scared and slowed
# print("time1\n" + bee.place.name)   #'tunnel_0_4'
# print(bee.slow_turn, bee.scare_turn)
# print(bee.pre_actions)
# print(bee.real_action)
# print("\n")

# gamestate.time = 2
# bee.action(gamestate) # slowed
# print("time2\n" + bee.place.name)   #'tunnel_0_3'
# print(bee.slow_turn, bee.scare_turn)
# print(bee.pre_actions)
# print(bee.real_action)

# test for myself
def info(n):
    print(f"time{n}\n{bee.place.name}")      #'tunnel_0_4'
    print(f"{bee.slow_turn} {bee.scare_turn}\n")
   #  print(bee.pre_actions)

scary = ScaryThrower()
slow = SlowThrower()
bee = Bee(3)
gamestate.places["tunnel_0_0"].add_insect(scary)
gamestate.places["tunnel_0_1"].add_insect(slow)
gamestate.places["tunnel_0_7"].add_insect(bee)

print(f"{bee.place.name}\n")      #'tunnel_0_4'
for _ in range(3): # slow bee three times
    slow.action(gamestate)

for i in range(1,3):
   gamestate.time = i
   bee.action(gamestate)
   info(i)

slow.action(gamestate)
scary.action(gamestate)

for i in range(3,8):
   gamestate.time = i
   bee.action(gamestate)
   info(i)
