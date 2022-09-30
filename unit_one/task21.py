#todo: Задан словарь, его значения необходимо внести по соответвющим тегам и атрибутам вместо вопросов (?)
# заполненный шаблон записать в файл index.html

page = {"title": "Тег BODY",
        "charset": "utf-8",
        "alert": "Документ загружен",
        "p": "Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat."}


template = """ 
<!DOCTYPE HTML>
<html>
 <head>
  <title> ? </title>
  <meta charset=?>
 </head>
 <body onload="alert(?)">
 
  <p>?</p>

 </body>
</html>
"""

template_new = """ 
<!DOCTYPE HTML>
<html>
 <head>
  <title> Тег BODY </title>
  <meta charset=utf-8>
 </head>
 <body onload="alert Документ загружен">

  <p> Ut wisis enim ad minim veniam,  suscipit lobortis nisl ut aliquip ex ea commodo consequat. </p>

 </body>
</html>
"""


def create_file():
        fd = open('index.html', 'wt', encoding='utf-8')
        fd.write(template)
        fd.seek(1)
        fd.write(template_new)
        fd.close()

create_file()



