# ITMO_ICT_WebDevelopment_2020-2021
Репозиторий для реализации дистанционного обучения по дисциплине "Web-программирование".

[Учебный журнал](https://docs.google.com/spreadsheets/d/1rY3GdS3yUNuSwOL_6xIlhF1UsHbzj0WrrxrA6l0c8Xw/edit?usp=sharing) по дисциплине. Тут доступна информация о сроках сдачи работ, о текущей успеваемости студентов и описаны все материалы необходимые для реализации курса.

60 баллов - лабы. 20 баллов - тесты. 20 - экзамен. При выполнении всех лаб по дисциплине в срок - экзамен-автомат.

## Инструкции
Дополнительные материалы делятся на 3 категории:

1. Для тех, кто считает, что имеет недостаточно базовых знаний об информатике, веб-разработке и сетях (обзначается **(+)**).
2. Для тех, кто считает, что имеет базовые знания  (обзначается **(++)**).
3. Для тех, кто хочет поглубже изучить материал  (обзначается **(+++)**).

## Лекция 1.1 - Концепции разработки веб сервисов.
Презентация с лекции [тут](https://drive.google.com/file/d/1uZMyzGn_42krfuEdR-pLmcrb2LGqYNmx/view?usp=sharing).

Допонительные материалы:

1. [Иерархия компьютерных информационных систем для разработки сайта](https://habr.com/ru/post/513486/) **(+)**
2. [Топ-5 наиболее популярных CMS: какую выбрать?](https://habr.com/ru/post/151879/) **(++)**
3. [Веб-фреймворки: введение для новичков (классификация фреймворков)](https://tproger.ru/translations/web-frameworks-how-to-get-started/) **(++)**
4. [Чем отличаются фронтенд- и бэкенд-разработка](https://techrocks.ru/2020/07/01/front-end-vs-back-end-development/) **(+)**
5. [Что такое MVC: базовые концепции и пример приложения](https://skillbox.ru/media/code/chto_takoe_mvc_bazovye_kontseptsii_i_primer_prilozheniya/) **(++)**

## Лекция 1.2 - Компоненты клиент-серверного взаимодействия.
Презентация лекции [тут](https://drive.google.com/file/d/1Jp_7c5GcK8TeLii2yEDuSmjLyXIlGQs1/view?usp=sharing).

Дополнительные материалы:

1. [Сетевая модель OSI](https://ru.wikipedia.org/wiki/%D0%A1%D0%B5%D1%82%D0%B5%D0%B2%D0%B0%D1%8F_%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D1%8C_OSI) **(+)**
2. [Адресация в сетях](https://support.microsoft.com/ru-ru/help/164015/understanding-tcp-ip-addressing-and-subnetting-basics) **(+)**
3. [TCP vs UDP](https://habr.com/ru/company/oleg-bunin/blog/461829/) **(+++)**

## Лабораторная работа 1. Работа с сокетами.
[Текст работы](https://drive.google.com/file/d/1p5FUB09uZlniENeAmPSuXjYvI-G7bCGy/view?usp=sharing)

Срок сдачи: **25.09.2020** (включительно). Вес работы в баллах – 10. Выполнение пунктов 1-3 и 4 (однопользовательский чат без потоков) – 8. Выполнение пунктов 1-3 и 4 (многопользовательский чат с потоками) – 10. После срока сдачи максимальный бал 6.

### Полезные материалы:
- [Большой мануал про сокеты, http, wsgi](https://iximiuz.com/ru/posts/writing-python-web-server-part-1/)**(+++)**

### Сдача работы №1

Полученную модель, код и отчет залить в папку репозитория **students/группа/laboratory_works/фамилия_имя/laboratory_work_1**. Инструкция о загрузке работы ниже. Не забывайте о файле gitignor.

На git должен быть загружен pdf-файл с отчетом, код программамы, **где каждая папка соотвествует части работы (task_1, task_2...)**.

Шаблон имени файла отчета: **Фамилия_Имя_группа_№лабы**. Отчет должен содержать титульный лист, листинг кода по каждому пункту с комментариями, скрины работы программ.

Как делать пул-реквест описано в разделе **[Сдача работ](https://github.com/TonikX/ITMO_ICT_WebDevelopment_2020-2021/blob/master/README.md#%D1%81%D0%B4%D0%B0%D1%87%D0%B0-%D1%80%D0%B0%D0%B1%D0%BE%D1%82)**

## Дополнительный контент к первой лабе
Те студенты, которые хотят получить более обширное представление о работе с конструкторами сайтов, могут пройти [этот курс](https://geekbrains.ru/courses/74).

## Лабораторная работа 2. Реализация простого сайта на django.

### Практическая работа №2.1

Цель работы: дать краткое представление о работе Django **WEB** фреймворка.
Необходимо выполнить все пункты [лога](https://docs.google.com/document/d/1zHvKAh_CDcSnpFPgtNQq7JulRoBTiY4OdMlRth-Rjuc/edit?usp=sharing) практической работы. Полученную программу залить в папку этого репозитория **sutdents/группа/practical_works/фамилия_имя/simple_django_web_project**. Инструкция о загрузке работы ниже. Не забывайте о файле гитигнор.

### Практическая работа №2.2

Цель работы: дать подробное представление о реализации CRUD(Create, read, update and delete) интерфейсов средствами Django **WEB** фреймворка.
Необходимо выполнить все задлания с пометкой **"задача"** [практической работы №2](https://docs.google.com/document/d/1koLV9iGXJfL2yh88InKo4AVXxWqMIJOqmzT4XFYlWuU/edit?usp=sharing) практической работы. Полученную программу залить в папку этого репозитория **sutdents/группа/practical_works/фамилия_имя/simple_django_web_project**. Инструкция о загрузке работы ниже. Не забывайте о файле гитигнор.

### Практическая работа №2.3

Необходимо выполнить все задлания с пометкой **"задача"** [практической работы №3](https://docs.google.com/document/d/1kQ36RlRtxqpjtUtfr-WCWkuJ1SYvSG4220Ops2X0viw/edit?usp=sharing
) практической работы. Полученную программу залить в папку этого репозитория **sutdents/группа/practical_works/фамилия_имя/simple_django_web_project**. Инструкция о загрузке работы ниже. Не забывайте о файле гитигнор.

## Лабораторная часть

Реализовать веб сервис, в соответствии с вариантом из задания (студент с порядковым номером 6 в списке группы делает 6 вариант, седьмой - вариант номер 1). Текст лабораторной работы [тут](https://drive.google.com/file/d/1kp4xcF-6r-g5jvephy69n9XvS-7hU4KT/view?usp=sharing). Срок сдачи: **20.10.2020** (включительно)

Обращаю внимание, что **доступна возможность предложить свой индивидуальный вариант** и делать работу по нему. 
Если Вы хотите индивидулаьный враиант, советую не использовать вариант из дисциплины "Адаптивный веб-дизайн" в этой работе, эффективнее Вы сможете его использовать в следующих работах.

## Полезные материалы

[Фундаментально](https://www.youtube.com/playlist?list=PLlWXhlUMyooaDkd39pknA1-Olj54HtpjX) - плейлист уроков по джанго для тех кто хочет **фундаментально** изучить, как работает джанго веб фремйворк и заниматься этим в будущем.

[Базово](https://www.youtube.com/playlist?list=PLF-NY6ldwAWqP4S95brtPHZ5fTCxilgei) - годный плейлист, который позволит **быстро** понять, как и что работает и сделать лабу.

### Сдача работы №2

Все файлы загрузить в папку **students/группа/laboratory_works/фамилия_имя/laboratory_work_2**. Инструкция о загрузке работы ниже. Не забывайте о файле gitignor.

На git должен быть загружен pdf-файл с отчетом, код программамы.

Шаблон имени файла отчета: **Фамилия_Имя_группа_№лабы**. Отчет должен содержать титульный лист, описание модели данных, описание контроллеров в файле views, описание роутеров файла urls, скрины работы программы.

Как делать пул-реквест описано в разделе **[Сдача работ](https://github.com/TonikX/ITMO_ICT_WebDevelopment_2020-2021/blob/master/README.md#%D1%81%D0%B4%D0%B0%D1%87%D0%B0-%D1%80%D0%B0%D0%B1%D0%BE%D1%82)**


## Лабораторная работа 3. Реализация серверной части на django rest. Документирование API.

Лекция 1

Содержание:

- rest и альтернативы (GrapgQL…)
- django rest framework
- подробно о формате json
- сериализация

[Запись лекции в аудитории](https://youtu.be/PI-FPq3zhpc)<br>
[Видео по сериализации от Давида](https://www.youtube.com/watch?v=sxdPf3z6Uw8&feature=youtu.be)

Лекция 2

- документирование апи
- Виды авторизации (сессии, токены)
- JWT + Использование JWT в Django
- Djoser 

Полезные материалы:

[простой курс](https://www.youtube.com/playlist?list=PLF-NY6ldwAWqP9PqPU3LA7mX2KJVyLhC_) - плейлист уроков по джанго для тех, кто хочет **быстро** изучить, как работает работает джанго рест фреймворк в связке с vue.js.

П.С. В 4 уроке изменился путь для получения токена авторизации (см. официальную докумекнтацию Djoser https://djoser.readthedocs.io/en/latest/getting_started.html)

Для тех, кто хочет лучше изучить DRF и работать с ним в будущем:
1) https://www.youtube.com/playlist?list=PLF-NY6ldwAWqSxUpnTBObEP21cFQxNJ7C
2) https://youtu.be/2rCjdYY-8R4?list=PLF-NY6ldwAWpktIw6ailetqjXibKlOLY_

### Практическая работа №3.1

Цель работы: дать представление об использовании возмжностей работы контроллеров и серриализаторов в Django Rest Framework.
Необходимо выполнить все задлания с пометкой **"задача"** [практической работы №3.1](https://docs.google.com/document/d/1PkpwxCUYQ2_Pi8Fpcgno6te3oCQHZfkh03Zxt6DhHSw/edit?usp=sharing) практической работы. Полученную программу залить в папку этого репозитория **sutdents/группа/practical_works/фамилия_имя/simple_drf_project. Инструкция о загрузке работы ниже. Не забывайте о файле гитигнор.

### Практическая работа №3.2 (Разрабатывается)

Цель работы: овладеть навыками написания документации к API.


### Лабораторная часть

Срок сдачи **04.12.2020**

Реализация серверной части приложения средствами django и djangorestframework в соответствии с заланием из [текста работы](
https://drive.google.com/file/d/1QxQo5jln6soFUj6EmOVEo1yauCo375PP/view?usp=sharing). Напоминаю, что Вы имеете возможность написать мне в Вк и мы утвердим Вам личный вариант.

Порядок выполнения работы:<br>
1.	Выполнить практическую работу 3.1 (https://docs.google.com/document/d/1PkpwxCUYQ2_Pi8Fpcgno6te3oCQHZfkh03Zxt6DhHSw/edit)<br>
2.	Выбрать вариант или предложить свой, есть 3 способа:<br>
2.1.	Предложить свой вариант.<br>
2.2.	Использовать вариант из дисциплины «Адаптивный веб-дизайн».<br>
2.3.	Выбрать вариант из вариантов по курсу «Основы баз данных» (https://drive.google.com/file/d/174gPjJ7AOHfzteYcobPY0x7sFBTkN1Xx/view?usp=sharing).<br>
2.4.	Выбрать бонусный вариант от Давида или Максима Валерьевича Хлопотова (см. пункт Бонусные варинты [тут](
https://drive.google.com/file/d/1QxQo5jln6soFUj6EmOVEo1yauCo375PP/view?usp=sharing).<br>
По любому из способов функционал нужно согласовать с преподавателем на консультации.<br>
3.	Реализовать модель базы данных средствами DjangoORM (согласовать с преподавателем на консультации).<br>
4.	Реализовать логику работу API средствами Django REST Framework (используя методы сериализации).<br>
5.	Подключить регистрацию / авторизацию по токенам / вывод информации о текущем пользователе средствами Djoser.<br>
6.	Выполнить практическую работу 3.2 по оформлению документации (в процессе разработки)<br>
7.	Реализовать документацию, описывающую работу всех используемых endpoint-ов из пункта 3 и 4 средствами Read the Docs или MkDocs.<br>

Работа выполняется индивидуально.<br>
Код практический и лабораторной части должен быть загружен в репозиторий курса, в соответствии с инструкциями тут.<br>
Работу необходимо защитить на консультации или прислать видео с описанием проделанной работы.<br>

### Сдача работы №3

Работа выполняется индивидуально.<br>
Работу необходимо защитить на консультации или прислать видео с описанием проделанной работы.<br>

#### Этап 1
Полученную программу залить в папку этого репозитория **sutdents/группа/laboratory_works/фамилия_имя/laboratiry_work_3**. Инструкция о загрузке работы ниже. Не забывайте о файле gitignore.

#### Этап 2
Работу необходимо защитить на консультации или прислать видео с описанием проделанной работы.

## Лабораторная работа 4. Реализация клиентской части средствами Vue.js.

Лекция 1

Содержание:

- Отличие многостраничного приложения от SPA [ссылка](https://drive.google.com/file/d/1aUwwy7xKJ32J9rXumK-xcI_ttWm1vcSx/view?usp=sharing)
- Angular vs. Vue vs. React [ссылка]()
- Компонентный подход + как работает роутинг на фронтенде [ссылка]()

[Запись лекции в аудитории]()<br>

## Лабораторная работа 5. Контейниризация и оркестрация.

## Сдача работ

Для сдачи работы в связи с переходом на дистанционную форму обучения введены дополднительные правила игры.

Все отчеты сохраняются в **pdf** (документы и презентации).

Все студенческие работы хранятся в папке **Students**
Для сдачи работы необходимо:

1. Зарегистрироваться на Git.
2. Сделать форк репозитория с заданиями в свой аккаунт (на странице https://github.com/TonikX/ITMO_ICT_DataBases_2020 кнопка fork справа, сверху).
3. Установить Git на компьютер.
4. Открыть папку, где хранятся Ваши проекты. В контекстом меню нажать "Open Git Bash here". Склонировать форкнутый репозиторий на комьютер (git clone https://github.com/ваш аккаунт/ITMO_ICT_DataBases_2020).
5. В файловой системе Вашего компрьютера в склонированном репозитории создать в папке students/группа Вашу личную папку в формате Фамилия_Имя латиницей (Пример **sutdents/k3340/Petrov_Vasya**).
6. В личной папке сделать подпапку с текущей работой в формате lr_номер (Пример **sutdents/k3340/Petrov_Vasya/Lr1**).
7. Записать в папку отчетные материалы.
8. Сделать коммит, описать его адекватно (Пример "был добавлен файл перезентация_петров.pdf"). Набрать команлы git add и git commit -m "название комита".
9. Сделать push в Ваш форкнутый репозиторий (git push).
10. Сделать пул-реквест в репозиторий преподавателя из вашего форкнутого, описать его. Структура заголовка пулреквеста: **Фамилия_Имя-Работа_Номер** (Пример: Петров_Василий-Лабораторная_работа_1).

Пользуйтесь [этой](https://vk.com/@efimchik_post_edu-tfm-2019-1) инструкцией, у нас нет веток с заданиями, как тут, но Вам поможет.
Все работы сдаются средствами создания Pull Requests в папку students в этом репозитории.

Еще один мануал о том, как сделать Pull Request описано [тут](https://rustycrate.ru/%D1%80%D1%83%D0%BA%D0%BE%D0%B2%D0%BE%D0%B4%D1%81%D1%82%D0%B2%D0%B0/2016/03/07/contributing.html).

