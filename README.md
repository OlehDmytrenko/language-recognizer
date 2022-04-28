# Програмна система language-recognizer | Вступ

**Програмна система language-recognizer – "Програмна система автоматизованої ідентифікації української та російської мови усного мовлення"**, яка написана мовою програмування `Python`, призначена для ідентифікації української та російської мови усного мовлення, що подається на вхід системи у вигляді відео- або аудіофайлів, зокрема з відеосервісів мережі Інтернет, таких як [Youtube](https://www.youtube.com/).


### Зміст
- [Позначення та найменування програмного модуля](#name)
- [Програмне забезпечення, необхідне для функціонування програмного модуля](#software)
- [Функціональне призначення](#function)
- [Опис логічної структури](#structure)
- [Використовувані технічні засоби](#hardware)
- [Виклик та завантаження](#run)

<a name="name"></a>
<h2>Позначення та найменування програмної системи</h2>

Програмна система має позначення **"language-recognizer"**.

Повне найменування програмної системи – **"Програмна система автоматизованої ідентифікації української та російської мови усного мовлення"**.

<a name="software"></a>
<h2>Програмне забезпечення, необхідне для функціонування програмної системи</h2>

Для функціонування програмної системи, написаної мовою програмування `Python`, необхідне наступне програмне забезпечення:
- `python 3.8.0` or newer [v3.8.0](https://www.python.org/downloads/release/python-380/)

```sh
python --version Python 3.8.0
```

пакети:
- `MoviePy` [v2.0.0](https://pypi.org/project/moviepy/2.0.0.dev2/)
- `Vosk` [v0.3.32](https://pypi.org/project/vosk/0.3.32/)
- `wave` [v0.0.2](https://pypi.org/project/Wave/0.0.2/)
- `scipy` [v1.8.0](https://pypi.org/project/scipy/1.8.0/)
- `csv` [latest version](https://docs.python.org/3/library/csv.html)
- `codecs` [latest version](https://docs.python.org/3/library/codecs.html)
- `re` [v2.2.1](https://docs.python.org/3/library/re.html)

```sh
pip install moviepy
pip install vosk
pip install wave
pip install scipy
pip install csv
pip install codecs
pip install re
```

моделі:
- `vosk-model-uk-v3` [v3](https://alphacephei.com/vosk/models/vosk-model-uk-v3.zip)
- `vosk-model-small-ru-0.22` [0.22](https://alphacephei.com/vosk/models/vosk-model-small-ru-0.22.zip)
які необхідно вивантажити та розпакувати у директорію `models`.

<a name="function"></a>
<h2>Функціональне призначення</h2>

Програмна система **"language-recognizer"** для ідентифікації української та російської мови усного мовлення, що подається на вхід системи у вигляді відео- або аудіофайлів, зокрема з відеосервісів мережі Інтернет, таких як [Youtube](https://www.youtube.com/).

<a name="structure"></a>
<h2>Опис логічної структури</h2>

Програмний модуль складається з частин (Рис. 1):
- Отримання на вхід аудіо- (у форматі `.wav`) або відеофайлу (у форматі `.mp4` або `.avi`) для ідентифікації
- Конвертування вхідного відеопотоку (у випадку отримання відеофайлу) в аудіо (отримання звукової доріжки) у форматі `.wav`
- Перетворення мовлення у текст (формування стенограми) за допомогою бібліотеки [`Vosk`](https://alphacephei.com/vosk/)
- Ідентифікація мови мовлення, представленого e відео- чи аудіофайлі, за допомогою класифікатора мови, заснованого на частотному аналізі отриманих стенограм мовлення та порівняння їх зі списками пар слів-маркерів, що характеризують українське та російське мовлення
- Повернення мітки конкретної мови (наприклад, «**українська**», «**російська**» або «**невизначена мова**»)

<p align="center">
  <img src="https://github.com/OlehDmytrenko/language-recognizer/blob/main/Flowchart.jpg">
</p>

Рис. 1 - Блок-схема програмної системи автоматизованої ідентифікації мови

Детальний опис програмної системи доступний за [посиланням](https://1drv.ms/b/s!Aoxig03HBVPLgdpVkcCmbAFJvkQNUg?e=2Q78Gz).

<a name="hardware"></a>
<h2>Використовувані технічні засоби</h2>

Програмна система експлуатується на сервері (або у хмарі серверів) під управлінням операційної системи типу `Linux` (64-х разрядна) або під керівництвом операційної системи сімейства `Windows OS`.
Загальний обсяг пам'яті, яку займає програмна ситема разом із завантаженими мовними моделями та без вхідних відеофайлів досягає 1,5 Гб.

<a name="run"></a>
<h2>Виклик та завантаження</h2>

Щоб розпізнати мову з відео необхідно на підготовчому етапі помістити відповідні відеофайли `.avi` у директорію `/videos`/.

Для серверів, які працюють під керівництвом операційних систем сімейства `Windows OS`, виклик програмної системи **"language-recognizer"** здійснюється шляхом запуску скрипта `ім'я скрипта.py` з використанням команди `python`. Потрібно відкрити командний рядок – термінал `cmd` та написати `python ім'я скрипта.py`. Важливо, щоб скрипт знаходився або в директорії, з якої запущено командний рядок, або в каталозі, прописаному у змінній середовища `PATH`. 
Тож завантаження програмної системи забезпечується введенням в командному рядку повного імені завантажувальної програми без додаткових параметрів (шлях до директорії з відео- чи аудіофайлами, мову мовлення яких потрібно розпізнати, задано за замовчуванням `/videos/` та `/audios/`, відповідно):
```sh
python main.py
```

Для серверів, які працюють під керівництвом `Unix`-подібних операційних систем (наприклад, `Linux`) також можна скористатися цим способом, але на початку скрипта `Python` у першому рядку має бути вказаний повний шлях до інтерпретатора:
```sh
#!/usr/bin/python3
```
або
```sh
#!/usr/bin/env python3
```

Далі необхідно клонувати репозиторій та проінсталювати залежності:
```sh
git clone https://github.com/OlehDmytrenko/language-recognizer.git
cd language-recognizer
```
Запуск програмної системи виконується за допомогою введення в терміналі ім'я головного виконуваного скрипта ```main.py```:
```sh
python main.py
```

Запуск програмної системи з зовнішніми налаштуваннями виконується шляхом введення цих налаштувань після імені головного виконуваного скрипта `main.py` з додатковими параметрами `[<path to settings>]`:
```sh
python <path to script> [<path to settings>]

```

В якості вхідного параметра може бути повний шлях до відео- /...повний шлях.../імʼя_відеофайла.mp4 чи аудіофайла `/....повний шлях.../імʼя_аудіофайла.wav/`. В такому випадку, завантаження програмної системи забезпечується введенням в командному рядку повного імені головного виконуваного скрипта `main.py` з додатковими параметрами:
```sh
python main.py ./...повний шлях.../імʼя_відеофайла.mp4
````
або
```sh
python main.py ./...повний шлях.../імʼя_аудіофайла.wav
```

В результаті запуску скрипта `language-recognizer.py` здійснюється попередня конвертація вхідних відеофайлів формату `.avi` у аудіо формату `.wav`. Вихідні аудіофайли буде автоматично збережено у директорії `/audios`/ та додано до черги для ідентифікації представленої у них мови мовлення.
Далі програмна система по черзі вибиратиме файли для ідентифікації мови із директорії `/audios/` та виводитиме результат у консоль.

Дані, отримані в результаті застосування програмної системи та які стосуються основних результатів виводяться в консолі. 
Також вивід може перенаправлятися із консолі у файл, який зберігаюється у директорії `results` у вигляді `.log` файла. Для цього використовується оператор `>`.
Повна команда виглядає так:
```sh
python main.py > outlog.log
```
Тут `outlog.log` – це текстовий файл, у який записуються проміжні результати та  виконання програмної системи.

Операція може використовуватися як в операційній системі `Windows OS`, так і в `Unix`-подібних системах.
Якщо файла, в який повинен вивестися результат, не існує – система створить його автоматично.
При використанні оператора `>` вміст файлу, в який відображаються дані, повністю перезаписується. Якщо наявні дані потрібно зберегти, а нові дописати до існуючих, то використовується оператор `>>`:
```sh
python language-recognizer.py >> outlog.log
```

© 2022 [Oleh Dmytrenko](https://github.com/OlehDmytrenko)