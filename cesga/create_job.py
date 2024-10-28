import argparse


def create_script(job_name, cores, gpu_num, run_time, memory, notification):

    if notification != None:
        script = f"""#!/bin/bash
#SBATCH -J {job_name}       # Job name
#SBATCH -o {job_name}_%j.o       # Name of stdout output file(%j expands to jobId)
#SBATCH -e {job_name}_%j.e       # Name of stderr output file(%j expands to jobId)
#SBATCH -c {cores}          # Cores per task requested
#SBATCH --gres=gpu:a100:{gpu_num}   # Solicitar 2 GPUs A100 (40GB cada una)
#SBATCH -t {run_time}       # Run time (hh:mm:ss) - 10 min
#SBATCH --mem={memory}         # Memory per core demandes (24 GB = 3GB * 8 cores)
#SBATCH --mail-type=ALL       # Send email on start, end and abortion
#SBATCH --mail-user={notification}  # Email to send notifications
# 
# Load the necessary modules
module load python/3.9.9
#
#
source $LUSTRE/.venv/bin/activate
pip3 install -r $LUSTRE/requirements.txt
echo "Running the script"
python3 $LUSTRE/{job_name}/main.py
"""

    return script


def main():
    parser = argparse.ArgumentParser(description="Create a new job for CESGA TASK")
    parser.add_argument("--job_name", help="Name of the job")
    parser.add_argument("--cores", help="Cores per task to use", default=64)
    parser.add_argument("--gpu_num", help="Number of GPUs to use", default=2)
    parser.add_argument("--run_time", help="Run time (hh:mm:ss)", default="01:00:00")
    parser.add_argument("--memory", help="Memory per core demandes", default="128GB")
    parser.add_argument("--notification", help="Email to send notifications")
    args = parser.parse_args()

    script = create_script(
        args.job_name,
        args.cores,
        args.gpu_num,
        args.run_time,
        args.memory,
        args.notification,
    )

    with open(f"jobs/{args.job_name}.sh", "w") as f:
        f.write(script)


if __name__ == "__main__":
    main()
