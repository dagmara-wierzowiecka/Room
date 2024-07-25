import gym
import numpy as np
from gym import spaces  # , envs
import random
import csv
import os

simulation_time = 240  # minutes
max_iterations_amount = 16  # max 16 iteracji, każda symuluje zmianę nastroju po 15 minutach

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
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
        [0, 0, 2, 0, 0, 0, 0, 0, 0],  # light color
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
        elif 25 <= user_age <= 30:
            preferences = group_2_default_preferences
            range = "25-30"
        elif user_age >= 31:
            preferences = group_3_default_preferences
            range = "31+"

        print("User age range: ", range)

        return preferences

    def setDefaultRoomSettings(self, group_preferences, current_scenario_index):
        room_settings = []
        for element in range(6):  # 6 elementów, indeksy 0-5
            # przypisz największą z posortowanych wartości
            room_settings.append(group_preferences[current_scenario_index][element].index(
                max(group_preferences[current_scenario_index][element])))
        print("--- Generating default room settings combinations for scenario", current_scenario_index, "---")
        print("-- Default setting: ", room_settings, "--")

        # zwraca w formacie tablicy [2, 3, 1, 0, 5, 8]
        return room_settings

    def setNewRoomSettingsPopular(self, group_preferences, current_scenario_index, default_room_settings):
        # największe prawdopodobieństwo trafienia powinno być wśród najpopularniejszych odpowiedzi, więc sprawdzamy je najpierw, żeby oszczędzić na czasie

        print("\n--- Generating new room settings combinations for scenario", current_scenario_index, "---")

        yield default_room_settings

        popular_indexes = [[], [], [], [], [], []]

        for element in range(6):
            for i in range(len(group_preferences[current_scenario_index][element])):
                if group_preferences[current_scenario_index][element][i] == 2:
                    popular_indexes[element].append(i)
            for i in range(len(group_preferences[current_scenario_index][element])):
                if group_preferences[current_scenario_index][element][i] == 1:
                    popular_indexes[element].append(i)

        for light in popular_indexes[0]:
            for color in popular_indexes[1]:
                for temperature in popular_indexes[2]:
                    for music in popular_indexes[3]:
                        for volume in popular_indexes[4]:
                            for fragrance in popular_indexes[5]:
                                if [light, color, temperature, music, volume, fragrance] != default_room_settings:
                                    print("\n-- New setting: ", light, color, temperature, music, volume, fragrance,
                                          "--")
                                    yield [light, color, temperature, music, volume, fragrance]

    def setNewRoomSettingsAll(self, group_preferences, current_scenario_index, default_room_settings):

        popular_indexes = [[], [], [], [], [], []]
        for element in range(6):
            for i in range(len(group_preferences[current_scenario_index][element])):
                if group_preferences[current_scenario_index][element][i] == 2:
                    popular_indexes[element].append(i)
            for i in range(len(group_preferences[current_scenario_index][element])):
                if group_preferences[current_scenario_index][element][i] == 1:
                    popular_indexes[element].append(i)

        all_indexes = [[], [], [], [], [], []]
        for element in range(6):
            for i in range(len(group_preferences[current_scenario_index][element])):
                all_indexes[element].append(i)

        for light in popular_indexes[0]:
            for color in popular_indexes[1]:
                for temperature in popular_indexes[2]:
                    for music in popular_indexes[3]:
                        for volume in popular_indexes[4]:
                            for fragrance in all_indexes[5]:
                                if [light, color, temperature, music, volume, fragrance] != default_room_settings:
                                    print("\n-- New setting: ", light, color, temperature, music, volume, fragrance, "--")
                                    yield [light, color, temperature, music, volume, fragrance]

        for light in popular_indexes[0]:
            for color in popular_indexes[1]:
                for temperature in popular_indexes[2]:
                    for music in popular_indexes[3]:
                        for volume in all_indexes[4]:
                            for fragrance in all_indexes[5]:
                                if [light, color, temperature, music, volume, fragrance] != default_room_settings:
                                    print("\n-- New setting: ", light, color, temperature, music, volume, fragrance, "--")
                                    yield [light, color, temperature, music, volume, fragrance]

        for light in popular_indexes[0]:
            for color in popular_indexes[1]:
                for temperature in popular_indexes[2]:
                    for music in all_indexes[3]:
                        for volume in all_indexes[4]:
                            for fragrance in all_indexes[5]:
                                if [light, color, temperature, music, volume, fragrance] != default_room_settings:
                                    print("\n-- New setting: ", light, color, temperature, music, volume, fragrance, "--")
                                    yield [light, color, temperature, music, volume, fragrance]

        for light in popular_indexes[0]:
            for color in popular_indexes[1]:
                for temperature in all_indexes[2]:
                    for music in all_indexes[3]:
                        for volume in all_indexes[4]:
                            for fragrance in all_indexes[5]:
                                if [light, color, temperature, music, volume, fragrance] != default_room_settings:
                                    print("\n-- New setting: ", light, color, temperature, music, volume, fragrance, "--")
                                    yield [light, color, temperature, music, volume, fragrance]

        for light in popular_indexes[0]:
            for color in all_indexes[1]:
                for temperature in all_indexes[2]:
                    for music in all_indexes[3]:
                        for volume in all_indexes[4]:
                            for fragrance in all_indexes[5]:
                                if [light, color, temperature, music, volume, fragrance] != default_room_settings:
                                    print("\n-- New setting: ", light, color, temperature, music, volume, fragrance, "--")
                                    yield [light, color, temperature, music, volume, fragrance]
        for light in all_indexes[0]:
            for color in all_indexes[1]:
                for temperature in all_indexes[2]:
                    for music in all_indexes[3]:
                        for volume in all_indexes[4]:
                            for fragrance in all_indexes[5]:
                                if [light, color, temperature, music, volume, fragrance] != default_room_settings:
                                    print("\n-- New setting: ", light, color, temperature, music, volume, fragrance, "--")
                                    yield [light, color, temperature, music, volume, fragrance]

    def __init__(self, user):
        super(Room, self).__init__()
        self.reward = None
        self.action = None
        self.done = False
        self.is_scenario_changed = False
        self.info = {}
        self.correct_input = True

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
            self.correct_input = False
            print("Nieprawidłowy nastrój docelowy: ", self.user.target_mood)
        # wyłapanie wygenerowania losowego nastroju początkowego takiego samego jak nastrój docelowy
        elif self.user.current_mood == self.user.target_mood:
            print("Wylosowany nastrój użytkownika jest taki sam jak nastrój docelowy!")
            self.done = True
            self.correct_input = False
        # inicjacja i deklaracje, jeśli nie złapano błędów
        else:
            # Definiujemy domyślne ustawienia
            self.default_group_preferences = self.getDefaultGroupPreferences(self.user.age)

            # określenie nastroju pośredniego (może okazać się taki sam jak nastrój docelowy)
            self.step_mood = self.setStepMood(self.user.current_mood, self.user.target_mood)
            print("Step mood: ", self.step_mood)

            # pierwsze określenie scenariusza na podstawie bieżącego i pośredniego nastroju
            [self.current_scenario_name, self.current_scenario_index] = self.setScenarioNameAndIndex(
                self.user.current_mood, self.step_mood)
            print("Scenario: ", self.current_scenario_name, "/", self.current_scenario_index)

            self.default_room_settings = self.setDefaultRoomSettings(self.default_group_preferences,
                                                                     self.current_scenario_index)
            # Inicjalizacja stanu na domyślne ustawienia
            self.state = tuple(self.default_room_settings)
            # print("State: ", self.default_room_settings)

            # obliczanie nowego nastroju użytkownika na podstawie nowej akcji (nowych ustawień otoczenia)
            self.mood_change = self.user.calculateNewMood(self.default_room_settings, self.user.current_mood, self.step_mood)

            self.action_sequence_popular = self.setNewRoomSettingsPopular(self.default_group_preferences, self.current_scenario_index, self.default_room_settings)

            self.action_sequence_all = self.setNewRoomSettingsAll(self.default_group_preferences, self.current_scenario_index, self.default_room_settings)

    def reset(self):
        super(Room, self).__init__()
        self.reward = None
        self.action = None
        self.done = False
        self.is_scenario_changed = False
        self.info = {}
        self.correct_input = True

        # wyłapania błędnego nastroju docelowego
        if self.user.target_mood == 0 or self.user.target_mood == 1:
            self.done = True
            self.correct_input = False
            print("Nieprawidłowy nastrój docelowy: ", self.user.target_mood)
        # wyłapanie wygenerowania losowego nastroju początkowego takiego samego jak nastrój docelowy
        elif self.user.current_mood == self.user.target_mood:
            print("Wylosowany nastrój użytkownika jest taki sam jak nastrój docelowy!")
            self.done = True
            self.correct_input = False
        # inicjacja i deklaracje, jeśli nie złapano błędów
        else:
            # określenie nastroju pośredniego (może okazać się taki sam jak nastrój docelowy)
            self.step_mood = self.setStepMood(self.user.current_mood, self.user.target_mood)
            print("Step mood: ", self.step_mood)

            # pierwsze określenie scenariusza na podstawie bieżącego i pośredniego nastroju
            [self.current_scenario_name, self.current_scenario_index] = self.setScenarioNameAndIndex(
                self.user.current_mood, self.step_mood)
            print("Scenario: ", self.current_scenario_name, "/", self.current_scenario_index)

            self.default_room_settings = self.setDefaultRoomSettings(self.default_group_preferences,
                                                                     self.current_scenario_index)
            # Inicjalizacja stanu na domyślne ustawienia
            self.state = tuple(self.default_room_settings)
            # print("State: ", self.default_room_settings)

            # obliczanie nowego nastroju użytkownika na podstawie nowej akcji (nowych ustawień otoczenia)
            self.mood_change = self.user.calculateNewMood(self.default_room_settings, self.user.current_mood, self.step_mood)

            self.action_sequence_popular = self.setNewRoomSettingsPopular(self.default_group_preferences,
                                                                          self.current_scenario_index,
                                                                          self.default_room_settings)

            self.action_sequence_all = self.setNewRoomSettingsAll(self.default_group_preferences,
                                                                  self.current_scenario_index,
                                                                  self.default_room_settings)
        # return self.reward, self.done, self.info

    def step(self, _action):
        # domyślnie nie jest zakończony (done = true, jeśli current_mood == target_mood jak w if poniżej)
        self.done = False
        self.is_scenario_changed = False

        # print(action_id)
        # Przypisujemy kolejne parametry otoczenia zgodnie z action wywołanym poza klasą, która odnosi się do setNewRoomSettingsPopular(), wywoływanego w __init__
        (light_intensity_action, light_color_action, temperature_action, music_action, volume_action,
         fragrance_action) = _action
        # Aktualizujemy stan zgodnie z akcją
        self.state = (
        light_intensity_action, light_color_action, temperature_action, music_action, volume_action, fragrance_action)

        # obliczanie nowego nastroju użytkownika na podstawie nowej akcji (nowych ustawień otoczenia)
        # print("Calculating new user mood for:", list(self.state), self.user.current_mood, self.step_mood)
        self.mood_change = self.user.calculateNewMood(list(self.state), self.user.current_mood, self.step_mood)

        # warunki zakończenia i zmiany step_mood oraz scenariusza
        if self.user.current_mood == self.user.target_mood:
            # jeśli osiągnięto nastrój docelowy
            self.reward = 2
            self.done = True
            print("User is already in target mood!\nCurrent user mood, arousal, relax: ", self.user.current_mood,
                  self.user.current_arousal, self.user.current_relax, "\nTarget mood: ",
                  self.user.target_mood)
        else:
            if self.user.current_mood == self.step_mood:
                self.reward = 1
                self.is_scenario_changed = True
                # jeśli osiągnięto nastrój pośredni to przyjmij nastrój docelowy jako kolejny step_mood
                print("Step mood achieved! Current mood: ", self.user.current_mood, "Step mood: ", self.step_mood,
                      "Target mood: ", self.user.target_mood)

                # self.step_mood = self.user.target_mood
                self.step_mood = self.setStepMood(self.user.current_mood, self.user.target_mood)

                # określ nowy scenariusz dla nowego current_mood i step_mood

                [self.current_scenario_name, self.current_scenario_index] = self.setScenarioNameAndIndex(self.user.current_mood, self.step_mood)

                print("New scenario: ", self.current_scenario_name)

                # Nowa sekwencja akcji dla nowego scenariusza
                self.action_sequence_popular = self.setNewRoomSettingsPopular(self.default_group_preferences, self.current_scenario_index, self.default_room_settings)
                self.action_sequence_all = self.setNewRoomSettingsAll(self.default_group_preferences, self.current_scenario_index, self.default_room_settings)

            # Dodatkowe możliwości nagrody
            if self.user.current_relax > (self.user.max_relax / 2):
                self.reward = 0
            else:
                self.reward = -1  # jeśli nastrój nie został osiągnięty i użytkownik jest zestresowany, to nagroda jest ujemna (zależy nam na tym, żeby użytkownik przede wszystkim był zrelaksowany)

            # Niezależnie od zmiany/braku zmiany scenariusza:

            # # Przypisujemy kolejne parametry otoczenia zgodnie z action wywołanym poza klasą, która odnosi się do setNewRoomSettingsPopular(), wywoływanego w __init__
            # (light_intensity_action, light_color_action, temperature_action, music_action, volume_action,
            #  fragrance_action) = _action
            # # Aktualizujemy stan zgodnie z akcją
            # self.state = (light_intensity_action, light_color_action, temperature_action, music_action, volume_action, fragrance_action)
            #
            # # obliczanie nowego nastroju użytkownika na podstawie nowej akcji (nowych ustawień otoczenia)
            # # print("Calculating new user mood for:", list(self.state), self.user.current_mood, self.step_mood)
            # self.mood_change = self.user.calculateNewMood(list(self.state), self.user.current_mood, self.step_mood)

        # objaśnienie: możliwe, że będzie jednak konieczne wprowadzenie upływu czasu np. jeśli wg preferencji grupy na osiągnięcie danego nastroju potrzebne jest 30 minut to pętla z tymi samymi parametrami (po stronie pokoju lub ew. po stronie użytkownika) ma być wykonana np 30 razy - wtedy reakcja użytkownika na zmianę otoczenia będzie reakcją na 1 minutę tego otoczenia czyli np jeśli reakcja użytkownika to relax+=1 to po 30 minutach relax wzrośnie o 30

        # self.reward = 0
        # # dodatnia nagroda za osiągnięcie przejściowego / docelowego nastroju (step_mood = target_mood, jeśli wcześniej step_mood został osiągnięty lub nie ma innego nastroju pośredniego)
        # if self.user.current_mood == self.step_mood:
        #     self.reward = 1
        # else:
        #     # jeśli nastrój nie został osiągnięty, ale użytkownik jest zrelaksowany, to nie ma nagrody (jest zerowa)
        #     if self.user.current_relax > (self.user.max_relax / 2):
        #         self.reward = 0
        #     # jeśli nastrój nie został osiągnięty i użytkownik jest zestresowany, to nagroda jest ujemna (zależy nam na tym, żeby użytkownik przede wszystkim był zrelaksowany)
        #     else:
        #         self.reward = -1

        self.info = {}

        return self.state, self.reward, self.done, self.info

    def render(self):
        light_intensity_action, light_color_action, temperature_action, music_action, volume_action, fragrance_action = self.state

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
        self.current_arousal = initial_arousal
        self.current_relax = initial_relax
        print("Initial arousal = ", self.current_arousal)
        print("Initial relax = ", self.current_relax)

        # numeryczny nastrój
        self.current_mood = self.getMoodNumber()

        # nazwa nastroju
        self.current_mood_name = self.getMoodName()

        return [self.current_mood, self.current_mood_name, self.current_relax, self.current_arousal]

    def getInitialMood(self):

        self.current_mood = self.initial_mood
        self.current_mood_name = self.initial_mood_name
        self.current_relax = self.initial_relax
        self.current_arousal = self.initial_arousal

        # print("Setting back user's initial mood, relax, arousal: ", self.current_mood, self.current_relax, self.current_arousal)

        return [self.current_mood, self.current_mood_name, self.current_relax, self.current_arousal]

    def calculateNewMood(self, current_room_settings, current_mood, step_mood):

        # TODO dodać stres (spadek relaksu na każdą iterację)

        # print("Calculating new user current_mood for settings:", current_room_settings)

        previous_arousal = self.current_arousal
        previous_relax = self.current_relax
        previous_mood = self.current_mood

        # scenario A (mood 1->2) R+
        if current_mood == 1 and step_mood == 2:
            current_user_scenario_preferences = self.preferences[0]

            mood_change = current_user_scenario_preferences[0][current_room_settings[0]] + \
                          current_user_scenario_preferences[1][current_room_settings[1]] + \
                          current_user_scenario_preferences[2][current_room_settings[2]] + \
                          current_user_scenario_preferences[3][current_room_settings[3]] + \
                          current_user_scenario_preferences[4][current_room_settings[4]] + \
                          current_user_scenario_preferences[5][current_room_settings[5]]

            # print("Mood change: ", current_user_scenario_preferences[0][current_room_settings[0]],
            #       current_user_scenario_preferences[1][current_room_settings[1]],
            #       current_user_scenario_preferences[2][current_room_settings[2]],
            #       current_user_scenario_preferences[3][current_room_settings[3]],
            #       current_user_scenario_preferences[4][current_room_settings[4]],
            #       current_user_scenario_preferences[5][current_room_settings[5]], " = ", mood_change)

            self.current_relax += np.sum(mood_change)

        # scenario B (mood 2->3) A-
        elif current_mood == 2 and step_mood == 3:
            current_user_scenario_preferences = self.preferences[1]

            mood_change = current_user_scenario_preferences[0][current_room_settings[0]] + \
                          current_user_scenario_preferences[1][current_room_settings[1]] + \
                          current_user_scenario_preferences[2][current_room_settings[2]] + \
                          current_user_scenario_preferences[3][current_room_settings[3]] + \
                          current_user_scenario_preferences[4][current_room_settings[4]] + \
                          current_user_scenario_preferences[5][current_room_settings[5]]

            # print("Mood change: ", current_user_scenario_preferences[0][current_room_settings[0]],
            #       current_user_scenario_preferences[1][current_room_settings[1]],
            #       current_user_scenario_preferences[2][current_room_settings[2]],
            #       current_user_scenario_preferences[3][current_room_settings[3]],
            #       current_user_scenario_preferences[4][current_room_settings[4]],
            #       current_user_scenario_preferences[5][current_room_settings[5]], " = ", mood_change)

            self.current_arousal -= np.sum(mood_change)

        # scenario C (mood 0->3) R+
        elif current_mood == 0 and step_mood == 3:
            current_user_scenario_preferences = self.preferences[2]

            mood_change = current_user_scenario_preferences[0][current_room_settings[0]] + \
                          current_user_scenario_preferences[1][current_room_settings[1]] + \
                          current_user_scenario_preferences[2][current_room_settings[2]] + \
                          current_user_scenario_preferences[3][current_room_settings[3]] + \
                          current_user_scenario_preferences[4][current_room_settings[4]] + \
                          current_user_scenario_preferences[5][current_room_settings[5]]

            # print("Mood change: ", current_user_scenario_preferences[0][current_room_settings[0]],current_user_scenario_preferences[1][current_room_settings[1]],
            #       current_user_scenario_preferences[2][current_room_settings[2]],
            #       current_user_scenario_preferences[3][current_room_settings[3]],
            #       current_user_scenario_preferences[4][current_room_settings[4]],
            #       current_user_scenario_preferences[5][current_room_settings[5]], " = ", mood_change)

            self.current_relax += np.sum(mood_change)

        # scenario D (mood 3->2) A+
        elif current_mood == 3 and step_mood == 2:
            current_user_scenario_preferences = self.preferences[3]

            mood_change = current_user_scenario_preferences[0][current_room_settings[0]] + \
                          current_user_scenario_preferences[1][current_room_settings[1]] + \
                          current_user_scenario_preferences[2][current_room_settings[2]] + \
                          current_user_scenario_preferences[3][current_room_settings[3]] + \
                          current_user_scenario_preferences[4][current_room_settings[4]] + \
                          current_user_scenario_preferences[5][current_room_settings[5]]

            self.current_arousal += np.sum(mood_change)

        else:
            print("No scenario could be set", current_mood, step_mood)

        self.current_mood = self.getMoodNumber()

        # print("Previous mood, arousal, relax: ", previous_mood, previous_arousal, previous_relax)
        # print("Current mood, arousal, relax:  ", self.current_mood, self.current_arousal, self.current_relax)
        # print(mood_change)

        return mood_change

    def __init__(self, name, age, preferences, target_mood):
        self.max_relax = 96
        self.max_arousal = 96
        self.name = name
        self.age = age
        self.preferences = preferences
        self.target_mood = target_mood

        [self.current_mood, self.current_mood_name, self.current_relax,
         self.current_arousal] = self.generateRandomMood()

        self.initial_mood = self.current_mood
        self.initial_mood_name = self.current_mood_name
        self.initial_relax = self.current_relax
        self.initial_arousal = self.current_arousal

# symulacja
mood_threshold = 6

initial_arousal = 10  # 0: 10, 1: 70, 2: 70, 3: 10
initial_relax = 10  # 0: 10, 1: 10, 2:70, 3: 70
target_mood = 2

# Parametry różnych użytkowników do kolejnych testów
# respondent nr 1 (K, 21l.)
user1 = User("User 1 (F21)", 21, user1_preferences, target_mood)
# respondent nr 40 (M, 26l.)
user2 = User("User 2 (M26)", 26, user2_preferences, target_mood)
# respondent nr 45 (K, 52l.)
user3 = User("User 3 (F52)", 52, user3_preferences, target_mood)

# Tworzymy nasze środowisko, przekazując preferencje użytkownika
# symulacja
current_user = user2
env = Room(current_user)

# Przykład użycia
# obs = env.reset()

# Iterujemy przez akcje generowane przez generator
# TODO tu jakoś trzeba będzie złapać zmianę action_sequence_popular przy zmianie scenariusza
# pierwsza propozycja - przechodź przez pętle akcji z kolejnymi sekwencjami dopóki nie zostanie osiągnięcty cel
# while not env.done:

results = []
best_results = []
continuous_simulation_results = []
highest_mood_change = 0

def getResultsArray(_env, _action_id, _iteration, _time):
    resultArray=[
        _env.user.name,
        _env.user.initial_mood,
        _env.user.current_mood,
        _env.user.target_mood,
        mood_threshold,
        _env.done,
        _env.is_scenario_changed,
        _action_id,
        _iteration, 
        _time,
        _env.mood_change,
        list(_env.state)[0], list(_env.state)[1], list(env.state)[2], list(_env.state)[3], list(_env.state)[4], list(_env.state)[5],
        _env.user.initial_relax,
        _env.user.initial_arousal,
        _env.user.current_relax,
        _env.user.current_arousal
    ]

    return resultArray
def getResultsArrayHeaders():
    resultArrayHeaders = [
        "User",
        "Initial mood",
        "Current mood",
        "Target mood",
        "Mood threshold",
        "Done",
        "Is scenario changed",
        "Action id",
        "Iteration",
        "Time",
        "Mood change",
        "light intensity", "Light color", "Temperature", "Music type", "Music volume", "Fragrance",
        "Initial relax",
        "Initial arousal",
        "Current relax",
        "Current arousal"
    ]

    return resultArrayHeaders

def runSingleTest(action_sequence, _action_id, _highest_mood_change):
    for action in action_sequence:
        iteration = 1
        time = 15
        action_id = _action_id
        highest_mood_change = _highest_mood_change

        while iteration <= max_iterations_amount:
            # print("[", iteration,"]", env.user.current_mood, env.user.current_arousal, env.user.current_relax, "(", env.mood_change, ")")
            obs, reward, done, info = env.step(action)

            if env.done:
                print("Stopped at", action_id)
                print("Mood change:", env.mood_change, "Mood threshold:", mood_threshold)

                # Znaleziono wystarczająco dobry wynik
                if env.mood_change >= mood_threshold:
                    print("Satisfying mood change found:", env.mood_change)

                if env.mood_change > highest_mood_change:
                    _highest_mood_change = env.mood_change
                    best_results.append(getResultsArray(env, action_id, iteration, time))

                env.user.getInitialMood()

                # kończenie iterowania bieżącego ustawienia
                break

            elif time >= simulation_time:
                print("Time runout")

                env.user.getInitialMood()
                # kończenie iterowania bieżącego ustawienia
                break

            else:
                env.render()
                # print("Action:", action)
                # print("State after action:", obs)
                # print("Reward:", reward)
                # print("Done:", done)
                # print("Info:", info)
            iteration += 1
            time += 15

        # Zapisz wynik niezależnie od zakończenia
        results.append(getResultsArray(env, action_id, iteration, time))

        _action_id += 1

        if env.mood_change >= mood_threshold:
            print("Satisfying solution found, no new settings will be applied")
            break

    return [_action_id, _highest_mood_change]
def runContinuousSimulation(action_sequence, _action_id, _highest_mood_change):
    for action in action_sequence:
        iteration = 1
        time = 15
        action_id = _action_id

        while iteration <= max_iterations_amount:
            # print("[", iteration,"]", env.user.current_mood, env.user.current_arousal, env.user.current_relax, "(", env.mood_change, ")")
            obs, reward, done, info = env.step(action)

            if env.is_scenario_changed or env.done:
                print("Stopped at", action_id)
                print("Mood change:", env.mood_change, "Mood threshold:", mood_threshold)

                if env.mood_change > _highest_mood_change:
                    _highest_mood_change = env.mood_change
                print("Done/Scenario changed")

                # jeśli osiągnięto przejście z satysfakcjonującym wynikiem
                if env.mood_change >= mood_threshold:
                    print("Stopped at", action_id)
                    print("Mood change:", env.mood_change, "Mood threshold:", mood_threshold)

                    # continuous_simulation_results.append(getResultsArray(env, action_id, iteration, time))

                    if env.is_scenario_changed:
                        [env.user.initial_mood, env.user.initial_arousal, env.user.initial_relax] = [env.user.current_mood, env.user.current_arousal, env.user.current_relax]

                else:
                    env.user.getInitialMood()
                    env.step_mood = env.setStepMood(env.user.current_mood, env.user.target_mood)
                    print("Keep looking...")
                break
            elif time >= simulation_time:
                print("Time runout")
                env.user.getInitialMood()
                break
            else:
                env.render()
                # print("Action:", action)
                # print("State after action:", obs)
                # print("Reward:", reward)
                # print("Done:", done)
                # print("Info:", info)
            iteration += 1
            time += 15

        # Zapisz wynik niezależnie od zakończenia
        results.append(getResultsArray(env, action_id, iteration, time))
        print("Mood change:", env.mood_change)

        if (env.is_scenario_changed or env.done) and env.mood_change >= mood_threshold:
            break
        # else:
        #     env.user.getInitialMood()

        _action_id += 1

    return [_action_id, _highest_mood_change]


abc = 0

# Single Test
if env.correct_input and current_user.target_mood != current_user.initial_mood + 2:
    # while env.reward != 2:
    [action_id, highest_mood_change] = runSingleTest(env.action_sequence_popular, 1, 0)

    print("Mood change:", highest_mood_change)
    print("Reward:", env.reward)

    if highest_mood_change >= mood_threshold:
        print("Solution found among popular settings!")
    elif highest_mood_change < mood_threshold:
        print("Couldn't find the best result among popular settings, trying All settings.")
        [action_id, highest_mood_change] = runSingleTest(env.action_sequence_all, action_id, highest_mood_change)

    filename = "results.csv"
    file_exists = os.path.isfile(filename)
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(filename) == 0:
            writer.writerow(getResultsArrayHeaders())
        writer.writerows(results)

    filename2 = "best_results.csv"
    file_exists = os.path.isfile(filename2)
    with open(filename2, 'a', newline='') as file:
        writer = csv.writer(file)

        # Jeśli plik nie istnieje lub jest pusty, dodaj nagłówki
        if not file_exists or os.path.getsize(filename2) == 0:
            writer.writerow(getResultsArrayHeaders())
        writer.writerows(best_results)

# Continuous Run
elif env.correct_input and current_user.target_mood == current_user.initial_mood + 2:
    # _action_sequence = [*env.action_sequence_popular, *env.action_sequence_all]
    # print(_action_sequence)
    while env.reward != 2:
        action_id = 1
        [action_id, highest_mood_change] = runContinuousSimulation(env.action_sequence_popular, action_id, 0)
        if not env.is_scenario_changed and not env.done:
            [action_id, highest_mood_change] = runContinuousSimulation(env.action_sequence_all, action_id, highest_mood_change)

    filename3 = "results.csv"
    file_exists = os.path.isfile(filename3)
    with open(filename3, 'w', newline='') as file:
        writer = csv.writer(file)

        if not file_exists or os.path.getsize(filename3) == 0:
            writer.writerow(getResultsArrayHeaders())
        writer.writerows(results)

    filename4 = "continuous-simulation-results.csv"
    file_exists = os.path.isfile(filename4)
    with open(filename4, 'a', newline='') as file:
        writer = csv.writer(file)

        # Jeśli plik nie istnieje lub jest pusty, dodaj nagłówki
        if not file_exists or os.path.getsize(filename4) == 0:
            writer.writerow(getResultsArrayHeaders())
        writer.writerows(continuous_simulation_results)