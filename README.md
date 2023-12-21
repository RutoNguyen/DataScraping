<span style="color:red">If you have not downloaded anaconda, please download with instructions: [Anaconda](https://docs.anaconda.com/free/anaconda/install/windows/){:target="_blank"}</span>

# 1.Create a new Conda virtual environment named "DataScraping" with Python version 3.9. 
'conda create -n DataScraping python=3.9'
# 2.Activate the virtual environment named "DataScraping"
'conda activate DataScraping'
# 3.Upgrade the Pip package manager to the latest version.
'pip install --upgrade pip=23.3.2'
# 4.Points to the 'path' where the txt file is saved. 
> path: where you save the Requirements.txt file.
'cd path'
Exam:'cd C:\Users\Ruto\ScrapingData'
# 5.Install the libraries and dependencies listed in the [Requirements](https://github.com/RutoNguyen/ScrapingData/Requirement.txt) file.
'pip install -r Requirements.txt'
# 6.Run [DataScraping.py](https://github.com/RutoNguyen/ScrapingData/DataScraping.py) file
'python DataScraping.py'