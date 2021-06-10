### О проекте:

Проект направлен на разработку системы **обмена текстовыми сообщениями** в зашифрованном виде. Система поддерживает различные алгоритмы шифрования сообшений: **шифр Вернама, шифр Виженера, AES, вертикальная перестановка, El Gamal, А5/1**. Также поддерживается обмен ключами шифрования по алгоритму **Диффи-Хелмана**
---
### Ветвление проекта:

Разработка проекта осуществляется на 5 ветках:

- development - ветка преднозначена для комитов связанных с изменением кода.
- testing - ветка предназначена для загрузки кода требующего тестирования.
- prod - ветка предназначена для загрузки оттестированного кода готового приложения.
- main - ветка преднозначена для оттестированного кода не вошедшего в релиз.
- Documrnt - ветка предназна для загрузки документации по проекту.
---
### Роли в проекте при работе с гитом:
- Разработчик - написание кода, сборка приложения. Данная роль использует такие ветки как: **development. (Сергей, Максим)**
- Тестировщик - тестирование написанного кода. Данная роль использует такие ветки как: **testing, main.** Ветка **testing** используется тестировщиком для получения исходного кода требующего тестирования, а ветка **main** используется для загрузки оттестированного кода.(Сергей, Александр)
- PM - аркестрация кода по веткам. Данная роль использует ветки **prod** и **main**, из ветки **main** PM берет оотестированную часть приложения и в необходимое время, после согласования с командой загружает ее в ветку **prod** для дальнейшего развертывания в боевой среде.(Александр)*

*Проработать вопрос автоматизированного развертывания при помощи git lab CI.

---

### Структура git репозитория:
![image](https://user-images.githubusercontent.com/74994249/115714857-409b6800-a380-11eb-98d9-f8e3eaf732c5.png)
