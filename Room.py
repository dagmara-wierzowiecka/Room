import gym
import numpy as np
from gym import spaces  # , envs
import random

# docelowy nastrój użytkowników, z którym uruchamiana jest symulacja, może być tylko 2 lub 3 (z założenia systemu użytkownik dostaje tylko takie do wyboru)
user1_target_mood = 3
user2_target_mood = 2
user3_target_mood = 2
# preferencje użytkowników
user1_preferences = [
    [
        [1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # [0, 1, 0, 0, 0, 0] # time needed
    ],
    [
        [0, 0, 0, 1, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # [1, 0, 0, 0, 0, 0]  # time needed
    ],

    [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # [1, 0, 0, 0, 0, 0] # time needed
    ],
    [
        [0, 0, 1, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # [0, 1, 0, 0, 0, 0] # time needed
    ]
]
user2_preferences = [
    [
        [1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        # [1, 0, 0, 0, 0, 0] # time needed
    ],
    [
        [0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # [0, 1, 0, 0, 0, 0] # time needed
    ],
    [
        [0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # [0, 1, 0, 0, 0, 0] # time needed
    ],
    [
        [1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        # [0, 1, 0, 0, 0, 0] # time needed
    ]
]
user3_preferences = [
    [
        [1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # [0, 1, 0, 0, 0, 0] # time needed
    ],
    [
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 1, 0, 0, 0] # time needed
    ],
    [
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 1, 0, 0, 0] # time needed
    ],
    [
        [1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # [1, 0, 0, 0, 0, 0] # time needed
    ]
]

# grupa wiekowa 18-24
group_1_default_preferences = [
    # scenariusz A
    [
        [2, 0, 0, 0, 0],  # light intensity
        [0, 0, 2, 1, 0, 0, 0, 0, 0],  # light color
        [0, 2, 1, 0],  # temperature
        [1, 0, 0, 0, 0, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # music
        [0, 0, 0, 2, 1, 0],  # music volume
        [2, 0, 1, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # fragrance
        # [2, 2, 0, 0, 0, 0]  # time needed
    ],
    # scenariusz B
    [
        [0, 0, 0, 2, 0],  # light intensity
        [2, 0, 0, 2, 0, 0, 0, 0, 0],  # light color
        [0, 2, 2, 0],  # temperature
        [2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # music
        [2, 0, 2, 0, 0, 0],  # volume
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # fragrance
        #  [2, 2, 0, 0, 0, 0]  # time needed
    ],
    # scenariusz C
    [
        [0, 0, 1, 2, 2],  # light intensity
        [2, 0, 0, 1, 0, 0, 0, 0, 0],  # light color
        [0, 2, 2, 0],  # temperature
        [2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # music
        [2, 0, 1, 0, 0, 0],  # volume
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # fragrance
        # [1, 2, 0, 0, 0, 0]  # time needed
    ],
    # scenariusz D
    [
        [2, 0, 0, 0, 0],  # light intensity
        [0, 0, 2, 0, 0, 0, 0, 0, 0, 0],  # light color
        [0, 2, 1, 0],  # temperature
        [0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0],  # music
        [0, 0, 1, 2, 2, 0],  # volume
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # fragrance
        #  [2, 2, 0, 0, 0, 0]  # time needed
    ]
]
# grupa wiekowa 25-30
group_2_default_preferences = [
    # scenariusz A
    [
        [2, 2, 0, 0, 0],
        [0, 0, 2, 1, 0, 0, 0, 0, 0],
        [0, 2, 1, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #  [2, 1, 0, 0, 0, 0]
    ],
    # scenariusz B
    [
        [0, 0, 0, 2, 0],
        [2, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 2, 2, 0],
        [2, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 1, 2, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #  [1, 2, 0, 0, 0, 0]
    ],
    # scenariusz C
    [
        [0, 0, 0, 2, 1],
        [2, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 2, 2, 0],
        [2, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 2, 2, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #  [2, 1, 1, 0, 0, 0]
    ],
    # scenariusz D
    [
        [2, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [0, 2, 2, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # [2, 0, 0, 0, 0, 0]
    ]
]
# grupa wiekowa 31+
group_3_default_preferences = [
    # scenariusz A
    [
        [0, 2, 0, 0, 0],
        [0, 1, 1, 2, 0, 0, 0, 0, 0],
        [0, 0, 2, 0],
        [0, 1, 0, 1, 1, 2, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 1, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #   [1, 2, 0, 0, 0, 0]
    ],
    # scenariusz B
    [
        [0, 0, 0, 2, 1],
        [2, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 2, 1],
        [2, 1, 0, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 2, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #  [0, 2, 1, 0, 0, 0]
    ],
    # scenariusz C
    [
        [0, 0, 0, 2, 0],
        [2, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 2, 1, 0],
        [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0],
        [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        #  [0, 1, 0, 2, 0, 0]
    ],
    # scenariusz D
    [
        [2, 0, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 0, 0],
        [1, 1, 2, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 2, 0],
        [2, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        #   [0, 2, 0, 0, 0, 0]
    ]
]


# class User(gym.Env):
#     def generateRandomArousalRelax(self):
#         # losowanie nastroju użytkownika
#         current_arousal = round(random.randrange(0, self.max_arousal), 2)
#         print("Initial arousal = ", current_arousal)
#         current_relax = round(random.randrange(0, self.max_relax), 2)
#         print("Initial relax = ", current_relax)
#
#         return [current_arousal, current_relax]
#     # zwraca numeryczną wartość nastroju na podstawie poziomu current_arousal i current_relax
#     def getMoodNumber(self):
#         if self.current_relax < self.max_relax / 2:
#             if self.current_arousal < self.max_arousal / 2:
#                 current_mood = 0
#             else:
#                 current_mood = 1
#         else:
#             if self.current_arousal < self.max_arousal / 2:
#                 current_mood = 3
#             else:
#                 current_mood = 2
#
#         return current_mood
#     # zwraca słowną nazwę nastroju na podstawie wartości numerycznej 0-3
#     def getMoodName(self):
#         if self.current_mood == 0:
#             mood_name = "STRESSED, DROWSY :("
#         if self.current_mood == 1:
#             mood_name = "Initial mood: STRESSED, AROUSED :<"
#         if self.current_mood == 2:
#             mood_name = "Initial mood: RELAXED, AROUSED :D"
#         if self.current_mood == 3:
#             mood_name = ("Initial mood: RELAXED, DROWSY :)")
#
#         return mood_name
#     def calculateNewUserMood(self, current_room_settings = []):
#         self.previous_arousal = self.current_arousal
#         self.previous_relax = self.current_relax
#
#         # scenario A (mood 1->2) R+
#         if self.current_mood == 1 and self.target_mood == 2:
#             current_user_scenario_preferences = self.preferences[0]
#             mood_change = np.multiply(current_user_scenario_preferences, current_room_settings)
#             self.current_relax += np.sum(mood_change)
#
#         # scenario B (mood 2->3) A-
#         if self.current_mood == 2 and self.target_mood == 3:
#             current_user_scenario_preferences = self.preferences[1]
#             mood_change = np.multiply(current_user_scenario_preferences, current_room_settings)
#             self.current_arousal -= np.sum(mood_change)
#
#         # scenario C (mood 0->3) R+
#         if self.current_mood == 0 and self.target_mood == 3:
#             current_user_scenario_preferences = self.preferences[2]
#             mood_change = np.multiply(current_user_scenario_preferences, current_room_settings)
#             self.current_relax += np.sum(mood_change)
#
#         # scenario D (mood 3->2) A+
#         if self.current_mood == 3 and self.target_mood == 2:
#             current_user_scenario_preferences = self.preferences[3]
#             mood_change = np.multiply(current_user_scenario_preferences, current_room_settings)
#             self.current_arousal += np.sum(mood_change)
#
#         self.previous_mood = self.current_mood
#         self.current_mood = self.getMoodNumber()
#
#         print("Previous: ", self.previous_mood, self.previous_arousal, self.previous_relax)
#         print("Current:  ", self.current_mood, self.current_arousal, self.current_relax)
#
#         return [
#             [self.previous_mood, self.previous_arousal, self.previous_relax],
#             [self.current_mood, self.current_arousal, self.current_relax]
#         ]
#     def __init__(self, age, name, target_mood, preferences=[]):
#         self.max_relax = 50
#         self.max_arousal = 50
#         self.previous_mood = None
#         self.previous_arousal = None
#         self.previous_relax = None
#         self.age = age
#         self.name = name
#         self.preferences = preferences
#         [self.current_arousal, self.current_relax] = self.generateRandomArousalRelax()
#         self.current_mood = self.getMoodNumber()
#         self.target_mood = target_mood
#        # self.step_mood = target_mood
#         print(self.name)
#         print("Current mood: ", self.getMoodName())
#
#         # return self.current_arousal, self.current_relax, self.current_mood

class Room(gym.Env):
    def setStepMood(self, current_mood, target_mood):
        step_mood = None

        if target_mood == 2 or target_mood == 3:
            if current_mood == 1:
                step_mood = 2
            elif current_mood == 0:
                step_mood = 3
            elif current_mood == 2 or current_mood == 3:
                step_mood = target_mood
            else:
                    print("ERROR: Incorrect current_mood: ", current_mood)
        else:
            print("ERROR: Incorrect target_mood: ", target_mood)

        return step_mood

    def setScenarioNameAndIndex(self, current_mood, step_mood):
        current_scenario_name = "-"
        current_scenario_index = None

        if current_mood == 1 and step_mood == 2:
            current_scenario_name = "A"
            current_scenario_index = 0
        elif current_mood == 2 and step_mood == 3:
            current_scenario_name = "B"
            current_scenario_index = 1
        elif current_mood == 0 and step_mood == 3:
            current_scenario_name = "C"
            current_scenario_index = 2
        elif current_mood == 3 and step_mood == 2:
            current_scenario_name = "D"
            current_scenario_index = 3
        else:
            print("ERROR: None of the scenarios could be applied ", current_mood, step_mood)

        return [current_scenario_name, current_scenario_index]

    def getDefaultGroupPreferences(self, user_age):
        preferences = []
        range = "-"

        # wybór grupy ze względu na wiek użytkownika
        if user_age <= 24:
            preferences = group_1_default_preferences
            range = "18-24"
        elif user_age <= 30:
            preferences = group_2_default_preferences
            range = "25-30"
        elif user_age > 30:
            preferences = group_3_default_preferences
            range = "31+"

        return preferences

    def setDefaultRoomSettings(self, group_preferences, current_scenario_index):
        room_settings = []
        for element in range(6):  # 6 elementów, indeksy 0-5
            # przypisz największą z posortowanych wartości
            room_settings.append(group_preferences[current_scenario_index][element].index(max(group_preferences[current_scenario_index][element])))

        # print("setDefaultRoomSettings room_settings:  ", room_settings)

        # zwraca w formacie tablicy [2, 3, 1, 0, 5, 8]
        return room_settings

    def setNewRoomSettings(self, group_preferences, current_scenario_index):
        # ta metoda jest wywoływana tylko raz w __init__ i jej wynik używany jest tylko raz — na zewnątrz klasy do stworzenia pętli, po której następuje iteracja akcji

        # kod z AI
        # # .n zwraca ilość możliwości w tuple (analogicznie do rozmiaru tablicy)
        # light_max = self.action_space[0].n
        # color_max = self.action_space[1].n
        # temperature_max = self.action_space[2].n
        # music_max = self.action_space[3].n
        # volume_max = self.action_space[4].n
        # fragrance_max = self.action_space[5].n
        #
        # # Pierwsza akcja z domyślnych wartości
        # yield group_preferences
        #
        # # póki co przechodzi przez wszystkie opcje po kolei, a docelowo ma przechodzić przez wszystkie akcje w kolejności popularności, czyli trzeba posortować i przechodzić po kolejnych elementach posortowanych tablic. Pozostaje pytanie czy przechodzić np. [0,0] [0,1] [0,2] [0,3] [1,0] [1,1] [1,2] [1,3] [2,0] etc. czy [0,0], [0,1] [1,0] [1,1] [0,2] [1,2] etc.
        #
        # # 2 to wgl nie uwzględnia scenariusza
        # # Generujemy kolejne akcje
        # for light in range(light_max):
        #     for color in range(color_max):
        #         for temperature in range(temperature_max):
        #             for music in range(music_max):
        #                 for volume in range(volume_max):
        #                     for fragrance in range(fragrance_max):
        #                         if [light, color, temperature, music, volume, fragrance] != default_settings_array:
        #                             yield [light, color, temperature, music, volume, fragrance]

        # największe prawdopodobieństwo trafienia powinno być wśród najpopularniejszych odpowiedzi, więc sprawdzamy je najpierw, żeby oszczędzić na czasie

        print("--- Generating new room settings combinations for scenario", current_scenario_index, "---")

        popular_indexes = [[],[],[],[],[],[]]

        for element in range(6):


            for i in range(len(group_preferences[current_scenario_index][element])):
                if group_preferences[current_scenario_index][element][i] == 2:
                    popular_indexes[element].append(i)
            for i in range(len(group_preferences[current_scenario_index][element])):
                if group_preferences[current_scenario_index][element][i] == 1:
                    popular_indexes[element].append(i)
            print("group_preferences[", current_scenario_index, "][", element, "]:",
                  group_preferences[current_scenario_index][element], "Popular_indexes: ", popular_indexes[element])
        print(popular_indexes[0])
        for light in popular_indexes[0]:
            for color in popular_indexes[1]:
                for temperature in popular_indexes[2]:
                    for music in popular_indexes[3]:
                        for volume in popular_indexes[4]:
                            for fragrance in popular_indexes[5]:
                                if [light, color, temperature, music, volume, fragrance] != self.setDefaultRoomSettings(group_preferences, current_scenario_index):
                                    print("New setting: ", light, color, temperature, music, volume, fragrance)
                                    yield [light, color, temperature, music, volume, fragrance]

        # TODO tymczasowo zakomentowany, żeby rozwiązać inne błędy
        # # jeśli nie trafimy z najpopularniejszymi to przechodzimy przez wszystkie
        # all_indexes = []
        #
        # for element in range(6):
        #     all_indexes[element] = sorted(range(len(group_preferences[current_scenario_index][element])), key=lambda i: group_preferences[current_scenario_index][element][i], reverse=True)
        #
        # for light in range(len(all_indexes[0])):
        #     for color in range(len(all_indexes[1])):
        #         for temperature in range(len(all_indexes[2])):
        #             for music in range(len(all_indexes[3])):
        #                 for volume in range(len(all_indexes[4])):
        #                     for fragrance in range(len(all_indexes[5])):
        #                         if [light, color, temperature, music, volume, fragrance] != self.setDefaultRoomSettings(
        #                                 group_preferences, current_scenario_index):
        #                             yield [light, color, temperature, music, volume, fragrance]

    def __init__(self, user):
        super(Room, self).__init__()
        self.reward = None
        self.action = None
        self.done = False
        self.is_scenario_changed = False
        self.info = {}

        # Definiujemy przestrzeń akcji (5 opcji dla light intensity, 9 opcji dla light color etc)
        self.action_space = spaces.Tuple((
            spaces.Discrete(5),  # light_intensity: (1) very_bright, (2) bright,(3) dimmed, (4) semidark, (5) darkness
            spaces.Discrete(9),
            # light_color: (1) none, (2) cold, (3) neutral, (4) warm), (5) red, (6) orange, (7) green, (8) blue, (9) purple
            spaces.Discrete(4),  # temperature: (0) <=18, (1) 19-21, (2), 22-24, (3) 25<=
            spaces.Discrete(18),
            # sound_type: (1) none, (2) noise, (3) nature_forest, (4) nature_water, (5) background, (6) speech, (7) calm_instrumental, (8) calm_vocal, (9) lively, (10) hard, (11) soundtrack, (12) celtic, (13) rave, (14) focus, (15) lofi, (16) classical, (17) asmr, (18) ambient
            spaces.Discrete(6),
            # sound_volume: (1) none, (2) very_quiet, (3) quiet, (4) moderate, (5) loud, (6) very_loud
            spaces.Discrete(16),
            # fregrance: (1) none, (2) vanilla, (3) citrus, (4) mint, (5) lavender, (6) sweet, (7) forest, (8) coffee, (9) cake, (10) water_lily, (11_ lilac, (12) black_opium, (13) ginger, (14) chocolate, (15) tea, (16) rain)
        ))

        # Definiujemy przestrzeń stanu (aktualny stan ustawień
        self.observation_space = spaces.Tuple((
            spaces.Discrete(5),  # light_intensity: (1) very_bright, (2) bright,(3) dimmed, (4) semidark, (5) darkness
            spaces.Discrete(9),
            # light_color: (1) none, (2) cold, (3) neutral, (4) warm), (5) red, (6) orange, (7) green, (8) blue, (9) purple
            spaces.Discrete(4),  # temperature: (0) <=18, (1) 19-21, (2), 22-24, (3) 25<=
            spaces.Discrete(18),
            # sound_type: (1) none, (2) noise, (3) nature_forest, (4) nature_water, (5) background, (6) speech, (7) calm_instrumental, (8) calm_vocal, (9) lively, (10) hard, (11) soundtrack, (12) celtic, (13) rave, (14) focus, (15) lofi, (16) classical, (17) asmr, (18) ambient
            spaces.Discrete(6),
            # sound_volume: (1) none, (2) very_quiet, (3) quiet, (4) moderate, (5) loud, (6) very_loud
            spaces.Discrete(16),
            # fragrance: (1) none, (2) vanilla, (3) citrus, (4) mint, (5) lavender, (6) sweet, (7) forest, (8) coffee, (9) cake, (10) water_lily, (11_ lilac, (12) black_opium, (13) ginger, (14) chocolate, (15) tea, (16) rain)
        ))

        # przypisanie użytkownika
        self.user = user
        print("Current_mood: ", self.user.current_mood)
        print("Target_mood: ", self.user.target_mood)

        # wyłapania błędnego nastroju docelowego
        if self.user.target_mood == 0 or self.user.target_mood == 1:
            self.done = True
            print("Nieprawidłowy nastrój docelowy: ", self.user.target_mood)
        # wyłapanie wygenerowania losowego nastroju początkowego takiego samego jak nastrój docelowy
        elif self.user.current_mood == self.user.target_mood:
            print("Wylosowany nastrój użytkownika jest taki sam jak nastrój docelowy!")
            self.done = True
        # inicjacja i deklaracje, jeśli nie złapano błędów
        else:
            # Definiujemy domyślne ustawienia
            self.default_group_preferences = self.getDefaultGroupPreferences(self.user.age)

            # określenie nastroju pośredniego (może okazać się taki sam jak nastrój docelowy)
            self.step_mood = self.setStepMood(self.user.current_mood, self.user.target_mood)
            print("Step_mood: ", self.step_mood)

            # pierwsze określenie scenariusza na podstawie bieżącego i pośredniego nastroju
            [self.current_scenario_name, self.current_scenario_index] = self.setScenarioNameAndIndex(self.user.current_mood_number, self.step_mood)
            print("Scenario: ", self.current_scenario_name, "/", self.current_scenario_index)

            default_room_settings = self.setDefaultRoomSettings(self.default_group_preferences, self.current_scenario_index)
            # Inicjalizacja stanu na domyślne ustawienia
            self.state = tuple(default_room_settings)
            print("State: ", default_room_settings)

            # obliczanie nowego nastroju użytkownika na podstawie nowej akcji (nowych ustawień otoczenia)
            self.user.calculateNewMood(self.setDefaultRoomSettings(self.default_group_preferences, self.current_scenario_index))

            self.action_sequence = self.setNewRoomSettings(self.default_group_preferences, self.current_scenario_index)
    def reset(self):
        print("reset")
        # Definiujemy domyślne ustawienia
        self.default_group_preferences = self.getDefaultGroupPreferences(self.user.age)
        # określenie nastroju pośredniego (może okazać się taki sam jak nastrój docelowy)
        self.step_mood = self.setStepMood(self.user.current_mood, self.user.target_mood)
        # pierwsze określenie scenariusza na podstawie bieżącego i pośredniego nastroju
        [self.current_scenario_name, self.current_scenario_index] = self.setScenarioNameAndIndex(self.user.current_mood, self.step_mood)

        # Inicjalizacja stanu na domyślne ustawienia
        self.state = tuple(self.setDefaultRoomSettings(self.default_group_preferences, self.current_scenario_index))
        return self.state

    def step(self, _action):
        # domyślnie nie jest zakończony (done = true, jeśli current_mood == target_mood jak w if poniżej)
        self.done = False
        self.is_scenario_changed = False

        # warunki zakończenia i zmiany step_mood oraz scenariusza
        if self.user.current_mood == self.user.target_mood:
            # jeśli osiągnięto nastrój docelowy
            self.done = True
            print("User is already in target mood!\nCurrent user mood: ", self.user.current_mood, "\nTarget mood: ",
                  self.user.target_mood)
        else:
            if self.user.current_mood == self.step_mood:
                print("Generowanie nowego scenariusza dla nastrójów: ", self.user.current_mood, " i ", self.step_mood)
                self.is_scenario_changed = True
                # jeśli osiągnięto nastrój pośredni to przyjmij nastrój docelowy jako kolejny step_mood
                print("Step mood achieved!\nCurrent mood: ", self.user.current_mood, "\nStep mood: ", self.step_mood,
                      "\nTarget mood: ", self.user.target_mood)
                self.step_mood = self.user.target_mood
                # określ nowy scenariusz dla nowego current_mood i step_mood
                [self.current_scenario_name, self.current_scenario_index] = self.setScenarioNameAndIndex(
                    self.user.current_mood, self.step_mood)
                print("Scenario: ", self.current_scenario_name)

                # nowa sekwencja akcji dla nowego scenariusza
                self.action_sequence = self.setNewRoomSettings(self.default_group_preferences, self.current_scenario_index)

            # Przypisujemy kolejne parametry otoczenia zgodnie z action wywołanym poza klasą, która odnosi się do setNewRoomSettings(), wywoływanego w __init__
            (light_intensity_action, light_color_action, temperature_action, music_action, volume_action, fragrance_action) = _action
            # Aktualizujemy stan zgodnie z akcją
            self.state = (light_intensity_action, light_color_action, temperature_action, music_action, volume_action, fragrance_action)

            # obliczanie nowego nastroju użytkownika na podstawie nowej akcji (nowych ustawień otoczenia)
            self.user.calculateNewMood(list(self.state))

        # TODO możliwe, że będzie jednak konieczne wprowadzenie upływu czasu np. jeśli wg preferencji grupy na osiągnięcie danego nastroju potrzebne jest 30 minut to pętla z tymi samymi parametrami (po stronie pokoju lub ew. po stronie użytkownika) ma być wykonana np 30 razy - wtedy reakcja użytkownika na zmianę otoczenia będzie reakcją na 1 minutę tego otoczenia czyli np jeśli reakcja użytkownika to relax+=1 to po 30 minutach relax wzrośnie o 30

        # TODO zobaczyć jak działa system z takimi nagrodami i w razie potrzeby modyfikować
        self.reward = 0
        # dodatnia nagroda za osiągnięcie przejściowego / docelowego nastroju (step_mood = target_mood, jeśli wcześniej step_mood został osiągnięty lub nie ma innego nastroju pośredniego)
        if self.user.current_mood == self.step_mood:
            self.reward = 1
        else:
            # jeśli nastrój nie został osiągnięty, ale użytkownik jest zrelaksowany, to nie ma nagrody (jest zerowa)
            if self.user.current_relax > (self.user.max_relax / 2):
                self.reward = 0
            # jeśli nastrój nie został osiągnięty i użytkownik jest zestresowany, to nagroda jest ujemna (zależy nam na tym, żeby użytkownik przede wszystkim był zrelaksowany)
            else:
                self.reward = -1

        self.info = {}

        return self.state, self.reward, self.done, self.info

    def render(self):
        light_intensity_action, light_color_action, temperature_action, music_action, volume_action, fragrance_action = self.state
        print("Light intensity: ", light_intensity_action, "\nLight color: ", light_color_action, "\nTemperature: ",
              temperature_action, "\nMusic: ", music_action, "\nVolume: ", volume_action, "\nFragrance: ",
              fragrance_action)


class User:
    def getMoodNumber(self):
        if self.current_relax < self.max_relax / 2:
            if self.current_arousal < self.max_arousal / 2:
                current_mood = 0
            else:
                current_mood = 1
        else:
            if self.current_arousal < self.max_arousal / 2:
                current_mood = 3
            else:
                current_mood = 2

        return current_mood

    # zwraca słowną nazwę nastroju na podstawie wartości numerycznej 0-3
    def getMoodName(self):
        if self.current_mood == 0:
            mood_name = "STRESSED, DROWSY :("
        if self.current_mood == 1:
            mood_name = "STRESSED, AROUSED :<"
        if self.current_mood == 2:
            mood_name = "RELAXED, AROUSED :D"
        if self.current_mood == 3:
            mood_name = "RELAXED, DROWSY :)"

        return mood_name

    def generateRandomMood(self):
        # losowanie relax i arousal
        # TODO przywrócić, tymczasowo zrobiony hardcode do testów
        # self.current_arousal = round(random.randrange(0, self.max_arousal), 2)
        # self.current_relax = round(random.randrange(0, self.max_relax), 2)
        self.current_arousal = 10
        self.current_relax = 10
        print("Initial arousal = ", self.current_arousal)
        print("Initial relax = ", self.current_relax)

        # numeryczny nastrój
        self.current_mood = self.getMoodNumber()

        # nazwa nastroju
        self.mood_name = self.getMoodName()

        return [self.current_mood, self.mood_name, self.current_relax, self.current_arousal]

    def calculateNewMood(self, action_tuple):
        print("Calculating new user current_mood for settings:", action_tuple)

        current_room_settings = list(action_tuple)
        previous_arousal = self.current_arousal
        previous_relax = self.current_relax
        previous_mood = self.current_mood

        # scenario A (mood 1->2) R+
        if self.current_mood == 1 and self.target_mood == 2:
            current_user_scenario_preferences = self.preferences[0]
            mood_change = current_user_scenario_preferences[current_room_settings[0]] + \
                          current_user_scenario_preferences[current_room_settings[1]] + \
                          current_user_scenario_preferences[current_room_settings[2]] + \
                          current_user_scenario_preferences[current_room_settings[3]] + \
                          current_user_scenario_preferences[current_room_settings[4]] + \
                          current_user_scenario_preferences[current_room_settings[5]]
            self.current_relax += np.sum(mood_change)

        # scenario B (mood 2->3) A-
        if self.current_mood == 2 and self.target_mood == 3:
            current_user_scenario_preferences = self.preferences[1]
            mood_change = current_user_scenario_preferences[current_room_settings[0]] + \
                          current_user_scenario_preferences[current_room_settings[1]] + \
                          current_user_scenario_preferences[current_room_settings[2]] + \
                          current_user_scenario_preferences[current_room_settings[3]] + \
                          current_user_scenario_preferences[current_room_settings[4]] + \
                          current_user_scenario_preferences[current_room_settings[5]]
            self.current_arousal -= np.sum(mood_change)

        # scenario C (mood 0->3) R+
        if self.current_mood == 0 and self.target_mood == 3:
            current_user_scenario_preferences = self.preferences[2]
            mood_change = current_user_scenario_preferences[current_room_settings[0]] + \
                          current_user_scenario_preferences[current_room_settings[1]] + \
                          current_user_scenario_preferences[current_room_settings[2]] + \
                          current_user_scenario_preferences[current_room_settings[3]] + \
                          current_user_scenario_preferences[current_room_settings[4]] + \
                          current_user_scenario_preferences[current_room_settings[5]]
            self.current_relax += np.sum(mood_change)

        # scenario D (mood 3->2) A+
        if self.current_mood == 3 and self.target_mood == 2:
            current_user_scenario_preferences = self.preferences[3]
            mood_change = current_user_scenario_preferences[current_room_settings[0]] + \
                          current_user_scenario_preferences[current_room_settings[1]] + \
                          current_user_scenario_preferences[current_room_settings[2]] + \
                          current_user_scenario_preferences[current_room_settings[3]] + \
                          current_user_scenario_preferences[current_room_settings[4]] + \
                          current_user_scenario_preferences[current_room_settings[5]]
            self.current_arousal += np.sum(mood_change)

        self.current_mood = self.getMoodNumber()

        print("Previous: ", previous_mood, previous_arousal, previous_relax)
        print("Current:  ", self.current_mood, self.current_arousal, self.current_relax)

        # return [
        #     [previous_mood, previous_arousal, previous_relax],
        #     [self.current_mood, self.current_arousal, self.current_relax]
        # ]

    def __init__(self, name, age, preferences, target_mood):
        self.max_relax = 50
        self.max_arousal = 50
        self.name = name
        self.age = age
        self.preferences = preferences
        self.target_mood = target_mood
        [self.current_mood_number, self.current_mood_name, self.current_relax,
         self.current_arousal] = self.generateRandomMood()

#
# # respondent nr 1 (K, 21l.)
# user1 = User("User 1 (F21)", 21, user1_preferences, user1_target_mood)
# # respondent nr 40 (M, 26l.)
# user2 = User("User 2 (M26)", 26, user2_preferences, user2_target_mood)
# # respondent nr 45 (K, 52l.)
# user3 = User("User 3 (F52)", 52, user3_preferences, user3_target_mood)


# Tworzymy nasze środowisko, przekazując preferencje użytkownika
env = Room(User("User 1 (F21)", 21, user1_preferences, user1_target_mood))

# Przykład użycia
# obs = env.reset()

# Iterujemy przez akcje generowane przez generator
# TODO tu jakoś trzeba będzie złapać zmianę action_sequence przy zmianie scenariusza
# pierwsza propozycja - przechodź przez pętle akcji z kolejnymi sekwencjami dopóki nie zostanie osiągnięcty cel
while not env.done:
    for action in env.action_sequence:
        # przerwij, jeśli zauważono zmianę scenariusza (nwm czy to zadziała) - powinno przejść do kolejnej iteracji while, tym razem biorąc nowy action_sequence
        if env.is_scenario_changed:
            print("Scenario changed!")
            break

        obs, reward, done, info = env.step(action)
        print("Action:", action)
        print("State after action:", obs)
        print("Reward:", reward)
        print("Done:", done)
        print("Info:", info)
        env.render()


#
#
#         # SECTION ustawianie pierwszych ustawień otoczenia na preferowane ustawienia domyślnej grupy
#
#         current_scenario = 1
#         current_scenario_default_group_light_preferences = self.default_group_preferences[current_scenario][0]  # hardcode 0 jako scenariusz A, TODO podstawić automatyczny dobór scenariusza
#
#         # Posortowane indeksy - kolejność preferowanych ustawień dla light dla podanego scenariusza
#         current_scenario_default_group_light_preferences_indexes_sorted = sorted(range(len(current_scenario_default_group_light_preferences )), key=lambda i: current_scenario_default_group_light_preferences[i], reverse=True)
#
#         # światło, które ma zostać ustawione
#         room_light_setting_index = current_scenario_default_group_light_preferences_indexes_sorted[0]  # indeks ustawienia o najsilniejszej preferencji grupy domyślnej
#         # TODO deklaracja self.current_room_settings
#         # room_light_setting = self.current_room_settings[0][room_light_setting_index]
#
#         print("current_scenario_default_group_light_preferences: ", current_scenario_default_group_light_preferences )
#         print("current_scenario_default_group_light_preferences_indexes_sorted: ", current_scenario_default_group_light_preferences_indexes_sorted)
#         # print("room_light_setting: ", room_light_setting)
#         self.temperature = np.random.uniform(self.min_temperature, self.max_temperature)
#
#
#     def reset(self):
#         # Reset light and temperature to random values
#         self.light = np.random.choice([0, 1, 2])
#         self.temperature = np.random.uniform(12, 30)
#         return self.light, np.array([self.temperature])
#
#     def step(self, action):
#         # Unpack the action (light setting, heater temperature)
#         light_intesitivity, light_color, temperature, sound_type, sound_volume, fregrance = action
#
#         print("action: ", action)
#
#         # Update the state
#         self. light_intesitivity =  light_intesitivity
#         self.light_color = light_color
#         self.temperature = np.clip(temperature[0], self.min_temperature, self.max_temperature)
#         self.sound_type = sound_type
#         self.sound_volume = sound_volume
#         self.fregrance = fregrance
#
#         # TODO zaimplementować tak, żeby done=true tylko kiedy osiągnie pożądany nastrój (lub jeśli minie dany czas)
#         done = False  # Generally, set this to True when the episode should end
#
#         reward = 0
#         # Return the new observation, reward, done flag, and additional info (if any)
#         return (self.light, np.array([self.temperature])), reward, done, {}
#
#     # def render(self, mode='human'):
#     #     light_colors = ["Warm", "Neutral", "Cold"]  # Mapping light settings to string
#     #     light_str = light_colors[self.light]
#     #     temperature_str = f"{self.temperature:.2f}"  # Convert temperature to a formatted string
#     #
#     #     print(f"Light setting: {light_str}, Temperature: {temperature_str}°C")
#
# # respondent nr 1 (K, 21l.)
# user1 = User(21, "User 1 (F21)", user1_target_mood, user1_preferences)
# # respondent nr 40 (M, 26l.)
# user2 = User(26, "User 2 (M26)", user2_target_mood, user2_preferences)
# # respondent nr 45 (K, 52l.)
# user3 = User(52, "User 3 (F52)", user3_target_mood, user3_preferences)
#
# # uruchomienie symulacji dla danego użytkownika
# room = Room(user1)
#
# # Reset the roomironment
# obs = room.reset()
#
# default_group_preferences = room.get_current_group_preferences(0)
#
# action = (default_group_preferences[0], default_group_preferences[1], default_group_preferences[2], default_group_preferences[3], default_group_preferences[4], default_group_preferences[5])
#
# obs, reward, done, info, abc = room.step(action)
#
# # TODO dodać pętlę (while?) z iteracją czasu i inkrementacją czasu w każdej pętli - while z warunkiem końcowym w postaci odpowiedniej nagrody / poziomu procentowego spełnienia
#
#
# # TODO iteracje uczące - doszukać jak to powinno wyglądać
# while reward < 2:
#     # TODO tu chyba powinno być wywołanie room -> step
#
#     # to poniżej to nwm czy tutaj wgl ???
#     # aktualizacja(sprawdzenie, czy nastrój już się nie zmienił
#     # room.current_user.getMoodNumber()
#     # # wybór zostawu preferencji na podstawie sceriusza (porównania current_mood i target_mood)
#     # current_user_scenario_preferences = []
#     # # scenariusz A:
#     # if room.current_user.current_mood == 1 and room.current_user.step_mood == 2:
#     #     current_scenario = "A"
#     #     current_user_scenario_preferences = room.current_user.preferences_set[0]
#     # # scenariusz B:
#     # elif room.current_user.current_mood == 2 and room.current_user.step_mood == 3:
#     #     current_scenario = "B"
#     #     current_user_scenario_preferences = room.current_user.preferences_set[1]
#     # # scenariusz C:
#     # elif room.current_user.current_mood == 0 and room.current_user.step_mood == 3:
#     #     current_scenario = "C"
#     #     current_user_scenario_preferences = room.current_user.preferences_set[2]
#     # # scenariusz D:
#     # elif room.current_user.current_mood == 3 and room.current_user.step_mood == 2:
#     #     current_scenario = "D"
#     #     current_user_scenario_preferences = room.current_user.preferences_set[3]
#     # else:
#     #     print("None of the scenarios could be applied")
#
#
#     # TODO zmienić format room.current_room_settings na analogiczny do current_user_scenario_preferences
#     # mood_change = np.multiply(current_user_scenario_preferences, room.current_room_settings)
#     #
#     # # zmiana nastroju na podstawie obliczeń z preferencji użtkownika i bieżących ustawień pokoju
#     # if current_scenario == "A":
#     #     room.current_user.current_relax += np.sum(mood_change)
#     # if current_scenario == "B":
#     #     room.current_user.current_arousal -= np.sum(mood_change)
#     # if current_scenario == "C":
#     #     room.current_user.current_relax += np.sum(mood_change)
#     # if current_scenario == "D":
#     #     room.current_user.current_arousal += np.sum(mood_change)
#
#     # przechodź po kolejnych ustawieniach otoczenia
#     action = (room.light + 1, np.array(([room.temperature + 1])))
#
# print("New observation:", obs)
# print("Reward:", reward)
#
# # Render the room
# room.render()
