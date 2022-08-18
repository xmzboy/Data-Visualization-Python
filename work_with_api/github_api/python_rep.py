import module_data_and_plot as mod


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = mod.connection(url)                         # Подключение к апи
stars, labels, repo_links = mod.data_proc(r)    # Сбор и обработка данных
mod.draw_html(stars, labels, repo_links)        # Отрисовка веб-страницы с графиком
