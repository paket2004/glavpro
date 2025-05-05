Проект автоматизации проведения отчётов glavpro.

Изначальные требования: установленный python, git bash, и vpn.

Шаги по тестированию системы и формированию отчёта.

!!! СИСТЕМА НАХОДИТСЯ В РАЗРАБОТКЕ И ЭТО ЕЁ САМЫЙ ПЕРВЫЙ МИНИМАЛЬНО РАБОЧИЙ ВАРИАНТ.
    В ДАЛЬНЕЙШЕМ ПОДХОД БУДЕТ МЕНЯТЬСЯ И СИЛЬНО СОВЕРШЕНСТВОВАТЬСЯ. !!!

1. Клонируем репозиторий 

Нажимаем на <> code -> https -> копируем ссылку в окне

Открываем git bash и пишем команду git clone <ссылка>, нажимаем enter.

2. Отчёт состоит из многих разделов. На текущий момент реализация таков, что разные разделы делаются в различных директориях, а потом сливаются воедино.

Первым делом нужно создать виртуальную среду и установить все зависимости, для этого делаем следующее:
В терминал пишем команды
python -m venv venv
venv/scripts/activate
pip install -r requirements.txt
Готово! переходим к формированию отчёта.
**Получение содержания**
Все команды будут выполняться через командную строку!

python content\content.py

Отлично! в папке content вы должны увидеть Содержание_отчета.docx файл.

**Основные термины, используемые в проекте и сокращения**

Здесь нужно включить vpn, потому что используется API, который недоступен для пользователей из России.

Также, нужен сам ключ API. Если у вас его нет, то нужно его получить (OpenAIApiKey) для того, чтобы была возможность генерировать ответ с помощью большой языковой модели.
После этого, вводим в консоль
streamlit run termins_and_short\termins_and_short_front.py

вводим через enter все наши термины и сокращения, получаем dictionary_table.docx файл в папке termins_and_short. Если это так, то всё здорово, идём дальше
(ВПН МОЖНО ОТКЛЮЧАТЬ)
**ВВЕДЕНИЕ**
Пишем в консоль streamlit run introduction\intro_front.py, вводим то, что от нас требуется, получаем файл introduction.docx в папке introduction

**СВЕДЕНИЯ О ХОЗЯЙСТВУЮЩЕМ СУБЪЕКТЕ, ОБЪЕКТЕ ОНВ, ЕГО ОТДЕЛЬНЫХ ТЕРРИТОРИЯХ И ПРОИЗВОДСТВЕННОЙ ДЕЯТЕЛЬНОСТИ, ВКЛЮЧАЯ СВЕДЕНИЯ О КОЛИЧЕСТВЕ, ХАРАКТЕРИСТИКАХ И ЭФФЕКТИВНОСТИ ГОУ**

1) streamlit run inventarization_description\punkt1\izav_info.py, заполняем, нажимаем сохранить. Получаем файл inventarization_description\punkt1\organization_sources_info.docx.

2) переходим к генерации описания СЗЗ. streamlit run object_property\sanitary_zone\sanitary_zone.py, заполняем, получаем файл object_property\sanitary_zone\description.docx

3) Характеристика пылегазоочистного оборудования и оценка его эффективности: streamlit run object_property\dust_and_gas\dust_and_gas.py, получаем файл object_property\dust_and_gas\dust_and_gus_info.docx.

4)  Сведения о результатах предыдущей инвентаризации: streamlit run object_property\previous_inventarization\prev_inv.py, заполняем, получаем файл object_property\previous_inventarization\prev_inv_info.docx

Теперь нужно всё слить воедино: python object_property\sanitary_zone\merger.py

**2. ОПИСАНИЕ ПРОВЕДЕННЫХ РАБОТ ПО ИНВЕНТАРИЗАЦИИ С УКАЗАНИЕМ НОРМАТИВНО-МЕТОДИЧЕСКИХ ДОКУМЕНТОВ И ПЕРЕЧНЯ ИСПОЛЬЗОВАННЫХ МЕТОДИК ВЫПОЛНЕНИЯ ИЗМЕРЕНИЙ ЗАГРЯЗНЯЮЩИХ ВЕЩЕСТВ И РАСЧЁТНОГО ОПРЕДЕЛЕНИЯ ВЫБРОСОВ**

streamlit run inventarization_description\izav_info\general_info_front.py, заполняем, получаем файлик inventarization_description\izav_info\description.docx
streamlit run inventarization_description\izav_info\boiler.py, нажимаем отправить, получаем файлик inventarization_description\izav_info\part2_without_intro.docx.

Сливаем их вместе: python inventarization_description\izav_info\merger.py.

**ХАРАКТЕРИСТИКИ ИСТОЧНИКОВ ЗАГРЯЗНЕНИЯ АТМОСФЕРНОГО ВОЗДУХА, ПОКАЗАТЕЛИ РАБОТЫ ГАЗООЧИСТНЫХ И ПЫЛЕУЛАВЛИВАЮЩИХ УСТАНОВОК, СУММАРНЫЕ ВЫБРОСЫ ПО ОБЪЕКТУ ОНВ**
python calculations\tables\razdel3\intro.py -> calculations\tables\razdel3\intro.docx
python calculations\tables\3_6.py -> calculations\tables\razdel3\3_6.docx
streamlit run calculations\tables\fill_table_3_2.py -> calculations\tables\razdel3\3_2docx

python calculations\tables\razdel3\merger_razdel3.py -> calculations\tables\razdel3\razdel3.docx

финальное, python report_combiner_docx.py ->combined_file.docx - наш сгенерированный отчёт!
