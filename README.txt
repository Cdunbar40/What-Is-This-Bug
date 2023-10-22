This project was the final capstone project for WGU. THe goal for this project was to create an application that incorporated a machine learning model to identify 15 common species of pest insect encountered in agriculture in the US. The 15 species selected were: 

1. African Honey Bee
2. Aphid
3. Armyworm Moth
4. Brown Marmorated Stink Bug
5. Cabbagee Looper Moth
6. Colorado Potato Beetle
7. Corn Earworm Moth
8. European Corn Borer Moth
9. Five-Spotted Hawk Moth
10. Flea Beetle
11. Fruit Fly
12. Japanese Beetle
13. Spider Mite
14. Thrip
15. Western Corn Rootworm Beetle

The final model had an overall accuracy of 79%. 

User Instructions:

Use of the application requires Anaconda/Miniconda and Pycharm. Both of these are free from their respective sites. 

1.	If not already done, install Anaconda or Miniconda:
	a.	Navigate to https://www.anaconda.com/download (for Anaconda) or https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html (for miniconda) and follow the 		website instructions to install. 

2.	If not already done, install Pycharm:
	a.	Navigate to https://www.jetbrains.com/pycharm/ and download Pycharm Community Edition. 

3.	Create the necessary environment
	a.	If not already done, create a directory on your computer and unzip the folder for this submission (C964-Capstone-Dunbar.zip) in that directory. 
	b.	Launch Anaconda Prompt (which should be in your list of applications after installing Anaconda/Miniconda).
	c.	Using Anaconda Prompt, navigate to the C964-Capstone-Dunbar folder. Ensure that the ‘environment.yml’ file is in the directory. 
	d.	Type the following command into the prompt: conda env create -–prefix ./env -f environment.yml
	e.	Wait until the environment has been created. 

4.	Open the project in PyCharm:
	a.	Launch PyCharm. From the menu, select File -> Open, then navigate to the C964-Capstone-Dunbar folder and select the What-Is-This-Bug – Application Files folder. 

5.	Associate the environment with the Project: 
	a.	In PyCharm, select File -> Settings -> Project: What-Is-This-Bug -> Python Interpreter -> Add Interpreter -> Add local interpreter -> Conda Environment
	b.	In the conda executable box, browse to the location of your conda.exe file – This is usually located in C:\ProgramData\Anaconda\Scripts or C:\ProgramData\Miniconda			\Scripts, but location may vary depending on where you installed Ancaonda/Miniconda. This will load a list of conda environments to choose from. 
	c.	Select the environment created in step 3, then click ok. In the next window, click apply and then ok. Allow PyCharm some time to load the environment. 

6.	Launch the application:
	a.	Navigate to C964-Capstone-Dunbar\What-Is-This-Bug - Application Files\Model and open the main.py file in PyCharm. 
	b.	Click the run button to launch the application. 

7.	Use the model:
	a.	Click browse to locate the image you would like to identify. Note that the model can only identify the insects listed in Table D.1. 
	b.	Click upload to run the model – The application will report a result and a confidence level. 

8.	To view visualizations of the data used for the model and the model’s performance in the application, click on the About the Model button, then click on the metric you would like 	to view. 

9.	Additionally, if you would like to view and interact with the notebook used to create the model, WGU C964 (Capstone) - Harmful Insect Classification.ipynb, perform the following:
	a.	Using Anaconda Prompt, navigate to the folder containing the environment created in step 3. 
	b.	Enter ‘conda activate ./env’ in the prompt. 
	c.	Enter ‘jupyter notebook’ in the prompt
	d.	Once Jupyter Notebook has launched, navigate to Model Creation Files\WGU C964 (Capstone) - Harmful Insect Classification.ipynb and double click the notebook to open it.
