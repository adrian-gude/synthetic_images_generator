import json
import itertools


def generate_prompts():
    animals = ["dog", "cat", "deer", "bird", "fish", "fox"]
    environments = ["park", "beach", "forest", "countryside", "city"]
    weather_conditions = ["sunny", "rainy", "snowy", "cloudy", "at sunset"]
    activities = ["playing", "resting", "hunting", "swimming", "looking at the camera"]

    combinations = list(
        itertools.product(animals, environments, weather_conditions, activities)
    )

    prompts = []
    for animal, environment, weather, activity in combinations:
        prompt = f" Generate an image of a {animal} {activity} in a {environment} on a {weather} day"
        prompts.append(prompt)

    return prompts


def save_prompts(prompts):
    with open("data/animal_prompts.json", "w") as f:
        json.dump(prompts, f, indent=4)


def main():
    prompts = generate_prompts()
    save_prompts(prompts)


if __name__ == "__main__":
    main()
