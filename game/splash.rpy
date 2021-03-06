## splash screen is first thing that gets shown to player

# disclaimers
init python:
    menu_trans_time = 1

    splash_message_default = "这是非官方的粉丝向 mod，与 Team Salvato 无关。\n本 mod 不适合儿童或者极易受影响的人。\n\n不要说我们没有警告过你.png"

    splash_messages = [
        "请支持 Doki Doki Literature Club。",
        splash_message_default,
        "Monika 在看着你在码。",
        "突然忸忸怩怩牛牛牛男男女女扭扭捏捏牛牛牛牛牛哪尼侬额呢喃你你弄",
        "突然nnnnnnnnnnnnnnnnnnnnn nnnnnn",
        "这 TM 是噩梦吧？",
        "噫啊↑啊↗啊→啊↘啊↓啊↓啊↓啊↓！！！ —— Natsuki",
        "WDNMD，嘿，mod 作者，听说你喜欢写 BUUUUUUUUUUUUUG？ —— Natsuki",
        "哇啊啊啊啊啊啊啊啊啊啊啊啊啊！ —— Natsuki",
        "啊哈↓↓↓↓↓↓↓哈↓↓↓↓↓哈↓↓↓↓↓哈↓↓↓↓哈↓↓↓哈↓↓哈↓ —— Yuri",
        "我咋变成疯nggggggggggggggggg人nnnnnnnnnnnn了eeeeeeeeeee？！ —— Yuri",
        "噫啊啊啊啊啊啊啊啊啊！ —— Sayori",
        "这也许是你游最烂的 mod...",
        "我永远爱你。",
        "爱你们喵！",
        "我会一直爱你的呐！", # those 3 are intended
        "祝你好运！",
        "您有 1/6 的几率触发死不瞑目的 Sayori 彩蛋，如果你看到了这行警告，请加油触发（"
    ]


image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)


image menu_logo:
    "/moddata/insidethedark.png"
    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_move

image menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_move

image game_menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_loop

image menu_fade:
    "white"
    menu_fadeout

image menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_y_ghost:
    subpixel True
    "gui/menu_art_y_ghost.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n_ghost:
    subpixel True
    "gui/menu_art_n_ghost.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s_ghost:
    subpixel True
    "gui/menu_art_s_ghost.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m_ghost:
    subpixel True
    "gui/menu_art_m_ghost.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_s_glitch:
    subpixel True
    "gui/menu_art_s_break.png"
    xcenter 470
    ycenter 600
    zoom 0.68
    menu_art_move(.8, 470, .8)

image menu_nav:
    "gui/overlay/main_menu.png"
    menu_nav_move

image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=20, particleTime=2.0, particleXSpeed=6, particleYSpeed=4).sm
    particle_fadeout

transform particle_fadeout:
    easeout 1.5 alpha 0

transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500

transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0

image intro:
    truecenter
    "white"
    0.5
    "bg/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image tos = "bg/warning.png"
image tos2 = "bg/warning2.png"

label splashscreen:


    python:
        firstrun = ""
        try:
            firstrun = renpy.file("firstrun").read(1)
        except:
            with open(config.basedir + "/game/firstrun", "wb") as f:
                f.write('1')
                pass
    if not firstrun:
        if persistent.first_run and not persistent.do_not_delete:
            $ quick_menu = False
            show game_menu_bg zorder 1
            "你似乎删除了 firstrun 文件，并且我们发现还有之前的存档。"
            "如果你触发了大 bug，这里可以让你逃离 bug。"
            "但是，你收集的 CG 状态也会被删除。"
            menu:
                "是否重置游戏？"
                "是的，删除存档":
                    "正在删除存档...{nw}"
                    python:
                        for savegame in renpy.list_saved_games(fast=True):
                            renpy.unlink_save(savegame)
                        renpy.loadsave.location.unlink_persistent()
                        renpy.persistent.should_save_persistent = False
                        renpy.utter_restart()
                "不，继续游戏":
                    pass

        python:
            if not firstrun:
                with open(config.basedir + "/game/firstrun", "w") as f:
                    f.write("1")
            filepath = renpy.file("firstrun").name
            open(filepath, "a").close()


    default persistent.first_run = False
    if not persistent.first_run:
        $ quick_menu = False
        scene white
        pause 0.5
        show game_menu_bg zorder 1
        with Dissolve(1.0)
        pause 1.0

        "[config.name] 是 Doki Doki Literature Club 的粉丝向 mod，与 Team Salvato 无关。"
        "本 mod 理应在通关原游戏后再进行游玩，因为本 mod 包含大量剧透。"
        "本 mod 包含来自原游戏的恐怖部分，因此，本 mod 不适合儿童或者极易受影响的人。更多详情可以访问 {a=https://ddlc.moe/warning.html}https://ddlc.moe/warning.html{/a}（亦包含剧透）。"
        "**不要说我们没有警告过你.png**"

        menu:
            "如果继续游玩 [config.name] 将视为你已经通关原游戏，并接受任何剧透和恐怖的内容。"
            "我同意。":
                pass
            "我不同意，退出。":
                $ renpy.quit()

        scene white
        with Dissolve(1.5)
        
        call import_ddlc_persistent from _call_import_ddlc_persistent

        $ persistent.first_run = True

    python:
        basedir = config.basedir.replace('\\', '/')

    if persistent.autoload and not _restart:
        jump autoload

    $ config.allow_skipping = False

    show white
    $ persistent.ghost_menu = True
    $ splash_message = splash_message_default
    $ config.main_menu_music = audio.mend
    $ renpy.music.play(config.main_menu_music)
#    show intro with Dissolve(0.5, alpha=True)
#    pause 2.5
#    hide intro with Dissolve(0.5, alpha=True)

    if renpy.random.randint(0, 3) == 0:
        $ splash_message = renpy.random.choice(splash_messages)
    show splash_warning "[splash_message]" with Dissolve(0.5, alpha=True)
    pause 2.0
    hide splash_warning with Dissolve(0.5, alpha=True)
    $ config.allow_skipping = True
    return

label warningscreen:
#   hide intro
    show warning
    pause 3.0

label after_load:
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ persistent.ghost_menu = True
    $ style.say_dialogue = style.normal

    if persistent.yuri_kill > 0 and persistent.autoload == "yurikill2":
        if persistent.yuri_kill >= 1380:
            $ persistent.yuri_kill = 1440
        elif persistent.yuri_kill >= 1180:
            $ persistent.yuri_kill = 1380
        elif persistent.yuri_kill >= 1120:
            $ persistent.yuri_kill = 1180
        elif persistent.yuri_kill >= 920:
            $ persistent.yuri_kill = 1120
        elif persistent.yuri_kill >= 720:
            $ persistent.yuri_kill = 920
        elif persistent.yuri_kill >= 660:
            $ persistent.yuri_kill = 720
        elif persistent.yuri_kill >= 460:
            $ persistent.yuri_kill = 660
        elif persistent.yuri_kill >= 260:
            $ persistent.yuri_kill = 460
        elif persistent.yuri_kill >= 200:
            $ persistent.yuri_kill = 260
        else:
            $ persistent.yuri_kill = 200

    if anticheat != persistent.anticheat:
        stop music
        scene black
        "存档无法加载。"
        "您是不是想作弊？"
        "或者有 bug 发生了？"
        "如果确实有此事，请将游戏目录内的 firstrun 文件删除，以便重置存档。"
        "正在重启...{w=2.0}{nw}"

        $ renpy.utter_restart()
    return


label autoload:
    python:

        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.block_rollback()


        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None

    if persistent.yuri_kill > 0 and persistent.autoload == "yurikill2":
        $ persistent.yuri_kill += 200

    $ renpy.pop_call()
    jump expression persistent.autoload

# this label is for use of main menu's yuri kill jump
# not needed there
label autoload_yurikill:
    if persistent.yuri_kill >= 1380:
        $ persistent.yuri_kill = 1440
    elif persistent.yuri_kill >= 1180:
        $ persistent.yuri_kill = 1380
    elif persistent.yuri_kill >= 1120:
        $ persistent.yuri_kill = 1180
    elif persistent.yuri_kill >= 920:
        $ persistent.yuri_kill = 1120
    elif persistent.yuri_kill >= 720:
        $ persistent.yuri_kill = 920
    elif persistent.yuri_kill >= 660:
        $ persistent.yuri_kill = 720
    elif persistent.yuri_kill >= 460:
        $ persistent.yuri_kill = 660
    elif persistent.yuri_kill >= 260:
        $ persistent.yuri_kill = 460
    elif persistent.yuri_kill >= 200:
        $ persistent.yuri_kill = 260
    else:
        $ persistent.yuri_kill = 200
    jump expression persistent.autoload

label before_main_menu:
    $ config.main_menu_music = audio.mend
    return

label quit:

    # stuff that happens when the game closes

    return
