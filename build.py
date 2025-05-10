from setuptools import setup

setup(
    name="OP Media Player",
    options={
        "build_apps": {
            "gui_apps": {
                "op_media_player": "runner.py",
            },
            "log_filename": "$USER_APPDATA/OPMediaPlayer/output.log",
            "log_append": False,
            "include_patterns": [
                "**/*.png",
                "**/*.jpg",
                "**/*.prc",
                "Main.py",
                "updater.py",
                "remove_index.json",
                "__YOUTUBEDOWNLOADER.py",
                "po-token-generator/**",
                "src/**",
            ],
            "plugins": [
                "pandagl",
                "p3openal_audio",
            ],
            "prefer_discrete_gpu": True,
            "platforms": ["win_amd64", "linux_x86_64", "macosx_10_13_x86_64"],
        }
    },
)
