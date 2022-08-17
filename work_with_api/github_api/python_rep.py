import module_data_and_plot as mod


url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = mod.connection(url)
stars, labels, repo_links = mod.data_proc(r)
mod.draw_html(stars, labels, repo_links)
