Please follow the below steps to run and test this project.
1. Download python 
2. Download any editor(i.e. Vscode)
3. Open cmd and run command pip install Django
4. Once above steps has been done then open FileProject in Vs code.
5. Open terminal in VS code and run Python manage.py runserver


Endurl Test:

http://127.0.0.1:8000/   -- If you will not give any file name in url then by default it will show the content of "file1.txt"
http://127.0.0.1:8000/file2.txt/ -- It will give the content of file2.txt similary you can also check url with other files.
http://127.0.0.1:8000/file2.txt/?startline=0&endline=23  - if you will pass such type of qwery string then it will show filteration data of lines between 0 to 23
