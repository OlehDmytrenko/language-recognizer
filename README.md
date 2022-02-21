# Програмна система languageRecognizer | Вступ

**Програмна система languageRecognizer – "Програмна система автоматизованої ідентифікації української та російської мови усного мовлення"**, яка написана мовою програмування `Python`, призначена для ідентифікації української та російської мови усного мовлення, що подається на вхід системи у вигляді відео- або аудіофайлів, зокрема з видеосервісів мережі Інтернет, таких як Youtube.


### Зміст
- [Позначення та найменування програмного модуля](#name)
- [Програмне забезпечення, необхідне для функціонування програмного модуля](#software)
- [Функціональне призначення](#function)
- [Опис логічної структури](#structure)
- [Використовувані технічні засоби](#hardware)
- [Виклик та завантаження](#run)

<a name="name"></a>
<h2>Позначення та найменування програмної системи</h2>

Програмна система має позначення **"languageRecognizer"**.

Повне найменування програмної системи – **"Програмна система автоматизованої ідентифікації української та російської мови усного мовлення"**.

<a name="software"></a>
<h2>Програмне забезпечення, необхідне для функціонування програмної системи</h2>

Для функціонування програмної системи, написаної мовою програмування `Python`, необхідне наступне програмне забезпечення, пакети та моделі:

- `python 3.8.0` or newer [v3.8.0](https://www.python.org/downloads/release/python-380/)
- `MoviePy` [v2.0.0](https://pypi.org/project/moviepy/2.0.0.dev2/)
- `vosk` [v0.3.32](https://pypi.org/project/vosk/0.3.32/)
- `wave` [v0.0.2](https://pypi.org/project/Wave/0.0.2/)
- `scipy` [v1.8.0](https://pypi.org/project/scipy/1.8.0/)
- `csv` [latest version](https://docs.python.org/3/library/csv.html)
- `codecs` [latest version](https://docs.python.org/3/library/codecs.html)
- `re` [v2.2.1](https://docs.python.org/3/library/re.html)

- `vosk-model-uk-v3` [v3](https://alphacephei.com/vosk/models/vosk-model-uk-v3.zip)
- `vosk-model-small-ru-0.22` [0.22](https://alphacephei.com/vosk/models/vosk-model-small-ru-0.22.zip)

<a name="function"></a>
<h2>Функціональне призначення</h2>

Програмна система **"languageRecognizer"** для ідентифікації української та російської мови усного мовлення, що подається на вхід системи у вигляді відео- або аудіофайлів, зокрема з видеосервісів мережі Інтернет, таких як Youtube.

<a name="structure"></a>
<h2>Опис логічної структури</h2>

Програмний модуль складається з частин (Рис. 1):
- Отримання на вхід аудіо- або відеофайлу для розпізнавання
- Конвертування вхідного відеопотоку (у випадку отримання відеофайлу) в аудіо (отримання звукової доріжки)
- Перетворення мовлення у текст (формування стенограми)
- Ідентифікація мови мовлення, представленого в аудіофайлі, за допомогою класифікатора мови
- Повернення мітки конкретної мови (наприклад, «українська», «російська» або «невизначена мова»)

<p align="center">
  <img src="http://ic.pics.livejournal.com/skirlinxxx/24636159/83141/83141_900.jpg">
</p>

Рис. 1 - Поки що товстий котик (має бути "Блок-схема програмної системи автоматизованої ідентифікації мови")


© 2022 [Oleh Dmytrenko](https://github.com/OlehDmytrenko)