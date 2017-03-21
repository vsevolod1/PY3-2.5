import glob
import os.path

folder = 'Migrations'
results = set()
not_found = True

# функция вывода результатов, возвращает True, если необходимы уточнения
def print_result (results_set):
	if len(results_set) > 0:
		print('Список найденных файлов:\n')
		for item in results_set:
			print(item)
		print('Всего: {}\n'.format(len(results_set)))
		if len(results_set) == 1:
			return False
		else:
			return True
	else:
		print('Ничего не найдено\n')
		return False




#функция для поиска
def search (search_input, search_dict):
	if len(search_dict) == 0:
		files = glob.glob(os.path.join(folder, "*.sql"))
		for file in files:
			with open (file) as f:
				for line in f:
					if search_input in line:
						search_dict.add(file)
		return (search_dict)
	else:
		new_set = set()
		for item in search_dict:
			with open (item) as f:
				for line in f:
					if search_input in line:
						new_set.add(item)
		if len(new_set) > 0:
			return(new_set)
		else:
			return({})


# пользовательский интерфейс
while not_found:
    user_input = input('Введите запрос:\n')
    results = search(user_input, results)
    not_found = print_result(results)
