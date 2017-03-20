import glob
import os.path

# словарь для хранения результатов
results_dict = {}

# название папки
migrations = 'Migrations'

# что ищем
search = 'sp_dropuser'

# открываем папку и ищес sql-файлы
files = glob.glob(os.path.join('folder1', "*.sql"))
for file in files:
    with open (file) as f:
        results_line_nums = [] #список для хранения номеров строк
        for line_num, line in enumerate(f):
            if search in line:
                results_line_nums.append(line_num)
        if len(results_line_nums) > 0:
            results_dict[file] = results_line_nums
print(results_dict)
