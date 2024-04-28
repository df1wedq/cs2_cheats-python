with dpg.window(label=title, width=uiWidth, height=uiHeight, on_close=onClose):
    with dpg.tab_bar():
        with dpg.tab(label="Aimbot"):
            checkboxAimbot = dpg.add_checkbox(label="Aimbot", default_value=nameItClass.config["aimbot"]["active"], callback=toggleAimbot)

            Sep1 = dpg.add_separator()
            sliderAimbotFov = dpg.add_slider_float(label="Aimbot FOV", min_value=0.0, max_value=180.0, default_value=nameItClass.config["aimbot"]["fov"], callback=updateFovSlider)

            Sep2 = dpg.add_separator()
            dropdownAimbotToggleKey = dpg.add_combo(label="Aimbot Toggle Key", items=nameItClass.config["aimbot"]["toggleKeyList"], default_value=nameItClass.config["aimbot"]["toggleKey"], width=-1)

        with dpg.tab(label="Misc"):
            checkboxBunnyHop = dpg.add_checkbox(label="Bunny Hop", default_value=nameItClass.config["misc"]["bhop"], callback=toggleBunnyHop)

            Sep1 = dpg.add_separator()    
            checkboxNoFlash = dpg.add_checkbox(label="No Flash", default_value=nameItClass.config["misc"]["noFlash"], callback=toggleNoFlash)
            
            Sep2 = dpg.add_separator()
            checkboxWatermark = dpg.add_checkbox(label="Watermark", default_value=nameItClass.config["misc"]["watermark"], callback=toggleWatermark)

        with dpg.tab(label="Settings"):
            checkboxSaveSettings = dpg.add_checkbox(label="Save Settings", default_value=nameItClass.config["settings"]["saveSettings"], callback=toggleSaveSettings)
            checkboxStreamProof = dpg.add_checkbox(label="Stream Proof", default_value=nameItClass.config["settings"]["streamProof"], callback=toggleStreamProof)

            dpg.add_input_int(label=title, readonly=True, default_value=version, enabled=False)
            checkboxAlwaysOnTop = dpg.add_checkbox(label="Always On Top", default_value=True, callback=toggleAlwaysOnTop)

    dpg.setup_viewport(title, uiWidth, uiHeight)
    
    nameItClass.guiWindowHandle = pm.find_window(title)

    dpg.render_dearpygui()
