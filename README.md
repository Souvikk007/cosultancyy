GitHub usage:
git clone <link> //cloning to local machine

git add . //adding the new files

git commit -m "Your message" //committing changes to the file 

git push origin main //push the local file changes to github repository



Step1 :(create virtual environment)
python -m venv myenv
myenv\Scripts\activate

Step 2:(install packages)
python -m pip install Django
python -m pip install pillow

step3: (run application)
python manage.py runserver

step4 :(after usage)
myenv\Scripts\deactivate.bat
