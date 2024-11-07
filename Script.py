import os

# Define the base directory name
base_dir = r'D:\Code\100-Days-Of-Python'

# Ensure the base directory exists
if not os.path.exists(base_dir):
    os.mkdir(base_dir)

# Create directories for each day with leading zeros
for day in range(1, 101):
    day_dir = os.path.join(base_dir, f'Day-{day:03}')
    os.mkdir(day_dir)

    # Optionally, create a README.md file in each day's directory
    readme_path = os.path.join(day_dir, 'README.md')
    with open(readme_path, 'w') as readme_file:
        readme_file.write(f'# Day {day} Project\n\nDescription of the project for Day {day}.\n')

print('Directories for all 100 days have been created successfully.')
