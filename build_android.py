from setuptools import setup

PRC_DATA = """
load-display pandagles2
aux-display pandagles

notify-level info
gl-debug true
"""

setup(
    name="OP Media Player",
    version="0.0.6",
    options={
        "build_apps": {
            "application_id": "com.maybebroken.opmediaplayer",
            "android_version_code": 1,
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
                "pandagles2",
                "pandagles",
                "p3openal_audio",
            ],
            "prefer_discrete_gpu": True,
            "platforms": ["android"],
            "extra_prc_data": PRC_DATA,
        },
        "bdist_apps": {
            "signing_certificate": "cert.pem",
            "signing_private_key": "private.pem",
            "signing_passphrase": "panda3d_is_cool",
        },
    },
    classifiers=[
        "Topic :: Multimedia :: Sound/Audio :: Players",
    ],
)
