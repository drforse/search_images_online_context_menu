# search_images_online_context_menu
Create context menu in Windows to open urls for searching images online right from explorer

Supported Search Engines: Yandex, Google

Install process:
1) Clone repository
2) Copy files to the directory where you would like them to be (you won't be able to move them without complete reinstalling later)
3) Run installation_files/install_root.py as administrator
4) In config.py set yandex_cookies_file_path to firefox's cookies.sqlite file and your User-Agent. If some of them is empty/wrong, script just won't use it

Uninstall process:
1) Run installation_files/uninstall_root.py as administrator
2) Remove all the files
