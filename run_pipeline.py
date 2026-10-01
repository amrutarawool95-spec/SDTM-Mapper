import subprocess

steps = [
    "src/generate_raw_data.py",
    "src/build_sdtm.py",
    "src/validate_sdtm.py",
    "src/export_xpt.py"
]

for step in steps:

    print(f"\nRunning {step}")

    subprocess.run([
        "python",
        step
    ], check=True)

print("\nSDTM pipeline completed.")
