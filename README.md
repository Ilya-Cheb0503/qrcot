# Учебный проект «Cat Charity Fund» 
 
## Описание 
 
Проект Cat Charity Fund — это инвестиционный сервис. 
Его назначение — Собрать средства для оказания помощии пушистым братьям нашим меньшим. 
 
Данное приложение предоставляет возможность отправлять благотворительные донаты на общий счет пожертвований.
Все пожертвованные средства в дальнейшем буду реализованны в проектах, которые сделают мир пушистиков лучше.  
 
Задачи, выполняемые данным сервисом: 
 - Создание проектов по сбору средств [необходимы права администратора]; 
 - Создание пожертвований, которые автоматически будут распределены в первый в очереди проект;
 
 
Результируя описанное, данный проект направлен на улучшение жизни всех кошачих.
Если у Вас имеются идеи для новых проектов, Вы можете связаться с автором данного сервиса для его реализации.
 
 
##  В данном проекте использовались следующие технологии и модули: 
 
- FastApi
- Alembic 
- Pydantic 
- SQLAlchemy
- Uvicorn
  
 *Полный список Вы можете посмотреть в requirements.txt* 
 
 
 
## Алгоритм установки проекта: 
 
1. Клонировать репозиторий и перейти к нему в командной строке: 
 
```bash 
git clone git@github.com:Ilya-Cheb0503/cat_charity_fund.git
``` 
```bash 
cd cat_charity_fund/ 
``` 
2. Создать и активировать виртуальное окружение: 
```bash 
python -m venv env 
``` 
```bash 
source env/bin/activate 
``` 
3. Установить зависимости из файла requirements.txt: 
```bash 
python -m pip install --upgrade pip 
``` 
```bash 
pip install -r requirements.txt 
``` 
 
4. Запустить проект: 
```bash 
uvicorn app.main:app
``` 
 
## Примеры возможных запросов и ответов API: 
 
Возможный вариант запроса к адресу https://127.0.0.1:8000/charity_project/
[Необходимы права Администратора]
```javascript 
{
  "name": "Building",
  "description": "a lot of new houses for cats",
  "full_amount": 10000
}
 
``` 
Ответ API: 
 
```javascript 
{
  "name": "Building",
  "description": "a lot of new houses for cats",
  "full_amount": 10000,
  "id": 1,
  "invested_amount": 0,
  "fully_invested": false,
  "create_date": "2024-02-03T07:20:02.600068"
}
 
``` 
Возможный вариант запроса к адресу https://127.0.0.1:8000/donation/
```javascript 
{
  "full_amount": 500,
  "comment": "wish everyone lonely cat has got own home"
}
 
``` 
Ответ API: 
 
```javascript 
{
  "comment": "wish everyone lonely cat has got own home",
  "full_amount": 500,
  "id": 1,
  "create_date": "2024-02-03T07:20:32.702522",
  "close_date": "2024-02-03T07:20:32.724931"
}
 
``` 


### Авторы 
Чебан Илья - студент образовательной платформы "Яндек_Практикум"