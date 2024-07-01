from gymnasium.envs.registration import register

register(
    id="gym_examples/Room-v0",
    entry_point="gym_examples.envs:RoomEnv",
    max_episode_steps=300,
)