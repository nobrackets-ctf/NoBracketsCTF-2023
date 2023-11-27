# The redpanda website

We've created an automatic backup mecanism to save redpandas !
The website is saved in /backups/backup.tar every minute using **crontab** !
The cron rule is executed by root (see /etc/crontab).

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠊⡁⠠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⢠⠁⠀⢫⡑⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠐⠑⠆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢸⠀⢷⠀⠳⣄⠏⠢⣀⡀⢀⠀⠀⠀⢀⠴⠂⢩⠏⢀⡔⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢇⠈⣇⠼⣇⠀⢹⠟⠁⠁⠈⠉⠑⠃⠒⣷⣁⡔⠁⠀⣼⢁⠀⡌⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⢸⡄⢘⡦⠊⠀⠀⠀⠀⠀⠀⠀⠀⠛⡏⠀⠀⣸⠻⡼⢠⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡏⠀⠀⢈⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⣴⢁⠼⠇⢀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⠱⠤⢲⠀⠑⣄⣰⠗⠊⠉⠉⠱⡀⠀⠀⠀⢠⠴⠔⢤⣀⠀⠙⢅⠀⠀⣀⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠔⠀⠀⠀⣽⠃⢀⣴⣶⣄⠀⠇⠀⠀⠀⢧⠀⣀⣄⠀⠁⢄⠈⣢⠔⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⡠⠤⠤⣀⡀⠀⠀⠀⣼⠇⠀⡈⣿⣿⣿⡤⠖⠒⠢⢄⣸⣿⣻⣿⢷⠀⠀⢂⠱⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡠⠖⠉⠀⠀⠀⠀⠀⠉⠓⢄⠀⢿⠀⠀⣿⢿⣿⠏⠀⣤⣤⡀⠀⠙⣿⣿⣿⡿⠀⠀⢸⠀⢇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⣉⣩⣿⡺⢳⡀⠘⠿⢿⡄⠀⣨⣍⠀⠀⠀⣿⣾⠟⠁⠀⡠⠊⢀⠞⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠁⠀⣹⠀⠈⢻⣵⣦⣄⠉⠲⣬⣥⡤⠀⠚⠣⠤⠤⢒⣊⣠⠔⢛⠖⠀⠄⡀⠀⠀⠀⠀⠀
⠰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀⢀⣼⡿⠈⠈⠉⠛⠛⠛⠛⠛⠒⠒⠛⠛⠛⠻⡿⠄⠈⠢⠑⢄⠀⠀⠀⠀⠀⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠊⠀⠀⢸⡟⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡟⢄⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡏⠀⠀⠀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⡿⢷⠀⠣⡀⠀⠀⠀⠀⠀⠀⠀⠀
⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡀⠀⠀⡸⠗⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠞⠁⠸⡆⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀
⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠒⢤⣇⠀⠀⠳⣔⠀⠀⠀⠀⠀⠀⠀⣴⠟⠁⠀⠀⠀⣿⠀⠀⠛⢄⠀⠀⠀⠀⠀⠀
⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⡠⠃⢸⡆⠀⠀⠈⠷⣦⠀⠀⣀⠰⠟⣡⡤⣤⣄⡀⢠⣇⠀⠀⠀⠀⢻⠑⠠⡀⠀⠀
⠀⠙⣧⠀⠀⠀⠀⠀⠀⡮⠟⢽⢛⠁⢱⠃⣠⡞⣿⣄⣴⠋⠉⢻⡷⢴⠃⠀⢸⠁⠀⠀⠀⠙⢶⡉⠙⠲⣄⠀⠀⢃⠀⠈⢣⠀
⠀⠀⠀⠢⣀⠀⠀⠀⠀⠀⠺⡭⠏⠠⣾⣴⣿⣷⣿⠋⠋⠀⠀⣻⡇⢸⠀⠀⠘⣧⠀⠀⠀⢰⡈⣷⠀⠀⠈⢿⣄⢸⠀⠀⢸⡇
⠀⠀⠀⠀⠈⠳⢀⡀⠀⠀⠬⢧⡦⠀⢳⣾⢯⣽⣿⠀⠀⠀⣰⡟⠀⣿⠀⠀⠀⠸⣧⠀⠀⠈⠓⠛⠀⠀⠀⠰⣿⠏⠀⠀⣾⠇
⠀⠀⠀⠀⠀⢀⣀⣀⣉⣩⣷⣿⣷⣦⣼⣿⡟⢉⡇⠀⠀⢰⡟⠁⢀⡏⠀⠀⠀⢠⣿⣧⡀⠀⠀⠀⠀⠀⣀⣼⣧⣤⡶⠾⠇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠛⠛⠓⠿⠦⠶⠿⠷⠾⠿⠿⠶⠶⠶⠿⠿⠿⠷⠶⠶⠿⠟⠛⠉⠉⠉⠉⠀⠀⠀⠀
~ May the crons be ever in your favor