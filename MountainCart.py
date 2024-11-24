import gymnasium as gym

def main():
    # Create the MountainCar environment
    env = gym.make("MountainCar-v0", render_mode="human")

    # Reset the environment
    observation, info = env.reset(seed=42)

    # Run the game loop
    for _ in range(500):
        action = env.action_space.sample()  # Take random actions
        observation, reward, done, truncated, info = env.step(action)

        if done or truncated:

            print("Episode finished. Restarting...")
            observation, info = env.reset()

    env.close()

if __name__ == "__main__":
    main()