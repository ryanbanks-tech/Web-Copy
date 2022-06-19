#! usr/bin/venv python3

from pywebcopy import save_webpage

kwargs = {'project_name': 'Nick-Russo-Site'}

save_webpage(
  url = 'http://njrusmc.net/',

  project_folder = 'Copied-Sites/',
  **kwargs
)
