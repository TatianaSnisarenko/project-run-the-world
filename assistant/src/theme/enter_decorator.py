def enter_decorator_func(func):
    def inner():
        RED = "\33[91m"
        BLUE = "\33[94m"
        GREEN = "\033[32m"
        YELLOW = "\033[93m"
        PURPLE = '\033[0;35m' 
        CYAN = "\033[36m"
        END = "\033[0m"
        RESET = "\033[0m"

        print(f''' {CYAN}
██████   ██████   ██████  ██   ██      ██████  ███████     ███    ███ ██ ██████  ██████  ██      ███████       ███████  █████  ██████  ████████ ██   ██ 
██   ██ ██    ██ ██    ██ ██  ██      ██    ██ ██          ████  ████ ██ ██   ██ ██   ██ ██      ██            ██      ██   ██ ██   ██    ██    ██   ██ 
██████  ██    ██ ██    ██ █████       ██    ██ █████       ██ ████ ██ ██ ██   ██ ██   ██ ██      █████   █████ █████   ███████ ██████     ██    ███████ 
██   ██ ██    ██ ██    ██ ██  ██      ██    ██ ██          ██  ██  ██ ██ ██   ██ ██   ██ ██      ██            ██      ██   ██ ██   ██    ██    ██   ██ 
██████   ██████   ██████  ██   ██      ██████  ██          ██      ██ ██ ██████  ██████  ███████ ███████       ███████ ██   ██ ██   ██    ██    ██   ██ 
                                                                                                                                                        
                  ╔╦╗┌─┐┌─┐┬┌─┐┌┐┌┌─┐┌┬┐  ┌─┐┌┐┌┌┬┐  ┌┬┐┌─┐┬  ┬┌─┐┬  ┌─┐┌─┐┌─┐┌┬┐  ┌┐ ┬ ┬  ╔═╗┌─┐┌┐┌┌┬┐┌─┐┬  ┌─┐  ┌─┐┌┐┌┌┬┐  ╔═╗┌─┐ 
                   ║║├┤ └─┐││ ┬│││├┤  ││  ├─┤│││ ││   ││├┤ └┐┌┘├┤ │  │ │├─┘├┤  ││  ├┴┐└┬┘  ║ ╦├─┤│││ ││├─┤│  ├┤   ├─┤│││ ││  ║  │ │ 
                  ═╩╝└─┘└─┘┴└─┘┘└┘└─┘─┴┘  ┴ ┴┘└┘─┴┘  ─┴┘└─┘ └┘ └─┘┴─┘└─┘┴  └─┘─┴┘  └─┘ ┴   ╚═╝┴ ┴┘└┘─┴┘┴ ┴┴─┘└    ┴ ┴┘└┘─┴┘  ╚═╝└─┘o                                                                                                                                                                                 

                                                .#######**+=-:.               ..-+*##########*.                          
                                                .+#:...:::---=+*###*=..   ..-*##*=-:::....   =#-.                         
                                            .:+**#=.            ...:+#*:.:+#*-....           .+#*+=..                     
                                         ...:**:#*.                  .+###+..                 :#*:#+.....                 
                                         :#####:**:.                   .**...                  .=#--#####..                
                                       ..*#.=#--#-.                    .**.                     .*#.**::#+.                
                                       .+#::#+:#+.                     .**.                      :#+.#+.+#:                
                                      .-#=.*#.**..                     .**.                      .+#:-#=.*#..              
                                      :#+.+#:=#-.                      .**.                       .**.*#::#+.              
                                     .**.-#=-#=..                      .**.                        :#+.#*.=#:.             
                                    .=#-:#+.**.                        .**.                        .+#:-#=.*#..            
                                    -#=.**.+#:.                        .**.                      ....#*.*#::#+.            
                                   .**.=#-=#++**###########*+=.        .**.       ..=+*###########**++#=.#*.=#:            
                                  .*#.-#=.**+-:..      .....-+*#*=...  .**.    .=*#*+-.. ..  ......:-+**.-#=.*#..          
                                 .=#-:**-=++*################*=::+##+...**...+##+::=*################*++=-*#::#+.          
                                 :#+.:+=--:::................:-+*######+**+######*+-:................:::--=+:.=#:.         
                                .################################################################################.         
                                .################################################################################.         
                                                                     .+####+.                                             
                                              
                                 One Book to rule them all. One Book to find them. One Book to bring them all.
      {RESET}''')

        result = func()
        return result
    return inner