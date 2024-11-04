# Synthetic Images Generator

## Description

The `synthetic_images_generator` project is a tool for generating synthetic images based on prompts. This project utilizes deep learning models, specifically transformers and diffusion models, to create synthetic images. It is designed to help developers, researchers, and artists create images based on textual prompts, with applications in AI-assisted design, art generation, and synthetic dataset creation.

## Features

- Generate synthetic images from text prompts.
- Easily configurable with options for prompt customization.
- Compatible with Hugging Face models and diffusers.
- Flexible job configuration and data storage setup.

## Prerequisites

- Python 3.8 or higher
- Basic knowledge of Python and PyTorch is recommended for advanced customization.

## Installation

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd synthetic_images_generator

2. Install Dependencies Ensure that you have a virtual environment set up, then install the necessary packages:
    ````bash 
    python -m venv venv
    source venv/bin/activate  
    pip install -r requirements.txt
    ````

## Usage

### Generating Prompts

To create prompts for synthetic images, use the `generate_prompts.py` script:
````bash
python generate_prompts.py 
````


### Running the Main Script

The main script, main.py, is the entry point for generating images from prompts. Run it with:

`````bash
python main.py 
`````

This command will generate images based on the specified prompt and save them in the output directory.

## Configuration

Customize the behavior of the generator by editing configuration files in the `cesga` or `jobs` directories. These folders contain settings for various aspects of image generation and job management.

## Dependencies

The project relies on several Python libraries, as specified in `requirements.txt`, including:

- `torch`
- `transformers`
- `diffusers`
- `tqdm`
- `Pillow`
- `numpy`

Install these with:

````bash
pip install -r requirements.txt
````
## Folder Structure

- `cesga/`: Contains job configurations and templates.
- `data/`: Directory for storing generated data.
- `jobs/`: Additional configurations for managing multiple prompt generation tasks.
- `generate_prompts.py`: Script to generate text prompts.
- `main.py`: Main script to generate synthetic images.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For issues or feature requests, please open an issue in the GitHub repository.
