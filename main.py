import json
from diffusers import StableDiffusion3Pipeline
from accelerate import Accelerator
import torch
import os


def load_prompts():
    with open("animal_prompts.json", "r") as f:
        return json.load(f)


def main():

    accelerator = Accelerator(mixed_precision="bf16")
    device = accelerator.device

    pipe = StableDiffusion3Pipeline.from_pretrained(
        "stabilityai/stable-diffusion-3.5-large", torch_dtype=torch.bfloat16
    )

    prompts = load_prompts()
    num_gpus = torch.cuda.device_count()
    prompts_batches = [prompts[i::num_gpus] for i in range(num_gpus)]
    pipe = accelerator.prepare(pipe)

    for i, batch_prompts in enumerate(prompts_batches):
        print(f"Processing batch {i+1}/{len(prompts_batches)} on {device}")

        for prompt in batch_prompts:
            with accelerator.autocast():
                image = pipe(prompt).images[0]

            image_filename = f"data/{prompt.replace(' ', '_')}.jpeg"
            image.save(image_filename)


if __name__ == "__main__":
    main()
