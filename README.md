# Team Proect "Cafe Journey Web Application"
Course: CISC 593-90- O-2023/Late Fall - Software Verification & Validation
Professor:  Abrar Qureshi, Ph.D. (Professor of CS & Software Engineering)
Students: Team 1 (Evgenii Kharitonov, Edwin Herrera, Haiying Xu, Leiyu Yue)

On the root folder you can find the working FILES for the project. DON'T change the files in the root folder. Working files to experiment "CafeJourney" and number of version you can find in the folder "development".

Running IPYNB (Jupyter Notebook) files directly in GitHub Codespaces involves setting up a Python environment and ensuring that Jupyter is installed and configured correctly:

#### Step 1: Start Jupyter Notebook Server
   - In the Codespaces terminal, navigate to the directory containing your IPYNB files.
   - Start the Jupyter Notebook server in Terminal:
     "jupyter notebook --no-browser --ip=0.0.0.0"
   - This command runs the Jupyter server without launching a browser and binds it to all available IPs.

#### Step 2: Access Jupyter Notebook
   - Jupyter will provide a URL in the terminal, which includes a token for access. It will look something like "http://127.0.0.1:8888/?token=...".
   - Copy this URL.

#### Step 3: Configure Port Forwarding
   - In Codespaces, set up port forwarding for the port used by the Jupyter server (usually "8888").
   - This allows you to access the Jupyter server from your local browser.

#### Step 4: Open the IPYNB File
   - Paste the copied URL with the token into your browser.
   - Navigate to the IPYNB file in the Jupyter interface and open it.

#### Step 5: Work with Your Notebook
   - You can now edit and run the notebook as you would in a local Jupyter environment.


Updating the "requirements.txt" file for a Python project involves specifying the necessary libraries and their versions that your project depends on. This file is used by package managers like "pip" to install all the dependencies in one go. Here's a step-by-step guide on how to update it:

#### Step 1: Identify Dependencies
- List all the external Python libraries your project uses. This can be done by reviewing your project's import statements or existing documentation.
- If you're working in a virtual environment (which is recommended), you can generate a list of currently installed packages and their versions using "pip freeze".

#### Step 2: Generate a Requirements File
- If you don't already have a "requirements.txt" file or want to update it with your current environment, run the following command in your virtual environment:
  "pip freeze > requirements.txt"
  This command creates (or overwrites) a "requirements.txt" file with a list of installed packages and their versions.

#### Step 3: Edit the Requirements File
- Open the "requirements.txt" file in a text editor.
- Review and edit the file:
  - Remove unnecessary packages that might have been included.
  - If specific version numbers are not required, you can remove the version specification. For example, change "flask==1.1.2" to just "flask".
  - If you need a specific version or a version range for a package, specify it. For example, "requests>=2.24.0" ensures that version 2.24.0 or newer is installed.

#### Step 4: Test the Updated Requirements
- To test if your "requirements.txt" works correctly, you can create a new virtual environment and install the packages using:
  "pip install -r requirements.txt"
- Run your project to ensure all dependencies are correctly installed and the project works as expected.

#### Step 5: Commit and Push Changes
- Once you've verified that everything works, commit the updated "requirements.txt" file to your version control system (like Git).
- Push the changes to your remote repository.