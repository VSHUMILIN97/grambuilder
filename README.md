### GramBuilder

Сервис для создания однокорневых закрытых грамматик для VoiceNavigator от ЦРТ
из текстовых файлов.

Для создания грамматики нужен текстовый файл, который будет содержать элементы
грамматики в нормализованном виде (без знаков пунктуации и цифр). Новый элемент
располагать на новой строке. Для грамматики из 4 вхождений должен получиться
следующий файл (example.txt):
```text
привет
здравствуй
дарова
хаюшки
```

Веб форма интиутивно понятная и предлагает ввести имя грамматики (чтобы не
пришлось своими ручками менять) плюс загрузить файл с текстовками. В случае
ошибки на экран будет выведен pop-up с описанием проблемы.

#### TODO
* [ ] Tests for web module (Only for further work)
* [x] Add project description and docs :) (Same as p.1)
* [ ] Add csv/xml parsers (Same as p.1)
* [ ] Add console API (Same as p.1)
* [ ] Correct typechecking (Same as p.1)
* [ ] Jokes Jokes Jokes!!!! (Never enough)
