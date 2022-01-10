import pytube

link = str(input("Введите линк видео:\n"))
link = pytube.YouTube(link)  #в переменной link будет храниться вся инфа о видео

tt = link.title
print('Получаем название видео--->>>\n',tt)
print('Количество просмотров---->>> ',link.views)
print('Длина видео--->>> ', link.length)

print('Начинаем загрузку видео ...')
stream = link.streams.get_highest_resolution()
stream.download('./')       #Путь установки. По дефолту - в папку проекта.
print('Загрузка завершена!')
