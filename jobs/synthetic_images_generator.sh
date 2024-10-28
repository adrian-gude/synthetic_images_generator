#!/bin/bash
#SBATCH -J synthetic_images_generator       # Job name
#SBATCH -o synthetic_images_generator_%j.o       # Name of stdout output file(%j expands to jobId)
#SBATCH -e synthetic_images_generator_%j.e       # Name of stderr output file(%j expands to jobId)
#SBATCH -c 64          # Cores per task requested
#SBATCH --gres=gpu:a100:4   # Solicitar 2 GPUs A100 (40GB cada una)
#SBATCH -t 48       # Run time (hh:mm:ss) - 10 min
#SBATCH --mem=128GB         # Memory per core demandes (24 GB = 3GB * 8 cores)
#SBATCH --mail-type=ALL       # Send email on start, end and abortion
#SBATCH --mail-user=adrian.lopez.gude@udc.es  # Email to send notifications
# 
# Load the necessary modules
module load python/3.9.9
#
#
source $LUSTRE/.venv/bin/activate
pip3 install -r $LUSTRE/synthetic_images_generator/requirements.txt
echo "Running the script"
python3 $LUSTRE/synthetic_images_generator/main.py
